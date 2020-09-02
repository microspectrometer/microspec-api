# -*- coding: utf-8 -*-
"""
To run the documentation examples and/or the unit test suite, first
connect a dev-kit over USB.

Run the documentation examples
------------------------------

The examples in the documentation are tested with ``doctest``. Running
:mod:`microspec.__main__` runs all of the documentation examples:

.. code-block:: bash

    python -m microspec

Running the documentation examples only requires installing
``microspec``, it does not require cloning the project repository.

Run the unit tests
------------------

Running unit tests requires cloning the project repository. Unit tests
are in the ``tests`` folder of the ``microspec`` module.

First clone the project repository:

.. code-block:: bash

    git clone https://github.com/microspectrometer/microspec.git
    cd microspec/microspec/tests

These tests are completely separate from the top-level ``tests`` folder
which is for the ``microspeclib`` module. The ``tests`` inside the
``microspec`` module all require the physical dev-kit, while the
underlying ``microspeclib`` will skip hardware tests if no hardware is
connected.

``pytest`` without any options reports if all tests pass:

.. code-block:: bash

    pytest

Use option ``--testdox`` to read the test names as a form of
documentation:

.. code-block:: bash

    pytest --testdox

Devkit behavior
---------------

Open serial communication by instantiating Devkit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

>>> kit = usp.Devkit()
>>> kit.serial.is_open
True

Serial communication closes automatically when the application exits.

There are three cases that are not applications: the REPL, docstring
examples, and unit tests.

- *REPL* -- communication closes when you ``exit()`` the REPL
- *examples in docstrings* -- communication closes when the docstring ends
- *unit tests* -- ``conftest.py`` defines a test fixture that opens
  communication for the entire ``pytest`` test session, so communication
  closes when the test session ends.

Indicator LEDs
^^^^^^^^^^^^^^

The indicator LED on the **Bridge board** defaults to ``GREEN``. It is
available for dev-kit users to control in their application code.

The two indicator LEDs on the **Sensor board** are controlled by
firmware and are **not intended** for dev-kit users to control in an
application.

Indicator LEDs on the Sensor board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sensor ``led0`` indicates *busy*:

- ``led0`` is **OFF** while the Sensor board is **busy**
  executing a command
- ``led0`` is **ON** when execution is **done**

.. note::

    Sensor ``led0`` should **always** be **GREEN** when it is on.

    The firmware turns ``led0`` **RED** if the SPI Rx buffer is
    full. This is a serial communication error. Chromation has
    never seen this error occur in practice. *Please contact
    Chromation if you encounter this condition.*

Sensor ``led1`` indicates *auto-expose status*:

- ``led1`` is **RED** while auto-expose is **busy**
- ``led1`` stays **RED** if auto-expose **fails**
- ``led1`` turns **GREEN** if auto-expose **succeeds**

Nothing bad happens if reading/writing the sensor LEDs, but the firmware
uses these LEDs for visual indication about its state. Reading or
writing the LED states in an application will have unpredictable
results. Reading sensor LED1 does have predictable results -- it
indicates success/failure of auto-expose -- but it is more direct for
application code to read the ``success`` attribute of the
``autoExposure`` response.

Test spectrometer configuration commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**setSensorConfig**

>>> kit.setSensorConfig(
...     binning    = usp.BINNING_ON,
...     gain       = usp.GAIN1X,
...     row_bitmap = usp.ALL_ROWS
...     )
setSensorConfig_response(status='OK')

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

import microspec
import doctest
FLAGS = doctest.ELLIPSIS | doctest.FAIL_FAST
VERBOSE = False
# Run doctests in each submodule: commands, replies, constants, helpers
doctest.testmod(m=microspec.commands,  verbose=VERBOSE, optionflags=FLAGS)
doctest.testmod(m=microspec.replies,   verbose=VERBOSE, optionflags=FLAGS)
doctest.testmod(m=microspec.constants, verbose=VERBOSE, optionflags=FLAGS)
doctest.testmod(m=microspec.helpers,   verbose=VERBOSE, optionflags=FLAGS)

# import microspec
# kit = microspec.Devkit()
# print(kit.getBridgeLED())
# kit.setSensorLED(led_num=1, led_setting=microspec.RED)
# print(kit.getSensorLED(led_num=1))
# print(f"led_setting {microspec.RED} is RED")

