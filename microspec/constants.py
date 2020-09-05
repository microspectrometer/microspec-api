# -*- coding: utf-8 -*-
"""Names for common constants used by the API.

Example
-------

>>> import microspec as usp
>>> usp.GREEN
1

See the complete :ref:`list-of-constants`.

View the :ref:`test_constants-source` for examples using
constants.

Use constants instead of hard-coded numbers
-------------------------------------------

Calls using these constants should refer to them by the names
defined here instead of hard-coding the values in application
code. For example:

.. code-block:: python

    kit.setBridgeLED(led_setting=usp.GREEN) # <-- Do this.
    kit.setBridgeLED(led_setting=1)         # <-- NOT this!

Constants in microspec match microspeclib
-----------------------------------------

List constants in microspeclib:

>>> import microspeclib.datatypes.types as dtypes
>>> dtypes.__all__
['StatusOK', 'StatusError', ...]

These constants are defined in the ``globals`` object in the
:ref:`JSON API config file <dev-kit-API-JSON>`.

Example
^^^^^^^

microspec ``OK`` equals microspeclib ``StatusOK``:

>>> usp.OK == dtypes.StatusOK
True

The tests in
:class:`microspec.tests.test_constants.TestConsistent_with_microspeclib`
checks if the constants in the API are consistent with the JSON
config file.

.. _list-of-constants:

list of constants
-----------------
"""
# Sphinx autodoc starts the list of constants here.

import microspeclib.datatypes.types as _dtypes

# types.__all__ is the list of names in JSON section "globals"
_global_names = _dtypes.__all__

# Create a list of values for each name.
_global_values = [getattr(_dtypes, name) for name in _global_names]

# Combine the names and values into a dictonary.
_constants = dict(zip(_global_names, _global_values))

# Define user-friendly names for each value
# Put an empty docstring after each for pick-up by Sphinx autodoc

# status
OK = _constants['StatusOK']
"""int: The dev-kit successfully executed the command.

See Also
--------
ERROR
"""
ERROR = _constants['StatusError']
"""int: The dev-kit failed to execute the command.

The usual cause is that the command was called with one or more
invalid inputs. For example, ``42`` is invalid for ``led_num`` in
``getBridgeLED(led_num=42)``.

Other possible reasons are:

    - the command itself is invalid
    - serial communication failed

See Also
--------
OK
"""
TIMEOUT = 2
"""int: The command timed out before a response was received.

For applications that run a long time, such as data loggers and
free-running plot GUIs, there are occasional timeouts when
calling :func:`~micropsec.commands.Devkit.captureFrame`. These
applications should check the
:class:`~micropsec.replies.captureFrame_response.status`
attribute of responses to
:func:`~micropsec.commands.Devkit.captureFrame` and ignore the
data if the status is 'TIMEOUT'.

A ``UserWarning`` is also issued when a timeout occurs,
identifying which command timed out. This is not an exception, so
it does not cause the application to terminate.

Notes
-----
The :class:`~microspec.commands.Devkit` attribute ``timeout``
defaults to 2 seconds, which is usually long enough to send a
command, execute it on the dev-kit, and receive a response back
on the host computer running the application. It is rare to
observe a timeout when sending commands at the REPL or executing
a script that runs a few commands and exits. Users can observe
a timeout condition by setting a very short timeout such as 1ms.
"""

# led_setting
GREEN = _constants['LEDGreen']
"""int: LED is ON and GREEN.

See Also
--------
OFF
RED
"""
RED = _constants['LEDRed']
"""int: LED is ON and RED.

See Also
--------
OFF
GREEN
"""
OFF = _constants['LEDOff']
"""int: LED is OFF.

See Also
--------
GREEN
RED
"""

# binning
BINNING_OFF = 0
"""int: Pixels are not binned.

There are 784 pixels with 7.8µm pitch. The first 14 are optically
black.

See Also
--------
BINNING_ON
"""
BINNING_ON = 1
"""int: Pixels are binned.

There are 392 pixels with 15.6µm pitch. The first 7 are optically
black. This is the recommended and default configuration.

See Also
--------
BINNING_OFF
"""

# gain
GAIN1X = _constants['Gain1x']
"""int: Pixel analog voltage gain is 1x.

This is the recommended and default configuration.
"""
GAIN2_5X = _constants['Gain2_5x']
"""int: Pixel analog voltage gain is 2.5x."""
GAIN4X = _constants['Gain4x']
"""int: Pixel analog voltage gain is 4x."""
GAIN5X = _constants['Gain5x']
"""int: Pixel analog voltage gain is 5x."""

# row_bitmap
ALL_ROWS = _constants['RowsDefault']
"""int: Use all five rows of pixels.

Pixel height is divided into five rows. Using all five rows, the
pixels are 312.5µm tall. This is the recommended and default
configuration.

``row_bitmap=31`` means "all five rows" because 31 in binary is
``0001 1111``:

>>> 0b00011111
31

Similarly, ``row_bitmap=7`` means only use rows 1, 2, and 3:

>>> 0b00000111
7
"""

# TODO: add to JSON config file
MAX_CYCLES = 65500 # 1310 milliseconds
"""int: Longest exposure time (integration time)."""
MIN_CYCLES = 1 # 0.02 milliseconds
"""int: Shortest exposure time (integration time)."""

# Define user-friendly dicts to look up names from values in context.
_status_constants   = [ OK,   ERROR ,  TIMEOUT  ]
_status_names       = ['OK', 'ERROR', 'TIMEOUT' ]
status_dict = dict(zip(_status_constants, _status_names))
""" """
_led_setting_constants  = [ OFF,   GREEN,   RED ]
_led_setting_names      = ['OFF', 'GREEN', 'RED']
led_dict = dict(zip(_led_setting_constants, _led_setting_names))
""" """
_binning_constants  = [ BINNING_OFF,   BINNING_ON ]
_binning_names      = ['BINNING_OFF', 'BINNING_ON']
binning_dict = dict(zip(_binning_constants, _binning_names))
""" """
_gain_constants  = [ GAIN1X,   GAIN2_5X,   GAIN4X,   GAIN5X ]
_gain_names      = ['GAIN1X', 'GAIN2_5X', 'GAIN4X', 'GAIN5X']
gain_dict = dict(zip(_gain_constants, _gain_names))
""" """
row_dict = {ALL_ROWS: 'ALL_ROWS'}
""" """

