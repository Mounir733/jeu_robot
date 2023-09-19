import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/obstacles/big_box.png")
        self.image = pygame.transform.scale(self.image, (100, 100))  # Réglage de la nouvelle taille (100x100 par exemple)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Mettez ici la logique de mise à jour de l'obstacle si nécessaire
        pass
