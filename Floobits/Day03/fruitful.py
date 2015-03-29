"""Testing fruitful functions"""

def double(x):
    """Return 2*x"""
    return 2*x

def is_even(x):
    """
    Return True if x is even, otherwise return False

    >>> is_even(5)
    False
    >>> is_even(4)
    True
    >>> is_even(3)
    False

    """
    if (x % 2) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

