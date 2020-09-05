# -*- coding: utf-8 -*-
"""Send commands to the dev-kit.

Example
-------

>>> import microspec
>>> kit = microspec.Devkit()

"""

__all__ = ['Devkit']

from microspeclib.simple import MicroSpecSimpleInterface
from microspec.constants import *
from microspec.helpers import *
import microspec.replies as replies
import warnings

class TimeoutWarning():
    def _issue_timeout_warning(self,
            command_name: str,
            suggestion:str =""
            ):
        warnings.warn(
            f"Command {command_name} timed out. {suggestion}",
            stacklevel=2
            )
    def _is_out_of_time(self, reply):
        """Return True if the command timed out.

        This exists solely for testing purposes.
        It creates a seam where the unit tests monkeypatch a timeout
        condition to test the path that issues the UserWarning when a
        command timeouts.
        """
        return True if reply == None else False
    def handle_hardware_timeout(self,
            reply,
            command_name: str,
            suggestion:str = ""
            ) -> bool:
        """Return True and issue a warning if the command timed out.

        Parameters
        ----------
        reply:
            The return value of the
            :class:`~microspeclib.simple.MicrospecSimpleInterface`
            command, *not* the return value of the commands
            defined in :class:`Devkit`.
        command_name: str
            The :class:`Devkit` method name, e.g., "captureFrame".
        suggestion: str
            A message to the user on how to troubleshoot the
            timeout. If omitted or an empty string, a standard
            suggestion is used.
        """
        is_out_of_time = self._is_out_of_time(reply)
        if is_out_of_time:
            if suggestion == "":
                suggestion=(""
                "Expect this is a rare hardware event. "
                f"Retry {command_name} and increase the timeout "
                "if the command timed out again. "
                "If that does not help, "
                "try a different USB cable or USB port, "
                "or a different host computer."
                )
                self._issue_timeout_warning(command_name, suggestion)
        return is_out_of_time



