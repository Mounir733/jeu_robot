import pygame

class Player(pygame.sprite.Sprite):
    _SCREEN_WIDTH = 1024
    _SCREEN_HEIGHT = 768

    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/robots/OrangeRobot/SeparetedImages/OrangeRobot1.png")
        self.image = pygame.transform.scale(self.original_image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (self._SCREEN_WIDTH // 2, self._SCREEN_HEIGHT // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.3
        self.jump_power = -14
        self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False  # Définir le joueur comme étant en l'air

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        else:
            self.velocity.x = 0

        if keys[pygame.K_SPACE]:  # Gestion de la touche Espace pour le saut
            self.jump()

        if not self.on_ground:
            self.velocity.y += self.gravity
        else:
            self.velocity.y = 0

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self._SCREEN_WIDTH:
            self.rect.right = self._SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self._SCREEN_HEIGHT:
            self.rect.bottom = self._SCREEN_HEIGHT
            self.on_ground = True  # Le joueur touche le sol

    #####Maxence#######

    def has_magnet():
        return True
    
    def collect_ore(self, ore_vein):
        if ore_vein.collecting_timer > 0:
            self.collecting_timer -= 1
            return True
        else:
            return False