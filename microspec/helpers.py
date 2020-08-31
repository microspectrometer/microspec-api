__all__ = [
    'to_cycles',
    'to_ms'
    ]
def to_cycles(ms : float) -> int:
    u"""Convert exposure time from milliseconds to cycles.

    Parameters
    ----------
    ms
        Exposure time in milliseconds. Valid exposure times are
        from 0.02ms to 1310.0ms. ``ms`` is clamped to these
        values to guarantee the return value is a valid exposure
        time.

    Returns
    -------
    float
        Exposure time in cycles.

    See Also
    --------
    to_ms
    """

    # Do not return cycles < minimum allowed cycles
    if ms < 0.02: ms = 0.02
    # Do not return cycles > maximum allowed cycles
    if ms > 1310: ms = 1310
    return round(ms*1e-3/20e-6)

def to_ms(cycles: int) -> float:
    u"""Convert from cycles to milliseconds.

    Parameters
    ----------
    cycles
        Time in cycles. One cycle is 20µs.

    Returns
    -------
    float
        Time in milliseconds.

    Notes
    -----
    Dev-kit firmware measures exposure time in units of cycles
    and stores exposure time as a 16-bit unsigned integer. The
    smallest exposure time is 1 cycle. The largest exposure time
    is 65500 (1310.0ms).

    See Also
    --------
    to_cycles
    """

    return cycles*20e-3

