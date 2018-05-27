# Import the os module, for the os.walk function
from os import walk

# SHA1 Hashing
from hashlib import sha1

blocksize = 65536
hasher = sha1()


def sha1_hash(file, directory=''):
    print("file name is " + file)
    print("directory name is " + directory)

    with open(directory+'\\'+file, 'rb') as afile:
        buf = afile.read(blocksize)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(blocksize)
    print(hasher.hexdigest())


# Set the directory you want to start from
rootDir = '.'
# rootDir = os.path.abspath(os.sep)

for dirName, subdirList, fileList in walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

        sha1_hash(fname, dirName)
