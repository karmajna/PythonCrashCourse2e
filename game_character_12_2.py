"""

Find a bitmap image of a game character you like or 
convert an image to a bitmap. Make a class that draws
the character at the center of the screen and match 
the background color of the image to the back- ground 
color of the screen, or vice versa.

"""
import sys
import pygame

from settings import Settings
from ship import GalagaShip

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Galaga Invasion")

        self.ship = GalagaShip(self)

        # Set the background color.
        self.bg_color = (0, 0, 30)

    def run_game(self):
        """ Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game. Make sure instance uses constants for pygame.
    AI = AlienInvasion()
    AI.run_game()
    