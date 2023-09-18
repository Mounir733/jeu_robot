import pygame

class Consumable(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def consume(self, player):
        # Méthode générique pour consommer l'objet.
        # Le comportement peut être modifié par les classes filles.
        pass