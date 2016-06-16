def testable(x):
    r"""
    The testable function returns the spuare root of it's argument or 3.0, whichever is larger
    
    >>> testable(7)
    3.0
    
    >>> testable(16)
    4.0
    
    >>> testable(9)
    3.0
    
    >>> testable(10) == 10 ** .5
    TRUE
    """
    if x < 9:
        return 3.0
    return x ** .5
