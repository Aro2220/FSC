# Copyright (c) 2018, Matheus Xavier Silva, Aro2220


class Atlas:
    """"This class is intended to work with the atlas list format"""

    def __init__(self, version, comment):
        self.contents = bytearray(b'\xF5\xA7')
        if version == 1:
            self.contents.append(1)
        else:
            raise ValueError
        self.comment = comment.encode('utf-8')
        self.contents.append(self.comment)

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
