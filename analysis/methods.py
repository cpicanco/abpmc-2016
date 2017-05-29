# -*- coding: utf-8 -*-
'''
	Copyright (C) 2017 Rafael Picanço.

	The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

	You should have received a copy of the GNU General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
from os.path import isfile

import numpy as np
import constants as K

# correction methods
##############

def remove_outside_screen(data, xmax=1, ymax=1):
    x = (0 <= data[0, :]) & (data[0, :] < xmax)
    y = (0 <= data[1, :]) & (data[1, :] < ymax)
    print(data.shape)
    data_clamped = data[:, x & y]
    deleted_count = data.shape[1] - data_clamped.shape[1]
    if deleted_count > 0:
        print "\nRemoved", deleted_count, "data point(s) with", \
        "out-of-screen coordinates!"
    return data_clamped

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

# stimuli timestamps
def color_pair(behavioral_data, pair):  
	"""
		behavioral_data: np.genfromtxt object; "behavioral_events.txt" as path
	"""
	def all_events(string):
		return [line['time'] for line in behavioral_data if line['event'] == string]
		
	return [[all_events('1a'), all_events('1b')],
	        [all_events('1b'), all_events('2a')],
	        [all_events('2a'), all_events('2b')],
	        [all_events('2b'), all_events('1a')[1:]]][pair]

def stimuli_onset(behavioral_data):  
	"""
		behavioral_data: np.genfromtxt object; "behavioral_events.txt" as path
	"""
	def all_events(string):
		return [line['time'] for line in behavioral_data if line['event'] == string]
		
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

def load_data(path):
	if not isfile(path):
		print path
		raise IOError, path+": was not found."

	return np.genfromtxt(path, delimiter="\t",missing_values=["NA"],
		filling_values=None,names=True, autostrip=True, dtype=None)