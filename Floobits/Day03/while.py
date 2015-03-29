"""While loops"""

def sum_of_integers(n):
    """
    Return sum of all integers up to n

    >>> sum_of_integers(4)
    10

    """

    i = 0
    result = 0
    while i <= n:
        result = result + i
        i = i + 1
    return result

print sum_of_integers(4)
