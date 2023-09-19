import pygame

class BossPart(pygame.sprite.Sprite):
    def __init__(self, x, y, color, health, destroy_method):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.destroy_method = destroy_method

    def take_damage(self, damage):
        # Réduisez la santé de la partie du corps lorsque le joueur inflige des dégâts
        self.health -= damage
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        # Méthode spécifique pour la destruction de la partie du corps
        self.destroy_method(self)