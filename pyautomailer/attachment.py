from pathlib import Path

class Attachment:

    def __init__(self, records_fields, index_fields):
        self.attachments_found = [] # Attachments found into source file.
        self.attachments_loaded = [] # Attachments exist into disk space.
        self.attachments_unloaded = [] # Attachments not exist into disk space.
        self.source_fields = records_fields
        self.index_fields = index_fields
        self.read_attachments()

    def read_attachments(self):
        for i in range(1,len(self.source_fields[self.index_fields])):
            header = self.source_fields[0][i]
            if header.find('[attachment-') != -1:
                # Field is an attachment
                attachment = self.source_fields[self.index_fields][i]
                self.attachments_found.append(attachment)

                # Check if attachment exist on disk.
                f_attachment = Path(attachment)
                if f_attachment.is_file():
                    self.attachments_loaded.append(attachment)
                else:
                    self.attachments_unloaded.append(attachment)
