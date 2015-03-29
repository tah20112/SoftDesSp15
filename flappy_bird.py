""" A Collaboratively-Coded Clone of Flappy Bird """

import pygame
import random
import time

class DrawableSurface():
    """ A class that wraps a pygame.Surface and a pygame.Rect """

    def __init__(self, surface, rect):
        """ Initialize the drawable surface """
        self.surface = surface
        self.rect = rect

    def get_surface(self):
        """ Get the surface """
        return self.surface

    def get_rect(self):
        """ Get the rect """
        return self.rect

class FlappyModel():
    """ Represents the game state of our Flappy bird clone """
    def __init__(self, width, height):
        """ Initialize the flappy model """
        self.width = width
        self.height = height

    def update(self):
        """ Updates the model and its constituent parts """
        pass

class Background():
    def __init__(self, screen_height):
        self.image = pygame.image.load('images/plant_tile.png')
        self.tiles = []
        for i in range(100):
            self.tiles.append(DrawableSurface(self.image, pygame.Rect(0,0,32,32)))
    def draw(self, screen):
        for drawable_surface in self.tiles:
            screen.blit(drawable_surface.get_surface(),
                        drawable_surface.get_rect())

class FlappyUser():
    def __init__(self, x_position, y_position, x_velocity, y_velocity, y_acceleration, life_state):
        self.image = pygame.image.load('images/olin_o.png')
        self.x_position = x_position
        self.y_position = y_position
        self.x_velocity = 6.5
        self.y_velocity = 0
        self.y_acceleration = -9.8
        self.life_state = True

class FlappyView():
    def __init__(self, model, width, height):
        """ Initialize the view for Flappy Bird.  The input model
            is necessary to find the position of relevant objects
            to draw. """
        pygame.init()
        # to retrieve width and height use screen.get_size()
        self.screen = pygame.display.set_mode((width, height))
        # this is used for figuring out where to draw stuff
        self.model = model
        self.background = Background(height)

    def draw(self):
        """ Redraw the full game window """
        self.screen.fill((0,51,102))
        self.background.draw(self.screen)
        pygame.display.update()

class FlappyBird():
    """ The main Flappy Bird class """

    def __init__(self):
        """ Initialize the flappy bird game.  Use FlappyBird.run to
            start the game """
        self.model = FlappyModel(640, 480)
        self.view = FlappyView(self.model, 640, 480)
        # we will code the controller later

    def run(self):
        """ the main runloop... loop until death """
        while True:
            self.view.draw()
            self.model.update()

if __name__ == '__main__':
    flappy = FlappyBird()
    flappy.run()