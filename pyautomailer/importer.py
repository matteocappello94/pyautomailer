import logging as log

class Importer:

    def __init__(self, input_file):
        # Init log
        self.logger = log.getLogger(__name__)
        
        self.records_fields = [] # List of input file fields, first is always email to.
        self.file_readed = False # Indicates that file is readed successfully or not.
        self.attachments = False # Indicates the presence of attachments.
        self.input_file = input_file
        self.read_file()

    def read_file(self):
        try:
            header = True
            with open(self.input_file) as f:
                for line in f:
                    record = []
                    for field in line.rstrip().split(';'):
                        record.append(field)
                        # Check presence of one attachments.
                        if field.find('[attachment-') != -1 and header == True:
                            self.attachments = True
                    self.records_fields.append(record)
                    header = False
            f.close()
            self.file_readed = True
        except FileNotFoundError:
            self.logger.error('Source file %s not found!' % (self.input_file))
