import sys
import pygame
import pygame.display as dis


class AlienInvasion:
    """Overall class to manage game assets and behevaiour."""

    def __init__(self):
        """Initialise the game, and create game resource"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion - by rajesh ")

    def run_game(self):
        # Run the event loop
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                # When Game's close button is called shut down the game
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
