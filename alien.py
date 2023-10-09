import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent each individual alien"""

    def __init__(self, ai_game):
        """initialize alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        #Start new aliens near top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizontal position
        self.x = float(self.rect.x)

