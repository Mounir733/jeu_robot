import pygame
import sys
import time
from start import show_menu

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Magnet")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Police stylée pour le nom du jeu
font = pygame.font.Font("Jeu/Font/androidnation.ttf", 72)  # Vous pouvez choisir une police personnalisée
font2 = pygame.font.Font("Jeu/Font/androidnation.ttf", 30)  # Vous pouvez choisir une police personnalisée

# Texte à afficher
game_name = "Simple Magnet"
team_name = "SimpleTeam presente"

# Création des surfaces de texte
game_name_surface = font.render(game_name, True, WHITE)
team_name_surface = font2.render(team_name, True, WHITE)

# Positionnement du texte au centre de l'écran
game_name_rect = game_name_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
team_name_rect = team_name_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

# Temps de la transition (en secondes)
transition_duration = 5  # Par exemple, 5 secondes

# Horodatage du début de la transition
transition_start_time = time.time()

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculer le niveau de transparence en fonction du temps écoulé
    elapsed_time = time.time() - transition_start_time
    alpha = min(255, int((elapsed_time / transition_duration) * 255))

    # Effacement de l'écran
    screen.fill((0, 0, 0))

    # Affichage du texte
    screen.blit(game_name_surface, game_name_rect)
    screen.blit(team_name_surface, team_name_rect)

    # Surface semi-transparente pour l'effet de fondu
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    fade_surface.fill((0, 0, 0, alpha))  # Couleur noire avec niveau de transparence

    # Superposition de la surface semi-transparente
    screen.blit(fade_surface, (0, 0))

    # Mise à jour de l'écran
    pygame.display.flip()

    # Vérifier si le temps de transition est écoulé
    if elapsed_time >= transition_duration:
        show_menu(True)  # Sortir de la boucle après la transition

# Quitter Pygame
pygame.quit()
sys.exit()


# Après la cinématique, vous pouvez exécuter le script "start.py" ici
