"""Dealing with rectangles"""

class Point():
    """Point with x and y position"""
    pass

my_point = Point()
my_point.x = 4
my_point.y = 5

class Rectangle():
    """Rectangle defined by lower left and upper right point"""
    pass

# TODO: 
# print_point
# print_rectangle
# Implement find_center(a_rectangle) -> returns Point

def find_center(my_rect):
    """
    Return the Point at the center of my_rect

    Note: Your doctest may be different depending on your 
    implementation of Rectangle
    >>> p1 = Point()
    >>> p1.x = 0
    >>> p1.y = 0
    >>> p2 = Point()
    >>> p2.x = 6
    >>> p2.y = 4
    >>> rect = Rectangle()
    >>> rect.lower_left = p1
    >>> rect.upper_right = p2
    >>> print find_center(rect)
    (3.0, 2.0)
    """
    pass

## Challenge problem:
def bounding_box(rects):
    """
    Given a list of Rectangles, return a Rectangle
    that contains all of them
    """
    pass

