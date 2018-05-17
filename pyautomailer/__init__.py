import os
import smtplib
import mimetypes
from email.message import EmailMessage
from pyautomailer.importer import Importer
from pyautomailer.body import Body
from pyautomailer.subject import Subject
from pyautomailer.attachment import Attachment

class PyAutoMailer:

    def set(self, m_from, m_subject, source_file, body_file):
        self.m_from = m_from
        self.m_subject = m_subject
        self.source_file = source_file
        self.body_file = body_file
        self.importer = Importer(self.source_file)

    def set_emailclient(self, host, port, user, pwd):
        self.ec_host = host
        if port != None:
            self.ec_port = port
        else:
            self.ec_port = 25 # Default email client port
        self.ec_user = user
        self.ec_pwd = pwd
        self.ec = smtplib.SMTP(self.ec_host, self.ec_port)
        self.ec.login(self.ec_user, self.ec_pwd)

    def emailclient_quit(self):
        self.ec.quit()

    def run_service(self, test_mode):
        for i in range(1,len(self.importer.records_fields)):
            b = Body(self.body_file, self.importer.records_fields, i)
            dynamic_subject = Subject(self.m_subject, self.importer.records_fields, i)
            msg = self.create_message(
                dynamic_subject.subject,
                self.m_from, # Sender.
                self.importer.records_fields[i][0], # First fields is email.
                b.html,
                i)
            if not test_mode:
                self.ec.send_message(msg)

    def create_message(self, m_subject, m_from, m_to, m_body, index_fields):
        m = EmailMessage()
        m.set_content(m_body)
        m.add_alternative(m_body, subtype='html')
        m['Subject'] = m_subject
        m['From'] = m_from
        m['To'] = m_to

        # Attachments section
        if self.importer.attachments:
            att = Attachment(self.importer.records_fields, index_fields)
            for att_file in att.attachments_loaded:
                ctype, encoding = mimetypes.guess_type(att_file)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream'
                maintype, subtype = ctype.split('/', 1)
                with open(att_file, 'rb') as af:
                    m.add_attachment(af.read(),
                                     maintype=maintype,
                                     subtype=subtype,
                                     filename=os.path.basename(att_file))
        
        return m
