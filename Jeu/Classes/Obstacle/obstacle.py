import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width,height):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))  # Réglage de la nouvelle taille (100x100 par exemple)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Mettez ici la logique de mise à jour de l'obstacle si nécessaire
        pass
