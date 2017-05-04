# -*- coding: utf-8 -*-
'''
  Copyright (C) 2016 Rafael Picanço.

  The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import math
import numpy as np
import os

def get_pixels_per_degree(sw_px,sh_px,sw_d,sh_d):
    return np.sqrt((sw_px**2)+(sh_px**2))/np.sqrt((sw_d**2)+(sh_d**2))

def get_values_per_degree(sw_d,sh_d):
    return np.sqrt((1**2)+(1**2))/np.sqrt((sw_d**2)+(sh_d**2))

# size of the screen monitor, in pixels; used as real values of the screen surface 
SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX = 1280,768

# http://en.wikipedia.org/wiki/Visual_angle
def get_visual_angle(sw,sd,screen_width_px=SCREEN_WIDTH_PX,screen_height_px=SCREEN_HEIGHT_PX):
    """
    sw :screen width in cm
    sd :screen distance in cm

    """
    V = 2 * math.atan(sw/(sd*2))
    # print 'Radians:', V
    degrees = math.degrees(V)

    # x, y
    return degrees, (screen_height_px*degrees)/screen_width_px

INNER_PATHS_24 = [
    'P000'+os.path.sep+'2015-05-13' # 1280,768
]

INNER_PATHS = [
    'P001'+os.path.sep+'2015-05-19', # 1280,768
    'P001'+os.path.sep+'2015-05-27',
    'P002'+os.path.sep+'2015-05-19',
    'P002'+os.path.sep+'2015-05-20',
    'P003'+os.path.sep+'2015-05-20',
    'P004'+os.path.sep+'2015-05-20',
    'P005'+os.path.sep+'2015-05-19',
    'P006'+os.path.sep+'2015-05-25',
    'P007'+os.path.sep+'2015-05-25',
    'P008'+os.path.sep+'2015-05-26',
    'P009'+os.path.sep+'2015-05-26',
    'P010'+os.path.sep+'2015-05-26'
]

ROOM_LOW_AREA = 15.0 # square metters

# 4 X GE ( F32T8/BF ), 4100K
LIGHT_INITIAL_LUMENS = 2600 # estimated from F32T8/SP
LIGHT_DESIGN_LUMENS = 2400 # estimated from F32T8/SP
ROOM_LUX = (LIGHT_DESIGN_LUMENS * 2.0)/ROOM_LOW_AREA

# object size, in cm
SCREEN_WIDTH = 70.0

# how far the object was from the participant's head, in cm
SCREEN_DISTANCE = 240.0

# physical measurements of the screen projection in degrees of the participant's visual angle
# SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG = 15.3336085236, 9.15224758754
# SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG = 16.5942899397, 9.90471680774
SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG = get_visual_angle(SCREEN_WIDTH, SCREEN_DISTANCE)

PIXELS_PER_DEGREE = get_pixels_per_degree(SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX, SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG)

if __name__ == '__main__':
    print 'width_deg:', SCREEN_WIDTH_DEG, 'height_deg', SCREEN_HEIGHT_DEG
    print 'room_lux:',ROOM_LUX