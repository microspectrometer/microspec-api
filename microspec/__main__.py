# -*- coding: utf-8 -*-
"""
Unit test: Run package as a module
----------------------------------

>>> import microspec

Package ``microspec`` unit tests are the doctests in this
``__main__.py`` docstring.

Setup
^^^^^

Connect a dev-kit over USB. Then run the tests with this command:

.. code-block:: bash

    python -m microspec

.. _test-constants:

Test microspec.constants
------------------------

Responses use a dictionary to get the string form of constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``OK`` maps to 0:

>>> print(f"{microspec.status_dict.get(microspec.OK)} == {microspec.OK}")
OK == 0

``ERROR`` maps to 1:

>>> print(f"{microspec.status_dict.get(microspec.ERROR)} == {microspec.ERROR}")
ERROR == 1

``OFF`` maps to 0:

>>> print(f"{microspec.led_dict.get(microspec.OFF)} == {microspec.OFF}")
OFF == 0

``GREEN`` maps to 1:

>>> print(f"{microspec.led_dict.get(microspec.GREEN)} == {microspec.GREEN}")
GREEN == 1

``RED`` maps to 2:

>>> print(f"{microspec.led_dict.get(microspec.RED)} == {microspec.RED}")
RED == 2

``BINNING_OFF`` maps to 0:

>>> print(f"{microspec.binning_dict.get(microspec.BINNING_OFF)} "
... f"== {microspec.BINNING_OFF}")
BINNING_OFF == 0

``BINNING_ON`` maps to 1:

>>> print(f"{microspec.binning_dict.get(microspec.BINNING_ON)} "
... f"== {microspec.BINNING_ON}")
BINNING_ON == 1

``GAIN1X`` maps to 1:

>>> print(f"{microspec.gain_dict.get(microspec.GAIN1X)} "
... f"== {microspec.GAIN1X}")
GAIN1X == 1

``GAIN2_5X`` maps to 0x25:

>>> print(f"{microspec.gain_dict.get(microspec.GAIN2_5X)} "
... f"== 0x{microspec.GAIN2_5X:X}")
GAIN2_5X == 0x25

``GAIN4X`` maps to 4:

>>> print(f"{microspec.gain_dict.get(microspec.GAIN4X)} "
... f"== {microspec.GAIN4X}")
GAIN4X == 4

``GAIN5X`` maps to 5:

>>> print(f"{microspec.gain_dict.get(microspec.GAIN5X)} "
... f"== {microspec.GAIN5X}")
GAIN5X == 5

``ALL_ROWS`` maps to 0x1F:

>>> print(f"{microspec.rows_dict.get(microspec.ALL_ROWS)} "
... f"== 0x{microspec.ALL_ROWS:X}")
ALL_ROWS == 0x1F

Constants match if defined in both microspec and microspeclib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List constants defined by microspeclib:

>>> import microspeclib.datatypes.types as dtypes
>>> dtypes.__all__
['StatusOK', 'StatusError', 'LEDOff', 'LEDGreen', 'LEDRed', 'BinningDefault', 'Gain1x', 'Gain2_5x', 'Gain4x', 'Gain5x', 'GainDefault', 'RowsDefault']

``OK`` equals ``StatusOK``:

>>> microspec.OK == dtypes.StatusOK
True

``ERROR`` equals ``StatusError``:

>>> microspec.ERROR == dtypes.StatusError
True

``OFF`` equals ``LEDOff``:

>>> microspec.OFF == dtypes.LEDOff
True

``GREEN`` equals ``LEDGreen``:

>>> microspec.GREEN == dtypes.LEDGreen
True

``RED`` equals ``LEDRed``:

>>> microspec.RED == dtypes.LEDRed
True

``GAIN1X`` equals ``Gain1x``:

>>> microspec.GAIN1X == dtypes.Gain1x
True

``GAIN2_5X`` equals ``Gain2_5x``:

>>> microspec.GAIN2_5X == dtypes.Gain2_5x
True

``GAIN4X`` equals ``Gain4x``:

>>> microspec.GAIN4X == dtypes.Gain4x
True

``GAIN5X`` equals ``Gain5x``:

>>> microspec.GAIN5X == dtypes.Gain5x
True

.. _test-commands-and-responses:

Test microspec.commands and microspec.replies
---------------------------------------------

Open serial communication by instantiating Devkit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> kit = microspec.Devkit()
>>> kit.serial.is_open
True

Test setup
^^^^^^^^^^

Set the bridge LED before testing ``getBridgeLED``

>>> kit.setBridgeLED(led_num=0, led_setting=microspec.GREEN)
setBridgeLED_response(status='OK')

Test the different ways to send each command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Call ``getBridgeLED`` with its optional parameter:

>>> kit.getBridgeLED(led_num=0)
getBridgeLED_response(status='OK', led_setting='GREEN')

Call ``getBridgeLED`` without its optional parameter:

>>> kit.getBridgeLED()
getBridgeLED_response(status='OK', led_setting='GREEN')

Call ``getBridgeLED`` with an invalid parameter value:

>>> kit.getBridgeLED(led_num=1)
getBridgeLED_response(status='ERROR', led_setting=None)

Call ``setBridgeLED`` with its optional parameter:

>>> kit.setBridgeLED(led_num=0, led_setting=microspec.GREEN)
setBridgeLED_response(status='OK')

Call ``setBridgeLED`` without its optional parameter:

>>> kit.setBridgeLED(led_setting=microspec.GREEN)
setBridgeLED_response(status='OK')

Call ``setBridgeLED`` with an invalid parameter value:

>>> kit.setBridgeLED(led_num=1, led_setting=microspec.GREEN)
setBridgeLED_response(status='ERROR')

---left off here---

``getSensorLED`` always replies LED0 is ``OFF``

>>> # Setup: make LED0 green
>>> kit.setSensorLED(led_num=0, led_setting=microspec.GREEN)
setSensorLED_response(status='OK')
>>> # Test: still replies that LED0 is off
>>> kit.getSensorLED(led_num=0)
getSensorLED_response(status='OK', led_setting='OFF')

*LED0 turns OFF to indicate the Sensor board is busy executing
commands*

getSensorLED LED0 always returns 0 because LED0 indicates busy
>>> kit.setSensorLED(led_num=0, led_setting=1)
>>> print(kit.getSensorLED(led_num=0))
SensorGetSensorLED(status=0, led_setting=0)

getSensorLED LED1 returns GREEN if LED1 is GREEN
>>> kit.setSensorLED(led_num=1, led_setting=1)
>>> print(kit.getSensorLED(led_num=1))
SensorGetSensorLED(status=0, led_setting=1)

getSensorLED LED1 returns RED if LED1 is RED
>>> kit.setSensorLED(led_num=1, led_setting=microspec.RED)
>>> print(kit.getSensorLED(led_num=1))
SensorGetSensorLED(status=0, led_setting=2)
>>> print(f"led_setting {microspec.RED} is RED")
led_setting 2 is RED

Each command has a reply defined with its own attributes.

GetBridgeLED_reply has attribute status
>>> reply = kit.getBridgeLED()
>>> reply.status
0
>>> print(microspec.status_dict.get(reply.status))
OK

GetBridgeLED_reply has attribute led_setting
>>> reply = kit.getBridgeLED()
>>> print(reply.led_setting)
1
"""

import doctest
doctest.testmod(verbose=False, optionflags=doctest.FAIL_FAST)

# import microspec
# kit = microspec.Devkit()
# print(kit.getBridgeLED())
# kit.setSensorLED(led_num=1, led_setting=microspec.RED)
# print(kit.getSensorLED(led_num=1))
# print(f"led_setting {microspec.RED} is RED")

