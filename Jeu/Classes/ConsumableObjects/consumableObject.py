import pygame

class Consumable(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_image):
        super().__init__()
        self.image = pygame.image.load(sprite_image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.consumed = False

    def consume(self, player):
        pass