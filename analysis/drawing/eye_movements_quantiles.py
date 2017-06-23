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

from categorization import relative_rate_switching, rate_switching

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

        left_gaze_mask, right_gaze_mask = gaze_mask_left_right(all_data)
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

def draw_single_switching_rate(src_dir, show=True):
    print(os.path.dirname(src_dir))
    ID = os.path.basename(os.path.dirname(src_dir))
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    x_label = 'Successive cycles'
    y_label = 'Switchings per second'
    # title = ID
    figure, axarr = plt.subplots(1, 3, sharey=True, sharex=True, figsize=(9, 3)) 
    # figure.suptitle(title);
    data = rate_switching(src_dir,slice(0,9))
    for (red_rate, blue_rate, br_sum), axis in zip(data,axarr):
        axis.plot(red_rate,ls='dashed', color="k",marker='x')
        axis.plot(blue_rate,color="k", label="S-",marker='.')

        # remove outer frame
        axis.spines['top'].set_visible(False)
        axis.spines['bottom'].set_visible(False)
        axis.spines['left'].set_visible(False)
        axis.spines['right'].set_visible(False)

        (_, top) = axis.get_ylim()
        axis.set_ylim(0.,top+(top/10.))
        axis.set_xlim(-0.5, 9+0.5)
        axis.set_xticklabels([x for x in range(-1,9+1,2)])
        
        #remove ticks
        axis.xaxis.set_ticks_position('none')
        axis.yaxis.set_ticks_position('none')
        axis.text(.45,.9,r'$\sum$=%d'%br_sum,transform = axis.transAxes)

    # specificities
    # (red_rate, blue_rate, _) = data[0]
    # axarr[0].text(9,red_rate[0],"S+")
    # axarr[0].text(9,blue_rate[-1],"S-")
    axarr[0].set_ylabel(y_label)
    axarr[0].spines['left'].set_visible(True)
    axarr[1].set_xlabel(x_label)
    figure.tight_layout()
    figure.text(.15, .85, ID)

    # save/plot figure
    if show:
        plt.show()
    else:
        plt.savefig(os.path.join(src_dir,'switchings.png'), bbox_inches='tight')
        plt.close()

def draw_single_switching_proportion(src_dir, show=True):
    print(os.path.dirname(src_dir))
    ID = os.path.basename(os.path.dirname(src_dir))
    paths = sorted(glob(os.path.join(src_dir,'0*')))
    x_label = 'Successive cycles'
    y_label = 'S+ switching proportion'
    # title = ID
    figure, axarr = plt.subplots(1, 3, sharey=True, sharex=True, figsize=(9, 3)) 
    # figure.suptitle(title);
    data = relative_rate_switching(src_dir,slice(0,8))
    for relative_rate, axis in zip(data,axarr):

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

    filenames = [os.path.join(get_data_path(), filename) for filename in INNER_PATHS]
    for filename in filenames:
        print(filename)
        draw_single_switching_rate(filename, False)

    # from drawing.eye_movements_quantiles import draw_single as draw_gaze_quantiles # NOTE: xy must be normalized
    # from drawing.responses import draw_single as draw_responses

    # data_path = get_data_path()
    # for path in INNER_PATHS:
    #     # draw_responses(os.path.join(data_path, path))
    #     draw_gaze_quantiles(os.path.join(data_path, path))
    #     break
        