import pygame
import math

class Shockwave(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))  # Couleur verte pour l'onde de choc
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.player = player
        self.speed = 5  # Vitesse de l'onde de choc (ajustez selon vos besoins)
        self.distance_limit = 300  # Distance maximale de l'onde de choc (ajustez selon vos besoins)

    def update(self):
        # Déplace l'onde de choc vers le joueur
        dx = self.player.rect.centerx - self.rect.centerx
        dy = self.player.rect.centery - self.rect.centery
        distance = max(1, math.sqrt(dx**2 + dy**2))
        if distance <= self.distance_limit:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed
        else:
            self.kill()  # Supprimer l'onde de choc une fois qu'elle atteint la distance limite
