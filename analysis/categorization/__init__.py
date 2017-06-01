# -*- coding: utf-8 -*-
'''
    Copyright (C) 2017 Rafael Picanço.

    The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import sys
sys.path.append('../../analysis')

import numpy as np
from matplotlib.path import Path as mp

from constants import CIRCLE, SQUARE_P, S_SIZE, SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX
from correction import unbiased_gaze, ALGORITHM_QUANTILES, plot

def ellipse(center, width, height, n = 360):
    thetas = [np.pi*2 * i/n for i in range(n)]
    points = [(center[0] + np.cos(t) * width, center[1] + np.sin(t) * height) for t in thetas]
    return np.array(points)

if __name__ == '__main__':
    import os
    from methods import load_data, get_filenames, remove_outside_screen

    keyword_arguments = {
        'screen_center':np.array([0.5, 0.5])
        } 

    left_shape = mp(np.array([
        [SQUARE_P[0], SQUARE_P[1]],
        [SQUARE_P[0], SQUARE_P[3]],
        [SQUARE_P[2], SQUARE_P[3]],
        [SQUARE_P[2], SQUARE_P[1]]
        ])
    )

    right_shape = mp(ellipse(CIRCLE, S_SIZE[0]/2,S_SIZE[1]/2))

    for filename in get_filenames('dizzy-timers','gaze_coordenates_on_screen.txt'):
        print('\n'+filename)
        all_data = load_data(filename)
        gaze_data = np.array([all_data['x_norm'], all_data['y_norm']])
        #plot(gaze_data)

        gaze_data, mask = remove_outside_screen(gaze_data)
        all_data = all_data[mask]
        gaze_data, d = unbiased_gaze(gaze_data.T, ALGORITHM_QUANTILES, min_block_size=1000, **keyword_arguments)
        
        all_data['x_norm'],all_data['y_norm'] = gaze_data.T[0], gaze_data.T[1]
        gaze_data = np.array([all_data['x_norm'], all_data['y_norm']])

        left_gaze_mask = left_shape.contains_points(gaze_data.T)
        left_data = all_data[left_gaze_mask]
        print('Data inside left shape: %d'%len(left_data))

        right_gaze_mask = right_shape.contains_points(gaze_data.T)
        right_data = all_data[right_gaze_mask]
        print('Data inside left shape: %d'%len(right_data))
        
        plot([all_data['x_norm'],all_data['y_norm']])
        plot([left_data['x_norm'],left_data['y_norm']])
        plot([right_data['x_norm'],right_data['y_norm']])

    # output folder
    # output_path = os.path.join(data_path,'categorization')

    # if not os.path.exists(output_path):
    #     os.makedirs(output_path) 