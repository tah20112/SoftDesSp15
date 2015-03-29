""" Recursion examples """

def factorial(n):
    """
    Returns n!

    >>> factorial(1)
    1
    >>> factorial(5)
    120
    """
    if n == 1:
        return 1
    else:
        previous = factorial(n-1)
        return n*previous

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result


def fib(n):
    """
    Return Fibonacci(n)

    n must be a positive integer
    """
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



# Run doctests if called from command line
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)