# -*- coding: utf-8 -*-
'''
	Copyright (C) 2016 Rafael Picanço.

	The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

	You should have received a copy of the GNU General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
# python
import os

# third party
import matplotlib

# self 
from constants import INNER_PATHS
from drawing import save_all 
from drawing.eye_movements import draw_single as draw_single_gaze # NOTE: xy must be normalized
from drawing.responses import draw_single as draw_single_responses

# matplotlib configurations 
font = {'family' : 'serif',
		'size'   : 16}
matplotlib.rc('font', **font)

# assign the root data folder
data_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.dirname(data_path)

# save all figures inside its respective data folder
# save_all(data_path,draw_single_gaze,'taxa_movimentos_oculares_A.png')
# save_all(data_path,draw_single_responses,'taxa_de_respostas_ao_botao_A.png')

# show single figure
ip = INNER_PATHS[0]
draw_single_responses(os.path.join(data_path, ip))
draw_single_gaze(os.path.join(data_path, ip))

# from helpers import delete_from_inner_paths
# from helpers import copy_to_inner_paths
# filenames = ['README.md']
# frompath = os.path.join(data_path,'[CHANGE-ME]')
# copy_to_inner_paths(data_path, frompath, filenames)
# delete_from_inner_paths(data_path, filenames)