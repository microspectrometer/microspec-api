Dev-kit
=======

Open serial communication
-------------------------

Open serial communication by instantiating Devkit:

>>> import microspec as usp
>>> kit = usp.Devkit()
>>> kit.serial.is_open
True

Close serial communication
--------------------------

Serial communication closes automatically when the application exits.

Serial communication also closes automatically in other use
cases:

Python REPL
^^^^^^^^^^^

Communication closes when you ``exit()`` the REPL.

Open a REPL::

    python

Open communication:

.. code-block:: python

    >>> import microspec
    >>> kit = microspec.Devkit()

Communication closes automatically on exit:

.. code-block:: python

    >>> exit()

Tests
^^^^^

Running ``doctest`` on a file with
:class:`~micropsec.commands.Devkit` examples, the dev-kit remains
open for the duration of the docstring and closes when the
docstring ends. If the file contains multiple docstrings that
contain examples using the dev-kit, each one needs to open
communication with the dev-kit.

For tests defined in a single file, import ``microspec`` and open
communication just as you would for an application. For tests
defined across multiple files, the tests run faster if the test
suite opens communication at the beginning of the session and
then closes communication only when all tests are finished.
Chromation recommends using ``pytest`` with a ``conftest.py``
to define a session-scoped test fixture that opens communication
and returns the ``Devkit`` instance for use by the entire test
session. This also reduces the number of lines of test code. See
the ``conftest.py`` in ``microspec/tests``.

Indicator LEDs
--------------

Indicator LED on the Bridge board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The indicator LED on the **Bridge board** defaults to ``GREEN``.
It is available for dev-kit users to control in their application
code with :func:`~microspec.commands.Devkit.getBridgeLED` and
:func:`~microspec.commands.Devkit.setBridgeLED` .

Indicator LEDs on the Sensor board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The two indicator LEDs on the **Sensor board** are controlled by
firmware and are **not intended** for dev-kit users to control in
an application.

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

Exposure time (integration time)
--------------------------------

Exposure time (a.k.a, integration time) is measured in units
of cycles in the dev-kit firmware. One cycle is 20µs (20.0e-6
s).

.. note::

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

