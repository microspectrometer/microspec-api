"""Module ``microspec`` is the API for the Chromation Spectrometer dev-kit.

Install
-------

Install the ``microspec`` project:

.. code-block:: bash

    pip install microspec

Usage
-----

Use the ``microspec`` module in an application:

.. code-block:: python

    import microspec
    kit = microspec.Devkit()

If the application uses ``microspec`` beyond the initial ``kit =
microspec.Devkit()``, Chromation recommends importing
``microspec`` *bound* as ``usp``:

.. code-block:: python

    import microspec as usp
    kit = usp.Devkit()
    kit.setBridgeLED(led_setting = usp.OFF)

Module List
-----------

The ``microspec`` module has four sub-modules:
:mod:`~microspec.commands`, :mod:`~microspec.constants`,
:mod:`~microspec.replies`, and :mod:`~microspec.helpers`.

:mod:`microspec.commands`
^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. note::

   The dev-kit commands are defined in the ``protocol.command``
   object of the :ref:`JSON API config file <dev-kit-API-JSON>`.

   - the **keys** are the **byte values** sent over serial to
     represent the command
   - the **values** are objects that **name the command** and
     describe its **parameters** and **byte format**.
   - **command names** are identical to the method names of
     ``Devkit`` except that the first letter is capitalized.

:mod:`microspec.constants`
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

:mod:`microspec.replies`
^^^^^^^^^^^^^^^^^^^^^^^^^

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

:mod:`microspec.helpers`
^^^^^^^^^^^^^^^^^^^^^^^^

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

"""
from .commands import * # class Devkit
from .constants import * # OK, ERROR, OFF, GREEN, RED, etc.
from .helpers import * # to_cycles(), to_ms()
