import pygame
import pygame.image


class Ship:

    def __init__(self, ai_game):
        """
        Initialises the s
        Args:
            ai_game (AlienInvasion): [description]
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start a new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value for the ships's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """
         Draw the ship at the current location
        """

        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Update the ship's position based on the movement flag.
        """
        # Upate the ship's x value no the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
