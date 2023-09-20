
import pygame
import sys
from niveau1 import main_game

# Initialisation de pygame
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police de caractères pour le menu
font = pygame.font.Font("Jeu/Font/androidnation.ttf", 25)  # Vous pouvez choisir une police personnalisée

# Créer une fonction pour afficher le menu
def show_menu():
    pygame.mixer.music.load('assets/music/menu.mp3')
    pygame.mixer.music.play(-1)
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False  # Lancer le jeu principal lorsque la touche Espace est pressée
        fond = pygame.image.load("assets/backgrounds/space.jpg")

        screen.blit(fond, (0, 0))

        # Afficher le titre du jeu
        title_text = font.render("Simple Magnet", True, WHITE)
        screen.blit(title_text, (30, 30))

        # Afficher les instructions
        instructions_text = font.render("Appuyez sur Espace pour commencer", True, WHITE)
        screen.blit(instructions_text, (125, SCREEN_HEIGHT - 100))

        pygame.display.flip()

    # Boucle de jeu
    pygame.mixer.music.stop()
    while True:
        main_game()  # Lancer le jeu principal
