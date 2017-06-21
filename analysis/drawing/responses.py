# -*- coding: utf-8 -*-
'''
    Copyright (C) 2016 Rafael Picanço.

    The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

# red and blue temporal perfil
# plot button response rate during red and during blue along time

import sys, os
from glob import glob

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

sys.path.append('../../analysis')
from drawing import temporal_perfil
from methods import all_responses,stimuli_onset,load_data,rate_in

def draw_single(src_dir, show=True):
    print(os.path.dirname(src_dir))
    ID = os.path.basename(os.path.dirname(src_dir))
    paths = sorted(glob(os.path.join(src_dir,'0*')))

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

    figure, axarr = plt.subplots(1, n_plots, sharey=True, sharex=False, figsize=figsize) 
    figure.suptitle(title);
    figure.text(0.5, 0.02, x_label)
    for i, d in enumerate(data):
        (onsets, responses) = d
        temporal_perfil(axarr[i], onsets, responses)

    axarr[0].set_ylabel(y_label)
    figure.tight_layout()
    
    # save/plot figure
    if show:
        plt.show()

def draw_single_proportion(src_dir, show=True):
    print(os.path.dirname(src_dir))
    ID = os.path.basename(os.path.dirname(src_dir))
    paths = sorted(glob(os.path.join(src_dir,'0*')))

    data = []
    ymax = 1
    x_label = 'Successive cycles'
    y_label = 'Button-pressing proportion'
    title = ID
    figure, axarr = plt.subplots(1, 3, sharey=True, sharex=True, figsize=(9, 3)) 
    # figure.suptitle(title);
    # figure.text(0.5, 0.02, x_label)
    for path, axis in zip(paths,axarr):

        beha_data = load_data(os.path.join(path,"behavioral_events.txt"))
        target_intervals = stimuli_onset(beha_data)
        red_intervals = zip(target_intervals[0], target_intervals[1])
        blue_intervals = zip(target_intervals[1], target_intervals[0][1:])
        responses = all_responses(beha_data)
        
        red_data = rate_in(red_intervals, responses)
        blue_data = rate_in(blue_intervals, responses)

        relative_rate = [r/(r+b) if r+b > 0 else None for r, b in zip(red_data, blue_data)]
        axis.plot(relative_rate,color="k", label="Right")

        # remove outer frame
        axis.spines['top'].set_visible(False)
        axis.spines['bottom'].set_visible(False)
        axis.spines['left'].set_visible(False)
        axis.spines['right'].set_visible(False)

        axis.set_ylim(0.,1.)
        axis.set_xlim(-0.5, len(relative_rate)+0.5)
        axis.set_xticklabels([x for x in range(-1,len(relative_rate)+1,2)])
        
        #remove ticks
        axis.xaxis.set_ticks_position('none')
        axis.yaxis.set_ticks_position('none')


    axarr[0].set_ylabel(y_label)
    axarr[0].spines['left'].set_visible(True)
    axarr[1].set_xlabel(x_label)
    figure.tight_layout()
    
    # save/plot figure
    if show:
        plt.show()

if __name__ == '__main__':
    from constants import INNER_PATHS
    from methods import get_data_path

    filenames = [os.path.join(get_data_path(),filename) for filename in INNER_PATHS]
    for filename in filenames:
        print(filename)

        # output folder
        draw_single_proportion(filename)