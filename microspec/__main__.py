# -*- coding: utf-8 -*-
"""
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
def _print_all_tests(FLAGS):
    """Run doctest examples in each submodule and print each test.

    Maintain the list of submodules.
    """
    doctest.testmod(m=microspec.commands,  verbose=True, optionflags=FLAGS)
    doctest.testmod(m=microspec.replies,   verbose=True, optionflags=FLAGS)
    doctest.testmod(m=microspec.constants, verbose=True, optionflags=FLAGS)
    doctest.testmod(m=microspec.helpers,   verbose=True, optionflags=FLAGS)
def _print_summary(FLAGS):
    """Run doctest examples in each submodule and print a summary only.

    Maintain the list of microspec submodules.
    """
    print("Running doctest examples...\n")
    print(f"{'module'   :10}| doctest results")
    print(f"{'------'   :10}| ---------------")
    print(f"{'commands' :10}| {doctest.testmod(m=microspec.commands,  optionflags=FLAGS)}")
    print(f"{'replies'  :10}| {doctest.testmod(m=microspec.replies,   optionflags=FLAGS)}")
    print(f"{'constants':10}| {doctest.testmod(m=microspec.constants, optionflags=FLAGS)}")
    print(f"{'helpers'  :10}| {doctest.testmod(m=microspec.helpers,   optionflags=FLAGS)}")
def run_doctest_examples(flags, verbose=False):
    """Run the doctest examples in all the microspec submodules.

    With verbose=True, this behaves identical to calling
    doctest.testmod() on each microspec submodule.

    With verbose=False, only the summary of test results is printed.

    The default verbose=False behavior of doctest is to print nothing.
    This function modifies that behavior by collecting the test
    summaries and printing them in a table.
    """
    if verbose: _print_all_tests(flags)
    else: _print_summary(flags)
FLAGS = doctest.ELLIPSIS | doctest.FAIL_FAST
# run_doctest_examples(FLAGS, verbose=False)
