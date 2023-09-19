import pygame
from Classes.InteractiveObject.interactiveObject import InteractiveObject

class MagneticObject(InteractiveObject):
    def __init__(self, x, y, sprite_image, magnetic_type, field_range, force, field_directions=None):
        super().__init__(x, y, sprite_image)
        self.magnetic_type = magnetic_type  # Type d'aimant (1 pour attractif, -1 pour répulsif)
        self.field_range = field_range  # Portée d'attraction
        self.force = force  # Force de champ magnétique
        self.field_directions = field_directions or []  # Liste des directions du champ de force

    def interact(self, player):
        dx = self.rect.centerx - player.rect.centerx
        dy = self.rect.centery - player.rect.centery

        force_x = 0
        force_y = 0

        distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)  # Évite la division par zéro

        if distance < self.field_range:
            if "left" in self.field_directions and dx > 0:
                force_x -= self.magnetic_type * self.force
            if "right" in self.field_directions and dx < 0:
                force_x += self.magnetic_type * self.force
            if "up" in self.field_directions and dy > 0:
                force_y -= self.magnetic_type * self.force
            if "down" in self.field_directions and dy < 0:
                force_y += self.magnetic_type * self.force

        player.rect.x += force_x
        player.rect.y += force_y    

        
        
