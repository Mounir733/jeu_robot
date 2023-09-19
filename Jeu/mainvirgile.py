from typing import Iterable, Union
import pygame
import sys

from pygame.sprite import AbstractGroup
from Classes.Player.player import Player
from Classes.Plateforme.plateforme import Plateforme
from pygame.locals import *



# Initialisation de Pygame
pygame.init()
# Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
WHITE = (255, 255, 255)

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
            starting=False
# Classe de la camera
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0]//2
        self.half_h = self.display_surface.get_size()[1]//2

        # box setup
        self.camera_borders = {'left':200,'right':200,'top':100,'bottom':100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] -(self.camera_borders['left']+self.camera_borders['right'])
        h = self.display_surface.get_size()[1] -(self.camera_borders['top']+self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)

        # ground
        self.ground_surf = pygame.image.load('./assets/backgrounds/niveau1.png').convert_alpha()
        self.fround_rect = self.ground_surf.get_rect(topleft  =(0,0))

    def center_target_camera(self,target):
        a=1

    def box_target_camera(self,target):

        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right < self.camera_rect.right:
            self.camera_rect.right = target.rect.right


        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']


    def custom_draw(self):

        # self.center_target_camera(player)

        # ground
        ground_offset = self.ground_rect.topleft + self.offset
        self.display_surface.blit(self.ground_surf,self.ground_rect)

        # active elements  
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image,offset_pos)  

        pygame.draw.rect(self.display_surface,'yellow',self.camera_rect, 5)"""

# Classe du joueur


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