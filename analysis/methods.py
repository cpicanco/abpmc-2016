# -*- coding: utf-8 -*-
'''
    Copyright (C) 2017 Rafael Picanço.

    The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import os
from glob import glob

import numpy as np

import constants as K

# correction methods
##############

def remove_outside_screen(data, xmax=1, ymax=1, horizontal=True):
    if horizontal:
        x = (0 <= data[0, :]) & (data[0, :] < xmax)
        y = (0 <= data[1, :]) & (data[1, :] < ymax)
        mask = x & y
        data_clamped = data[:, mask]
        deleted_count = data.shape[1] - data_clamped.shape[1]
    else:
        x = (0 <= data[:, 0]) & (data[:, 0] < xmax)
        y = (0 <= data[:, 1]) & (data[:, 1] < ymax)
        mask = x & y
        data_clamped = data[mask, :]
        deleted_count = data.shape[0] - data_clamped.shape[0]

    if deleted_count > 0:
        print("\nRemoved", deleted_count, "data point(s) with out-of-screen coordinates!")
    return data_clamped, mask

# def remove_out_of_screen(data,xmax=1,ymax=1):
#     for line in data:
#         x = (0 <= line['x_norm'][0, :]) and (data[0, :] < xmax) 

# convertion methods
##############

def normalized_to_pixel(gp):
    """
    gp:numpy.array.shape(x, 2)
    """
    gp[:,0] *= K.SCREEN_WIDTH_PX
    gp[:,1] *= K.SCREEN_HEIGHT_PX
    return gp

def pixel_to_degree(gp):
    """
    gp:numpy.array.shape(x, 2)
    """
    gp[:,0] /= K.PIXELS_PER_DEGREE
    gp[:,1] /= K.PIXELS_PER_DEGREE
    return gp

# def normalized_to_degree(gp):
#     """
#     gp:numpy.array.shape(x, 2)
#     """
#     values_per_degree = get_values_per_degree(K.SCREEN_WIDTH_DEG,K.SCREEN_HEIGHT_DEG)
#     gp[:,0] /= values_per_degree
#     gp[:,1] /= values_per_degree
#     return gp

def move_mean_to_zero(gp):
    """
    gp:numpy.array.shape(x, 2)
    """
    MX = np.mean(gp[:,0])
    MY = np.mean(gp[:,1])
    gp[:,0] = MX - gp[:,0]
    gp[:,1] = MY - gp[:,1]
    return gp



# analytics methods
############################

def root_mean_square(gp):
    """
    gp:numpy.array.shape(x, 2)
    """
    RMSX = np.sqrt(np.mean(gp[:,0]**2))
    RMSY = np.sqrt(np.mean(gp[:,1]**2))
    # return np.sqrt((RMSX**2)+(RMSY**2))
    return np.sqrt(np.mean(gp**2)), RMSX,RMSY



# data handle methods
############################

def rate_in(time_interval_pairwise,timestamps):
    def is_inside(timestamps,rangein, rangeout):
        return [t for t in timestamps if (t >= rangein) and (t <= rangeout)]

    return [len(is_inside(timestamps, begin, end))/(end-begin) for begin, end in time_interval_pairwise]

def switching_timestamps(all_gaze_data, left_gaze_mask, right_gaze_mask):
    # changeover_mask = left_gaze_mask | right_gaze_mask

    # all_gaze_data[left_gaze_mask]['time']
    changeover_mask = left_gaze_mask | right_gaze_mask 
    filtered_all_gaze = all_gaze_data[changeover_mask]
    filtered_left_gaze = left_gaze_mask[changeover_mask]

    filtered_changeover_mask = [True if a != b else False for a, b in zip(filtered_left_gaze,filtered_left_gaze[1:])]
    filtered_changeover_mask.append(False)
    filtered_changeover_mask = np.array(filtered_changeover_mask)
    switchings = filtered_all_gaze[filtered_changeover_mask]['time']
    print('Left-Right switchings:%d'%switchings.shape[0])
    return switchings

# stimuli timestamps
def color_pair(behavioral_data, pair):  
    """
        behavioral_data: np.genfromtxt object; "behavioral_events.txt" as path
    """
    def all_events(stimulus_code):
        return [line['time'] for line in behavioral_data if line['event'] == stimulus_code]
      
    return [[all_events('1a'), all_events('1b')],
            [all_events('1b'), all_events('2a')],
            [all_events('2a'), all_events('2b')],
            [all_events('2b'), all_events('1a')[1:]]][pair]

def stimuli_onset(behavioral_data):  
    """
        behavioral_data: np.genfromtxt object; "behavioral_events.txt" as path
    """
    def all_events(stimulus_code):
        return [line['time'] for line in behavioral_data if line['event'] == stimulus_code]
        
    return [all_events('1a'), all_events('2a')] # [[R1,R2,R3,..],[B1,B2,B3,..]] 

def all_stimuli(behavioral_data):
    """
        behavioral_data: np.genfromtxt object; "behavioral_events.txt" as path
    """
    return [line['time'] for line in behavioral_data if line['event_type'] == 'stimulus']

# responses timestamps
def all_responses(behavioral_data): 
    """
        behavioral_data: np.genfromtxt object; "behavioral_events.txt" as path
    """
    return [line['time'] for line in behavioral_data if line['event_type'] == 'response']

# file methods
############################

def load_data(path, delimiter="\t"):
    if not os.path.isfile(path):
        print(path)
        raise IOError(path+": was not found.")

    return np.genfromtxt(path, delimiter=delimiter,missing_values=["NA"],
        filling_values=None,names=True, autostrip=True, dtype=None)

def get_data_path():
    data_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(data_path)

def get_filenames(target_experiment, target_datafile):
    data_path = get_data_path()

    if 'dizzy-timers' in target_experiment:
        target_root = K.INNER_PATHS

    if 'eye-orientation' in target_experiment:
        target_root = K.INNER_PATHS_24

    filenames = []
    for inner_path in target_root:
        a_data_path = os.path.join(data_path,inner_path) 
        paths = sorted(glob(os.path.join(a_data_path,'0*')))
        paths = [os.path.join(data_path,path) for path in paths] 
        [filenames.append(os.path.join(filename,target_datafile)) for filename in paths]
           
    return filenames