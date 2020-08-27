# -*- coding: utf-8 -*-
"""
Format command responses for use in applications.

Notes
-----
Command responses are auto-generated classes defined in
``microspeclib``. The response's ``__str__()`` method shows the
attributes relevant to applications. But the response datatypes
are still too low-level for direct use in applications:

- the attribute values display as integer values
- the command response includes serial communication attributes
  that should not be accessed by the application

Module :mod:`~microspec.replies` defines high-level versions of
each command response. This creates a seam to:

- hide the serial communication attributes from the application
- replace integer values with strings which:

    - are human-readable
    - match the names of the constants defined in
      :mod:`~microspec.constants`

- add a ``__repr__`` to eliminate the need to wrap responses in a
  ``print()``

    - the ``__repr__`` comes for free with namedtuples
      (it's the ``collections.namedtuple.__repr__()``)

- add custom docstrings for each response
"""
__all__ = ['GetBridgeLED']
"""For developers:

Docstring formatting
--------------------
Module :mod:`~microspec.replies` uses substitution to create a
single source of truth for common docstring information.

Docstring substitution
^^^^^^^^^^^^^^^^^^^^^^
The docstrings in module :mod:`~microspec.replies` use dictionary
``_common`` for reusable docstring snippets.

Here is a simplified example to demonstrate docstring
substitution:

>>> _common = {"status": "STATUS", "notes": "NOTES"}
>>> replace_me = '''Docstring with {status} and {notes}.'''
>>> replace_me.format(**_common)
'Docstring with STATUS and NOTES.'

Docstring newlines
^^^^^^^^^^^^^^^^^^
Trailing ``\`` at the end of a line eliminates the newline
introduced by the multiline string:

>>> one_line = '''This is \
... one line'''
>>> print(one_line)
This is one line

Otherwise the multiline string includes all newlines:

>>> two_lines = '''This is
... two lines'''
>>> print(two_lines)
This is
two lines

Newlines are included even when they are the only character:

>>> three_lines = '''This is
... three lines
... '''
>>> print(three_lines)
This is
three lines
"""

from collections import namedtuple

# ----------------------
# | Docstring Snippets |
# ----------------------

_status = """\
status : str

    Serial communication status:

        'OK': :data:`~microspec.OK`

        'ERROR': :data:`~microspec.ERROR`

    If ``status`` is ``'ERROR'`` the other attributes are not
    valid.
"""

_led_setting = """\
led_setting : str

    State of the LED:

        'OFF': :data:`~microspec.OFF`

        'GREEN': :data:`~microspec.GREEN`

        'RED': :data:`~microspec.RED`
"""

_created_from = """\
Instances of this command response are created from the
attributes displayed by the ``__str__()`` method of the
lower-level command response:\
"""

_has_no_serial_attrs = """\
This response does not include the serial communication
attributes of the lower-level response. This is to prevent
applications from directly referencing the serial
communication data.
"""

_replaces_int_with_str = """\
In addition, this response replaces attribute integer values
with strings (e.g., 'OK' replaces 0). This makes the response
easier to read. The strings match the names of the constants
defined by `microspec`.
"""

_common = {
    "status"                : _status,
    "led_setting"           : _led_setting,
    "created_from"          : _created_from,
    "has_no_serial_attrs"   : _has_no_serial_attrs,
    "replaces_int_with_str" : _replaces_int_with_str,
    }

GetBridgeLED = namedtuple(
        'GetBridgeLED_reply',
        ['status', 'led_setting']
        )
GetBridgeLED.__doc__ = """
Response to command `getBridgeLED`.

Attributes
----------
{status}
{led_setting}

Notes
-----
{created_from}
:data:`~microspeclib.datatypes.bridge.BridgeGetBridgeLED`.

{has_no_serial_attrs}
{replaces_int_with_str}

See Also
--------
microspec.getBridgeLED
""".format(**_common)

