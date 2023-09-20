
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
font = pygame.font.Font(None, 36)

# Créer une fonction pour afficher le menu
def show_menu():
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
        title_text = font.render("KingOfMagnet", True, WHITE)
        screen.blit(title_text, (300, 200))

        # Afficher les instructions
        instructions_text = font.render("Appuyez sur Espace pour commencer", True, WHITE)
        screen.blit(instructions_text, (250, 300))

        pygame.display.flip()

# Boucle de jeu
show_menu()  # Afficher le menu au démarrage
while True:
    main_game()  # Lancer le jeu principal
