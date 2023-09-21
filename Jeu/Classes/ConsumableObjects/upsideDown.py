import pygame
from Classes.ConsumableObjects.consumableObject import Consumable

class UpsideDown(Consumable):
    def __init__(self, x, y, sprite_image):
        super().__init__(x, y, sprite_image)
        self.effect_active = False
        self.time_effect = 360

    def consume(self, player):
        if self.consumed and self.time_effect > 0:
            self.time_effect -= 1
            player.gravity = -0.04
        else:
            player.gravity = 0.04
            

        if self.rect.colliderect(player.rect):
            self.consumed = True
            self.effect_active = True
            return True
        else: 
            return False
        
        