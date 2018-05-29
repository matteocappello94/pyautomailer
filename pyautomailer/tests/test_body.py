from unittest import TestCase

from pyautomailer import importer,body

class TestBody(TestCase):
    def test_body_inputfile(self):
        i = importer.Importer('pyautomailer/tests/sourcefile.csv')
        if(i.file_readed):
            b = body.Body(body.BodyType.FILE,
                          'pyautomailer/tests/emailbody.htm',
                          i.records_fields, 1)
            self.assertTrue(b.html != '')
