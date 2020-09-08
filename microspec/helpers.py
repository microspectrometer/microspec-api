__all__ = [
    'to_cycles',
    'to_ms'
    ]
def to_cycles(ms : float) -> int:
    u"""Convert exposure time from milliseconds to cycles.

    Parameters
    ----------
    ms
        Exposure time in milliseconds.

    Returns
    -------
    int
        Exposure time in cycles.

    See Also
    --------
    to_ms
    """

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

