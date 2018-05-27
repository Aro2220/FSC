# Copyright (c) 2018, Matheus Xavier Silva, Aro2220


class _Atlas:
    """"This class is the base raw binary operations on atlas files"""

    def __init__(self, contents: bytearray):
        

    def _add_value(self, value: bytes, identifier):
        pass

    def _create_list(self, size, identifier):
        pass

    def _resize_list(self, identifier, new_size):
        pass

    def _open_list(self, identifier):
        pass

    def _close_list(self):
        pass

    def _goto(self, identifier):
        pass

    def _build_index(self):
        pass

class AtlasWriter(_Atlas):
    """"This class is intended to work with the atlas list format"""

    def __init__(self):
        self._raw = _Atlas()

    def add_value(self, value: bytes, identifier):
        pass

    def create_list(self, size, identifier):
        pass

    def open_list(self, identifier):
        pass

    def close_list(self):
        pass

    def goto(self, identifier):
        pass

    def build_index(self):
        pass

class AtlasReader(_Atlas):

if __name__ == '__main__':
    print("this is a class only module")
