from unittest import TestCase

from pyautomailer import command_line

class TestConsole(TestCase):
    def test_command_line_args(self):
        parser = command_line.parse_args(
            ['HOST','USER','PWD','SOURCE_FILE',
             'SENDER','BODY_FILE'])
