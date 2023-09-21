
import pygame
import sys
from niveau1 import main_game
from niveau2 import main_game_2

from creditScene import CreditsScene, CreditsButton

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
def show_menu(unlock_niveau2):
    pygame.mixer.music.load('assets/music/menu.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)
    credits_button = CreditsButton(800, 100, "Credits", font, (255, 255, 255))
    credits_scene = CreditsScene(SCREEN_HEIGHT, SCREEN_HEIGHT,)
    show_credits = False
    selected_earth = True
    menu = True
    earth = pygame.image.load("assets/planets/Terran_Selected.png")
    moon = pygame.image.load("assets/planets/Baren_Selected.png")

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False  # Lancer le jeu principal lorsque la touche Espace est pressée
            if credits_button.is_clicked(event):
                show_credits = True
            if credits_button.exit(event):
                show_credits = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False  # Lancer le jeu principal lorsque la touche Espace est pressée
            if credits_button.is_clicked(event):
                show_credits = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_earth = False  # Lancer le jeu principal lorsque la touche Espace est pressée
                if event.key == pygame.K_LEFT:
                    selected_earth = True  # Lancer le jeu principal lorsque la touche Espace est pressée
                               
        fond = pygame.image.load("assets/backgrounds/space.jpg")
        



        if(unlock_niveau2 == False):
            earth = pygame.image.load("assets/planets/Terran_Selected.png")
            moon = pygame.image.load("assets/planets/Baren_Blocked.png")
        else:
            if(selected_earth == True):
                earth = pygame.image.load("assets/planets/Terran_Selected.png")
                moon = pygame.image.load("assets/planets/Baren.png")
            else:
                moon = pygame.image.load("assets/planets/Baren_Selected.png")
                earth = pygame.image.load("assets/planets/Terran.png")
         
        moon = pygame.transform.scale(moon, (200, 200))  # Redimensionnez à la taille souhaitée
        earth = pygame.transform.scale(earth, (200, 200))  # Redimensionnez à la taille souhaitée

        screen.blit(fond, (0, 0))
        screen.blit(earth, (200, 300))

        earth_text = font.render("Terre", True, WHITE)
        screen.blit(earth_text, (240, 260))

        moon_text = font.render("Lune", True, WHITE)
        screen.blit(moon_text, (640, 260))

        # Créez une surface semi-transparente noire de la même taille que l'image
        filter_surface = pygame.Surface(moon.get_size(), pygame.SRCALPHA)
        filter_color = (0, 0, 0, 128)  # Couleur noire avec un niveau de transparence (128)

        # Remplissez la surface semi-transparente avec la couleur noire
        filter_surface.fill(filter_color)

        # Superposez la surface semi-transparente sur l'image
        screen.blit(filter_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        screen.blit(moon, (600, 300))


        # Afficher le titre du jeu
        title_text = font.render("Simple Magnet", True, WHITE)
        screen.blit(title_text, (30, 30))

        # Afficher les instructions
        instructions_text = font.render("Appuyez sur Espace pour commencer", True, WHITE)
        screen.blit(instructions_text, (125, SCREEN_HEIGHT - 100))

        # Afficher les crédits
        if show_credits:
            credits_scene.display_credits(screen, font)
        else:
            credits_button.draw(screen)


        pygame.display.flip()

    # Boucle de jeu
    pygame.mixer.music.stop()
    while True:
        if(selected_earth == True):
            main_game()  # Lancer le jeu principal
        else:
            main_game_2()  # Lancer le jeu principal

