# -*- coding: utf-8 -*-
from collections import namedtuple

ReplyToGetBridgeLED = namedtuple(
        'ReplyToGetBridgeLED',
        ['status', 'led_setting']
        )
ReplyToGetBridgeLED.__doc__="""\
Response to command `getBridgeLED`.

Attributes
----------
led_setting : int

    State of the LED:
    :data:`~microspec.OFF`,
    :data:`~microspec.GREEN`,
    :data:`~microspec.RED`

See Also
--------
microspeclib.datatypes.bridge.BridgeSetBridgeLED
"""


