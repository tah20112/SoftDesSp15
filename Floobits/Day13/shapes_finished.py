""" Drawing some shapes with pygame! """

import pygame
from pygame.locals import *
import time

class Polygon(object):
    """ A Class to represent an arbitrary Polygon that can be drawn to a window """
    def __init__(self, vertices):
        """ Creates a polygon that can be drawn to a pygame window

            vertices: a list of two-element tuples with the first element of the
                      tuple specifying the x-coordinate of a vertex and the
                      second element of the tuple representing the y-coordinate
                      of a vertex.  The vertices should be in the order that they
                      should be drawn.
        """
        self.vertices = vertices

    def draw(self, screen):
        """ Draws the Polygon object to the specified screen """
        for i,v in enumerate(self.vertices):
            next_v = self.vertices[(i + 1)%len(self.vertices)]
            # draw an edge of the polygon
            pygame.draw.line(screen, pygame.Color(0,0,0), v, next_v)

class Rectangle(Polygon):
    """ A Class to represent a rectangle that can be drawn to a window """
    def __init__(self, x_ul, y_ul, width, height):
        """ Create a rectangle that can be drawn to a pygame window

            x_ul: the x-coordinate of the upper left corner of the rectangle
            y_ul: the y-coordinate of hte upper left corner of the rectangle
            width: the width of the rectangle
            height: the height of the rectangle
        """
        super(Rectangle, self).__init__([(x_ul,y_ul),
                                         (x_ul+width, y_ul),
                                         (x_ul+width, y_ul+height),
                                         (x_ul, y_ul+height)])

class Square(Rectangle):
    """ A Class to represent a square that can be drawn to a window """

    def __init__(self,x_ul,y_ul,side_length):
        """ Create a square that can be drawn to a pygame window.

            x_ul: the x-coordinate of the upper left corner of the square
            y_ul: the y-coordinate of the upper left corner of the square
            side_length: the length of the square's side
        """
        super(Square, self).__init__(x_ul, y_ul, side_length, side_length)

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    square = Square(400,100,20)
    rectangle = Rectangle(100,100,200,20)
    triangle = Polygon([(200,200),(300,200),(250,250)])
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        square.draw(screen)
        rectangle.draw(screen)
        triangle.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()