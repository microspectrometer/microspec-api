# -*- coding: utf-8 -*-
"""Define classes of command responses.

Application code should **not** instantiate classes defined in
this module. Command responses are generated internally by module
:mod:`~microspec.commands`.
"""

from collections import namedtuple

# ----------------------
# | Docstring Snippets |
# ----------------------

_status = """\
status : str

    Serial communication status is either
    :data:`~microspec.constants.OK`, 
    :data:`~microspec.constants.ERROR`, or
    :data:`~microspec.constants.TIMEOUT`.

    Applications usually do not need to check ``status`` because
    the :mod:`~microspec.commands` check ``status`` internally
    and either issue a warning or raise an exception if
    ``status`` is not :data:`~microspec.constants.OK`.

    Applications *should* check ``status`` for the specific
    use-cases documented in the :mod:`~microspec.commands`.

    :data:`~microspec.constants.OK`:

        Usually ``status`` is ``'OK'``.

    :data:`~microspec.constants.ERROR`:

        ``'ERROR'`` indicates a serial communication error, so
        the other response attributes are not valid.

    :data:`~microspec.constants.TIMEOUT`:

        ``'TIMEOUT'`` means the command timed out before a
        response was received from the dev-kit, so the other
        response attributes are not valid. The timeout is set by
        :class:`~microspec.commands.Devkit` attribute
        ``timeout``.
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

captureFrame_response = namedtuple(
        'captureFrame_response',
        ['status', 'num_pixels', 'pixels', 'frame']
        )

autoExposure_response = namedtuple(
        'autoExposure_response',
        ['status', 'success', 'iterations']
        )

getAutoExposeConfig_response = namedtuple(
        'getAutoExposeConfig_response',
        [
            'status',
            'max_tries',
            'start_pixel',
            'stop_pixel',
            'target',
            'target_tolerance',
            'max_exposure'
         ])

setAutoExposeConfig_response = namedtuple(
        'setAutoExposeConfig_response',
        ['status']
        )
