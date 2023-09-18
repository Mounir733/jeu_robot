import pygame
import InteractiveObject

class MagneticObject(InteractiveObject):
    def __init__(self, x, y, width, height, color, magnetic_type):
        super().__init__(x, y, width, height, color)
        self.magnetic_type = magnetic_type  # Type d'aimant (1 pour attractif, -1 pour répulsif)

    def interact(self, player):
        # Comportement spécifique pour l'interaction avec un objet magnétique
        if player.has_magnet() and self.magnetic_type != 0:
            dx = self.rect.centerx - player.rect.centerx
            dy = self.rect.centery - player.rect.centery
            distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)  # Évite la division par zéro
            force = pygame.Vector2(dx, dy)
            force /= distance
            force *= self.magnetic_type  # Ajuste la force en fonction du type d'aimant

            # Applique la force au joueur (modification de la vitesse)
            player.velocity += force