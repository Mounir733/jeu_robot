import pygame

class Player(pygame.sprite.Sprite):
    _SCREEN_WIDTH = 800
    _SCREEN_HEIGHT = 600

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # Couleur bleue
        self.rect = self.image.get_rect()
        self.rect.center = (self._SCREEN_WIDTH // 2, self._SCREEN_HEIGHT // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.jumping = False
        self.jump_power = -200
    
    def jump(self):
        if not self.jumping:
            self.velocity.y = self.jump_power
            self.jumping = True

    def update(self):
        self.velocity = pygame.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        if keys[pygame.K_SPACE]:
            self.jump()

        # Appliquer la gravité
        self.velocity.y += 0.7

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Empêcher le joueur de sortir de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self._SCREEN_WIDTH:
            self.rect.right = self._SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self._SCREEN_HEIGHT:
            self.rect.bottom = self._SCREEN_HEIGHT
            # Vérifier si le joueur a touché le sol
        if self.rect.bottom >= self._SCREEN_HEIGHT:
            self.jumping = False
