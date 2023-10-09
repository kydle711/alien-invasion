import pygame.image

class Settings:

    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (40, 20, 40)

        #Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 18
        self.bullet_color = (180, 240, 180)
        self.bullets_allowed = 10