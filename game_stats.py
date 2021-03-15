
class GameStat:
    """Track statisrics of Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasions in an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during game"""
        self.ships_left = self.settings.ship_limit
