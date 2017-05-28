# -*- coding: utf-8 -*-
'''
  Copyright (C) 2017 François Tonneau.
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
# data correction using non-parametric barycenter of gaze

import numpy as np

fileName = "input.txt"
fileDelimiter = "\t"

xyData = np.loadtxt(fileName, delimiter = fileDelimiter)
xyData = np.float32(xyData)

xmax = 1
ymax = 1

# remove data points outside of the screen
def screenClamped(xy):
    xgood = (0 <= xy[:, 0]) & (xy[:, 0] < xmax)
    ygood = (0 <= xy[:, 1]) & (xy[:, 1] < ymax)
    xyClamped = xy[xgood & ygood, :]
    deletedCount = xy.shape[0] - xyClamped.shape[0]
    if deletedCount > 0:
        print "\nRemoved", deletedCount, "data point(s) with", \
        "out-of-screen coordinates!"
    return xyClamped

xyData = screenClamped(xyData)

# compute gaze "center" (= average of some quantiles of gaze points) and return
# gaze_center minus screen_center as an estimate of system bias
def xyBias(xyBlock):
    x=xyBlock[:, 0].copy()
    y=xyBlock[:, 1].copy()
    sampleSize = xyBlock.shape[0]
    x.sort()
    y.sort()
    xStat = 0
    yStat = 0
    # compute sums of a few chosen quantiles
    chosenQuantiles = [5, 10, 15, 85, 90, 95]
    for quantile in chosenQuantiles:
        rank = (sampleSize * quantile)/100
        xStat += x[rank]
        yStat += y[rank]
    # divide by length to get quantile average
    xStat = xStat/len(chosenQuantiles)
    yStat = yStat/len(chosenQuantiles)
    xyStat = np.array([xStat, yStat])
    screenCenter = np.array([xmax/2.0, ymax/2.0])
    return xyStat - screenCenter

def correct(block, bias):
    block[:, 0] = block[:, 0] - bias[0]
    block[:, 1] = block[:, 1] - bias[1]
    return block

dataCount = xyData.shape[0]
print "\nThere are", dataCount, "data points."

blockSize = 1000

if dataCount < blockSize:
    print "Too few data to proceed."
    print "Press ENTER to exit."
    raw_input()
    quit()

equallySpacedLines = range(0, dataCount, blockSize)

firstBlock = True

for blockStart in equallySpacedLines:
    blockEnd = blockStart + blockSize
    if blockEnd <= dataCount:
        dataBlock = xyData[blockStart:blockEnd, :]
        dataBias = xyBias(dataBlock)
    else:
        dataBlock = xyData[blockStart:dataCount, :]
    if firstBlock:
        biasAlongBlocks = dataBias
        unbiasedData = correct(dataBlock, dataBias)
        firstBlock = False
    else:
        biasAlongBlocks = np.vstack((biasAlongBlocks, dataBias))
        unbiasedData = np.vstack((unbiasedData, correct(dataBlock, dataBias)))

print "\nBias along blocks:"
print biasAlongBlocks

np.savetxt("bias_by_trim.txt", biasAlongBlocks)
np.savetxt("output_by_trim.txt", unbiasedData)

