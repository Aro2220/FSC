# Copyright (c) 2018, Matheus Xavier Silva, Aro2220


class FSH:
    """fileserializationhelper class to ease serialization"""

    def __init__(self, fname: str, path: str, fhash: bytes, timestamp):
        self.file_name = fname
        self.path = path
        self.hash = fhash
        self.timestamp


    def serialize(self):
