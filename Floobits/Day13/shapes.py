""" Drawing some shapes with pygame! """

import pygame
from pygame.locals import *
import time

class Rectangle(object):
    """ Represents a rectangle that can be drawn to a pygame window """
    def __init__(self, x_upperleft, y_upperleft, width, height):
        """ Initialize the rectangle with the specified geometry """
        self.x_upperleft = x_upperleft
        self.y_upperleft = y_upperleft
        self.width = width
        self.height = height

    def draw(self, screen):
        """ Render the rectangle to the screen """
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft, self.y_upperleft),
                         (self.x_upperleft + self.width, self.y_upperleft))
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft + self.width, self.y_upperleft),
                         (self.x_upperleft + self.width, self.y_upperleft + self.height))
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft + self.width, self.y_upperleft + self.height),
                         (self.x_upperleft, self.y_upperleft + self.height))
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft, self.y_upperleft + self.height),
                         (self.x_upperleft, self.y_upperleft))


class Square(Rectangle):
    """ Represents a square that can be drawn to a pygame window """
    def __init__(self, x_upperleft, y_upperleft, side_length):
        """ Initializes the square with upper left corner position of
            (x_upperleft, y_upperleft) and side length side_length """
        super(Square, self).__init__(x_upperleft, y_upperleft, side_length, side_length)


if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    running = True

    square = Square(100,100,25)
    rectangle = Rectangle(20,200,100,10)
    while running:
        screen.fill(pygame.Color(255,255,255))
        square.draw(screen)
        rectangle.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()