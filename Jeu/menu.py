import pygame
import sys
from Classes.Player.playerA import Player
from Classes.Obstacle.obstacle import Obstacle

# Initialisation de pygame
pygame.init()

# Définir la taille de la fenêtre d'affichage
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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

# Fonction principale du jeu
def main_game():
    
    # Constantes
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

    # Création de la fenêtre du jeu
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Jeu de Plateforme")

    # Créez une instance d'obstacle (ajoutez-le à votre scène)
    obstacle = Obstacle(750, 590, "assets/obstacles/big_box.png",100,100)
    obstacle2 = Obstacle(200, 490, "assets/obstacles/small_box.png",50,50)
    obstacle3 = Obstacle(300, 380, "assets/obstacles/plateforme.png",150,50)
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(obstacle)
    obstacles_group.add(obstacle2)
    obstacles_group.add(obstacle3)

        #Creer une filon de minerai
    ore_vein = OreVein(750, 550, "assets/objets_interactibles/Red_crystal1.png", "crystal", 4)
    camera.setObject(ore_vein)
    all_sprites.add(ore_vein)

    #Créer un objet magnétique
    magneticObject = MagneticObject(700, 650, "assets/objets_interactibles/objetMagnetique.png", 1, 400, 2, ["up"])
    camera.setObject(magneticObject)
    all_sprites.add(magneticObject)

        
    # Création des groupes de sprites
    all_sprites = pygame.sprite.Group()
    player = Player(obstacles_group)
    all_sprites.add(player)

    # Chargement de l'image de fond
    fond = pygame.image.load("assets/backgrounds/niveau1.png")
    sol = pygame.image.load("assets/backgrounds/sol.png")
    new_width = int((SCREEN_HEIGHT / fond.get_height()) * fond.get_width())
    fond = pygame.transform.scale(fond, (new_width, SCREEN_HEIGHT))
    sol = pygame.transform.scale(sol, (new_width, SCREEN_HEIGHT))
    background_surface = pygame.Surface((fond.get_width(), fond.get_height()))
    background_surface.blit(fond, (0, 0))
    background_surface.blit(sol, (0, 0))
    background_x = 0
    background_y = 0


    # Position du fond (initialisée à 0)
    fond_x = 0

    # Vitesse de défilement du fond
    vitesse_fond = 2



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


               
        # Vérifiez la collision entre le joueur et l'obstacle
        collisions = pygame.sprite.spritecollide(player, obstacles_group, False)
        if collisions:
            # Gérez la collision ici en empêchant le joueur de passer à travers l'obstacle
            player.rect.x = player.prev_x  # Réinitialisez la position du joueur à la position précédente
            player.rect.y = player.prev_y
        else:
            player.on_ground == False


        screen.blit(background_surface, (0, 0), pygame.Rect(background_x, background_y, SCREEN_WIDTH, SCREEN_HEIGHT))


        # Dessinez l'obstacle
        obstacles_group.update()
        obstacles_group.draw(screen)

        # Affichage
        all_sprites.draw(screen)


        pygame.display.flip()
        pygame.display.update()

    # Quitter Pygame
    pygame.quit()
    sys.exit() 

# Boucle de jeu
show_menu()  # Afficher le menu au démarrage
while True:
    main_game()  # Lancer le jeu principal
