import os
from shutil import copyfile

basepath = os.path.dirname(os.path.abspath(__file__))

filenames = ['README.md']

frompath = os.path.join(basepath,'P001/2015-05-19')
topaths = [
    'P001/2015-05-27',
    'P002/2015-05-19',
    'P002/2015-05-20',
    'P003/2015-05-20',
    'P004/2015-05-20',
    'P005/2015-05-19',
    'P006/2015-05-25',
    'P007/2015-05-25',
    'P008/2015-05-26',
    'P009/2015-05-26',
    'P010/2015-05-26']

topaths = [os.path.join(basepath,topath) for topath in topaths]
for fn in filenames:
    orig_filename = os.path.join(frompath,fn)
    print 'from:',orig_filename
    for dp in topaths:
        dest_filename = os.path.join(dp,fn)
        print 'to:',dest_filename
        copyfile(orig_filename, dest_filename)
        # os.remove(dest_filename)