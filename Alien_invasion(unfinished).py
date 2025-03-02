import sys
import pygame


class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)


class AlienInvasion():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  # Initialize the ship once

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # Display the ship
            pygame.display.update()


class Ship():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and resize it to fit properly
        self.image = pygame.image.load('rocket.bmp')  # Ensure this file exists
        self.image = pygame.transform.scale(self.image, (50, 80))  # Resize the image (width, height)

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    alien = AlienInvasion()
    alien.run_game()
