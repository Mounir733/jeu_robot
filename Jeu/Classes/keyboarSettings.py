import pygame

class KeyboardSettings:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((255, 255, 255))  # Fond blanc
        self.font = pygame.font.Font(None, 36)  # Police et taille du texte

        # Charger les images des touches
        self.arrows_image = pygame.image.load("assets/keyboard_keys/arrows.png")
        self.key_e_image = pygame.image.load("assets/keyboard_keys/key_e.png")
        self.key_escape_image = pygame.image.load("assets/keyboard_keys/escape.png")

    def display_instructions(self, screen):
        # Dessinez le fond
        screen.blit(self.background, (0, 0))

        # Dessinez les instructions
        text = self.font.render("Instructions:", True, (0, 0, 0))  # Couleur du texte : noir
        screen.blit(text, (20, 20))

        screen.blit(self.arrows_image, (20, 60))
        text = self.font.render("Move with arrow keys", True, (0, 0, 0))
        screen.blit(text, (100, 80))

        screen.blit(self.key_e_image, (20, 120))
        text = self.font.render("Press 'E' to collect minerals", True, (0, 0, 0))
        screen.blit(text, (100, 140))

        screen.blit(self.key_escape_image, (20, 180))
        text = self.font.render("Press 'Esc' to pause the game", True, (0, 0, 0))
        screen.blit(text, (100, 200))