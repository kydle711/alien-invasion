import pygame.image


class Ship:
    def __init__(self, ai_game):
        """Initialize ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect()

        #start each new ship at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update ships position based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)