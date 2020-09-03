Code coverage
-------------

Reporting code coverage requires cloning the project repository.

.. code-block:: bash

    git clone https://github.com/microspectrometer/microspec.git

Enter the top-level folder of the repository:

.. code-block:: bash

    cd microspec

Code coverage by unit tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Report how much of the microspec module code base is executed during
unit tests:

.. code-block:: bash

    coverage run -m pytest microspec
    coverage report -m --include microspec/*

Here is example output during development:

::

    Name                                Stmts   Miss  Cover   Missing
    -----------------------------------------------------------------
    microspec/__init__.py                   3      0   100%
    microspec/commands.py                  49      3    94%   340, 345, 385
    microspec/constants.py                 33      0   100%
    microspec/helpers.py                    7      0   100%
    microspec/replies.py                   20      0   100%
    microspec/tests/__init__.py             0      0   100%
    microspec/tests/conftest.py             5      0   100%
    microspec/tests/test_commands.py      158      0   100%
    microspec/tests/test_constants.py      82      0   100%
    -----------------------------------------------------------------
    TOTAL                                 357      3    99%

The above report shows 100% test coverage except for lines 340, 345, and
385 of ``microspec.commands``.

For example, at this stage of development, line 340 raises TypeError for
a missing argument. The test coverage report, therefore, says I did not
test the case where the exception is raised (the case where the argument
is missing).

After adding a test ``with pytest.raises(TypeError)``, line 340 is no
longer listed as missing:

::

    Name                                Stmts   Miss  Cover   Missing
    -----------------------------------------------------------------
    microspec/commands.py                  49      2    96%   345, 385

Code coverage by doctest examples
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Report how much of the microspec module code base is executed by
**doctest examples**:

.. code-block:: bash

    coverage run -m microspec
    coverage report -m --include microspec/*

(Running ``microspec`` runs all of the doctest examples.)

Here is example output during development:

::

    Name                     Stmts   Miss  Cover   Missing
    ------------------------------------------------------
    microspec/__init__.py        3      0   100%
    microspec/__main__.py       20     13    35%   383-386, 392-398, 411-412
    microspec/commands.py       49     33    33%   107-112, 149-153, 198-203, 265-269, 284-295, 315-319, 339-361, 376-382, 385
    microspec/constants.py      33      0   100%
    microspec/helpers.py         7      4    43%   27-30, 57
    microspec/replies.py        20      0   100%
    ------------------------------------------------------
    TOTAL                      132     50    62%

The coverage **should not** be 100%: examples are **not** meant to
exhaustively illustrate every corner case (that's what the unit tests
are for). Coverage should not be too lower either. There is no specific
goal for percentage coverage.

The useful information in this report is the missing lines. I manually
check that these lines are not example-worthy.

