"""Manipulating strings"""

def hello(name):
    """Return a personalized greeting
    >>> hello("Ben")
    Hello, Ben
    """
    return "Hello, " + name


# String methods
#   https://docs.python.org/2/library/stdtypes.html#string-methods

def shout(message):
    """
    Return a shouted version of message,
    useful for arguing on the Internet

    >>> shout("hello")
    HELLO!
    >>> shout("I don't think so")
    I DON'T THINK SO!
    """
    pass


def print_first_word(text):
    """
    Print only the first word of given text

    >>> print_first_word("Hello world")
    Hello
    """
    
    index = 0
    while index < len(text):
        letter = text[index]
        if letter == " ":
            break
        print letter,
        index = index + 1
    print



def wc(text):
    """Print the number of letters and the
    number of words in text"""
    pass
    

