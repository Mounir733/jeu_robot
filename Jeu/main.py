import pygame
import sys
from joueur import Player

# Initialisation de Pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu de Plateforme")

# Classe du joueur


# Création des groupes de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des sprites
    all_sprites.update()

    # Affichage
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
