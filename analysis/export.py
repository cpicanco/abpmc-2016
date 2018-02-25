import os

from categorization import relative_rate_left_right
from methods import get_data_path
from constants import INNER_PATHS

# assign the root data folder
data_path = get_data_path()


RED = 0
BLUE = 1

all_data = []
for ip in INNER_PATHS:
	print(ip)
	all_data.append(relative_rate_left_right(os.path.join(data_path, ip), target_intervals='red_blue_onsets'))

def line(contingency, phase, cycle):
	strings = []
	for data in all_data:
		try:
			strings.append(repr(data[contingency][phase][cycle]))
		except:
			strings.append('nan')
	return ','.join(strings)
	
print('Left-gaze proportion when left stimulus was red')
for cycle in range(9):
	print(line(0, RED, cycle))

for cycle in range(9):
	print(line(1, RED, cycle))

for cycle in range(9):
	print(line(2, RED, cycle))

print('Left-gaze proportion when left stimulus was blue')
for cycle in range(9):
	print(line(0, BLUE, cycle))

for cycle in range(9):
	print(line(1, BLUE, cycle))

for cycle in range(9):
	print(line(2, BLUE, cycle))
