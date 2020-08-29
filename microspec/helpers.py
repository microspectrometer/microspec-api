__all__ = [
    'to_cycles',
    'to_ms'
    ]
def to_cycles(ms):
    u"""Convert exposure time from milliseconds to cycles.

    Notes
    -----
    Dev-kit firmware measures exposure time in units of cycles.
    One cycle is 0.02ms.

    The smallest exposure time is 1 cycle (0.02ms).

    Dev-kit firmware stores cycles as 16-bit unsigned integers.
    The largest exposure time is 65535 (1310.7ms).

    See Also
    --------
    to_ms
    """

    # Do not return cycles < minimum allowed cycles
    if ms < 0.02: ms = 0.02
    # Do not return cycles > maximum allowed cycles
    if ms > 1310: ms = 1310
    return round(ms*1e-3/20e-6)

def to_ms(cycles):
    u"""Convert exposure time from cycles to milliseconds.

    See Also
    --------
    to_cycles
    """

    return cycles*20e-3

