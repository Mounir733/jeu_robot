import pygame
import Shockwave

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Couleur rouge pour l'ennemi
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.player = player

        self.shoot_delay = 60  # Délai entre chaque tir en frames (ajustez selon vos besoins)
        self.shoot_timer = 0

    def update(self):
        # Suivre le joueur
        target_x, target_y = self.player.rect.center
        self.move_towards(target_x, target_y)

        # Tirer des ondes de choc
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_delay:
            self.shoot()
            self.shoot_timer = 0

    def move_towards(self, target_x, target_y):
        # Déplace l'ennemi vers la position du joueur
        dx = target_x - self.rect.centerx
        dy = target_y - self.rect.centery
        distance = max(1, math.sqrt(dx**2 + dy**2))
        speed = 2  # Vitesse de déplacement (ajustez selon vos besoins)
        self.rect.x += (dx / distance) * speed
        self.rect.y += (dy / distance) * speed

    def shoot(self):
        # Créer une onde de choc dans la direction du joueur
        bullet = Shockwave(self.rect.centerx, self.rect.centery, self.player)
        all_sprites.add(bullet)
        bullets.add(bullet)