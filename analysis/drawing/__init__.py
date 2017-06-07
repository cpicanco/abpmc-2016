# -*- coding: utf-8 -*-
'''
  Copyright (C) 2016 Rafael Picanço.

  The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

  You should have received a copy of the GNU General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

from os.path import join
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from constants import INNER_PATHS 
from constants import SQUARE, CIRCLE, S_SIZE

from methods import all_responses,stimuli_onset,load_data,rate_in

def save_all(src, draw_func, output_name):
	source_dir = src
	source_directories = [join(source_dir,s) for s in INNER_PATHS]
	
	for src_dir in source_directories:
		draw_func(src_dir, False)
		output_path = join(src_dir,output_name)
		plt.savefig(output_path, bbox_inches='tight')
		plt.close()

def temporal_perfil(axis,onsets,timestamps, onsets_style='colors', c1="red", c2="blue", doreversed=False, nsize=None):
	w = 0.2
	if 'colors' in onsets_style:
		# red
		
		data = rate_in(zip(onsets[0], onsets[1]),timestamps)
		N = len(data)
		if doreversed:
			data = [-x for x in data]
		R = range(1,N+1)
		# axis.plot(data, color=c1, label="During Red")
		axis.bar(R,data,w, color=c1, label="Durante Verm.")
		

		# removing the first element and reversing give us the blue one
		data = rate_in(zip(onsets[1], onsets[0][1:]), timestamps)
		N = len(data)
		R = range(1,N+1)
		if doreversed:
			data = [-x for x in data]
		# axis.plot(data, color=c2, label="During Blue")
		axis.bar([x+w for x in R],data,w, color=c2, label="Durante Azul")
		axis.set_xlim([1,len(R)+w*2.])


	elif 'pair' in onsets_style:
		data = rate_in(zip(onsets[0], onsets[1]),timestamps)
		N = len(data)
		R = range(N)
		if doreversed:
			data = [-x for x in data]
			
		var = w * nsize
		print var, N
		axis.bar([x+var for x in R],data,w, color=c1)
		axis.set_xlim([1,len(R)+w*var])

	elif 'positions' in onsets_style:
		# left
		data = rate_in(zip(onsets,onsets[1:]),timestamps[0])
		axis.plot(data, color="black", label="Left")

		# right
		data = rate_in(zip(onsets,onsets[1:]),timestamps[1])
		axis.plot(data, color="grey", label="Right")

	# remove outer frame
	axis.spines['top'].set_visible(False)
	axis.spines['bottom'].set_visible(False)
	axis.spines['left'].set_visible(False)
	#axis.spines['right'].set_visible(False)

	# axis.set_xticklabels([round(1.3*x,2) for x in range(0,5)])

	#remove ticks
	axis.xaxis.set_ticks_position('none')
	axis.yaxis.set_ticks_position('none')

def plot_xy(data, square=SQUARE, ellipse=CIRCLE): 
    axes = plt.gca()
    axes.add_patch(
        patches.Rectangle(
            (square.Left,square.Top),   
            square.Width,          
            square.Height,
            facecolor="gray",
            alpha=0.3        
        )
    )

    axes.add_patch(
        patches.Ellipse(
            ellipse.Center,   
            width=ellipse.Width,          
            height=ellipse.Height,
            angle=360,
            facecolor="gray",
            alpha=0.3        
        )
    )

    axes.set_ylim(ymax = 1, ymin = 0)
    axes.set_xlim(xmax = 1, xmin = 0)
    plt.scatter(*data, s=1, c='b')    
    plt.show()   
    plt.gcf().clear() 

def plot_bias(data, screen_center):           
    bias = data+screen_center
    axes = plt.gca()
    axes.set_ylim(ymax = 1, ymin = 0)
    axes.set_xlim(xmax = 1, xmin = 0)
    plt.scatter(*screen_center, s=1.5)
    plt.plot(*bias.T)
    plt.show()
    plt.gcf().clear()