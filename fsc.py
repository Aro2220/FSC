# Copyright (c) 2018, Matheus Xavier Silva, Aro2220

from helpers.utilities.directory_traversal import *
from operator import itemgetter, attrgetter, methodcaller


def main():
    # Set the directory you want to start from
    root_dir = '.'
    # rootDir = os.path.abspath(os.sep)

    scan = Directory_Traversal()

    file_list = scan.directory_traversal(root_dir)

    # sorted_list = sorted(file_list, key=lambda hash_key: hash_key[2])
    sorted_list = sorted(file_list, key=itemgetter(2, 3))

    print(sorted_list)

if __name__ == '__main__':
    main()
