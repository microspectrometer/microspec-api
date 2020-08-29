"""Package ``microspec`` is the API for the Chromation Spectrometer dev-kit.

Install
-------

Install the ``microspec`` project:

.. code-block:: bash

    pip install microspec

Usage
-----

Use the ``microspec`` package in an application:

.. code-block:: python

    import microspec
    kit = microspec.Devkit()

Module List
-----------

The ``microspec`` package has three modules:
:mod:`~microspec.commands`, :mod:`~microspec.constants`, and
:mod:`~microspec.replies`

:mod:`~microspec.commands`
^^^^^^^^^^^^^^^^^^^^^^^^^^

- defines class :class:`~microspec.commands.Devkit`
- each command is a method in the ``Devkit`` class
- Example:

.. code-block:: python

    kit = microspec.Devkit()
    kit.getBridgeLED()

:mod:`~microspec.constants`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- defines names for constants
- Example:

.. code-block:: python

    >>> microspec.OK
    0
    >>> microspec.ERROR
    1

- defines dictionaries for converting an integer code to its
  constant's name
- Example:

.. code-block:: python

    >>> microspec.status_dict.get(0)
    'OK'
    >>> microspec.status_dict.get(microspec.OK)
    'OK'

- values of the constants match the ``globals`` section of
  JSON file ``microspec/cfg/microspec.json``

:mod:`~microspec.replies`
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Application code does not directly use the
    :mod:`~microspec.replies` module.

- defines a namedtuple for the response to each command
- class ``Devkit`` uses ``replies`` to re-package the
  response returned by the ``microspeclib`` API
"""
from .commands import * # class Devkit
from .constants import * # OK, ERROR, OFF, GREEN, RED, etc.
