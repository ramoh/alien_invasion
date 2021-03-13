import pygame as pygame


class Ship:

    def __init__(self, ai_game):
        """
        Initialises the s
        Args:
            ai_game (AlienInvasion): [description]
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start a new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
         Draw the ship at the current location
        """

        self.screen.blit(self.image, self.rect)
