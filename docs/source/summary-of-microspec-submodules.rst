Summary of microspec submodules
===============================

The ``microspec`` module has four submodules:
:mod:`~microspec.commands`, :mod:`~microspec.constants`,
:mod:`~microspec.replies`, and :mod:`~microspec.helpers`.

microspec.commands
------------------

:mod:`~microspec.commands` defines **class**
:class:`~microspec.commands.Devkit`:

.. code-block:: python
   :emphasize-lines: 2

   import microspec
   kit = microspec.Devkit()

Each command in the serial communication protocol is a ``Devkit``
**method**.

Example:

.. code-block:: python

   kit.getBridgeLED()

See the full list of commands in :mod:`microspec.commands`.

microspec.constants
-------------------

:mod:`~microspec.constants` **names** the constants in the serial
communication protocol.

  Example:

  .. code-block:: python
     :emphasize-lines: 2-3

     import microspec as usp
     usp.OK    # <---------------------- equals int 0
     usp.ERROR # <---------------------- equals int 1

See the full :ref:`list-of-constants`.

:mod:`~microspec.constants` also provides **dictionaries** for
converting a constant's **integer code** into a **string name**

  Example:

  .. code-block:: python
     :emphasize-lines: 2

     import microspec as usp
     usp.status_dict.get(usp.OK) # <---- returns str 'OK'

  .. note::

     Applications usually do not use these dictionaries. Module
     :mod:`~microspec.replies` uses these dictionaries to make
     command responses human-readable.

See the :ref:`test_constants-source` for examples using all
constants and all dicts in :mod:`~microspec.constants`.

Values of the constants match the values in the ``globals``
object in the :ref:`JSON API config file <dev-kit-API-JSON>`.

Consistency between constants defined in ``microspec`` and
``microspeclib`` is pinned by the unit tests in
:class:`~microspec.tests.test_constants.TestConsistent_with_microspeclib`.

.. note::

   Names of the constants are similar to the keys in the
   ``globals`` object, but the names are capitalized. Where
   possible, names are shortened for readability.

:mod:`~microspec.constants` defines additional constants
``MAX_CYCLES`` and ``MIN_CYCLES``. These are hard-coded in the
dev-kit firmware but are not (yet) listed in the JSON config
file.

microspec.replies
^^^^^^^^^^^^^^^^^

:mod:`~microspec.replies` defines a ``namedtuple`` for the
response to each command. Class ``Devkit`` uses ``replies`` to
re-package the response returned by the ``microspeclib`` API.

.. note::

    Do not directly use the :mod:`~microspec.replies` module in
    application code.

    The :mod:`~microspec.commands` module uses
    :mod:`~microspec.replies` to format responses. Application
    code should never need to instantiate a response.

.. note::

   The responses to each command are defined in the
   ``protocol.sensor`` object in the :ref:`JSON API config file
   <dev-kit-API-JSON>`. The responses to Bridge-specific commands
   are in ``protocol.bridge``. The API hides the bridge responses
   to commands directed at the sensor, which is most commands.

microspec.helpers
^^^^^^^^^^^^^^^^^

:mod:`~microspec.helpers` provides helper functions for common
application tasks. Use the helpers to reduce lines of code.

Example:

.. code-block:: python
   :emphasize-lines: 2

   import microspec as usp
   ms = usp.to_ms(usp.MAX_CYCLES)

The :mod:`~microspec.commands` module incorporates helpers where
possible. For example, :func:`~microspec.commands.setExposure`
and :func:`~microspec.commands.getExposure` already incorporate
the time conversion helpers.

Dev-kit behavior
----------------

Open serial communication
^^^^^^^^^^^^^^^^^^^^^^^^^

Open serial communication by instantiating Devkit:

>>> kit = usp.Devkit()
>>> kit.serial.is_open
True

Close serial communication
^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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



