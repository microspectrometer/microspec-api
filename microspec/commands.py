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
from microspec.helpers import *
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

    def getSensorConfig(self):
        _reply = super().getSensorConfig()
        reply = replies.getSensorConfig_response(
                status     = status_dict.get(_reply.status),
                binning    = binning_dict.get(_reply.binning),
                gain       = gain_dict.get(_reply.gain),
                row_bitmap = row_dict.get(_reply.row_bitmap)
                )
        return reply

    def setSensorConfig(
            self,
            binning : int,
            gain : int,
            row_bitmap : int
            ):
        _reply = super().setSensorConfig(binning, gain, row_bitmap)
        reply = replies.setSensorConfig_response(
                status_dict.get(_reply.status)
                )
        return reply

    def setExposure(
            self,
            ms : float = None,  # specify time in milliseconds
            cycles : int = None # OR time in cycles
            ):
        # Exposure time units are either ms or cycles
        if ms == None and cycles == None:
            raise TypeError(
                "setExposure() missing 1 required argument: "
                "'ms' or 'cycles'"
                )
        if ms != None and cycles != None:
            raise TypeError(
                "setExposure() got an unexpected keyword "
                "'cycles' (requires 'ms' or 'cycles' but "
                "received both)"
                )
        if ms == None: time = cycles
        else: time = to_cycles(ms)

        # Clamp exposure time to the min/max allowed by firmware
        if time < MIN_CYCLES: time = MIN_CYCLES
        if time > MAX_CYCLES: time = MAX_CYCLES

        _reply = super().setExposure(time)
        reply = replies.setExposure_response(
                status_dict.get(_reply.status)
                )
        return reply

    def getExposure(self):
        _reply = super().getExposure()
        reply = replies.getExposure_response(
                status = status_dict.get(_reply.status),
                ms     = to_ms(_reply.cycles),
                cycles = _reply.cycles
                )
        return reply

    def captureFrame(self):
        return super().captureFrame()
