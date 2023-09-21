import pygame
import sys

# Initialisation de pygame
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Variable qui change
GREEN = (144,238,144)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font("Jeu/Font/androidnation.ttf", 40)  # Vous pouvez choisir une police personnalisée
font2 = pygame.font.Font("Jeu/Font/androidnation.ttf", 30)  # Vous pouvez choisir une police personnalisée


def win_menu():
    unlock_niveau2 = True
    pygame.mixer.stop()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/music/gameover.mp3')
    pygame.mixer.music.set_volume(0.75)
    pygame.mixer.music.play(1)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Victoire")
    win_text = font.render("Vous avez gagnez !!", True, GREEN)
    win_text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    # Créez des boutons pour "Rejouer" et "Quitter"
    replay_button = font2.render("Niveau 2", True, WHITE)
    replay_button_rect = replay_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    quit_button = font2.render("Quitter", True, WHITE)
    quit_button_rect = quit_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                if replay_button_rect.collidepoint(event.pos):
                    # Lorsque le bouton "Rejouer" est cliqué, appelez la fonction main_game de niveau1.py
                    import niveau2
                    niveau2.main_game()
                elif quit_button_rect.collidepoint(event.pos):
                    # Lorsque le bouton "Quitter" est cliqué, appelez la fonction show_menu de start.py
                    import start
                    start.show_menu(unlock_niveau2)

            
        fond = pygame.image.load("assets/backgrounds/space.jpg")

        
        screen.fill((0, 0, 0))
        screen.blit(fond, (0, 0))

        screen.blit(win_text, win_text_rect)
        screen.blit(replay_button, replay_button_rect)
        screen.blit(quit_button, quit_button_rect)

        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()
    