import os
import smtplib
import mimetypes
from email.message import EmailMessage
from enum import Enum
from pyautomailer.importer import Importer
from pyautomailer.body import Body, BodyType
from pyautomailer.subject import Subject
from pyautomailer.attachment import Attachment

class PyAutoMailerMode(Enum):
    BULK_SEND = 1
    ONE_SEND = 2

class PyAutoMailer:

    def __init__(self, m_sender, ec_host, ec_port, ec_user, ec_pwd):
        # Email client init.
        self.ec = self.init_SMTP(ec_host, ec_port, ec_user, ec_pwd)
        self.mode = None
        self.test = False # Test mode default false
        self.sender = m_sender
        self.subject = None
        self.body = None
        self.body_file = None

    def init_SMTP(self, host, port, user, pwd):
        if port == None:
            port = 25 # Default email client port
        ec = smtplib.SMTP(host, port)
        ec.login(user, pwd)
        return ec

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, test):
        self.__test = test

    @property
    def sender(self):
        return self.__sender

    @sender.setter
    def sender(self, sender):
        self.__sender = sender

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, subject):
        self.__subject = subject

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def body_file(self):
        return self.__body_file

    @body_file.setter
    def body_file(self, body_file):
        self.__body_file = body_file

    # Close SMTP connection
    def close(self):
        self.ec.quit()

    # arg stands for source file in bulk-send mode or recipient in one-send
    # mode.
    def run_service(self, arg):
        if self.mode == PyAutoMailerMode.BULK_SEND:
            self.importer = Importer(arg)
            for i in range(1,len(self.importer.records_fields)):
                if self.body is None and self.body_file is not None:
                    b = Body(BodyType.FILE,
                             self.body_file, self.importer.records_fields, i)
                elif self.body is not None and self.body_file is None:
                    b = Body(BodyType.STRING,
                             self.body, self.importer.records_fields, i)
                dynamic_subject = Subject(self.subject,
                                          self.importer.records_fields, i)
                msg = self.create_message(
                    dynamic_subject.subject,
                    self.sender,
                    self.importer.records_fields[i][0], # First fields is email.
                    b.html,
                    i)
        elif self.mode == PyAutoMailerMode.ONE_SEND:
            # One-send mode not support dynamics body message, Body class isn't
            # used.
            msg = self.create_message(
                self.subject,
                self.sender,
                arg, # Recipient in this mode.
                self.body,
                None) # Index field is None in this mode.
        if not self.test:
            self.ec.send_message(msg)

    def create_message(self, m_subject, m_from, m_to, m_body, index_fields):
        m = EmailMessage()
        m.set_content(m_body)
        m.add_alternative(m_body, subtype='html')
        m['Subject'] = m_subject
        m['From'] = m_from
        m['To'] = m_to

        # Attachments section
        if self.mode == PyAutoMailerMode.BULK_SEND:
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
