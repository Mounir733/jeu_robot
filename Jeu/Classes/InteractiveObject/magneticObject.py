import pygame
from pygame.math import Vector2
from Classes.InteractiveObject.interactiveObject import InteractiveObject
""""
class MagneticObject(InteractiveObject):
    def __init__(self, x, y, sprite_image, magnetic_type, field_range, force, field_directions=["right"]):
        super().__init__(x, y, sprite_image)
        self.magnetic_type = magnetic_type  # Type d'aimant (1 pour attractif, -1 pour répulsif)
        self.field_range = field_range  # Portée d'attraction
        self.force = force  # Force de champ magnétique
        self.field_directions = field_directions  # Liste des directions du champ de force

    def calculate_field_zone(self, direction):
        object_center = Vector2(self.rect.center)

        # Calculez la zone du champ de force en fonction de la direction spécifiée
        if direction == "right":
            return pygame.Rect(object_center.x, object_center.y - self.rect.height / 2, self.field_range, self.rect.height)
        elif direction == "left":
            return pygame.Rect(object_center.x - self.field_range, object_center.y - self.rect.height / 2, self.field_range, self.rect.height)
        elif direction == "up":
            return pygame.Rect(object_center.x - self.rect.width / 2, object_center.y - self.field_range, self.rect.width, self.field_range)
        elif direction == "down":
            return pygame.Rect(object_center.x - self.rect.width / 2, object_center.y, self.rect.width, self.field_range)

    def interact(self, player):
        player_center = Vector2(player.rect.center)

        for direction in self.field_directions:
            # Vérifiez si la direction spécifiée est présente dans la liste des directions
            if direction in ["right", "left", "up", "down"]:
                # Calculez la zone du champ de force
                field_zone = self.calculate_field_zone(direction)

                # Vérifiez si la zone est valide
                if field_zone.width > 0 and field_zone.height > 0:
                    # Vérifiez si le joueur se trouve dans la zone du champ de force
                    if field_zone.collidepoint(player_center):
                        # Calculez le vecteur entre le joueur et l'objet
                        direction_vector = player_center - Vector2(self.rect.center)
                        direction_vector.normalize_ip()

                        # Appliquez la force magnétique en fonction de magnetic_type
                        force_vector = direction_vector * self.force * self.magnetic_type

                        # Appliquez la force au joueur en ajustant directement sa position
                        player.rect.center += force_vector
"""

class MagneticObject(InteractiveObject):
    def __init__(self, x, y, sprite_image, magnetic_type, field_range, force, field_directions=["right"]):
        super().__init__(x, y, sprite_image)
        self.magnetic_type = magnetic_type  # Type d'aimant (1 pour attractif, -1 pour répulsif)
        self.field_range = field_range  # Portée d'attraction
        self.force = force  # Force de champ magnétique
        self.field_directions = field_directions  # Liste des directions du champ de force

    def calculate_field_zone(self, direction):
        object_center = Vector2(self.rect.center)

        # Calculez la zone du champ de force en fonction de la direction spécifiée
        if direction == "right":
            return pygame.Rect(object_center.x, object_center.y - self.rect.height / 2, self.field_range, self.rect.height)
        elif direction == "left":
            return pygame.Rect(object_center.x - self.field_range, object_center.y - self.rect.height / 2, self.field_range, self.rect.height)
        elif direction == "up":
            return pygame.Rect(object_center.x - self.rect.width / 2, object_center.y - self.field_range, self.rect.width, self.field_range)
        elif direction == "down":
            return pygame.Rect(object_center.x - self.rect.width / 2, object_center.y, self.rect.width, self.field_range)
        
    def interact(self, player): 
        for direction in self.field_directions:
            # Calculez la zone du champ de force
            field_zone = self.calculate_field_zone(direction)

            if field_zone.colliderect(player.rect):
                if direction == "right":
                    player.rect.centerx += self.force * self.magnetic_type
                elif direction == "left":
                    player.rect.centerx -= self.force * self.magnetic_type
                elif direction == "up":
                    player.rect.centery -= self.force * self.magnetic_type
                elif direction == "down":
                    player.rect.centery += self.force * self.magnetic_type