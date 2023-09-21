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
font = pygame.font.Font("Jeu/Font/androidnation.ttf", 40)
font2 = pygame.font.Font("Jeu/Font/androidnation.ttf", 30)


def death_menu(niveau2, notCollectedAll):
    pygame.mixer.stop()
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/music/gameover.mp3')
    pygame.mixer.music.set_volume(0.75)
    pygame.mixer.music.play(1)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mort")
    if notCollectedAll:
        death_text = font.render("Mission Echoue", True, RED)
    else:
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
                pygame.mixer.music.stop()
                if replay_button_rect.collidepoint(event.pos):
                    import niveau1
                    import niveau2
                    if niveau2 == False:
                        niveau1.main_game()
                    else:
                        niveau2.main_game_2()
                elif quit_button_rect.collidepoint(event.pos):
                    import start
                    if niveau2 == False:
                        start.show_menu(False)
                    else:
                        start.show_menu(True)
                      

            
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
    