import pygame
# Classe pour la scène de crédits
class CreditsScene:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.background = pygame.Surface((SCREEN_WIDTH + 400, SCREEN_HEIGHT))
        self.background.fill((0, 0, 0))  # Fond noir

        # Créez une liste de crédits
        self.credits_text = [
            "",
            "",
            "",
            "",
            "Jeu cree par Mounir, Maxence et Virgile",
            "Sprites par EduSilvArt et Mounir",
            "Musique par Pixabay et Mixkit",

            "Développeurs : Mounir, Maxence, Virgile ",
            "Directeur Artistique : Mounir",
            "Directeur Musicale : Virgile",
            "Directeur Projet : Maxence",
            "",
            "",
            "",
            "Appuyez sur retour pour retourne sur le menu"
        ]

    def display_credits(self, screen, font):
        # Dessinez le fond
        screen.blit(self.background, (0, 0))

        # Dessinez les crédits
        y_position = 20
        for credit_line in self.credits_text:
            text = font.render(credit_line, True, (255, 255, 255))  # Couleur du texte : noir
            screen.blit(text, (20, y_position))
            y_position += 40

class CreditsButton:
    def __init__(self, x, y, text, font, color):
        self.rect = pygame.Rect(x, y, 200, 40)  # Rectangle du bouton
        self.text = text  # Texte à afficher sur le bouton
        self.font = font  # Police du texte
        self.color = color  # Couleur du texte

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  # Dessine un contour autour du bouton
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.centerx - text_surface.get_width() // 2, self.rect.centery - text_surface.get_height() // 2))

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                return self.rect.collidepoint(event.pos)
        return False

    def exit(self, event):
        if event.type == pygame.K_RETURN:
            return True