import pygame

class UpsideDown(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_image):
        super().__init__(x, y, sprite_image)


    def consume(self, player):
        player.gravity = -0.04
