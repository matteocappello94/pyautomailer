pyautomailer: a fully customizable automatic email client service.
##################################################################

pyautomailer is a Python module (with command line tool to use it from terminal) that allows you to send massive custom email. 
It can be used with massive SMTP sending service or with standard mailbox after setting sending limit.

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

The tool working with Python 3.x.

Usage
=====

.. code-block:: bash

	$ pyautomailer [-h] [-p PORT] [-s SUBJECT] [-t] HOST USER PWD SENDER SOURCE_FILE BODY_FILE
	
See also ``pyautomailer --help``.

Examples
--------

Soon...

Meta
====

Related projects
----------------

Dependencies
~~~~~~~~~~~~

Change log
----------

Licence
-------

Authors
-------

Matteo Cappello created pyautomailer.