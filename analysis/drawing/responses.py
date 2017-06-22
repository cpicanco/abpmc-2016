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

from constants import INNER_PATHS,INNER_PATHS_DISCRIMINATION
from methods import get_data_path

from categorization import relative_rate_blue_red

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

        relative_rate = [r/(r+b) if r+b > 0 else np.nan for r, b in zip(red_data, blue_data)]
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

def draw_proportions(cycles_set=slice(0,9),show=True, output_path=None):
    def get_axis_limits(ax, xscale=.45,yscale=0.05):
        """
        https://stackoverflow.com/questions/24125058/add-label-to-subplot-in-matplotlib
        """
        return ax.get_xlim()[1]*xscale, ax.get_ylim()[1]*yscale

    filenames = [os.path.join(get_data_path(), filename) for filename in INNER_PATHS if filename in INNER_PATHS_DISCRIMINATION]
    data = np.array([relative_rate_blue_red(filename,cycles_set) for filename in filenames])
    
    x_label = 'Successive cycles'
    y_label = 'Button-pressing proportion'
    figure, axarr = plt.subplots(1, 3, sharey=True, sharex=False, figsize=(6, 3)) 
    cycles_list = range(0,data.shape[2])
    for condition, axis in zip(range(0,3), axarr):
        data_means = np.array([np.nanmean(data[:, condition, cycles]) for cycles in cycles_list])
        data_min = np.array([np.nanmin(data[:, condition, cycles]) for cycles in cycles_list])
        data_max = np.array([np.nanmax(data[:, condition, cycles]) for cycles in cycles_list])

        axis.plot(data_means, color='k') 
        axis.plot((-0.5,len(data_means)-1+0.5), (0.5,0.5), color='k', ls='dotted', alpha=0.3)   
        axis.errorbar(np.arange(len(data_means)), data_means,
            [data_means-data_min,data_max-data_means],
            fmt='.k', ecolor='k', lw=1,alpha=0.3)

        axis.set_xlim([-0.5,len(data_means)-1 +0.5])
        # remove outer frame
        axis.spines['top'].set_visible(False)
        axis.spines['bottom'].set_visible(False)
        axis.spines['left'].set_visible(False)
        axis.spines['right'].set_visible(False)

        lowx, highx = axis.get_xlim()
        axis.yaxis.set_ticks(np.arange(0, 1.1, 0.25))
        axis.xaxis.set_ticks([0,8])

        #remove ticks
        axis.xaxis.set_ticks_position('none')
        axis.yaxis.set_ticks_position('none')

    size = 14
    axarr[0].set_ylabel(y_label)
    axarr[0].spines['left'].set_visible(True)
    axarr[0].annotate('A', xy=get_axis_limits(axarr[0]), size=size)

    axarr[1].set_xlabel(x_label)
    axarr[1].annotate('B', xy=get_axis_limits(axarr[1]), size=size)

    axarr[2].annotate('A', xy=get_axis_limits(axarr[2]), size=size)

    offset = 0
    x = 1
    for axis in axarr:
        axis.set_xticklabels([x+offset,9+offset])
        offset = offset + 9

    figure.tight_layout()
    figure.subplots_adjust(wspace=0.05)

    # bw = 0.26
    # w = .28
    # size = 14
    # figure.text(bw, 0.25, 'A',size=size)
    # figure.text(bw+w, 0.25, 'B',size=size)
    # figure.text(bw+(w*2), 0.25, 'A',size=size)

    if output_path:
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()
    else:
    # save/plot figure
        if show:
            plt.show()

# def draw_proportions():
#     from constants import INNER_PATHS
#     from methods import get_data_path

#     filenames = [os.path.join(get_data_path(), filename) for filename in INNER_PATHS]
#     data = np.array([relative_rate_blue_red(filename) for filename in filenames])
#     print(data.shape)
#     data_means = np.array([np.mean(data[:, condition, cycles]) for condition in range(0,3) for cycles in range(0,8)])
#     data_min = np.array([np.min(data[:, condition, cycles]) for condition in range(0,3) for cycles in range(0,8)])
#     data_max = np.array([np.max(data[:, condition, cycles]) for condition in range(0,3) for cycles in range(0,8)])

#     axis = plt.gca()
#     plt.plot(data_means, color='k')    
#     plt.errorbar(np.arange(len(data_means)),
#         data_means,
#         [data_means-data_min,data_max-data_means],
#         fmt='k', ecolor='gray', lw=1)
#     plt.show()   

if __name__ == '__main__':
    # from constants import INNER_PATHS
    # from methods import get_data_path

    # filenames = [os.path.join(get_data_path(), filename) for filename in INNER_PATHS if filename in INNER_PATHS_DISCRIMINATION]
    # for filename in filenames:
    #     print(filename)
    #     draw_single_proportion(filename)

    draw_proportions()
    # draw_proportions(output_path=os.path.join(get_data_path(),'button_press.png'))