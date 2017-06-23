# -*- coding: utf-8 -*-
'''
    Copyright (C) 2017 Rafael Picanço.

    The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import sys
sys.path.append('../../analysis')

import os
from glob import glob
import numpy as np
from matplotlib.path import Path as mp
import matplotlib.pyplot as plt

# from drawing import plot_xy as plot
from constants import Circle
from constants import BLUE_LEFT, RED_LEFT, GREEN_RIGHT, CYAN_RIGHT
from correction import unbiased_gaze, ALGORITHM_QUANTILES

from methods import load_data, get_filenames, remove_outside_screen
from methods import stimuli_onset, rate_in, all_stimuli, all_responses
from methods import switching_timestamps

# left_shape = mp(SQUARE.Points())
# right_shape = mp(CIRCLE.Points())

def gaze_mask_left_right(all_gaze_data):
    left_shape = mp(Circle('left').Points(factor=2))  
    right_shape = mp(Circle('right').Points(factor=2))

    x_norm = 'x_norm'
    y_norm = 'y_norm'
    
    keyword_arguments = {
        'screen_center':np.array([0.5, 0.5])
        }

    # load gaze data
    gaze_data = np.array([all_gaze_data[x_norm], all_gaze_data[y_norm]])

    gaze_data, mask = remove_outside_screen(gaze_data)
    all_gaze_data = all_gaze_data[mask]
    gaze_data, d = unbiased_gaze(gaze_data.T, ALGORITHM_QUANTILES, min_block_size=1000, **keyword_arguments)
    
    all_gaze_data[x_norm],all_gaze_data[y_norm] = gaze_data.T[0], gaze_data.T[1]
    gaze_data = np.array([all_gaze_data[x_norm], all_gaze_data[y_norm]])

    left_gaze_mask = left_shape.contains_points(gaze_data.T)
    left_data = all_gaze_data[left_gaze_mask]
    print('Data inside left shape: %d'%len(left_data))

    right_gaze_mask = right_shape.contains_points(gaze_data.T)
    right_data = all_gaze_data[right_gaze_mask]
    print('Data inside right shape: %d'%len(right_data))
    print('Data inside shapes: %d'%(len(left_data)+len(right_data)))
    
    return left_gaze_mask, right_gaze_mask

def relative_rate_left_right(gaze_filename, beha_filename):
    timestamps = 'time'
    
    print('\n'+gaze_filename)
    all_gaze_data = load_data(gaze_filename)

    left_gaze_mask, right_gaze_mask = gaze_mask_left_right(all_gaze_data)
    
    print(beha_filename)
    # load behavioral data
    beha_data = load_data(beha_filename)

    left_timestamps = all_gaze_data[left_gaze_mask][timestamps] 
    right_timestamps = all_gaze_data[right_gaze_mask][timestamps]
    all_target_intervals = all_stimuli(beha_data)
    all_target_intervals = zip(all_target_intervals, all_target_intervals[1:])
    
    left_data = rate_in(all_target_intervals, left_timestamps)
    right_data = rate_in(all_target_intervals, right_timestamps)

    color_set = [
        (RED_LEFT, GREEN_RIGHT),
        (RED_LEFT, CYAN_RIGHT),
        (BLUE_LEFT, CYAN_RIGHT),
        (BLUE_LEFT, GREEN_RIGHT)
    ]

    relative_rate = [l/(r+l) if r+l > 0 else np.nan for l, r in zip(left_data, right_data)]

    colors = []
    color_combination = 0
    for r in relative_rate:
        if r >= .5:
            colors.append(color_set[color_combination][0])

        if r < .5:
            colors.append(color_set[color_combination][1])  
            
        # if .6 > r > .4:
        #     colors.append('#000000')  
                      
        color_combination += 1
        if color_combination > 3:
            color_combination = 0
    plt.plot(relative_rate,c='black', marker='None')
    plt.scatter(range(len(relative_rate)),relative_rate,c=colors)
    plt.show()
    # print(left_data, right_data)

def relative_rate_blue_red(src_dir, cycles_set=slice(0,8)):
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    data = []
    for path in paths:
        beha_data = load_data(os.path.join(path,"behavioral_events.txt"))
        target_intervals = stimuli_onset(beha_data)
        red_intervals = zip(target_intervals[0], target_intervals[1])
        blue_intervals = zip(target_intervals[1], target_intervals[0][1:])
        responses = all_responses(beha_data)
        
        red_data = rate_in(red_intervals, responses)
        blue_data = rate_in(blue_intervals, responses)

        relative_rate = [r/(r+b) if r+b > 0 else np.nan for r, b in zip(red_data, blue_data)]
        data.append(relative_rate[cycles_set])
    return data

def rate_switching(src_dir, cycles_set=slice(0,8)):
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    data = []
    for path in paths:
        all_gaze_data = load_data(os.path.join(path,"gaze_coordenates_on_screen.txt"))
        left_gaze_mask, right_gaze_mask = gaze_mask_left_right(all_gaze_data)
        switchings = switching_timestamps(all_gaze_data, left_gaze_mask, right_gaze_mask)
        beha_data = load_data(os.path.join(path,"behavioral_events.txt"))
        target_intervals = stimuli_onset(beha_data)
        red_intervals = zip(target_intervals[0], target_intervals[1])
        blue_intervals = zip(target_intervals[1], target_intervals[0][1:])
        red_data = rate_in(red_intervals, switchings)[cycles_set]
        blue_data = rate_in(blue_intervals, switchings)[cycles_set]
        data.append((red_data,blue_data,switchings.shape[0]))
    return data

def relative_rate_switching(src_dir, cycles_set=slice(0,8)):
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    data = []
    for path in paths:
        all_gaze_data = load_data(os.path.join(path,"gaze_coordenates_on_screen.txt"))

        left_gaze_mask, right_gaze_mask = gaze_mask_left_right(all_gaze_data)
        switchings = switching_timestamps(all_gaze_data, left_gaze_mask, right_gaze_mask)
        print(switchings.shape)
        # stimuli
        beha_data = load_data(os.path.join(path,"behavioral_events.txt"))
        target_intervals = stimuli_onset(beha_data)
        red_intervals = zip(target_intervals[0], target_intervals[1])
        blue_intervals = zip(target_intervals[1], target_intervals[0][1:])


        red_data = rate_in(red_intervals, switchings)
        blue_data = rate_in(blue_intervals, switchings)

        relative_rate = [r/(r+b) if r+b > 0 else np.nan for r, b in zip(red_data, blue_data)]
        data.append(relative_rate[cycles_set])
    return data


if __name__ == '__main__':
    filenames = zip(
        get_filenames('dizzy-timers','gaze_coordenates_on_screen.txt'),
        get_filenames('dizzy-timers','behavioral_events.txt')
        )
    gaze_filename, beha_filename = filenames[0]
    relative_rate_left_right(gaze_filename, beha_filename)