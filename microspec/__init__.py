"""Module ``microspec`` is the API for the Chromation Spectrometer dev-kit.

Install
-------

Install the ``microspec`` project:

.. code-block:: bash

    pip install microspec

Usage
-----

Use the ``microspec`` module in an application:

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
"""
from .commands import * # class Devkit
from .constants import * # OK, ERROR, OFF, GREEN, RED, etc.
from .helpers import * # to_cycles(), to_ms()
