# -*- coding: utf-8 -*-
"""Convert microspeclib constants to user-friendly names.

Example
-------

.. code-block:: python

   import microspec as usp
   usp.GREEN

See the complete :ref:`list-of-constants`.

View the :ref:`test_constants-source` for examples using
constants. Also see the doctest examples in
:ref:`test-constants`.

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

See
:class:`microspec.tests.test_constants.TestConsistent_with_microspeclib`
for tests that the constants in the API are consistent with the
JSON config file.

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
"""The dev-kit successfully executed the command.

See Also
--------
ERROR
"""
ERROR = _constants['StatusError']
"""The dev-kit failed to execute the command.

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

# led_setting
GREEN = _constants['LEDGreen']
"""LED is ON and GREEN.

See Also
--------
OFF
RED
"""
RED = _constants['LEDRed']
"""LED is ON and RED.

See Also
--------
OFF
GREEN
"""
OFF = _constants['LEDOff']
"""LED is OFF.

See Also
--------
GREEN
RED
"""

# binning
BINNING_OFF = 0
"""Pixels are not binned.

There are 784 pixels with 7.8µm pitch. The first 14 are optically
black.

See Also
--------
BINNING_ON
"""
BINNING_ON = 1
"""Pixels are binned.

There are 392 pixels with 15.6µm pitch. The first 7 are optically
black. This is the recommended and default configuration.

See Also
--------
BINNING_OFF
"""

# gain
GAIN1X = _constants['Gain1x']
"""Pixel analog voltage gain is 1x.

This is the recommended and default configuration.
"""
GAIN2_5X = _constants['Gain2_5x']
"""Pixel analog voltage gain is 2.5x."""
GAIN4X = _constants['Gain4x']
"""Pixel analog voltage gain is 4x."""
GAIN5X = _constants['Gain5x']
"""Pixel analog voltage gain is 5x."""

# row_bitmap
ALL_ROWS = _constants['RowsDefault']
"""Use all five rows of pixels.

Pixel height is divided into five rows. Using all five rows, the
pixels are 312.5µm tall. This is the recommended and default
configuration.
"""

# TODO: add to JSON config file
MAX_CYCLES = 65500 # 1310 milliseconds
""" """
MIN_CYCLES = 1 # 0.02 milliseconds
""" """

# Define user-friendly dicts to look up names from values in context.
_status_constants   = [ OK,   ERROR ]
_status_names       = ['OK', 'ERROR']
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

