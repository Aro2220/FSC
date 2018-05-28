# Import the os module, for the os.walk function
import os
import platform
import time

from helpers.utilities.hashing import *

class Directory_Traversal:
    """File System Scanning"""
    def __init__(self):
        pass

    @staticmethod
    def creation_date(path_to_file):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(path_to_file)
        else:
            stat = os.stat(path_to_file)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                return stat.st_mtime

    @staticmethod
    def directory_traversal(root_dir):
        file_list = []

        for dir_name, sub_dir_list, fileList in os.walk(root_dir):
            print('Found directory: %s' % dir_name)
            for fname in fileList:
                print('\t%s' % fname)

                time_stamp = (Directory_Traversal.creation_date(dir_name + '\\' + fname))

                local_time = time.localtime(time_stamp)

                # print(str(local_time.tm_year) + ", " + str(local_time.tm_mon) + ", " + str(local_time.tm_mday))
                file_list.append([fname, dir_name, hash_file(fname, dir_name), local_time])

        return file_list

