import pygame
import sys
from Classes.Player.playerA import Player
from Classes.InteractiveObject.oreVein import OreVein
from Classes.InteractiveObject.magneticObject import MagneticObject
from Classes.Obstacle.obstacle import Obstacle
from Classes.ConsumableObjects.upsideDown import UpsideDown
from Classes.camera import Camera
from death import death_menu
from win_niveau1 import win_menu
from Classes.keyboard import Keyboard

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
    all_sprites = pygame.sprite.Group()

    #Création de la camera
    camera = Camera()

    # Démarrage de la musique
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/music/lvl1.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Créez une instance d'obstacle (ajoutez-le à votre scène)
    obstacle = Obstacle(3000, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(obstacle)
    camera.setObject(obstacle)

    keyboard = Keyboard(SCREEN_WIDTH, SCREEN_HEIGHT, "assets/keyboard_keys/arrows.png", 1000)
    escape = Keyboard(SCREEN_WIDTH, SCREEN_HEIGHT, "assets/keyboard_keys/escape.png",3000)
    attack = Keyboard(SCREEN_WIDTH, SCREEN_HEIGHT, "assets/keyboard_keys/key_e.png",4500)
    camera.setObject(keyboard)
    camera.setObject(escape)
    camera.setObject(attack)


    plateform = Obstacle(3200, 530, "assets/obstacles/plateforme.png",200,50)
    obstacles_group.add(plateform)
    camera.setObject(plateform)

    obstacle = Obstacle(7000, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle)
    camera.setObject(obstacle)
    obstacle = Obstacle(7000, 490, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle)
    camera.setObject(obstacle)
    obstacle = Obstacle(7000, 390, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle)
    camera.setObject(obstacle)

    # #Creer une filon de minerai
    ore_vein = OreVein(4500, 600, "assets/objets_interactibles/Red_crystal1.png", "crystal", 6)
    camera.setObject(ore_vein)
    all_sprites.add(ore_vein)

    ore_vein2 = OreVein(5500, 600, "assets/objets_interactibles/Red_crystal1.png", "crystal", 6)
    camera.setObject(ore_vein2)
    all_sprites.add(ore_vein2)

    #Créer un objet magnétique
    magneticObject = MagneticObject(6930, 630, "assets/objets_interactibles/objetMagnetique.png", 1, 400, 2, ["up"])
    camera.setObject(magneticObject)
    all_sprites.add(magneticObject)

    # plateforme
    plateform2 = Obstacle(8000, 570, "assets/obstacles/plateforme.png",300,50)
    obstacles_group.add(plateform2)
    camera.setObject(plateform2)
    # consumable
    consomable = UpsideDown(8120, 530, "assets/objets_interactibles/consomable.png")
    camera.setObject(consomable)
    all_sprites.add(consomable)

    # plateforme

    plateform3 = Obstacle(8800, 200, "assets/obstacles/plateforme.png",200,50)
    obstacles_group.add(plateform3)
    camera.setObject(plateform3)

    ore_vein3 = OreVein(8870, 150, "assets/objets_interactibles/Red_crystal1.png", "crystal", 6)
    camera.setObject(ore_vein3)
    all_sprites.add(ore_vein3)

        # plateforme

    plateform4 = Obstacle(9200, 400, "assets/obstacles/plateforme.png",300,50)
    obstacles_group.add(plateform4)
    camera.setObject(plateform4)

    plateform5 = Obstacle(9700, 450, "assets/obstacles/plateforme.png",300,50)
    obstacles_group.add(plateform5)
    camera.setObject(plateform5)

    ore_vein4 = OreVein(9770, 400, "assets/objets_interactibles/Red_crystal1.png", "crystal", 6)
    camera.setObject(ore_vein4)
    all_sprites.add(ore_vein4)

    # Créez une instance d'obstacle (ajoutez-le à votre scène)
    obstacle2 = Obstacle(10500, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle2)
    camera.setObject(obstacle2)

    ore_vein5 = OreVein(10525, 510, "assets/objets_interactibles/Red_crystal1.png", "crystal", 6)
    camera.setObject(ore_vein5)
    all_sprites.add(ore_vein5)

    # plateform5 = Obstacle(2200, 500, "assets/obstacles/plateforme.png",200,50)
    # obstacles_group.add(plateform5)
    # camera.setObject(plateform5)

    # plateform6 = Obstacle(2600, 420, "assets/obstacles/plateforme.png",200,50)
    # obstacles_group.add(plateform6)
    # camera.setObject(plateform6)
    
    # plateform7 = Obstacle(2900, 490, "assets/obstacles/plateforme.png",200,50)
    # obstacles_group.add(plateform7)
    # camera.setObject(plateform7)

        
    # Création des groupes de sprites
    player = Player(obstacles_group)
    all_sprites.add(player)
    all_sprites.add(keyboard)
    all_sprites.add(escape)
    all_sprites.add(attack)





    # #Création d'un consomable
    # consomable = UpsideDown(1600, 600, "assets/objets_interactibles/consomable.png")
    # camera.setObject(consomable)
    # all_sprites.add(consomable)

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

    arrows = pygame.image.load("assets/keyboard_keys/arrows.png")
    arrows = pygame.transform.scale(arrows, (arrows.get_width()/2, arrows.get_height()/2))
 

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
        keys = pygame.key.get_pressed()

        camera.displace_objects(player)
        # Mise à jour des sprites
        all_sprites.update()

        ore_vein.link(player,all_sprites,keys)
        ore_vein2.link(player,all_sprites,keys)
        ore_vein3.link(player,all_sprites,keys)
        ore_vein4.link(player,all_sprites,keys)
        ore_vein5.link(player,all_sprites,keys)

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

        if(player.numberOre == 5):
            win_menu()

        if(ore_vein5.rect.x == 0 and player.numberOre != 5):
            death_menu(False)

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
        player.is_dead = True
        if(player.is_dead == True):
            pygame.mixer.stop()
            pygame.mixer.Sound.play(player.death_sound)
            pygame.time.wait(1000)
            death_menu()
        return True
# Boucle de jeu

