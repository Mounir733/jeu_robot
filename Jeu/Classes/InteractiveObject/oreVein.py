import pygame
from interactive_object import InteractiveObject

class OreVein(InteractiveObject):
    def __init__(self, x, y, width, height, color, ore_type):
        super().__init__(x, y, width, height, color)
        self.ore_type = ore_type

    def interact(self):
        # Comportement spécifique pour l'interaction avec une veine de minerai
        print(f"Vous avez extrait du minerai de type {self.ore_type} de la veine.")
