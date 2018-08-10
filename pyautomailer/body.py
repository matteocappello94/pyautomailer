import logging as log
from enum import Enum

class BodyType(Enum):
    FILE = 1
    STRING = 2

class Body:

    # arg stands for input_file whene b_type is FILE or the body string whene is
    # STRING.
    def __init__(self, b_type, arg, records_fields, index_fields):
        # Init log
        self.logger = log.getLogger(__name__)
        
        self.html = '' # Email html body.
        self.file_readed = False    # Indicates that input file is readed
                                    # successfully or not.
        self.fields_found = [] # Fields found into html body.
        self.fields_loaded = [] # Fields loaded into html body.
        self.fields_unloaded = [] # Fields unloaded / not found in input file.
        self.arg = arg
        self.source_fields = records_fields
        self.index_fields = index_fields
        if b_type == BodyType.FILE:
            self.read_file()
        elif b_type == BodyType.STRING:
            self.html = self.arg
        self.load_fields()
        self.upload_fields()

    def read_file(self):
        try:
            with open(self.arg) as f:
                self.html = f.read()
            f.close()
            self.file_readed = True
        except FileNotFoundError:
            self.logger.error('Source body file %s not found!' % (self.arg))
            raise BodyFileNotFoundError

    def load_fields(self):
        exp = '{field:\''
        index = 0
        while index < len(self.html):
            index = self.html.find(exp, index)
            if index == -1:
                break
            # Expression found.
            start_index = index + len(exp)
            end_index = self.html.find('\'', start_index)
            self.fields_found.append(self.html[start_index:end_index])
            index += len(exp)

    def upload_fields(self):
        for f_found in self.fields_found:
            # Check if html field is present into source fields.
            # It is used only first row that contain header fields.
            found = False
            i_header = 0 # Header index
            for f_source in self.source_fields[0]:
                if f_found == f_source:
                    self.fields_loaded.append(f_found)
                    found = True
                    self.html = self.field_replacement('{field:\'%s\'}' %
                                                       (f_found),
                                      self.source_fields[self.index_fields]
                                                       [i_header])
                i_header += 1
            if not found:
                self.fields_unloaded.append(f_found)

    def field_replacement(self, exp, replacement):
        return self.html.replace(exp,replacement)

class BodyFileNotFoundError(Exception):
    pass
