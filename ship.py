import pygame

class Ship():

    def __init__(self, ai_settings,screen):
        """Initialize the ship and start its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship image and get its rectangle
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position based on the movement flag."""
        #Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


        