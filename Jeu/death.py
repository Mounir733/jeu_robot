import pygame
import sys

# Initialisation de pygame
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Variable qui change
RED = (240, 0, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font("Jeu/Font/androidnation.ttf", 40)  # Vous pouvez choisir une police personnalisée
font2 = pygame.font.Font("Jeu/Font/androidnation.ttf", 30)  # Vous pouvez choisir une police personnalisée


def death_menu():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mort")
    death_text = font.render("Vous etes mort !", True, RED)
    death_text_rect = death_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    # Créez des boutons pour "Rejouer" et "Quitter"
    replay_button = font2.render("Rejouer", True, WHITE)
    replay_button_rect = replay_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    quit_button = font2.render("Quitter", True, WHITE)
    quit_button_rect = quit_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button_rect.collidepoint(event.pos):
                    # Lorsque le bouton "Rejouer" est cliqué, appelez la fonction main_game de niveau1.py
                    import niveau1
                    niveau1.main_game()
                elif quit_button_rect.collidepoint(event.pos):
                    # Lorsque le bouton "Quitter" est cliqué, appelez la fonction show_menu de start.py
                    import start
                    start.show_menu()

            
        fond = pygame.image.load("assets/backgrounds/space.jpg")

        
        screen.fill((0, 0, 0))
        screen.blit(fond, (0, 0))

        screen.blit(death_text, death_text_rect)
        screen.blit(replay_button, replay_button_rect)
        screen.blit(quit_button, quit_button_rect)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()
    