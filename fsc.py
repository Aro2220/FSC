# Copyright (c) 2018, Matheus Xavier Silva, Aro2220

from helpers.utilities.directory_traversal import *


def main():
    # Set the directory you want to start from
    root_dir = '.'
    # rootDir = os.path.abspath(os.sep)

    test = Directory_Traversal()

    test.directory_traversal(root_dir)



if __name__ == '__main__':
    main()
