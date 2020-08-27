# -*- coding: utf-8 -*-
"""Convert microspeclib global constants to user-friendly names.

`globals` in `microspec/cfg/microspec.json` defines constants
used the by the API.

Calls using these constants should refer to them by the names
defined here instead of hard-coding the values in application
code.

`microspec` imports the constants.

Application code imports `microspec`. Application code does not
need to import `constants`.

Example
-------
>>> import microspec
>>> microspec.GREEN
1

TODO
----
Finish adding constants:
>>> import microspeclib.datatypes.types as dtypes
>>> dtypes.__all__
['StatusOK', 'StatusError', 'LEDOff', 'LEDGreen', 'LEDRed', 'BinningDefault', 'Gain1x', 'Gain2_5x', 'Gain4x', 'Gain5x', 'GainDefault', 'RowsDefault']

"""

import microspeclib.datatypes.types as _dtypes

# types.__all__ is the list of names in JSON section "globals"
_global_names = _dtypes.__all__

# Create a list of values for each name.
_global_values = [getattr(_dtypes, name) for name in _global_names]

# Combine the names and values into a dictonary.
_constants = dict(zip(_global_names, _global_values))

# Define user-friendly names for each value
GREEN = _constants['LEDGreen']
RED = _constants['LEDRed']
OFF = _constants['LEDOff']
OK = _constants['StatusOK']
ERROR = _constants['StatusError']
BINNING_OFF = 0
BINNING_ON = 1
GAIN1X = _constants['Gain1x']
GAIN2_5X = _constants['Gain2_5x']
GAIN4X = _constants['Gain4x']
GAIN5X = _constants['Gain5x']
ALL_ROWS = _constants['RowsDefault']

# Define user-friendly dicts to look up names from values in context.
_status_constants   = [ OK,   ERROR ]
_status_names       = ['OK', 'ERROR']
status_dict = dict(zip(_status_constants, _status_names))
_led_setting_constants  = [ OFF,   GREEN,   RED ]
_led_setting_names      = ['OFF', 'GREEN', 'RED']
led_dict = dict(zip(_led_setting_constants, _led_setting_names))
_binning_constants  = [ BINNING_OFF,   BINNING_ON ]
_binning_names      = ['BINNING_OFF', 'BINNING_ON']
binning_dict = dict(zip(_binning_constants, _binning_names))
_gain_constants  = [ GAIN1X,   GAIN2_5X,   GAIN4X,   GAIN5X ]
_gain_names      = ['GAIN1X', 'GAIN2_5X', 'GAIN4X', 'GAIN5X']
gain_dict = dict(zip(_gain_constants, _gain_names))
rows_dict = {ALL_ROWS: 'ALL_ROWS'}

