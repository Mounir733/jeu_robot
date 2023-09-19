import pygame
from Classes.InteractiveObject.interactiveObject import InteractiveObject

class OreVein(InteractiveObject):
    def __init__(self, x, y, sprite_image, ore_name, collecting_timer):
        super().__init__(x, y, sprite_image)
        self.ore_name = ore_name
        self.collecting_timer = collecting_timer * 60
        self.collectable = True

    def interact(self, player):
        if self.collecting_timer > 0 and self.collectable:
            self.collecting_timer -= 1
        elif self.collecting_timer == 0:
            print("Minerai récupéré!")
            self.collectable = False
            self.collecting_timer -= 1
        
