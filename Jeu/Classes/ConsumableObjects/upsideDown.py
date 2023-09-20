import pygame
from Classes.ConsumableObjects.consumableObject import Consumable

class UpsideDown(Consumable):
    def __init__(self, x, y, sprite_image):
        super().__init__(x, y, sprite_image)


    def consume(self, player):
        if self.rect.colliderect(player.rect):
            self.consumed = True
            return True
        else: 
            return False