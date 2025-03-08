import pygame


class Ship:
    def __init__(self,ai_game):
        self.screen =ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.x = 1
        if self.moving_left:
            self.rect.y = -1
    def blitme(self):
        self.screen.blit(self.image,self.rect)
