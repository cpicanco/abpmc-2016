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

def ellipse(center, width, height, n = 360):
    thetas = [np.pi*2 * i/n for i in range(n)]
    points = [(center[0] + np.cos(t) * width, center[1] + np.sin(t) * height) for t in thetas]
    return np.array(points)

def get_pixels_per_degree(sw_px,sh_px,sw_d,sh_d):
    return np.sqrt((sw_px**2)+(sh_px**2))/np.sqrt((sw_d**2)+(sh_d**2))

def get_values_per_degree(sw_d,sh_d):
    return np.sqrt((1**2)+(1**2))/np.sqrt((sw_d**2)+(sh_d**2))

# size of the screen monitor, in pixels; used as real values of the screen surface 
SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX = 1280,768
SCREEN_PX = (SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX)

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

SQUARE_LEFT_TOP = (362., 319.)
CIRCLE_LEFT_TOP = (789., 319.)
S_SIZE = (130., 130.)

class Circle(object):
    """Right Circle"""
    def __init__(self,position='right',size=S_SIZE, normalized=SCREEN_PX):           
        if normalized is None:
            screen = (1, 1)
        else:
            screen = normalized

        if 'right' in position:
            left=CIRCLE_LEFT_TOP[0]
            top=CIRCLE_LEFT_TOP[1]
        elif 'left' in position:
            left=SQUARE_LEFT_TOP[0]
            top=SQUARE_LEFT_TOP[1]

        self.Left = left/screen[0]
        self.Top = top/screen[1]
        self.Radius = [(size[0]/screen[0])/2, (size[1]/screen[1])/2]
        self.Width =  size[0]/screen[0]
        self.Height = size[1]/screen[1]
        self.Center = ((left+(size[0]/2))/screen[0], (top+(size[1]/2))/screen[1])

    def Points(self, factor=1.):
        self.Radius[0] *= factor
        self.Radius[1] *= factor
        self.Width = self.Radius[0]*2
        self.Height = self.Radius[1]*2
        self.Left = self.Center[0]-self.Radius[0]
        self.Top = self.Center[1]-self.Radius[1]
        return ellipse(self.Center, self.Radius[0], self.Radius[1])
     
class Square(object):
    """Left Square"""
    def __init__(self,
            left=SQUARE_LEFT_TOP[0], top=SQUARE_LEFT_TOP[1],
            right=SQUARE_LEFT_TOP[0]+S_SIZE[0], bottom=SQUARE_LEFT_TOP[1]+S_SIZE[1],
            size=S_SIZE, normalized=SCREEN_PX):           
        if normalized is None:
            screen = (1, 1)
        else:
            screen = normalized
        self.Left = left/screen[0]
        self.Top = top/screen[1]
        self.Right = right/screen[0]
        self.Bottom = bottom/screen[1]
        self.Width =  size[0]/screen[0]
        self.Height = size[1]/screen[1]

    def Points(self, factor=0):
        self.Left += factor
        self.Top += factor
        self.Right -= factor
        self.Bottom -= factor
        self.Width += factor*2
        self.Height += factor*2 
        return np.array([
            [self.Left, self.Top],
            [self.Right, self.Top],
            [self.Right, self.Bottom],
            [self.Left, self.Bottom]
        ])

# Targets
BLUE_LEFT = '#011EFE'
RED_LEFT = '#FE0000'

# Distractors
GREEN_RIGHT = '#49AC15' 
CYAN_RIGHT = '#A8E6CF' 

CIRCLE = Circle()
SQUARE = Square()
# physical measurements of the screen projection in degrees of the participant's visual angle
# SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG = 15.3336085236, 9.15224758754
# SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG = 16.5942899397, 9.90471680774
SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG = get_visual_angle(SCREEN_WIDTH, SCREEN_DISTANCE)

PIXELS_PER_DEGREE = get_pixels_per_degree(SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX, SCREEN_WIDTH_DEG, SCREEN_HEIGHT_DEG)

if __name__ == '__main__':
    print('width_deg:', SCREEN_WIDTH_DEG, 'height_deg', SCREEN_HEIGHT_DEG)
    print('room_lux:',ROOM_LUX)
