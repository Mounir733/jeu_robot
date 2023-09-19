import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))  # Couleur rouge pour le boss
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Barre de santé du boss
        self.max_health = 500  # Santé maximale du boss
        self.health = self.max_health

        # Liste des parties du corps du boss
        self.body_parts = []
        self.create_body_parts()  # Créez les parties du corps du boss

    def create_body_parts(self):
        # Créez ici les différentes parties du corps du boss
        # Chaque partie a sa propre position, couleur, santé, et méthode de destruction spécifique
        # Exemple : part = BossPart(x, y, color, health, destroy_method)
        pass

    def take_damage(self, damage):
        # Réduisez la santé du boss lorsque le joueur inflige des dégâts
        self.health -= damage
        if self.health <= 0:
            self.defeated()

    def defeated(self):
        # Méthode appelée lorsque le boss est vaincu
        print("Le boss a été vaincu !")