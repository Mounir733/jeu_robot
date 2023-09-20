import pygame
import sys

class Camera:

    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.SCREEN_WIDTH = 1024
        self.SCREEN_HEIGHT = 768

    def apply(self, entity):
        return entity.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Limitation pour éviter que la caméra ne sorte des limites du monde
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.SCREEN_WIDTH), x)
        y = max(-(self.height - self.SCREEN_HEIGHT), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
