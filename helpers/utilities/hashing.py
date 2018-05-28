# Copyright (c) 2018, Matheus Xavier Silva, Aro2220
from hashlib import sha1 as hashing


def hash_file(file, directory=''):
    hasher = hashing()
    with open(directory + '\\' + file, 'rb') as afile:
        buf = afile.read(64)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(64)
    return hasher.digest()
