import pygame
from pygame.math import Vector2
from Classes.InteractiveObject.interactiveObject import InteractiveObject

class MagneticObject(InteractiveObject):
    def __init__(self, x, y, sprite_image, magnetic_type, field_range, force, field_directions=["right"]):
        super().__init__(x, y, sprite_image)
        self.magnetic_type = magnetic_type  # Type d'aimant (1 pour attractif, -1 pour répulsif)
        self.field_range = field_range  # Portée d'attraction
        self.force = force  # Force de champ magnétique
        self.field_directions = field_directions  # Liste des directions du champ de force
        self.force_sound = pygame.mixer.Sound("assets/sound/magnet.mp3")
        self.force_sound.set_volume(0.2)



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
                pygame.mixer.Sound.play(self.force_sound)
                if direction == "right":
                    player.rect.centerx += self.force * self.magnetic_type
                elif direction == "left":
                    player.rect.centerx -= self.force * self.magnetic_type
                elif direction == "up":
                    player.rect.centery -= self.force * self.magnetic_type
                elif direction == "down":
                    print("youpi")
                    player.rect.centery += self.force * self.magnetic_type
            else:
                self.force_sound.stop()