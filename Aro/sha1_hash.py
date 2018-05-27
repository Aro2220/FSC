import hashlib

BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open('myfile.jpg', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())
