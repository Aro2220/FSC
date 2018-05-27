# Import the os module, for the os.walk function
import os

# SHA1 Hashing
import hashlib

BLOCKSIZE = 65536
hasher = hashlib.sha1()


def sha1_hash(file, directory=''):
    print("file name is " + file)
    print("directory name is " + directory)

    with open(directory+'\\'+file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    print(hasher.hexdigest())


# Set the directory you want to start from
rootDir = '.'
# rootDir = os.path.abspath(os.sep)

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

        sha1_hash(fname, dirName)
