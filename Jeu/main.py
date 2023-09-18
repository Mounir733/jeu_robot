import pygame
import sys
from player import Player
from platform import Platform

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
platform1 = Platform(100, 500, 200, 20)  # Example platform
all_sprites.add(platform1)
player = Player()
all_sprites.add(player)

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    collide_list = pygame.sprite.spritecollide(player, all_sprites, False)
    if collide_list:
    # Player is on a platform, handle jumping and gravity accordingly
        player.is_jumping = False
        player.rect.y = collide_list[0].rect.top  # Place player on top of the platform
    # Player is in the air, apply gravity or allow jumping


    # Mise à jour des sprites
    all_sprites.update()

    # Affichage
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()