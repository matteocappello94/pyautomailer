import argparse
import sys
import logging as log
from pyautomailer import PyAutoMailer, PyAutoMailerMode

def main():
    parser = parse_args(sys.argv[1:])

    # Auto mailer init.
    am = PyAutoMailer(parser.sender,
                      parser.host,
                      parser.port,
                      parser.username,
                      parser.password)
    
    # Auto mailer property
    am.test = parser.test # Test mode
    am.log_file = parser.log_file
    am.log_level = get_log_level(parser.log_level)
    
    am.subject = parser.subject
    am.body = parser.body
    am.body_file = parser.body_file

    # Attachments list separated by commas (ONE_SEND mode)
    if parser.attachments is not None:
        am.attachments = parser.attachments.split(',')

    parser.func(parser, am)

def parse_args(args):
    parser = argparse.ArgumentParser(prog='pyautomailer',
        description='A fully customizable automatic bulk email sending script')
    subparsers = parser.add_subparsers(title='List of subcommands',
                                       description='Sending modes')
    bs = subparsers.add_parser('bulk-send', aliases=['bs'])
    os = subparsers.add_parser('one-send', aliases=['os'])

    parser.add_argument('-H', '--host', type=str,
                        help='email client connection host')
    parser.add_argument('-P', '--port', type=int,
                        help='email client connection port')
    parser.add_argument('-U', '--username', type=str,
                        help='email client connection username')
    parser.add_argument('-PWD', '--password', type=str,
                        help='email client connection password')
    parser.add_argument('-SND', '--sender', type=str,
                        help='sender of message')
    parser.add_argument('-S', '--subject', type=str,
                        help='subject of message')
    parser.add_argument('-A', '--attachments', type=str,
                        help='attachments of message separated by commas')
    body_group = parser.add_mutually_exclusive_group()
    body_group.add_argument('-BF', '--body-file', type=str,
                        help='a file that contains HTML body code')
    body_group.add_argument('-B', '--body', type=str,
                        help='body message')        
    parser.add_argument('-t', '--test', action='store_true',
                        help='run script in TEST mode without sending emails')
    parser.add_argument('-lf', '--log-file', type=str,
                        help='log file path')
    parser.add_argument('-ll', '--log-level', type=str,
                        choices=['CRITICAL',
                                 'ERROR',
                                 'WARNING',
                                 'INFO',
                                 'DEBUG'],
                        help='log level, default set to INFO')

    # Bulk send arguments
    bs.add_argument('source_file', metavar='SOURCE_FILE', type=str,
                        help='.CSV file source that contains emails and \
dynamics fields')

    # One send arguments
    os.add_argument('recipient', metavar='RECIPIENT', type=str,
                        help='recipient of message')

    # Commands function
    bs.set_defaults(func=bulk_send)
    os.set_defaults(func=one_send)
    
    return parser.parse_args(args)

# Bulk-send mode function
def bulk_send(args, am):
    am.mode = PyAutoMailerMode.BULK_SEND
    run_service(am, args.source_file)

# One-send mode function
def one_send(args, am):
    am.mode = PyAutoMailerMode.ONE_SEND
    run_service(am, args.recipient)

# From log_level string get log_level object of logging module
def get_log_level(self, log_level = 'INFO'):
    str_log_level = { 'CRITICAL': log.CRITICAL,
                      'ERROR': log.ERROR,
                      'WARNING': log.WARNING,
                      'INFO': log.INFO,
                      'DEBUG': log.DEBUG
                      }
    ll = str_log_level.get(log_level, lambda: log.INFO)
    return ll

def run_service(am, arg):
    # Start sending service
    am.run_service(arg)
    
    # Close connection
    am.close()

