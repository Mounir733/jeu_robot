import pygame

class Plateforme(pygame.sprite.Sprite):
    def __init__(self, x, y, largeur, hauteur):
        super().__init__()
        self.image = pygame.Surface((largeur, hauteur))
        self.image.fill((0, 255, 0))  # Couleur verte pour la plateforme (vous pouvez utiliser une image à la place)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
