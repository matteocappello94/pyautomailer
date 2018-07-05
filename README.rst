pyautomailer: a fully customizable automatic bulk email sending script.
#######################################################################

pyautomailer is a Python module (with command line tool to use it from terminal) that allows you to send massive custom email. 
It can be used with massive SMTP sending service or with standard mailbox after set sending limit to avoid SPAM and black-lists.

.. class:: no-web no-pdf

|pypi|

.. contents::

.. section-numbering::

Main features
=============

* E-Mail bulk sending.
* HTML dynamic Body message.
* Dynamic Subjects and Attachments.

Installation
============

Windows, etc.
-------------

On Windows, pyautomailer can be installed via PyPi (recommended):

.. code-block:: bash

	$ pip install pyautomailer

or manually from source code:

.. code-block:: bash

	$ python setup.py install

Ufficially MacOS and Linux aren't supported but tool use standard Python library that can allow it to work. Not tested at the moment.

Python version
--------------

Pyautomailer works with Python 3.

Usage
=====

as Python module
----------------

Import module:

.. code-block:: python

	from pyautomailer import PyAutoMailer, PyAutoMailerMode

Class initialization indicating SMTP parameters:

.. code-block:: python

	am = PyAutoMailer('SENDER', 'HOST', 25, 'USERNAME', 'PASSWORD')

Set properties:

.. code-block:: python

	am.subject = 'SUBJECT STRING'
	am.body_file = 'BODYMESSAGE.TXT'
	
	# Sending mode
	am.mode = PyAutoMailerMode.BULK_SEND
	
Send messages:

.. code-block:: python

	am.run_service('SOURCEFILE.CSV')
	
Close connection:

.. code-block:: python

	am.close()

Additional proprierties
~~~~~~~~~~~~~~~~~~~~~~~
   
.. code-block:: python

	# Enable TEST mode.
	am.test = True
	
	# Set body message with string and not using a text file.
	am.body = 'BODY OF MESSAGE'
	
One-send mode
~~~~~~~~~~~~~

Pyautomailer can send single email message using ONE-SEND mode.

.. code-block:: python

	# Sending mode
	am.mode = PyAutoMailerMode.ONE_SEND
	
	# Attachments
	am.attachments = ['PATH_TO_ATTACHMENT_1','PATH_TO_ATTACHMENT_1',...]
	
	# Recipient of message is passed as run_service parameter.
	am.run_service('RECIPIENT')

Attachments properties is available only in ONE-SEND mode.

Using this mode, dynamic subject and dynamics body message aren't supported.

Examples
~~~~~~~~

.. code-block:: python

	from pyautomailer import PyAutoMailer, PyAutoMailerMode

	# Initialization
	am = PyAutoMailer('sender@email.com', 'smtphost.com', 25, 'senderuser', 'senderpassword')

	# Message proprierties
	am.subject = 'This is a test email.'
	am.body_file = 'C:\bodymessage.txt'
	
	# Sending mode
	am.mode = PyAutoMailerMode.BULK_SEND

	# Run sending
	am.run_service('C:\sourcefile.csv')

	# Close connection
	am.close()

as command-line tool
--------------------

.. code-block:: bash

	$ pyautomailer [-h] [-H HOST] [-P PORT] [-U USERNAME] [-PWD PASSWORD] [-SND SENDER] [-S SUBJECT] [-A ATTACHMENTS] [-BF BODY_FILE | -B BODY] [-t] {bulk-send,bs,one-send,os} ...
	
See also ``pyautomailer --help`` and ``pyautomailer <command> --help``.

Examples
~~~~~~~~

Bulk sending mode:

.. code-block:: bash

	$ pyautomailer -H smtphost.com -U senderuser -PWD senderpassword -SND sender@email.com -S "This is a test email." -BF "C:\bodymessage.txt" bulk-send "C:\sourcefile.csv"

One email sending mode:

.. code-block:: bash

	$ pyautomailer -H smtphost.com -U senderuser -PWD senderpassword -SND sender@email.com -S "This is a test email." -A "C:\attachment_1.jpg,C:\attachments_2.txt" -B "This is body message of email." one-send mariorossi@email.com

Meta
====

User support
------------

Please use the following support channel `GitHub issues <https://github.com/matteocappello94/pyautomailer/issues>`_ for bug reports and feature requests.

Related projects
----------------

Dependencies
~~~~~~~~~~~~

Pyautomailer uses only standard Python 3 libraries.

Change log
----------

See `CHANGELOG <https://github.com/matteocappello94/pyautomailer/blob/master/CHANGELOG.rst>`_.

Licence
-------

MIT: `LICENSE <https://github.com/matteocappello94/pyautomailer/blob/master/LICENSE>`_.

Authors
-------

`Matteo Cappello`_ created pyautomailer.

.. _Matteo Cappello: http://matteocappello.com

.. |pypi| image:: https://img.shields.io/badge/PyPI-latest-yellow.svg?longCache=true&style=flat-square
	:target: https://pypi.org/project/pyautomailer/
	:alt: Latest version released on PyPi
 