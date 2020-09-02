# -*- coding: utf-8 -*-
"""Send commands to the dev-kit.

Class :class:`~microspec.commands.Devkit` **is the interface**
for applications to communicate with the Chromation dev-kit.

Example
-------

>>> import microspec
>>> kit = microspec.Devkit()

:class:`~microspec.commands.Devkit` inherits from
:class:`microspeclib.simple.MicroSpecSimpleInterface` to
customize its auto-generated methods. The customizations simplify
application programming:

- add default parameter values
- format responses to use strings instead of numbers
- add a timeout handler via a mix-in
- add custom docstrings with examples

Notes
-----

The dev-kit commands are defined in the ``protocol.command``
**object** of the :ref:`JSON API config file <dev-kit-API-JSON>`.

- the **keys** are the **byte values** sent over serial to
  represent the command
- the **values** are **objects** that:

  - **name** the command
  - describe the command **parameters**
  - define the **byte format** of the complete message

- **command names** are identical to the **method names** in
  ``Devkit`` (except that the first letter is capitalized)

"""

__all__ = ['Devkit']

from microspeclib.simple import MicroSpecSimpleInterface
from microspec.constants import *
from microspec.helpers import *
import microspec.replies as replies

class Devkit(MicroSpecSimpleInterface):
    """Interface for dev-kit communication.

    Every communication with the dev-kit consists of:

    - a **command** sent to the dev-kit
    - a **response** received from the dev-kit

    Calling a ``Devkit`` method sends the **command**. The method's
    return value is the **response**.

    Examples
    --------

    >>> import microspec
    >>> kit = microspec.Devkit()
    >>> kit.getBridgeLED()
    getBridgeLED_response(status='OK', led_setting='GREEN')

    Assign the **response** to variable ``reply`` and access each
    part of the response as an attribute:

    >>> reply = kit.getBridgeLED()
    >>> reply.status
    'OK'
    >>> reply.led_setting
    'GREEN'

    """

    def getBridgeLED(
            self,
            led_num: int = 0 # LED0 is the only Bridge LED
            ):
        """Read the state of the indicator LED on the Bridge PCB.

        Examples
        --------

        *Setup* -- set the LED to a known state:

        >>> import microspec as usp
        >>> kit = usp.Devkit()
        >>> kit.setBridgeLED(led_num=0, led_setting=usp.GREEN)
        setBridgeLED_response(status='OK')

        Call ``getBridgeLED``:

        >>> kit.getBridgeLED()
        getBridgeLED_response(status='OK', led_setting='GREEN')

        See Also
        --------
        setBridgeLED
        """
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
        """Set the LED on the Bridge PCB to OFF, GREEN, or RED.

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()

        Call ``setBridgeLED`` with optional parameter ``led_num``:

        >>> kit.setBridgeLED(led_num=0, led_setting=usp.GREEN)
        setBridgeLED_response(status='OK')

        Call ``setBridgeLED`` without optional parameter ``led_num``:

        >>> kit.setBridgeLED(led_setting=usp.GREEN)
        setBridgeLED_response(status='OK')

        Call ``setBridgeLED`` with an invalid parameter value:

        >>> kit.setBridgeLED(led_num=1, led_setting=usp.GREEN)
        setBridgeLED_response(status='ERROR')

        See Also
        --------
        getBridgeLED
        """

        _reply = super().setBridgeLED(led_num, led_setting)
        reply = replies.setBridgeLED_response(
            status = status_dict.get(_reply.status)
            )
        return reply

    def getSensorLED(
            self,
            led_num : int
            ):
        """Read the state of an indicator LED on the Sensor PCB.

        There are two indicator LEDS: led0 and led1.

        .. note::

            Application code should never call this method:

            - led0 is OFF while commands execute, so the state returned
              by :func:`microspec.commands.Devkit.getSensorLED` is
              always OFF
            - led1 indicates the success of auto-expose, but this is
              directly available from the ``success`` attribute of the
              response to :func:`microspec.commands.Devkit.autoExposure`

        Examples
        --------

        *Setup* -- set the LEDs to a known state:

        >>> import microspec as usp
        >>> kit = usp.Devkit()
        >>> kit.setSensorLED(usp.GREEN, led_num=0)
        setSensorLED_response(status='OK')
        >>> kit.setSensorLED(usp.GREEN, led_num=1)
        setSensorLED_response(status='OK')

        Call ``getSensorLED``:

        >>> kit.getSensorLED(0) # Expect OFF
        getSensorLED_response(status='OK', led_setting='OFF')
        >>> kit.getSensorLED(1) # Expect GREEN
        getSensorLED_response(status='OK', led_setting='GREEN')

        See Also
        --------
        setSensorLED
        """

        _reply = super().getSensorLED(led_num)
        reply = replies.getSensorLED_response(
                status = status_dict.get(_reply.status),
                led_setting = led_dict.get(_reply.led_setting)
                )
        return reply

    def setSensorLED(
            self,
            led_setting : int,
            led_num : int
            ):
        """Set the LEDs on the Sensor PCB to OFF, GREEN, or RED.

        There are two indicator LEDS:

        - led0

            - usually appears GREEN
            - is OFF while a command is being executed
            - only turns RED if there is a serious error in serial
              communication (this should never happen)

        - led1

            - usually appears GREEN
            - turns RED during auto-expose
            - stays RED if auto-expose fails
            - turns GREEN if auto-expose succeeds

        .. note::

            Application code should never call this method. The LEDs are
            controlled by firmware to indicate status. Controlling the
            LEDs from the application undermines the LEDs purpose as
            status indicators.

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()

        Turn led0 and led1 OFF:

        >>> kit.setSensorLED(usp.OFF, 0)
        setSensorLED_response(status='OK')
        >>> kit.setSensorLED(usp.OFF, 1)
        setSensorLED_response(status='OK')

        Turn led0 and led1 RED:

        >>> kit.setSensorLED(usp.RED, 0)
        setSensorLED_response(status='OK')
        >>> kit.setSensorLED(usp.RED, 1)
        setSensorLED_response(status='OK')

        Turn led0 and led1 GREEN:

        >>> kit.setSensorLED(usp.GREEN, 0)
        setSensorLED_response(status='OK')
        >>> kit.setSensorLED(usp.GREEN, 1)
        setSensorLED_response(status='OK')

        """
        _reply = super().setSensorLED(led_num, led_setting)
        reply = replies.setSensorLED_response(
                status = status_dict.get(_reply.status)
                )
        return reply

    def getSensorConfig(self):
        """One-liner

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()


        """
        _reply = super().getSensorConfig()
        reply = replies.getSensorConfig_response(
                status     = status_dict.get(_reply.status),
                binning    = binning_dict.get(_reply.binning),
                gain       = gain_dict.get(_reply.gain),
                row_bitmap = (
                    row_dict.get(_reply.row_bitmap)
                    if _reply.row_bitmap == ALL_ROWS
                    else _reply.row_bitmap
                    )
                )
        return reply

    def setSensorConfig( # TODO: add default values
            self,
            binning : int = BINNING_ON,
            gain : int = GAIN1X,
            row_bitmap : int = ALL_ROWS
            ):
        """One-liner

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()


        """
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
        """One-liner

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()


        """
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
        """One-liner

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()


        """
        _reply = super().getExposure()
        reply = replies.getExposure_response(
                status = status_dict.get(_reply.status),
                ms     = to_ms(_reply.cycles),
                cycles = _reply.cycles
                )
        return reply

    def captureFrame(self):
        return super().captureFrame()
