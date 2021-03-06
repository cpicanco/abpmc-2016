# -*- coding: utf-8 -*-
'''
    Copyright (C) 2016 Rafael Picanço.

    The present file is distributed under the terms of the GNU General Public License (GPL v3.0).

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''
import os
from constants import INNER_PATHS
from shutil import copyfile

def copy_to_inner_paths(data_path,fromfullpath, filenames):
    topaths = [os.path.join(data_path,topath) for topath in INNER_PATHS]
    for fn in filenames:
        orig_filename = os.path.join(fromfullpath,fn)
        print 'from:',orig_filename
        for dp in topaths:
            dest_filename = os.path.join(dp,fn)
            if not os.path.isfile(dest_filename):
                print 'to:',dest_filename
                copyfile(orig_filename, dest_filename)
            else:
                print 'will not override:',dest_filename 

def delete_from_inner_paths(data_path, filenames):
    topaths = [os.path.join(data_path,topath) for topath in INNER_PATHS]
    for fn in filenames:
        for dp in topaths:
            dest_filename = os.path.join(dp,fn)
            os.remove(dest_filename)
            print 'delete:',dest_filename