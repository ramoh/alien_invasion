import sys
import pygame
import pygame.display
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behevaiour."""

    def __init__(self):
        """Initialise the game, and create game resource"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        """
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion - by rajesh ")
        """
        self.ship = Ship(self)

    def run_game(self):
        """
        Start the main loop of the game.
        """
        # Run the event loop
        while True:
            self._check_events()
            self.ship.update()

            self._update_screen()

    def _check_events(self):
        """
        Respond to keypresses and mouse events.
        """
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            # When Game's close button is called shut down the game
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key press"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """
        Update images on the screen, and flip to new screen
        """

        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
