# -*- coding: utf-8 -*-
"""Send commands to the dev-kit.

For examples using this module, see doctests in
:ref:`test-commands-and-responses`.

TODO:

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
        reply = replies.getBridgeLED_response(
            status = status_dict.get(_reply.status),
            led_setting = led_dict.get(_reply.led_setting)
            )
        return reply

    def setBridgeLED(
            self,
            led_setting: int,
            led_num: int = 0 # LED0 is the only Bridge LED
            ):
        _reply = super().setBridgeLED(led_num, led_setting)
        reply = replies.setBridgeLED_response(
            status = status_dict.get(_reply.status)
            )
        return reply

    def getSensorLED(
            self,
            led_num : int
            ):
        _reply = super().getSensorLED(led_num)
        reply = replies.getSensorLED_response(
                status = status_dict.get(_reply.status),
                led_setting = led_dict.get(_reply.led_setting)
                )
        return reply

    def setSensorLED(
            self,
            led_num : int,
            led_setting : int
            ):
        _reply = super().setSensorLED(led_num, led_setting)
        reply = replies.setSensorLED_response(
                status = status_dict.get(_reply.status)
                )
        return reply
