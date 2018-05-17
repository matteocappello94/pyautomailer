class Subject:

    def __init__(self, subject, records_fields, index_fields):
        self.fields_found = [] # Fields found into subject.
        self.fields_loaded = [] # Fields loaded into subject.
        self.fields_unloaded = [] # Fields unloaded / not found in input file.
        self.subject = subject
        self.source_fields = records_fields
        self.index_fields = index_fields
        self.load_fields()
        self.upload_fields()

    def load_fields(self):
        exp = '{field:\''
        index = 0
        while index < len(self.subject):
            index = self.subject.find(exp, index)
            if index == -1:
                break
            # Expression found.
            start_index = index + len(exp)
            end_index = self.subject.find('\'', start_index)
            self.fields_found.append(self.subject[start_index:end_index])
            index += len(exp)

    def upload_fields(self):
        for f_found in self.fields_found:
            # Check if subject field is present into source fields.
            # It is used only first row that contain header fields.
            found = False
            i_header = 0 # Header index
            for f_source in self.source_fields[0]:
                if f_found == f_source:
                    self.fields_loaded.append(f_found)
                    found = True
                    self.subject = self.field_replacement('{field:\'%s\'}' % (f_found),
                                      self.source_fields[self.index_fields][i_header])
                i_header += 1
            if not found:
                self.fields_unloaded.append(f_found)

    def field_replacement(self, exp, replacement):
        return self.subject.replace(exp,replacement)
