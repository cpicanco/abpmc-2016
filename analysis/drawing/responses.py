# -*- coding: utf-8 -*-
'''
	Copyright (C) 2016 Rafael Picanço.

	The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

	You should have received a copy of the GNU General Public License
	along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

# plot timestamped events using a cumulative frequency graph

import sys, os
from glob import glob

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from drawing import temporal_perfil
from methods import all_responses,stimuli_onset,load_data

def draw_single(src_dir, show=True):
	print os.path.dirname(src_dir)
	ID = os.path.basename(os.path.dirname(src_dir))
	paths = sorted(glob(os.path.join(src_dir,'0*')))
	# global vars
	data = []
	ymax = []
	for path in paths:

			be = load_data(os.path.join(path,"behavioral_events.txt"))
			responses = all_responses(be)
			data.append((stimuli_onset(be), responses))

			ymax.append(len(responses))

	ymax = np.amax(ymax)
	x_label = 'Ciclos'
	y_label = 'Taxa (respostas por segundo)'
	title = 'Particip. '+ID+': taxa de resp. durante as cores Verm. e Azul.'

	n_plots = len(paths)
	if n_plots == 1:
			figsize = (4, 4)
	elif n_plots == 2:
			figsize = (8, 4)
	elif n_plots == 3:
			figsize = (12, 4)
	else:
			figsize = (14, 4)

	# figure.add_axes([0.1, 0.1, 0.8, 0.8], frameon = 0)
	figure, axarr = plt.subplots(1, n_plots, sharey=True, sharex=False, figsize=figsize) 
	figure.suptitle(title);
	figure.text(0.5, 0.02, x_label)
	#figure.text(0.014, 0.5, y_label, rotation='vertical',verticalalignment='center',horizontalalignment='right')

	for i, d in enumerate(data):
			(onsets, responses) = d
			temporal_perfil(axarr[i], onsets, responses)
			#plt.xlim(xmax = 300)

	axarr[0].set_ylabel(y_label)
	# axarr[0].legend(loc='upper right')
	# axarr[1].set_xlabel(x_label)
	#plt.ylim(ymax = ymax, ymin = 0)
	#plt.text(-16,4,ID,fontsize=18)
	#figure.subplots_adjust(wspace=0.05,left=0.05, right=.98,bottom=0.1,top=0.92)
	figure.tight_layout()
	
	# save/plot figure
	if show:
		plt.show()