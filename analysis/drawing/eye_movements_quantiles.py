# -*- coding: utf-8 -*-
'''
  Copyright (C) 2017 Rafael Picanço.

  The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

# note: fps should be as constant as possible

import sys
sys.path.append('../../analysis')

import os
from glob import glob

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path as mp

from methods import load_data, stimuli_onset, all_stimuli, color_pair, remove_outside_screen
from drawing import temporal_perfil
from constants import BLUE_LEFT, RED_LEFT, GREEN_RIGHT, CYAN_RIGHT, Circle
from correction import unbiased_gaze, ALGORITHM_QUANTILES

def draw_single(src_dir, show=True):
    ID = os.path.basename(os.path.dirname(src_dir))
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    x_label = 'Ciclo'
    y_label = 'dir. < Taxa (gaze/s) > esq.'
    title = 'Particip. '+ID+': Taxa de movim. oculares durante cada cor'

    n_plots = len(paths)
    if n_plots == 1:
        figsize = (4, 4)
    elif n_plots == 2:
        figsize = (8, 4)
    elif n_plots == 3:
        figsize = (12, 4)
    else:
        figsize = (14, 4)

    figure, axarr = plt.subplots(1, n_plots, sharey=True, sharex=False, figsize=figsize) 
    figure.suptitle(title);
    figure.text(0.5, 0.02, x_label)

    keyword_arguments = {
        'screen_center':np.array([0.5, 0.5])
        } 
    
    left_shape =mp(Circle('left').Points(2))
    # left_shape = mp(SQUARE.Points())    
    right_shape = mp(Circle('right').Points(2))

    for i, path in enumerate(paths):    
        data_folder = os.path.join(src_dir, path)
        print(data_folder)
        beha_events_path = os.path.join(data_folder, "behavioral_events.txt")
        gaze_events_path = os.path.join(data_folder, 'gaze_coordenates_on_screen.txt')
        beha_data = load_data(beha_events_path)
        all_data = load_data(gaze_events_path)

        gaze_data = np.array([all_data['x_norm'], all_data['y_norm']])

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
        print('Data inside right shape: %d'%len(right_data))
        print('Data inside shapes: %d'%(len(left_data)+len(right_data)))

        left_timestamps = all_data[left_gaze_mask]['time'] 
        right_timestamps = all_data[right_gaze_mask]['time']

        temporal_perfil(axarr[i],color_pair(beha_data,0), left_timestamps,'pair', c1=RED_LEFT, nsize=0)
        temporal_perfil(axarr[i],color_pair(beha_data,0), right_timestamps,'pair', c1=GREEN_RIGHT, nsize=0, doreversed=True)

        temporal_perfil(axarr[i],color_pair(beha_data,1), left_timestamps,'pair', c1=RED_LEFT, nsize=1)
        temporal_perfil(axarr[i],color_pair(beha_data,1), right_timestamps,'pair', c1=CYAN_RIGHT, nsize=1, doreversed=True)

        temporal_perfil(axarr[i],color_pair(beha_data,2), left_timestamps,'pair', c1=BLUE_LEFT, nsize=2)
        temporal_perfil(axarr[i],color_pair(beha_data,2), right_timestamps,'pair', c1=CYAN_RIGHT, nsize=2, doreversed=True)
                        
        temporal_perfil(axarr[i],color_pair(beha_data,3), left_timestamps,'pair', c1=BLUE_LEFT, nsize=3)
        temporal_perfil(axarr[i],color_pair(beha_data,3), right_timestamps,'pair', c1=GREEN_RIGHT, nsize=3, doreversed=True)
        
    ticks = [30,20,10,0,10,20,30]
    axarr[0].set_yticklabels(labels=ticks)

    plt.ylim(ymin = -30)
    plt.ylim(ymax = 30)

    axarr[0].set_ylabel(y_label)
    figure.tight_layout()
    if show:            
        plt.show()

if __name__ == '__main__':
    from methods import get_data_path
    from constants import INNER_PATHS
    from drawing.eye_movements_quantiles import draw_single as draw_gaze_quantiles # NOTE: xy must be normalized
    from drawing.responses import draw_single as draw_responses

    data_path = get_data_path()
    for path in INNER_PATHS:
        # draw_responses(os.path.join(data_path, path))
        draw_gaze_quantiles(os.path.join(data_path, path))
        break
        