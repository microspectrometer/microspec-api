Unit tests
----------

Running unit tests requires cloning the project repository:

.. code-block:: bash

    git clone https://github.com/microspectrometer/microspec.git

Unit tests are in the ``tests`` folder of the ``microspec``
module:

.. code-block:: bash

    microspec/microspec/tests

These tests are *completely separate* from the top-level
``tests`` folder which is for the ``microspeclib`` module. The
``tests`` inside the ``microspec`` module all require the
physical dev-kit, while the underlying ``microspeclib`` test
suite skips hardware tests if no hardware is connected.

Run the unit tests
^^^^^^^^^^^^^^^^^^

First connect a dev-kit over USB.

Next, enter the top-level directory of the ``microspec`` project
(the top-level of the repository clone):

.. code-block:: bash

   cd microspec

``pytest`` without any options runs **all tests in
microspec and microspeclib**

.. code-block:: bash

   pytest

Add module name ``microspec`` to run **only** the tests in
``microspec``:

.. code-block:: bash

   pytest microspec

Add option ``-x`` to stop after the first failing test:

.. code-block:: bash

   pytest microspec -x

Without any other options, ``pytest`` only reports if tests pass
or fail. Add option ``--testdox`` to read the test names:

.. code-block:: bash

   pytest microspec --testdox

.. note::

   The ``--testdox`` output is much easier to read than using
   pytest's ``-v`` (verbose) option. With ``--testdox``, the
   tests read like prose. With ``-v``, there is a lot of noise in
   the output.

