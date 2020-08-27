# -*- coding: utf-8 -*-
from typing import NamedTuple

class ReplyToGetBridgeLED(NamedTuple):
    """Response to command `getBridgeLED`.

    Attributes
    ----------
    status : int

        Serial communication status:
        :data:`~microspec.OK`,
        :data:`~microspec.ERROR`

    led_setting : int

        State of the LED:
        :data:`~microspec.OFF`,
        :data:`~microspec.GREEN`,
        :data:`~microspec.RED`

    See Also
    --------
    microspeclib.datatypes.bridge.BridgeSetBridgeLED
    """

    status: int
    led_setting: int
