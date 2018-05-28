# Import the os module, for the os.walk function
from os import walk

from helpers.utilities.hashing import *

class Directory_Traversal:
    """File System Scanning"""
    @staticmethod
    def directory_traversal(root_dir):
        for dir_name, sub_dir_list, fileList in walk(root_dir):
            print('Found directory: %s' % dir_name)
            for fname in fileList:
                print('\t%s' % fname)

                print(hash_file(fname, dir_name))
                print(dir_name + " +++ " + fname)
