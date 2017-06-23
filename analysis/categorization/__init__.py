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

def relative_rate_left_right(src_dir, target_intervals='all_onsets'):
    timestamps = 'time'
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    data = []
    for path in paths:
        all_gaze_data = load_data(os.path.join(path,"gaze_coordenates_on_screen.txt"))
        left_gaze_mask, right_gaze_mask = gaze_mask_left_right(all_gaze_data)
        left_timestamps = all_gaze_data[left_gaze_mask][timestamps] 
        right_timestamps = all_gaze_data[right_gaze_mask][timestamps]

        beha_data = load_data(os.path.join(path,"behavioral_events.txt"))
        if 'all_onsets' in target_intervals: 
            l_target_intervals = all_stimuli(beha_data)
            l_target_intervals = zip(l_target_intervals, l_target_intervals[1:])
            left_data = rate_in(l_target_intervals, left_timestamps)
            right_data = rate_in(l_target_intervals, right_timestamps)
            relative_rate = [l/(r+l) if r+l > 0 else np.nan for l, r in zip(left_data, right_data)]
            data.append(relative_rate[cycles_set])

        elif 'red_blue_onsets' in target_intervals:
            l_target_intervals = stimuli_onset(beha_data)
            red_intervals = zip(l_target_intervals[0], l_target_intervals[1])
            blue_intervals = zip(l_target_intervals[1], l_target_intervals[0][1:])

            left_red_data = rate_in(red_intervals, left_timestamps)
            right_red_data = rate_in(red_intervals, right_timestamps)
            relative_rate_positive = [l/(r+l) if r+l > 0 else np.nan for l, r in zip(left_red_data, right_red_data)]

            left_blue_data = rate_in(blue_intervals, left_timestamps)
            right_blue_data = rate_in(blue_intervals, right_timestamps)
            relative_rate_negative = [l/(r+l) if r+l > 0 else np.nan for l, r in zip(left_blue_data, right_blue_data)]
            data.append((relative_rate_positive, relative_rate_negative))

    return data

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