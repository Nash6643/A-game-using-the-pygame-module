
import sys
import pygame


class Settings:
    """A class to store game settings."""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)  # Light gray
        self.ship_speed = 5  # Adjust speed as needed


class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings  # Get settings for speed

        # Load the ship image and resize it
        try:
            self.image = pygame.image.load('rocket.bmp')  # Ensure the image exists
            self.image = pygame.transform.scale(self.image, (50, 80))  # Resize
        except pygame.error:
            print("Error: Could not load 'rocket.bmp'. Make sure the file exists.")
            self.image = pygame.Surface((50, 80))  # Create a blank rectangle as a fallback

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # Position the ship at the bottom center

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


class AlienInvasion:
    """Main game class."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)  # Create a ship instance

    def run_game(self):
        """Main game loop."""
        while True:
            self._check_events()
            self.ship.update()  # Update the ship's position
            self.update_screen()

    def _check_events(self):
        """Handle keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def update_screen(self):
        """Update and redraw the screen."""
        self.screen.fill(self.settings.bg_color)  # Fill the screen
        self.ship.blitme()  # Draw the ship
        pygame.display.update()  # Refresh the display


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
