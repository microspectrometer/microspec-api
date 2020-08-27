#!python.exe
# -*- coding: utf-8 -*-
"""
Check values of constants defined by microspec
>>> import microspec

OK equals 0
>>> print(f"{microspec.status_dict.get(microspec.OK)} == {microspec.OK}")
OK == 0

ERROR equals 1 (StatusError)
>>> print(f"{microspec.status_dict.get(microspec.ERROR)} == {microspec.ERROR}")
ERROR == 1

OFF equals 0 (LedOff)
>>> print(f"{microspec.led_dict.get(microspec.OFF)} == {microspec.OFF}")
OFF == 0

GREEN equals 1 (LedGreen)
>>> print(f"{microspec.led_dict.get(microspec.GREEN)} == {microspec.GREEN}")
GREEN == 1

RED equals 2 (LedRed)
>>> print(f"{microspec.led_dict.get(microspec.RED)} == {microspec.RED}")
RED == 2

BINNING_OFF equals 0
>>> print(f"{microspec.binning_dict.get(microspec.BINNING_OFF)} "
... f"== {microspec.BINNING_OFF}")
BINNING_OFF == 0

BINNING_ON equals 1
>>> print(f"{microspec.binning_dict.get(microspec.BINNING_ON)} "
... f"== {microspec.BINNING_ON}")
BINNING_ON == 1

GAIN1X equals 1 (Gain1x)
>>> print(f"{microspec.gain_dict.get(microspec.GAIN1X)} "
... f"== {microspec.GAIN1X}")
GAIN1X == 1

GAIN2_5X equals 0x25 (Gain2_5x)
>>> print(f"{microspec.gain_dict.get(microspec.GAIN2_5X)} "
... f"== 0x{microspec.GAIN2_5X:X}")
GAIN2_5X == 0x25

GAIN4X equals 4 (Gain4x)
>>> print(f"{microspec.gain_dict.get(microspec.GAIN4X)} "
... f"== {microspec.GAIN4X}")
GAIN4X == 4

GAIN5X equals 5 (Gain5x)
>>> print(f"{microspec.gain_dict.get(microspec.GAIN5X)} "
... f"== {microspec.GAIN5X}")
GAIN5X == 5

ALL_ROWS equals 0x1F (RowsDefault)
>>> print(f"{microspec.rows_dict.get(microspec.ALL_ROWS)} "
... f"== 0x{microspec.ALL_ROWS:X}")
ALL_ROWS == 0x1F

Check match between constants defined by microspec and microspeclib.

List constants defined by microspeclib
>>> import microspeclib.datatypes.types as dtypes
>>> dtypes.__all__
['StatusOK', 'StatusError', 'LEDOff', 'LEDGreen', 'LEDRed', 'BinningDefault', 'Gain1x', 'Gain2_5x', 'Gain4x', 'Gain5x', 'GainDefault', 'RowsDefault']

OK equals StatusOK
>>> microspec.OK == dtypes.StatusOK
True

ERROR equals StatusError
>>> microspec.ERROR == dtypes.StatusError
True

OFF equals LEDOff
>>> microspec.OFF == dtypes.LEDOff
True

GREEN equals LEDGreen
>>> microspec.GREEN == dtypes.LEDGreen
True

RED equals LEDRed
>>> microspec.RED == dtypes.LEDRed
True

GAIN1X equals Gain1x
>>> microspec.GAIN1X == dtypes.Gain1x
True

GAIN2_5X equals Gain2_5x
>>> microspec.GAIN2_5X == dtypes.Gain2_5x
True

GAIN4X equals Gain4x
>>> microspec.GAIN4X == dtypes.Gain4x
True

GAIN5X equals Gain5x
>>> microspec.GAIN5X == dtypes.Gain5x
True

Instantiate Devkit to open serial communication
>>> kit = microspec.Devkit()
>>> kit.serial.is_open
True

Command getBridgeLED has a default value for parameter led_num.

getBridgeLED has parameter led_num
>>> kit.getBridgeLED(led_num=0)
ReplyToGetBridgeLED(status='OK', led_setting='GREEN')

getBridgeLED defaults parameter led_num to 0
>>> kit.getBridgeLED()
ReplyToGetBridgeLED(status='OK', led_setting='GREEN')

getBridgeLED led_num=0 is the only allowed value
>>> kit.getBridgeLED(led_num=1)
ReplyToGetBridgeLED(status='ERROR', led_setting=None)

--left off here--
setBridgeLED defaults to LED0
>>> kit.setBridgeLED(led_setting=microspec.GREEN)

getSensorLED does not have default parameters
>>> print(kit.getSensorLED())
TypeError: getSensorLED() missing 1 required positional argument: 'led_num'

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

ReplyToGetBridgeLED has attribute status
>>> reply = kit.getBridgeLED()
>>> reply.status
0
>>> print(microspec.status_dict.get(reply.status))

ReplyToGetBridgeLED has attribute led_setting
>>> reply = kit.getBridgeLED()
>>> print(reply.led_setting)
1
"""

import doctest
doctest.testmod(verbose=False, optionflags=doctest.FAIL_FAST)

# import microspec
# kit = microspec.Devkit()
# kit.getBridgeLED()
# kit.setSensorLED(led_num=1, led_setting=microspec.RED)
# print(kit.getSensorLED(led_num=1))
# print(f"led_setting {microspec.RED} is RED")

