import pygame
import sys
from Classes.Player.playerA import Player
from Classes.InteractiveObject.oreVein import OreVein
from Classes.InteractiveObject.magneticObject import MagneticObject
from Classes.Obstacle.obstacle import Obstacle
from Classes.ConsumableObjects.upsideDown import UpsideDown
from Classes.camera import Camera

# Initialisation de pygame
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Variable qui change
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)


# Fonction principale du jeu
def main_game():


    # Création de la fenêtre du jeu
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Niveau 1")

    #cration de la camera
    camera = Camera()

    # Créez une instance d'obstacle (ajoutez-le à votre scène)
    obstacle = Obstacle(1750, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(obstacle)
    camera.setObject(obstacle)
    
    plateform = Obstacle(1200, 315, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform)
    camera.setObject(plateform)
    plateform2 = Obstacle(1500, 490, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform2)
    camera.setObject(plateform2)
    plateform3 = Obstacle(1400, 210, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform3)
    camera.setObject(plateform3)
    plateform4 = Obstacle(1320, 120, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform4)
    camera.setObject(plateform4)
    plateform5 = Obstacle(2500, 310, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform5)
    camera.setObject(plateform5)
    plateform6 = Obstacle(2200, 120, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform6)
    camera.setObject(plateform6)
    plateform7 = Obstacle(2900, 490, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform7)
    camera.setObject(plateform7)

        
    # Création des groupes de sprites
    all_sprites = pygame.sprite.Group()
    player = Player(obstacles_group)
    all_sprites.add(player)

    #Creer une filon de minerai
    ore_vein = OreVein(1750, 550, "assets/objets_interactibles/Red_crystal1.png", "crystal", 4)
    camera.setObject(ore_vein)
    all_sprites.add(ore_vein)

    #Créer un objet magnétique
    magneticObject = MagneticObject(1700, 650, "assets/objets_interactibles/objetMagnetique.png", 1, 400, 2, ["up"])
    camera.setObject(magneticObject)
    all_sprites.add(magneticObject)

    #Création d'un consomable
    consomable = UpsideDown(600, 600, "assets/objets_interactibles/consomable.png")
    camera.setObject(consomable)
    all_sprites.add(consomable)

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
    camera.setObject(background_surface)


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

        camera.displace_objects(player)
        # Mise à jour des sprites
        all_sprites.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            if player.rect.colliderect(ore_vein.rect):
                ore_vein.interact(player)

            if ore_vein.collectable == False:
                all_sprites.remove(ore_vein)

        magneticObject.interact(player)

        is_consume = consomable.consume(player)
        if is_consume:
            all_sprites.remove(consomable)

        game_over(player)

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
        #dessine le compteur minerai
        show_ore_screen(screen, font, pygame.image.load("assets/objets_interactibles/Red_crystal1.png"), player.numberOre  )

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

def show_ore_screen(screen, font, ore_image, ore_collected):
    # Dessinez l'image du minerai à une position spécifique
    screen.blit(ore_image, (SCREEN_WIDTH - 120, 0))

    # Créez une surface pour le texte du nombre de minerais
    text_surface = font.render(f'x {ore_collected}', True, (255, 255, 255))

    # Dessinez le texte à côté de l'image du minerai
    screen.blit(text_surface, (SCREEN_WIDTH - 60, 10))

def game_over(player):
    if player.rect.left <=0:
        print("MORT!")
        return True
# Boucle de jeu

