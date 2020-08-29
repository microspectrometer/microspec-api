# -*- coding: utf-8 -*-
"""Format command responses for use in applications."""
# __all__ = [
#     'getBridgeLED_response',
#     'setBridgeLED_response',
#     'getSensorLED_response',
#     'setSensorLED_response',
#     'getSensorLED_response',
#     'setSensorConfig_response',
#     'setExposure_response',
#     ]

from collections import namedtuple

# ----------------------
# | Docstring Snippets |
# ----------------------

_status = """\
status : str

    Serial communication status is either
    :data:`~microspec.constants.OK`
    or :data:`~microspec.constants.ERROR`.
    If ``status`` is ``'ERROR'`` the other attributes are not
    valid.
"""

_led_setting = """\
led_setting : str

    The LED is set to one of three states:
    :data:`~microspec.OFF`, :data:`~microspec.GREEN`, or
    :data:`~microspec.RED`.
"""

_created_from = """\
This response contains the attributes output with the
``__str__()`` method of ``microspeclib`` response:\
"""

_has_no_serial_attrs = """\
This response does not include the serial communication
attributes of the lower-level response. This is to prevent
applications from directly referencing the serial
communication data.
"""

_replaces_int_with_str = """\
In addition, this response replaces attribute integer values
with strings (e.g., 'OK' replaces 0). This makes the response
easier to read. The strings match the names of the constants
defined in :mod:`microspec.constants`.
"""

_common = {
    "status"                : _status,
    "led_setting"           : _led_setting,
    "created_from"          : _created_from,
    "has_no_serial_attrs"   : _has_no_serial_attrs,
    "replaces_int_with_str" : _replaces_int_with_str,
    }

getBridgeLED_response = namedtuple(
        'getBridgeLED_response',
        ['status', 'led_setting']
        )
getBridgeLED_response.__doc__ = """
Response to command :func:`~microspec.commands.Devkit.getBridgeLED`.

Attributes
----------
{status}
{led_setting}

Notes
-----
{created_from}
:data:`~microspeclib.datatypes.bridge.BridgeGetBridgeLED`.

See Also
--------
~microspec.commands.Devkit.getBridgeLED
""".format(**_common)

setBridgeLED_response = namedtuple(
        'setBridgeLED_response',
        ['status']
        )
setBridgeLED_response.__doc__ = """
Response to command :func:`~microspec.commands.Devkit.setBridgeLED`.

Attributes
----------
{status}

Notes
-----
{created_from}
:data:`~microspeclib.datatypes.bridge.BridgeSetBridgeLED`.

See Also
--------
~microspec.commands.Devkit.setBridgeLED
""".format(**_common)

getSensorLED_response = namedtuple(
        'getSensorLED_response',
        ['status', 'led_setting']
        )
getSensorLED_response.__doc__ = """
Response to command :func:`~microspec.commands.Devkit.getSensorLED`.

Attributes
----------
{status}
{led_setting}

Notes
-----
{created_from}
:data:`~microspeclib.datatypes.sensor.SensorGetSensorLED`.

See Also
--------
~microspec.commands.Devkit.getSensorLED
""".format(**_common)

setSensorLED_response = namedtuple(
        'setSensorLED_response',
        ['status']
        )
setSensorLED_response.__doc__ = """
Response to command :func:`~microspec.commands.Devkit.setSensorLED`.

Attributes
----------
{status}

Notes
-----
{created_from}
:data:`~microspeclib.datatypes.sensor.SensorSetSensorLED`.

See Also
--------
~microspec.commands.Devkit.setSensorLED
""".format(**_common)

getSensorConfig_response = namedtuple(
        'getSensorConfig_response',
        ['status', 'binning', 'gain', 'row_bitmap']
        )

setSensorConfig_response = namedtuple(
        'setSensorConfig_response',
        ['status']
        )

setExposure_response = namedtuple(
        'setExposure_response',
        ['status']
        )

getExposure_response = namedtuple(
        'getExposure_response',
        ['status', 'ms', 'cycles']
        )
