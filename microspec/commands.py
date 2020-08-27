# -*- coding: utf-8 -*-
"""A wrapper to simplify using the `microspeclib` API.

Provide application developers with default parameter values to API
calls, names for API constants, and a simpler import.

Provide microspeclib developers with API function wrappers to add
docstrings and code to the API functions on an individual basis.

Notes
-----
The interface defined by `microspeclib` is auto-generated. This makes
the interface easy to extend: just one JSON file to edit, one test
suite to run, and one set of documentation to rebuild. But this
automation prevents customization on a per-call basis.

The end result is that `microspeclib.simple`, the API intended for
writing applications, is usable but missing some friendly features:

- default parameter values for API calls
- simple access to the names of the API global constants
- a namespace that only goes one level-deep for:
    - importing the packge
    - reading documentation with pydoc

And for developers building on `microspeclib`, auto-generated code means
there are no function definitions for placing:

- docstrings
- helper functions

Helper functions take the burden of responsibility from the application:

- converting between firmware units of time and seconds
- patching serial communication problems that cause dropped frames and
  garbled communication of parameter values

This package adds all of the above functionality with class `Devkit`.

`Devkit` inherits `MicroSpecSimpleInterface` and overrides each method
with a one-liner that calls the `super().method`, creating a place to
add:

- default parameter values
- docstrings
- helpers
- serial communication patches

This package also defines named constants that get their values from the
`globals` in `microspec/cfg/microspec.json`.

Example
-------
>>> import microspec
>>> kit = microspec.Devkit()
>>> print(kit.setBridgeLED(led_setting=microspec.OFF))
BridgeSetBridgeLED(status=0)

TODO
----
Add the other API calls.

"""

__all__ = ['Devkit']

from microspeclib.simple import MicroSpecSimpleInterface
from microspec.constants import *
# from microspec.replies import *
import microspec.replies as replies

class Devkit(MicroSpecSimpleInterface):
    """Customize MicroSpecSimpleInterface methods."""

    def getBridgeLED(
            self,
            led_num: int = 0 # LED0 is the only Bridge LED
            ):
        _reply = super().getBridgeLED(led_num)
        reply = replies.getBridgeLED(
            status = status_dict.get(_reply.status),
            led_setting = led_dict.get(_reply.led_setting)
            )
        return reply

    def setBridgeLED(
            self,
            led_setting: int,
            led_num: int = 0 # LED0 is the only Bridge LED
            ):
        return super().setBridgeLED(led_num, led_setting)

    def getSensorLED(
            self,
            led_num : int
            ):
        return super().getSensorLED(led_num)