class Devkit(MicroSpecSimpleInterface, TimeoutWarning):
    """Interface for dev-kit communication.

    Every communication with the dev-kit consists of:

    - a **command** sent to the dev-kit
    - a **response** received from the dev-kit

    Calling a ``Devkit`` method sends the **command**. The method's
    return value is the **response**.

    Example
    -------

    Command ``getBridgeLED`` returns ``getBridgeLED_response``:

    >>> import microspec
    >>> kit = microspec.Devkit()
    >>> kit.getBridgeLED()
    getBridgeLED_response(status='OK', led_setting='GREEN')

    Assign the **response** to variable ``reply``:

    >>> reply = kit.getBridgeLED()

    Access each part of the response as attributes ``status`` and
    ``led_setting``:

    >>> reply.status
    'OK'
    >>> reply.led_setting
    'GREEN'

    """

    def __init__(self):
        """Add attributes to Devkit.
        
        Attributes
        ----------
        exposure_time_cycles: int
            Exposure time in cycles. Updated every time getExposure()
            and setExposure() are called.
        exposure_time_ms: ms
            Exposure time in ms. Updated every time getExposure()
            and setExposure() are called.
        """
        super().__init__()
        # Sync exposure_time attrs with dev-kit state:
        exposure_time = self.getExposure()
        self.exposure_time_cycles = exposure_time.cycles
        self.exposure_time_ms     = exposure_time.ms
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
        >>> kit.setSensorConfig() # restore default config
        setSensorConfig_response(status='OK')

        Read the spectrometer's pixel configuration:

        >>> kit.getSensorConfig()
        getSensorConfig_response(status='OK', binning='BINNING_ON',
                                 gain='GAIN1X', row_bitmap='ALL_ROWS')
        """
        _reply = super().getSensorConfig()
        is_out_of_time = self.handle_hardware_timeout(
                            _reply,
                            command_name="getSensorConfig"
                            )
        reply = replies.getSensorConfig_response(
                status     = 'TIMEOUT',
                binning    = '',
                gain       = '',
                row_bitmap = ''
            ) if is_out_of_time else replies.getSensorConfig_response(
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

        Configure the spectrometer with pixel binning off:

        >>> kit.setSensorConfig(binning=usp.BINNING_OFF)
        setSensorConfig_response(status='OK')
        >>> kit.getSensorConfig()
        getSensorConfig_response(status='OK', binning='BINNING_OFF',
                                 gain='GAIN1X', row_bitmap='ALL_ROWS')

        Configure the spectrometer with the default pixel configuration:

        >>> kit.setSensorConfig()
        setSensorConfig_response(status='OK')
        >>> kit.getSensorConfig()
        getSensorConfig_response(status='OK', binning='BINNING_ON',
                                 gain='GAIN1X', row_bitmap='ALL_ROWS')

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

        ``setExposure`` accepts time in units of ms:

        >>> kit.setExposure(ms=5.0)
        setExposure_response(status='OK')

        ``setExposure`` accepts time in units of cycles:

        >>> kit.setExposure(cycles=250)
        setExposure_response(status='OK')

        ``setExposure`` requires an exposure time input

        >>> kit.setExposure()
        Traceback (most recent call last):
            ...
        TypeError: setExposure() missing 1 required argument: 'ms' or 'cycles'

        Calling ``setExposure`` with both ``ms`` and ``cycles`` is not
        allowed:

        >>> kit.setExposure(ms=5.0, cycles=250)
        Traceback (most recent call last):
            ...
        TypeError: setExposure() got an unexpected keyword 'cycles'
        (requires 'ms' or 'cycles' but received both)

        ``setExposure`` clamps time to the allowed range:

        >>> # Test clamping exposure time to MAX
        >>> usp.MAX_CYCLES
        65500
        >>> # Setup: set exposure time one cycle higher than the maximum
        >>> kit.setExposure(cycles=usp.MAX_CYCLES+1)
        setExposure_response(status='OK')
        >>> # Test: expect the exposure time is 65500, not 65501
        >>> kit.getExposure()
        getExposure_response(status='OK', ms=1310.0, cycles=65500)

        >>> # Test clamping exposure time to MIN
        >>> usp.MIN_CYCLES
        1
        >>> # Setup: set exposure time one cycle lower than the minimum
        >>> kit.setExposure(cycles=usp.MIN_CYCLES-1)
        setExposure_response(status='OK')
        >>> # Test: expect the exposure time is 1, not 0
        >>> kit.getExposure()
        getExposure_response(status='OK', ms=0.02, cycles=1)

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
        is_out_of_time = self.handle_hardware_timeout(
                _reply,
                command_name="setExposure"
                )
        reply = replies.setExposure_response(
                'TIMEOUT'
            ) if is_out_of_time else replies.setExposure_response(
                status_dict.get(_reply.status)
                )
        # Update Devkit exposure time attrs
        if reply.status == 'OK':
            self.exposure_time_cycles = time
            self.exposure_time_ms = to_ms(time)
        return reply

    def getExposure(self):
        """One-liner

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()

        ``getExposure`` reports exposure time in both units:

        >>> # Setup: set exposure time to 5ms
        >>> kit.setExposure(ms=5)
        setExposure_response(status='OK')
        >>> # Test: expect 5.0ms and 250 cycles
        >>> kit.getExposure()
        getExposure_response(status='OK', ms=5.0, cycles=250)
        """
        _reply = super().getExposure()
        is_out_of_time = self.handle_hardware_timeout(
                            _reply,
                            command_name="getExposure"
                            )
        reply = replies.getExposure_response(
                status = 'TIMEOUT',
                ms     = 0,
                cycles = 0
            ) if is_out_of_time else replies.getExposure_response(
                status = status_dict.get(_reply.status),
                ms     = to_ms(_reply.cycles),
                cycles = _reply.cycles
                )
        # Update Devkit exposure time attrs
        if reply.status == 'OK':
            self.exposure_time_cycles = reply.cycles
            self.exposure_time_ms = reply.ms
        return reply

    def captureFrame(self):
        """One-liner

        Return
        ------
        status : str
            Serial communication status, either 'OK', 'ERROR', or
            'TIMEOUT'.
        num_pixels : int
            The number of pixels in the frame (either 392 or 784
            depending on pixel binning).
        pixels : list
            The 16-bit ADC counts at each pixel, starting with pixel 1
            and ending with pixel 392 or 784 (depending on pixel
            binning).
        frame : dict
            Python dictionary where the key is the pixel number and
            the value is the 16-bit ADC counts at that pixel.

        Notes
        -----
        If there is a timeout, :func:`captureFrame` returns
        ``status='TIMEOUT'``, and fills the reply with obviously
        bad data:

            - ``num_pixels=0``
            - ``pixels=[]``
            - ``frame={}``

        In a data logging application, it might improve data
        quality to check for ``status='TIMEOUT'`` to note a
        missing frame and skip logging this bad dataset.

        Similarly, in a GUI plotting application, it might
        improve user experience (and simplify the plotting code)
        to check for ``status='TIMEOUT'`` and replot the
        *previous* (good) dataset rather than plot the bad
        dataset.

        Applications are protected from accidentally setting a
        :attr:`Devkit.timeout` that is shorter than the exposure
        time (because this *guarantees* that :func:`captureFrame`
        timeouts before a response is received). If the timeout
        is less than the exposure time, :func:`captureFrame` uses
        a :attr:`Devkit.timeout` that is one second longer than
        the exposure time.

        Even with :attr:`Devkit.timeout` one second longer than
        the exposure time, if an application loops
        :func:`captureFrame` for a long time (such as the data
        logging and plotting GUI examples above), there will
        likely be a timeout from the occasional hardware hiccup.

        In this case, :func:`captureFrame` issues a
        ``UserWarning`` describing which command caused the
        timeout. This is only a warning because the timeout is
        hardware-dependent. It does **not** indicate a bug in the
        application code.

        The timeout ``UserWarning`` prints to the console and can
        safely be ignored. If the timeouts are a frequent event,
        it indicates a problem with the host computer, its USB
        port, or the USB cable.

        Examples
        --------

        *Setup*:

        >>> import microspec as usp
        >>> kit = usp.Devkit()

        Capture a frame:

        >>> reply = kit.captureFrame()

        The frame is stored as a Python ``list`` of numbers. Each
        number is the signal strength at that pixel in units of
        *counts*.

        The list starts with pixel 1. With pixel binning on, the
        frame has 392 pixels, so the list ends with pixel 392:

        >>> print(reply)
        captureFrame_response(status='OK', num_pixels=392,
                              pixels=[...], frame={...})

        The list ``pixels`` is hard to read on its own (index 0
        is pixel 1, index 1 is pixel 2, etc.):

        >>> print(reply.pixels)
        [..., ..., ...]

        It is usually more convenient for applications to use the
        dict ``frame`` because it tags each pixel with its pixel
        number:

        >>> print(reply.frame)
        {1: ..., 2: ..., ..., 391: ..., 392: ...}

        This is still hard to read in the REPL. Put each pixel on
        its own line:

        >>> import pprint
        >>> pprint.pprint(reply.frame)
        {1: ...,
         2: ...,
         ...
         391: ...,
         392: ...}

        Alternatively, turn the ``(pixel number, pixel value)``
        pairs into a list of ``tuples``:

        >>> frame = list(zip(range(1,reply.num_pixels+1), reply.pixels))
        >>> pprint.pprint(frame)
        [(1, ...),
         (2, ...),
         ...,
         (391, ...),
         (392,...)]

        """
        # -----------------------------------
        # | Prevent timeout < exposure_time |
        # -----------------------------------
        # Save the user's timeout to restore later.
        _timeout = self.timeout
        # Adjust timeout if necessary.
        if self.timeout*1000 < self.exposure_time_ms:
            # Set timeout one second longer than exposure time.
            self.timeout = self.exposure_time_ms/1000 + 1
        # Now it is safe to capture a frame.
        _reply = super().captureFrame()
        # Restore the user's timeout.
        self.timeout = _timeout

        is_out_of_time = self.handle_hardware_timeout(
                _reply,
                command_name="captureFrame",
                )

        # Create the reply. Use bad data if there was a timeout.
        reply = replies.captureFrame_response(
                    status = 'TIMEOUT',
                    num_pixels = 0,
                    pixels = [],
                    frame = {}
                ) if is_out_of_time else replies.captureFrame_response(
                    status = status_dict.get(_reply.status),
                    num_pixels = _reply.num_pixels,
                    pixels = _reply.pixels,
                    # Format data into a "frame" dict where:
                    # - pixel number is the key
                    # - pixel ADC counts is the value
                    frame = dict(zip(
                        range(1,_reply.num_pixels+1), # <- pixel number 1:N
                        _reply.pixels) # <---------------- counts
                        )
                )
        return reply

    # def autoExposure(self):
    #     _reply = super().autoExposure()
    #     reply = replies.captureFrame_response(
    #             status = 'TIMEOUT',
    #             ) if is_out_of_time else replies.captureFrame_response(
    #                     status = status_dict.get(_reply.status),
    #                     )
    #     return reply
