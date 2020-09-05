Unit tests
==========

Run microspec tests
-------------------

Enter the ``microspec`` directory and run ``pytest``:

.. code-block:: bash

   cd microspec
   pytest

Limit tests to one module:

.. code-block:: bash

   pytest --pyargs microspec.tests.test_constants

Output shows the tests pass:

.. code-block:: bash

   ...
   microspec/tests/test_constants.py ....          [100%]

Use flag ``--testdox`` to read the list of tests as if the test
names are the documentation:


.. code-block:: bash

   pytest --testdox --pyargs microspec.tests.test_constants

Example ``--testdox`` output:

.. code-block:: bash

   Values_of_status
    ✓ OK is 0
    ✓ ERROR is 1
    ✓ 0 maps to str OK
    ✓ 1 maps to str ERROR
    ...

See these unit tests for code examples
--------------------------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   microspec.tests.test_commands
   microspec.tests.test_constants
