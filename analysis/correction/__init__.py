# -*- coding: utf-8 -*-
'''
    Copyright (C) 2017 Rafael Picanço & François Tonneau.

    The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import numpy as np
import cv2

ALGORITHM_KMEANS = 'kmeans'
ALGORITHM_QUANTILES = 'quantiles'

def unbiased_gaze(gaze_data, algorithm, min_block_size=1000,**kwargs):
    def bias(gaze_block,**kwargs):
        def kmeans(gaze_block,screen_center, k=2):
            """
                assumes gaze_data is in pixels
            """
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
            _, _, centers = cv2.kmeans(data=np.float32(gaze_block.T),
                                       K=k,
                                       criteria=criteria,
                                       attempts=10,
                                       flags=cv2.KMEANS_RANDOM_CENTERS)

            return screen_center - centers.mean() 

        def quantiles(gaze_block,screen_center,q=[5, 10, 15, 85, 90, 95]):
            """
                assumes normalized gaze_data
            """
            x = gaze_block[0,:].copy()
            y = gaze_block[1,:].copy()
            sample_size = gaze_block.shape[1]

            x.sort()
            y.sort()
            x_stat = 0
            y_stat = 0

            for quantile in q:
                rank = (sample_size * quantile)/100
                x_stat += x[rank]
                y_stat += y[rank]

            # divide by length to get quantile average
            x_stat = x_stat/len(q)
            y_stat = y_stat/len(q)
            xy_stat = np.array([[x_stat], [y_stat]])
            return xy_stat - screen_center

        kwargs['gaze_block'] = gaze_block
        if algorithm == ALGORITHM_KMEANS:
            return kmeans(**kwargs)
        elif algorithm == ALGORITHM_QUANTILES:
            return quantiles(**kwargs)

    def correction(gaze_block, bias):
        gaze_block[0,:] += bias[0]
        gaze_block[1,:] += bias[1]
        return gaze_block

    gaze_count = gaze_data.shape[1]    
    if gaze_count < min_block_size:
        print("\nToo few data to proceed. \nUsing min_block_size = %d"%gaze_count)
        min_block_size = gaze_count

    # bias_along_blocks = []
    data = []
    for block_start in range(0, gaze_count, min_block_size):
        block_end = block_start + min_block_size
        if block_end <= gaze_count:
            gaze_block = gaze_data[:,block_start:block_end]
            gaze_bias = bias(gaze_block, **kwargs)
        else:
            block_end = gaze_count
            gaze_block = gaze_data[:,block_start:block_end]

        # bias_along_blocks.append({'bias':gaze_bias, 'block':[block_start,block_end]})
        data.append(correction(gaze_block, gaze_bias))

    return np.hstack(data)

if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt
    import os
    from glob import glob
    import sys
    sys.path.append('../../analysis')

    # from constants import SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX

    from constants import INNER_PATHS
    from methods import load_data, remove_outside_screen
    
    data_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(data_path)
    data_path = os.path.dirname(data_path)
    
    # output folder
    output_path = os.path.join(data_path,'correction')

    if not os.path.exists(output_path):
        os.makedirs(output_path) 

    keyword_arguments = {
        'screen_center':np.array([[0.5], [0.5]])
        }

    for inner_path in INNER_PATHS:
        a_data_path = os.path.join(data_path,inner_path) 
        paths = sorted(glob(os.path.join(a_data_path,'0*')))
        for path in paths:
            filename = os.path.join(data_path,path)
            filename = os.path.join(filename,'gaze_coordenates_on_screen.txt')
            print('\n'+filename)
            data = load_data(filename)
            data = np.array([data['x_norm'], data['y_norm']])        
            data = remove_outside_screen(data)
            data = unbiased_gaze(data, ALGORITHM_QUANTILES, **keyword_arguments)
            plt.scatter(*data)
            plt.show()