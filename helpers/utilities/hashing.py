# Copyright (c) 2018, Matheus Xavier Silva, Aro2220
from hashlib import sha1 as hashing
import os

class HashUtils:
    """SHA1 hashing utilities"""
    @staticmethod
    def hash_file(path,  file):
        hasher = hashing()
        with open(os.path.join(path, file), 'rb') as file:
            buf = file.read(64)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(64)
        return hasher.digest()
