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

Pyautomailer works with Python 3.x.

Usage
=====

as Python module
----------------

Soon...

Examples
~~~~~~~~

Soon...

as command-line tool
--------------------

.. code-block:: bash

	$ pyautomailer [-h] [-p PORT] [-s SUBJECT] [-t] HOST USER PWD SENDER SOURCE_FILE BODY_FILE
	
See also ``pyautomailer --help``.

Examples
~~~~~~~~

Soon...

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
 