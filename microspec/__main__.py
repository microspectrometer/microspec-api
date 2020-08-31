# -*- coding: utf-8 -*-
"""
Unit tests
----------

Run package as a module
^^^^^^^^^^^^^^^^^^^^^^^

Package ``microspec`` unit tests are the doctests in the
:mod:`microspec.__main__.py` docstring.

Connect a dev-kit over USB. Then run the tests with this command:

.. code-block:: bash

    python -m microspec

Doctest setup
^^^^^^^^^^^^^

Import as ``usp`` to make doctests easier to read:

>>> import microspec as usp

.. _test-constants:

Test microspec.constants
------------------------

Responses use a dictionary to get the string form of constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``OK`` maps to 0:

>>> print(f"{usp.status_dict.get(usp.OK)} == {usp.OK}")
OK == 0

``ERROR`` maps to 1:

>>> print(f"{usp.status_dict.get(usp.ERROR)} == {usp.ERROR}")
ERROR == 1

``OFF`` maps to 0:

>>> print(f"{usp.led_dict.get(usp.OFF)} == {usp.OFF}")
OFF == 0

``GREEN`` maps to 1:

>>> print(f"{usp.led_dict.get(usp.GREEN)} == {usp.GREEN}")
GREEN == 1

``RED`` maps to 2:

>>> print(f"{usp.led_dict.get(usp.RED)} == {usp.RED}")
RED == 2

``BINNING_OFF`` maps to 0:

>>> print(f"{usp.binning_dict.get(usp.BINNING_OFF)} "
... f"== {usp.BINNING_OFF}")
BINNING_OFF == 0

``BINNING_ON`` maps to 1:

>>> print(f"{usp.binning_dict.get(usp.BINNING_ON)} "
... f"== {usp.BINNING_ON}")
BINNING_ON == 1

``GAIN1X`` maps to 1:

>>> print(f"{usp.gain_dict.get(usp.GAIN1X)} "
... f"== {usp.GAIN1X}")
GAIN1X == 1

``GAIN2_5X`` maps to 0x25:

>>> print(f"{usp.gain_dict.get(usp.GAIN2_5X)} "
... f"== 0x{usp.GAIN2_5X:X}")
GAIN2_5X == 0x25

``GAIN4X`` maps to 4:

>>> print(f"{usp.gain_dict.get(usp.GAIN4X)} "
... f"== {usp.GAIN4X}")
GAIN4X == 4

``GAIN5X`` maps to 5:

>>> print(f"{usp.gain_dict.get(usp.GAIN5X)} "
... f"== {usp.GAIN5X}")
GAIN5X == 5

``ALL_ROWS`` maps to 0x1F:

>>> print(f"{usp.row_dict.get(usp.ALL_ROWS)} "
... f"== 0x{usp.ALL_ROWS:X}")
ALL_ROWS == 0x1F

Constants match if defined in both microspec and microspeclib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

List constants defined by microspeclib:

>>> import microspeclib.datatypes.types as dtypes
>>> dtypes.__all__
['StatusOK', 'StatusError', 'LEDOff', 'LEDGreen', 'LEDRed', 'BinningDefault', 'Gain1x', 'Gain2_5x', 'Gain4x', 'Gain5x', 'GainDefault', 'RowsDefault']

``OK`` equals ``StatusOK``:

>>> usp.OK == dtypes.StatusOK
True

``ERROR`` equals ``StatusError``:

>>> usp.ERROR == dtypes.StatusError
True

``OFF`` equals ``LEDOff``:

>>> usp.OFF == dtypes.LEDOff
True

``GREEN`` equals ``LEDGreen``:

>>> usp.GREEN == dtypes.LEDGreen
True

``RED`` equals ``LEDRed``:

>>> usp.RED == dtypes.LEDRed
True

``GAIN1X`` equals ``Gain1x``:

>>> usp.GAIN1X == dtypes.Gain1x
True

``GAIN2_5X`` equals ``Gain2_5x``:

>>> usp.GAIN2_5X == dtypes.Gain2_5x
True

``GAIN4X`` equals ``Gain4x``:

>>> usp.GAIN4X == dtypes.Gain4x
True

``GAIN5X`` equals ``Gain5x``:

>>> usp.GAIN5X == dtypes.Gain5x
True

.. _test-commands-and-responses:

Test microspec.commands and microspec.replies
---------------------------------------------

Open serial communication by instantiating Devkit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> kit = usp.Devkit()
>>> kit.serial.is_open
True

.. _test-indicator-LED-commands:

Setup for indicator-LED tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set all LEDs to a known state

>>> kit.setBridgeLED(led_num=0, led_setting=usp.GREEN)
setBridgeLED_response(status='OK')

>>> kit.setSensorLED(led_num=0, led_setting=usp.GREEN)
setSensorLED_response(status='OK')

>>> kit.setSensorLED(led_num=1, led_setting=usp.GREEN)
setSensorLED_response(status='OK')

Test indicator LED commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**getBridgeLED**

Call ``getBridgeLED`` with its optional parameter:

>>> kit.getBridgeLED(led_num=0)
getBridgeLED_response(status='OK', led_setting='GREEN')

Call ``getBridgeLED`` without its optional parameter:

>>> kit.getBridgeLED()
getBridgeLED_response(status='OK', led_setting='GREEN')

Call ``getBridgeLED`` with an invalid parameter value:

>>> kit.getBridgeLED(led_num=1)
getBridgeLED_response(status='ERROR', led_setting=None)

**setBridgeLED**

Call ``setBridgeLED`` with its optional parameter:

>>> kit.setBridgeLED(led_num=0, led_setting=usp.GREEN)
setBridgeLED_response(status='OK')

Call ``setBridgeLED`` without its optional parameter:

>>> kit.setBridgeLED(led_setting=usp.GREEN)
setBridgeLED_response(status='OK')

Call ``setBridgeLED`` with an invalid parameter value:

>>> kit.setBridgeLED(led_num=1, led_setting=usp.GREEN)
setBridgeLED_response(status='ERROR')

**getSensorLED**

``getSensorLED`` has no optional parameters:

>>> kit.getSensorLED()
Traceback (most recent call last):
    ...
TypeError: getSensorLED() missing 1 required positional argument: 'led_num'

**setSensorLED**

``setSensorLED`` has no optional parameters:

>>> kit.setSensorLED()
Traceback (most recent call last):
    ...
TypeError: setSensorLED() missing 2 required positional arguments: 'led_num' and 'led_setting'

**Sensor LED behavior**

.. note::

    Sensor ``led0`` indicates *busy*:

    - ``led0`` is **OFF** while the Sensor board is **busy**
      executing a command
    - ``led0`` is **ON** when execution is **done**

    Sensor ``led0`` should **always** be **GREEN** when it is on.

    The firmware turns ``led0`` **RED** if the SPI Rx buffer is
    full. This is a serial communication error. Chromation has
    never seen this error occur in practice. *Please contact
    Chromation if you encounter this condition.*

    Sensor ``led1`` indicates *auto-expose status*:

    - ``led1`` is **RED** while auto-expose is **busy**
    - ``led1`` stays **RED** if auto-expose **fails**
    - ``led1`` turns **GREEN** if auto-expose **succeeds**

.. warning::

    *Sensor LEDs are controlled by firmware.* Chromation
    recommends that applications:

    - do not call ``setSensorLED`` for ``led0`` and ``led1``

        - this will lead to confusing LED behavior and defeat the
          point of the Sensor board's indicator LEDs

    - do not call ``getSensorLED`` for ``led0``

        - this is harmless, but there is no point because it will
          always report the LED is ``OFF``

``getSensorLED`` always replies ``led0`` is ``OFF``:

>>> # Setup: make ``led0`` green
>>> kit.setSensorLED(led_num=0, led_setting=usp.GREEN)
setSensorLED_response(status='OK')
>>> # Test: ``led0`` looks green but replies that ``led0`` is off
>>> kit.getSensorLED(led_num=0)
getSensorLED_response(status='OK', led_setting='OFF')
>>> # Test: ``led0`` turns back ON after executing this command
>>> kit.setSensorLED(led_num=0, led_setting=usp.OFF)
setSensorLED_response(status='OK')
>>> # Test: Turn ``led0`` RED (don't do this in an application)
>>> kit.setSensorLED(led_num=0, led_setting=usp.RED)
setSensorLED_response(status='OK')
>>> # Teardown: Put ``led0`` back to GREEN
>>> kit.setSensorLED(led_num=0, led_setting=usp.GREEN)
setSensorLED_response(status='OK')

``getSensorLED`` replies GREEN if ``led1`` is GREEN:

>>> # Setup: make ``led1`` green
>>> kit.setSensorLED(led_num=1, led_setting=usp.GREEN)
setSensorLED_response(status='OK')
>>> # Test: Reply indicates green
>>> kit.getSensorLED(led_num=1)
getSensorLED_response(status='OK', led_setting='GREEN')

``getSensorLED`` replies RED if ``led1`` is RED:

>>> # Setup: make ``led1`` red
>>> kit.setSensorLED(led_num=1, led_setting=usp.RED)
setSensorLED_response(status='OK')
>>> # Test: Reply indicates red
>>> kit.getSensorLED(led_num=1)
getSensorLED_response(status='OK', led_setting='RED')
>>> # Teardown: Put ``led1`` back to GREEN
>>> kit.setSensorLED(led_num=1, led_setting=usp.GREEN)
setSensorLED_response(status='OK')

Test spectrometer configuration commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**setSensorConfig**

>>> kit.setSensorConfig(
...     binning    = usp.BINNING_ON,
...     gain       = usp.GAIN1X,
...     row_bitmap = usp.ALL_ROWS
...     )
setSensorConfig_response(status='OK')

**getSensorConfig**

>>> print(kit.getSensorConfig())
getSensorConfig_response(status='OK', binning='BINNING_ON', gain='GAIN1X', row_bitmap='ALL_ROWS')

Test exposure commands
^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Exposure time (a.k.a, integration time) is measured in units
    of cycles in the dev-kit firmware. One cycle is 20µs (20.0e-6
    s).

    Applications should not need to convert between units of
    seconds and cycles:

        - ``setExposure`` accepts time in both units
        - ``getExposure`` returns time in both units

    Functions :func:`~microspec.helpers.to_cycles` and
    :func:`~microspec.helpers.to_ms` are available in case an
    application needs to convert time units.

Use :func:`~microspec.helpers.to_cycles` to convert milliseconds
to cycles.

>>> usp.to_cycles(ms=5.0)
250

Use :func:`~microspec.helpers.to_ms` to convert cycles to
milliseconds.

>>> usp.to_ms(cycles=250)
5.0

>>> # Maximum allowed exposure time is 65500 cycles
>>> usp.MAX_CYCLES
65500
>>> # Maximum allowed exposure time is 1310.0 ms
>>> usp.to_ms(cycles=65500)
1310.0
>>> # to_cycles() clamps the result at 65500
>>> usp.to_cycles(ms=1311)
65500
>>> # Minimum allowed exposure time is 0.02 ms
>>> usp.MIN_CYCLES
1
>>> usp.to_ms(cycles=1)
0.02
>>> # cycles is assumed to be between 1 and 65500
>>> # but since milliseconds are never sent to the firmware
>>> # to_ms() does not clamp the milliseconds result
>>> usp.to_ms(cycles=75500)
1510.0
>>> usp.to_ms(cycles=-1)
-0.02

**setExposure**

``setExposure`` accepts time in units of ms:

>>> kit.setExposure(ms=5.0)
setExposure_response(status='OK')

``setExposure`` accepts time in units of cycles:

>>> kit.setExposure(cycles=250)
setExposure_response(status='OK')

``setExposure`` requires an exposure time input

>>> kit.setExposure()
Traceback (most recent call last):
    ...
TypeError: setExposure() missing 1 required argument: 'ms' or 'cycles'

Calling ``setExposure`` with both ``ms`` and ``cycles`` is not
allowed:

>>> kit.setExposure(ms=5.0, cycles=250)
Traceback (most recent call last):
    ...
TypeError: setExposure() got an unexpected keyword 'cycles' \
(requires 'ms' or 'cycles' but received both)

``setExposure`` clamps time to the allowed range:

>>> # Test clamping exposure time to MAX
>>> usp.MAX_CYCLES
65500
>>> # Setup: set exposure time one cycle higher than the maximum
>>> kit.setExposure(cycles=usp.MAX_CYCLES+1)
setExposure_response(status='OK')
>>> # Test: expect the exposure time is 65500, not 65501
>>> kit.getExposure()
getExposure_response(status='OK', ms=1310.0, cycles=65500)

>>> # Test clamping exposure time to MIN
>>> usp.MIN_CYCLES
1
>>> # Setup: set exposure time one cycle lower than the minimum
>>> kit.setExposure(cycles=usp.MIN_CYCLES-1)
setExposure_response(status='OK')
>>> # Test: expect the exposure time is 1, not 0
>>> kit.getExposure()
getExposure_response(status='OK', ms=0.02, cycles=1)


**getExposure**

``getExposure`` reports exposure time in both units:

>>> # Setup: set exposure time to 5ms
>>> kit.setExposure(ms=5)
setExposure_response(status='OK')
>>> # Test: expect 5.0ms and 250 cycles
>>> kit.getExposure()
getExposure_response(status='OK', ms=5.0, cycles=250)

*captureFrame*

>>> reply = kit.captureFrame()

The frame is stored as a Python ``list`` of numbers. Each number
is the signal strength at that pixel in units of *counts*.

The list starts with pixel 1. With pixel binning on, the frame
has 392 pixels, so the list ends with pixel 392:

>>> print(reply)
SensorCaptureFrame(status=0, num_pixels=392, pixels=[...])

The list ``pixels`` is hard to read on its own. Tag each pixel
with its pixel number. Turn the ``(pixnum,pixel)`` pairs into
a list of ``tuples`` with ``list(zip(pixnum,pixels))`` or, as
shown in this example, into a ``dict``:

>>> frame = dict(zip(range(1,reply.num_pixels+1), reply.pixels))
>>> print(frame)
{1: ..., 2: ..., ..., 391: ..., 392: ...}

This is still hard to read. Put each pixel on its own line:

>>> import pprint
>>> pprint.pprint(frame)
{1: ...,
 2: ...,
 ...
 391: ...,
 392: ...}

**Next command to test**


.. _test-reply-attributes:

Test attributes of microspec.replies
------------------------------------

All commands respond with the attribute ``status``:

>>> reply = kit.getBridgeLED()
>>> reply.status
'OK'
>>> reply = kit.setBridgeLED(led_setting=usp.GREEN)
>>> reply.status
'OK'
>>> reply = kit.getSensorLED(led_num=0)
>>> reply.status
'OK'
>>> reply = kit.setSensorLED(led_num=0, led_setting=usp.GREEN)
>>> reply.status
'OK'
>>> reply = kit.getExposure()
>>> reply.status
'OK'

Response to ``getBridgeLED`` has attribute ``led_setting``:

>>> reply = kit.getBridgeLED()
>>> reply.led_setting
'GREEN'

Response to ``getSensorLED`` has attribute ``led_setting``:

>>> reply = kit.getSensorLED(led_num=0)
>>> reply.led_setting
'OFF'

"""

import doctest
doctest.testmod(verbose=False, optionflags=doctest.ELLIPSIS | doctest.FAIL_FAST)

# import microspec
# kit = microspec.Devkit()
# print(kit.getBridgeLED())
# kit.setSensorLED(led_num=1, led_setting=microspec.RED)
# print(kit.getSensorLED(led_num=1))
# print(f"led_setting {microspec.RED} is RED")

