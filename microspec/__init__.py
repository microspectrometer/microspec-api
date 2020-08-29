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

If the application uses ``microspec`` beyond the initial ``kit =
microspec.Devkit()``, Chromation recommends importing
``microspec`` *bound* as ``usp``:

.. code-block:: python

    import microspec as usp
    kit = usp.Devkit()
    kit.setBridgeLED(led_setting = usp.OFF)

Module List
-----------

The ``microspec`` package has three modules:
:mod:`~microspec.commands`, :mod:`~microspec.constants`, and
:mod:`~microspec.replies`

:mod:`microspec.commands`
^^^^^^^^^^^^^^^^^^^^^^^^^^

- defines class :class:`~microspec.commands.Devkit`
- each command is a method in the ``Devkit`` class
- Example:

.. code-block:: python

    import microspec
    kit = microspec.Devkit()
    kit.getBridgeLED()

:mod:`microspec.constants`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- defines names for constants
- Example:

.. code-block:: python

    import microspec as usp
    usp.OK      # equals int 0
    usp.ERROR   # equals int 1

- defines dictionaries for converting an integer code to its
  constant's name
- Example:

.. code-block:: python

    import microspec as usp
    usp.status_dict.get(usp.OK) # returns str 'OK'

- values of the constants match the ``globals`` section of the
  :ref:`JSON API config file <dev-kit-API-JSON>`

:mod:`microspec.replies`
^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Do not directly use the :mod:`~microspec.replies` module in
    application code.

    The :mod:`~microspec.commands` module uses
    :mod:`~microspec.replies` to format responses. Application
    code should never need to instantiate a response.

- defines a namedtuple for the response to each command
- class ``Devkit`` uses ``replies`` to re-package the
  response returned by the ``microspeclib`` API
"""
from .commands import * # class Devkit
from .constants import * # OK, ERROR, OFF, GREEN, RED, etc.
from .helpers import * # to_cycles(), to_ms()
