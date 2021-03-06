# -*- coding: utf-8 -*-
'''
  Copyright (C) 2017 Rafael Picanço.

  The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

# note: fps should be as constant as possible

# eye movements temporal perfil
# plot eye movements rate at
  # each color during
  # each presentation schema:
    # colorA-colorB, colorA-colorC, colorD-colorC. colorD-colorB... and so on

import os

if __name__ == '__main__':
    import sys
    sys.path.append('../../analysis')

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
#from sklearn.preprocessing import StandardScaler
from glob import glob
from methods import load_data, stimuli_onset, all_stimuli, color_pair
from drawing import temporal_perfil
from constants import BLUE_LEFT, RED_LEFT, GREEN_RIGHT, CYAN_RIGHT

def categorize_timestamps(src_timestamps, dbsc):
    clusters = {}
    labels = dbsc.labels_
    core_samples_mask = np.zeros_like(labels, dtype = bool)
    core_samples_mask[dbsc.core_sample_indices_] = True

    unique_labels = set(labels)
    for k in unique_labels:
        class_member_mask = (labels == k)

        # cluster
        timestamps = src_timestamps[class_member_mask & core_samples_mask]
        clusters['cluster_'+str(int(k))] = timestamps

        # noise
        timestamps = src_timestamps[class_member_mask & ~core_samples_mask]
        clusters['noise_'+str(int(k))] = timestamps
    return clusters

def categorize_masks(src_timestamps, dbsc):
    masks = {}
    labels = dbsc.labels_
    core_samples_mask = np.zeros_like(labels, dtype = bool)
    core_samples_mask[dbsc.core_sample_indices_] = True

    unique_labels = set(labels)
    for k in unique_labels:
        class_member_mask = (labels == k)

        # cluster
        masks['cluster_'+str(int(k))] = class_member_mask & core_samples_mask

        # noise
        masks['noise_'+str(int(k))] = class_member_mask & ~core_samples_mask
    return masks

def plot_dbscan(src_xy, dbsc, doplot=True):
    dictionary = {}
    labels = dbsc.labels_
    core_samples_mask = np.zeros_like(labels, dtype = bool)
    core_samples_mask[dbsc.core_sample_indices_] = True

    # Black removed; it is used for noise instead.
    unique_labels = set(labels)
    # print "labels:",unique_labels
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'

        class_member_mask = (labels == k)

        # clusters
        xy = src_xy[class_member_mask & core_samples_mask]
        if doplot:
            plt.plot(xy[:,0], xy[:,1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=3, label=str(int(k)))
        dictionary['cluster_'+str(int(k))] = xy

        # noise
        xy = src_xy[class_member_mask & ~core_samples_mask]
        if doplot:
            plt.plot(xy[:,0], xy[:,1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=1)
    if doplot:
        axes = plt.gca()
        axes.set_ylim(ymax = 1, ymin = 0)
        axes.set_xlim(xmax = 1, xmin = 0)
        axes.legend()
        # plt.axis('equal')
        plt.title('')
        plt.show()

    return dictionary

def draw_single(src_dir, show=True):
    ID = os.path.basename(os.path.dirname(src_dir))
    basepath = os.path.dirname(os.path.dirname(src_dir))

    print(src_dir)
    print(ID)
    print(basepath)

    if src_dir == os.path.join(basepath,'P001/2015-05-19'):
        data = [{'eps':0.07, 'min_samples':370},
                {'eps':0.06, 'min_samples':1000}]

    elif src_dir == os.path.join(basepath,'P001/2015-05-27'):
        data = [{'eps':0.02, 'min_samples':1000},
                {'eps':0.02, 'min_samples':1000},
                {'eps':0.02, 'min_samples':1000}]

    elif src_dir == os.path.join(basepath,'P002/2015-05-19'):
        data = [{'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000}]

    elif src_dir == os.path.join(basepath,'P002/2015-05-20'):
        data = [{'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':500}]

    elif src_dir == os.path.join(basepath,'P003/2015-05-20'):
        data = [{'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':800}]

    elif src_dir == os.path.join(basepath,'P004/2015-05-20'):
        data = [{'eps':0.06, 'min_samples':1500},
                {'eps':0.06, 'min_samples':1500},
                {'eps':0.06, 'min_samples':1500}]

    elif src_dir == os.path.join(basepath,'P005/2015-05-19'):
        data = [{'eps':0.08, 'min_samples':500},
                {'eps':0.07, 'min_samples':500},
                {'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000}]

    elif src_dir == os.path.join(basepath,'P006/2015-05-25'):
        data = [{'eps':0.065, 'min_samples':1700},
                {'eps':0.065, 'min_samples':1300},
                {'eps':0.065, 'min_samples':1200}]


    elif src_dir == os.path.join(basepath,'P007/2015-05-25'):
        data = [{'eps':0.06, 'min_samples':1200},
                {'eps':0.06, 'min_samples':1200},
                {'eps':0.06, 'min_samples':1200}]

    elif src_dir == os.path.join(basepath,'P008/2015-05-26'):
        data = [{'eps':0.06, 'min_samples':1200},
                {'eps':0.06, 'min_samples':1200},
                {'eps':0.06, 'min_samples':1200}]

    elif src_dir == os.path.join(basepath,'P009/2015-05-26'):
        data = [{'eps':0.06, 'min_samples':1700},
                {'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000},
                {'eps':0.06, 'min_samples':1000}]

    elif src_dir == os.path.join(basepath,'P010/2015-05-26'):
        data = [{'eps':0.06, 'min_samples':600},
                {'eps':0.06, 'min_samples':600},
                {'eps':0.06, 'min_samples':600},
                {'eps':0.06, 'min_samples':600}]

    paths = sorted(glob(os.path.join(src_dir,'0*')))
    for i, path in enumerate(paths):    
        data_folder = os.path.join(src_dir, path)
        beha_events_path = os.path.join(data_folder, "behavioral_events.txt")
        gaze_events_path = os.path.join(data_folder, 'gaze_positions.csv')
        
        gaze_data = load_data(gaze_events_path,',')

        data[i]['beha_data'] = load_data(beha_events_path)

        # DBSCAN expects data with shape (-1,2), we need to transpose ours first
        data[i]['src_xy'] = np.array([gaze_data['x_norm'], gaze_data['y_norm']]).T

        data[i]['dbsc'] = DBSCAN(eps=data[i]['eps'], min_samples=data[i]['min_samples']).fit(data[i]['src_xy'])
        data[i]['points_categorized'] = plot_dbscan(data[i]['src_xy'], data[i]['dbsc'])

        data[i]['masks'] = categorize_masks(data[i]['src_xy'], data[i]['dbsc'])

        data[i]['src_timestamps'] = gaze_data['time']
        data[i]['time_categorized'] = categorize_timestamps(data[i]['src_timestamps'],data[i]['dbsc'])

    x_label = 'Ciclo'
    y_label = 'dir. < Taxa (gaze/s) > esq.'
    title = 'Particip. '+ID+': Taxa de movim. oculares durante cada cor'

    n_plots = len(data)
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

    # look rate (left) 
    # look rate (right)
    
    for i, d in enumerate(data):
        turnover_count = 0
        turnover = [a for a,b in zip(d['masks']['cluster_0'],d['masks']['cluster_1']) if a or b]
        for c, n in zip(turnover,turnover[1:]):
            if c != n:
                turnover_count += 1
        print('\n','turnover_count:',turnover_count)

        left_right_xy = []
        left_right_timestamps = []
        for ttime, points in zip (d['time_categorized'].iteritems(),d['points_categorized'].iteritems()):
            _, xy = points

            time_key, timestamps = ttime 
            print(time_key, len(timestamps), len(xy))
            if len(timestamps) > 0 and 'cluster' in time_key:
                left_right_timestamps.append(timestamps)
                left_right_xy.append(xy)

        if np.mean(left_right_xy[0][0]) > np.mean(left_right_xy[1][0]):
            left_right_xy = [left_right_xy[1],left_right_xy[0]]
            left_right_timestamps = [left_right_timestamps[1],left_right_timestamps[0]]
        else:
            left_right_xy = [left_right_xy[0],left_right_xy[1]]
            left_right_timestamps = [left_right_timestamps[0],left_right_timestamps[1]]


        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],0), left_right_timestamps[0],'pair', c1=RED_LEFT, nsize=0)
        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],0), left_right_timestamps[1],'pair', c1=GREEN_RIGHT, nsize=0, doreversed=True)

        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],1), left_right_timestamps[0],'pair', c1=RED_LEFT, nsize=1)
        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],1), left_right_timestamps[1],'pair', c1=CYAN_RIGHT, nsize=1, doreversed=True)

        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],2), left_right_timestamps[0],'pair', c1=BLUE_LEFT, nsize=2)
        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],2), left_right_timestamps[1],'pair', c1=CYAN_RIGHT, nsize=2, doreversed=True)
                        
        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],3), left_right_timestamps[0],'pair', c1=BLUE_LEFT, nsize=3)
        temporal_perfil(axarr[i],color_pair(data[i]['beha_data'],3), left_right_timestamps[1],'pair', c1=GREEN_RIGHT, nsize=3, doreversed=True)
        
    ticks = [30,20,10,0,10,20,30]
    axarr[0].set_yticklabels(labels=ticks)

    plt.ylim(ymin = -30)
    plt.ylim(ymax = 30)

    axarr[0].set_ylabel(y_label)
    figure.tight_layout()
    if show:            
        plt.show()

def len_clusters(dbscan):
    labels = dbscan.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    return n_clusters_

def guess_dbscan_parameters(K,gaze_coordenates_on_screen,
    stimuli_size=(130, 130), # in pixels
    screen_size=(1280,768), # in pixels
    max_trials=50,
    data=[{}],
    do_plot=True
):
    """
    k: min clusters
    gaze_coordenates_on_screen: string  
    """
    def get_min_samples(all_places):
        N = len(gaze_data)
        if all_places >= N:
            return N
        else:
            return N/all_places

    dictionary = len(data)-1
    gaze_data = load_data(gaze_coordenates_on_screen)
    print('Target: ',gaze_coordenates_on_screen)

    # stimulus size in pixels
    width, height = stimuli_size[0],stimuli_size[1]

    # normalize stimulus size
    width /= float(screen_size[0])
    height /= float(screen_size[1])

    # assume stimuli with uniform diameter, assume eps as stimulus radius
    stimulus_radius = np.mean([width, height])/2 
    data[dictionary]['eps'] = stimulus_radius
    print('Using EPS: ',data[dictionary]['eps'])

    # assume min_samples as the quotient between the number of gaze points
    # and the number of places used to present stimuli
    # let the number of places be all possible paths in a graph
    data[dictionary]['all_places'] = (K * K) * (K - 1)
    data[dictionary]['min_samples'] = get_min_samples(data[dictionary]['all_places'])
    print('Using Min.Samples: ', data[dictionary]['min_samples'])

    # the researcher knowns how many clusters, so we use this information as a termination clause
    data[dictionary]['min_clusters'] = K
    print('Using Min.Clusters: ', data[dictionary]['min_clusters'])

    # DBSCAN expects data with shape (-1,2), we need to transpose ours first
    data[dictionary]['src_xy'] = np.array([gaze_data['x_norm'], gaze_data['y_norm']]).T
    data[dictionary]['src_timestamps'] = gaze_data['time']
    
    trials = 0 
    while True:        
        data[dictionary]['dbscan'] = DBSCAN(
            eps=data[dictionary]['eps'],
            min_samples=data[dictionary]['min_samples']).fit(data[dictionary]['src_xy'])
        data[dictionary]['categorized_xy'] = plot_dbscan(data[dictionary]['src_xy'], data[dictionary]['dbscan'],do_plot)
        n_clusters = len_clusters(data[dictionary]['dbscan'])
        if n_clusters >= data[dictionary]['min_clusters']:
            print('Finished with: ',n_clusters,' clusters.')
            break
        else:
            plt.gcf().clear()
            data[dictionary]['all_places'] /= 2
            data[dictionary]['min_samples'] = get_min_samples(data[dictionary]['all_places'])
            print('Min.Clusters were not found, trying again using:',data[dictionary]['min_samples'], ' min. samples.')
            
            trials += 1
            if trials == max_trials:
                print(max_trials," trials. Finished without clusters.")
                break

            if data[dictionary]['all_places'] < 2:
                print("Too few places. Finished without clusters.")
                break

def guess_all_dbscan():
    data_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.dirname(data_path)
    data_path = os.path.dirname(data_path)
    
    # output folder for charts
    dbscan_path = os.path.join(data_path,'dbscan')

    if not os.path.exists(dbscan_path):
        os.makedirs(dbscan_path)    
    for inner_path in INNER_PATHS:
        a_data_path = os.path.join(data_path,inner_path) 
        paths = sorted(glob(os.path.join(a_data_path,'0*')))
        for path in paths:
            filename = os.path.join(data_path,path)
            filename = os.path.join(filename,'gaze_coordenates_on_screen.txt')
            guess_dbscan_parameters(2,filename)

            graphic_name = path.replace(data_path,'').strip(os.path.sep)
            graphic_name = os.path.join(graphic_name.replace(os.path.sep,'_')+'.png')
            graphic_name = os.path.join(dbscan_path,graphic_name)

            plt.savefig(graphic_name, bbox_inches='tight')
            plt.close()
 

if __name__ == '__main__':
    draw_single('/home/rafael/git/abpmc/P001/2015-05-27')