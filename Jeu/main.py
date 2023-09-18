import pygame
import sys
from Classes.Player.player import Player
from Classes.Plateforme.plateforme import Plateforme

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
fond_rect = fond.get_rect()

# Position du fond (initialisée à 0)
fond_x = 0

# Vitesse de défilement du fond
vitesse_fond = 2

# Créez des instances de plateformes
plateformes = pygame.sprite.Group()
plateforme1 = Plateforme(100, 500, 200, 20)
plateforme2 = Plateforme(300, 400, 150, 20)
plateforme3 = Plateforme(500, 300, 200, 20)

# Ajoutez les plateformes à la liste
plateformes.add(plateforme1, plateforme2, plateforme3)

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des sprites
    all_sprites.update()

    keys = pygame.key.get_pressed()

        # Mise à jour de la position du fond pour le faire défiler
    fond_x -= vitesse_fond

    # Si le fond atteint la fin de l'image, réinitialisez-le à 0
    fond_x = 0

    screen.blit(fond, (fond_x, 0))
    screen.blit(fond, (fond_x + SCREEN_HEIGHT, 0))  # Deuxième copie pour le défilement continu

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
    screen.fill(WHITE)
    all_sprites.draw(screen)
    all_sprites.draw(fond)
    plateformes.draw(screen)
    plateformes.draw(fond)

    pygame.display.flip()
    pygame.display.update()

# Quitter Pygame
pygame.quit()
sys.exit() 