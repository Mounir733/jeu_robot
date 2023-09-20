from typing import Iterable, Union
import pygame
import sys

from pygame.sprite import AbstractGroup
from Classes.Player.player import Player
from Classes.Plateforme.plateforme import Plateforme
from pygame.locals import *
from pygame import mixer



# Initialisation de Pygame
pygame.init()
# Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WHITE = (255, 255, 255)

# Initialisation de mixer
mixer.init()

# Création de la fenêtre du jeu
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu de Plateforme")
"""screen.fill((120, 120, 0))
pygame.display.flip()
pygame.display.update()


starting = True
while starting:
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_SPACE:
            starting=False"""


"""screen.fill((60, 0, 60))
pygame.display.flip()
pygame.display.update()

starting = True
while starting:
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == KEYDOWN:
        if event.key == K_SPACE:
            starting=False"""


# Classe du joueur

pygame.mixer.music.load('assets/music/a-calm-soulful-atmosphere-for-a-documentary-film-166464.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.stop()
pygame.mixer.music.load('assets\music\pendulum-of-peril-165586.mp3')
pygame.mixer.music.play(-1)

# Création des groupes de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Chargement de l'image de fond
fond = pygame.image.load("assets/backgrounds/niveau1.png")
new_width = int((SCREEN_HEIGHT / fond.get_height()) * fond.get_width())
fond = pygame.transform.scale(fond, (new_width, SCREEN_HEIGHT))
background_surface = pygame.Surface((fond.get_width(), fond.get_height()))
background_surface.blit(fond, (0, 0))
background_x = 0
background_y = 0

# Position du fond (initialisée à 0)
fond_x = 0

# Vitesse de défilement du fond
vitesse_fond = 2

# Créez des instances de plateformes
plateformes = pygame.sprite.Group()
plateforme1 = Plateforme(100, 500, 200, 20)

# Ajoutez les plateformes à la liste
plateformes.add(plateforme1)


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
    #background_x += (player.velocity.x)/10


    # Gestion des collisions entre le joueur et les plateformes
    collisions = pygame.sprite.spritecollide(player, plateformes, False)
    on_platform = False  # Indique si le joueur est sur une plateforme
    
    for plateforme in collisions:
        if player.velocity.y > 0:  # Si le joueur est en train de tomber
            player.rect.bottom = plateforme.rect.top
            player.velocity.y = 0
            on_platform = True  # Indiquer que le joueur est sur une plateforme
                # Si le joueur est sur une plateforme, il peut sauter
            if on_platform:
                if keys[pygame.K_SPACE]:  # Gestion de la touche Espace pour le saut
                    player.jump()
                    

    # Affichage
    #screen.fill(WHITE)
    screen.fill((0, 0, 0))
    screen.blit(background_surface, (0, 0), pygame.Rect(background_x, background_y, SCREEN_WIDTH, SCREEN_HEIGHT))
    plateformes.draw(screen)
    all_sprites.draw(screen)
    

    pygame.display.flip()
    pygame.display.update()

# Quitter Pygame
pygame.quit()
sys.exit() 