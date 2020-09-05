"""Module ``microspec`` is the API for the Chromation Spectrometer dev-kit.

See the :ref:`API` reference docs.

Install
-------

Install the ``microspec`` project:

.. code-block:: bash

    pip install microspec

This installs the ``microspec`` package and a few command line
utilities. The ``microspec`` package has submodules ``microspec``
and ``microspeclib``. Applications should use the ``microspec``
module.

Usage
-----

Use the ``microspec`` module in an application:

.. code-block:: python

    import microspec
    kit = microspec.Devkit()

Chromation recommends importing ``microspec`` *bound* as ``usp``
to reduce code line length:

.. code-block:: python

    import microspec as usp
    kit = usp.Devkit()
    kit.setBridgeLED(led_setting = usp.OFF)
"""
from .commands import * # class Devkit
from .constants import * # OK, ERROR, OFF, GREEN, RED, etc.
from .helpers import * # to_cycles(), to_ms()
