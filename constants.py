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

