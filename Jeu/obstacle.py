import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, velocity_y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity_y = velocity_y

    def update(self):
        self.rect.y += self.velocity_y
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        self.rect.y = 0
        self.rect.x = 200  # Position de départ en haut
