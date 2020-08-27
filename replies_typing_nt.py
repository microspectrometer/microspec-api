# -*- coding: utf-8 -*-
"""
TODO: describe this module

A simple example to explain the docstring substitution
>>> _common = {"status": "STATUS", "notes": "NOTES"}
>>> replace_me = '''Docstring with {status} and {notes}.'''
>>> replace_me.format(**_common)
'Docstring with STATUS and NOTES.'
"""

from typing import NamedTuple

_status_docstring = "STATUS"
_status2_docstring = """
status : int

    Serial communication status:
    :data:`~microspec.OK`,
    :data:`~microspec.ERROR`
"""

_notes_docstring = """bob
"""

_common = {
    "status" : _status_docstring
    }

class ReplyToGetBridgeLED(NamedTuple):

    status: int
    led_setting: int

ReplyToGetBridgeLED.__doc__ = """
Response to command `getBridgeLED`.

Attributes
----------
{status}

led_setting : int

    State of the LED:
    :data:`~microspec.OFF`,
    :data:`~microspec.GREEN`,
    :data:`~microspec.RED`

Notes
-----
Instances of this command response are created from the
attributes displayed by the __str__() method of the
lower-level command response:
:data:`~microspeclib.datatypes.bridge.BridgeGetBridgeLED`.

This response does not include the serial communication
attributes of the lower-level response. This is to prevent
applications from directly referencing the serial
communication data.

In addition, this response replaces attribute integer values
with strings (e.g., 'OK' replaces 0). This makes the response
easier to read. The strings match the names of the constants
defined by `microspec`.

See Also
--------
microspec.getBridgeLED
""".format(**_common)


