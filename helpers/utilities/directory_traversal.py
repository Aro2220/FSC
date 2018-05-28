# Import the os module, for the os.walk function
from os import walk

from helpers.utilities.hashing import HashUtils

class Directory_Traversal:
    """File System Scanning"""
    @staticmethod
    def directory_traversal(self, root_dir):
        for dirName, subdirList, fileList in walk(root_dir):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)

                print(HashUtils.hash_file(fname, dirName))
                print(dirName + " +++ " + fname)
