from unittest import TestCase

from pyautomailer import importer

class TestImporter(TestCase):
    def test_import_sourcefile(self):
        i = importer.Importer('pyautomailer/tests/sourcefile.csv')
        self.assertTrue(i.file_readed)
