.. _chromation-dev-kit:

Chromation Dev-kit
==================

Open serial communication
-------------------------

Open serial communication by instantiating Devkit:

>>> import microspec as usp
>>> kit = usp.Devkit()
>>> kit.serial.is_open
True

Close serial communication
--------------------------

Serial communication **closes automatically** when the
application exits.

Serial communication also closes automatically when exiting the
Python REPL or running a test.

Open and close at the Python REPL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Communication closes when you ``exit()`` the REPL.

Open a REPL::

    python

Open communication:

.. code-block:: python

    >>> import microspec
    >>> kit = microspec.Devkit()

Exit the REPL:

.. code-block:: python

    >>> exit()

Communication is **automatically closed**.

Close communication manually with ``kit.serial.close()``.
Manually closing communication is handy when testing commands at
the REPL while developing an application:

    - use the REPL to test some code
    - close communication at the REPL with ``kit.serial.close()``
    - insert the code in the application
    - run the application to test the change
    - then resume work at the REPL with ``kit.serial.open()``

Manually close serial communication with
:func:`microspeclib.commands.Devkit.serial.close`:

.. code-block:: python

    >>> kit.serial.is_open
    True
    >>> kit.serial.close()
    >>> kit.serial.is_open
    False

Re-open serial communication after a close with
:func:`microspeclib.commands.Devkit.serial.open`:

.. code-block:: python

    >>> kit.serial.close()
    >>> kit.serial.is_open
    False
    >>> kit.serial.open()
    >>> kit.serial.is_open
    True

Open and close during doctest tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Running ``doctest`` on a file with
:class:`~micropsec.commands.Devkit` examples, the dev-kit remains
open for the duration of the docstring and closes when the
docstring ends. If the file contains multiple docstrings that
contain examples using the dev-kit, each one needs to open
communication with the dev-kit.

Open and close during pytest tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For tests defined in a **single file**, serial open/close happens
just as it does for any other application, i.e., open
communication at the module level (i.e., at the top of the test
script, outside of any test function or test class) and
communication closes automatically when the test script
terminates.

For tests defined across **multiple files**, the tests run faster
if the test suite opens communication at the beginning of the
session and then closes communication only when all tests are
finished. Chromation recommends using ``pytest`` with a
``conftest.py`` to define a session-scoped test fixture that
opens communication and returns the ``Devkit`` instance for use
by the entire test session. This also reduces the number of lines
of test code.

For example, the ``conftest.py`` in ``microspec/tests`` defines a
session-scope fixture named ``kit``:

.. code-block:: python

    @pytest.fixture(scope="session")
    def kit():
        """Open communication with the dev-kit once for all tests."""
        return usp.Devkit()

Then tests access the instance of ``usp.Devkit()`` by taking
``kit`` as an argument and using ``kit`` in the function body.

For example, from ``microspec/tests/test_commands.py``:

.. code-block:: python

    class TestCommandGetExposure(Setup):
        # Fixture 'kit' yields an instance of ``Devkit()``.
        def test_Call_getExposure(self, kit): # fixture name: kit
            # ``kit`` is the instance of ``Devkit()`` from the
            # fixture:
            assert kit.getExposure().status == 'OK'

Here is a version of the above fixture for the case where the
tests need setup before opening communication and teardown after
closing communication.

.. code-block:: python

    @pytest.fixture(scope="session")
    def kit(): # setup/teardown version
        """Open communication with the dev-kit once for all tests."""
        # Put SETUP code BEFORE the yield
        print("\nOpen communication with the dev-kit...")
        yield usp.Devkit()
        # Put TEARDOWN code AFTER the yield
        print("\n...Closed communication with the dev-kit.")

In the above example, the **setup** and **teardown** print a
message when communication opens and closes. The scope is for the
session, so:

    - the open message prints only once at the **beginning** of
      the test suite
    - the close message prints only once at the **end** of the
      test suite

If the actual setup and teardown code contains ``print()``
statements, run ``pytest`` with flag ``-s`` to make the
``print()`` output visible at the console.

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

The maximum allowed exposure time is 65500 cycles:

>>> usp.MAX_CYCLES
65500

The minimum allowed exposure time is 1 cycle:

>>> usp.MIN_CYCLES
1
