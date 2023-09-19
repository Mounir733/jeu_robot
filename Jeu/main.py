from typing import Iterable, Union
import pygame
import sys
from pygame.sprite import AbstractGroup
from Classes.Player.player import Player

# Initialisation de Pygame
pygame.init()

# Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WHITE = (255, 255, 255)

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu de Plateforme")
    

# Classe du joueur

    
# Création des groupes de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Chargement de l'image de fond
fond = pygame.image.load("assets/backgrounds/niveau1.png")
background_surface = pygame.Surface((fond.get_width(), fond.get_height()))
background_surface.blit(fond, (0, 0))
background_x = 0
background_y = 0

# Position du fond (initialisée à 0)
fond_x = 0

# Vitesse de défilement du fond
vitesse_fond = 2


# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    # Mise à jour des sprites
    all_sprites.update()
    collide_list = pygame.sprite.spritecollide(player, all_sprites, False)
    if collide_list:
    # Player is on a platform, handle jumping and gravity accordingly
        player.is_jumping = False
        player.rect.y = collide_list[0].rect.top # Place player on top of the platform
        player.on_ground
    # Player is in the air, apply gravity or allow jumping

    keys = pygame.key.get_pressed()

        # Mise à jour de la position du fond pour le faire défiler
    fond_x -= vitesse_fond

    # Si le fond atteint la fin de l'image, réinitialisez-le à 0
    fond_x = 0

    screen.blit(fond, (fond_x, 0))
    screen.blit(fond, (fond_x + SCREEN_HEIGHT, 0))  # Deuxième copie pour le défilement continu

    





    # Affichage
    screen.fill(WHITE)
    screen.blit(background_surface, (0, 0), pygame.Rect(background_x, background_y, SCREEN_WIDTH, SCREEN_HEIGHT))
    all_sprites.draw(screen)
    all_sprites.draw(fond)


    pygame.display.flip()
    pygame.display.update()

# Quitter Pygame
pygame.quit()
sys.exit() 