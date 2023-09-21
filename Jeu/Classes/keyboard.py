import pygame

class Keyboard(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, img, x_position):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        original_image = pygame.image.load(img)  # Chargez l'image spécifiée
        self.image = pygame.transform.scale(original_image, (original_image.get_width() // 2, original_image.get_height() // 2))  # Redimensionnez l'image par 4
        self.rect = self.image.get_rect()
        self.rect.centerx = x_position  # Utilisez la position en x spécifiée
        self.rect.top = 0  # En haut de l'écran

    def update(self):
        # Mettez à jour le sprite si nécessaire (par exemple, animations, etc.)
        pass
