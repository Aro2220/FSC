# Copyright (c) 2018, Matheus Xavier Silva, Aro2220

class File:
    """"file.py class to ease serialization"""

    def __init__(self, fname: str, path: str, fhash: bytes):
        self.file_name = fname
        self.path = path
        self.hash = fhash


    def serialize(self):
        self.file_name