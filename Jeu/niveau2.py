import pygame
import sys
from Classes.Player.playerA import Player
from Classes.InteractiveObject.oreVein import OreVein
from Classes.InteractiveObject.magneticObject import MagneticObject
from Classes.Obstacle.obstacle import Obstacle
from Classes.ConsumableObjects.upsideDown import UpsideDown
from Classes.camera import Camera
from death import death_menu
from win_niveau2 import win_menu_2

# Initialisation de pygame
pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Variable qui change
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

niveau2 = True

# Fonction principale du jeu
def main_game_2():


    # Création de la fenêtre du jeu
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Niveau 2")
    all_sprites = pygame.sprite.Group()

    #cration de la camera
    camera = Camera()

    # Démarrage de la musique
    pygame.mixer.music.stop()
    pygame.mixer.music.load('assets/music/lvl2.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Créez une instance d'obstacle (ajoutez-le à votre scène)
    obstacle = Obstacle(2000, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group = pygame.sprite.Group()
    obstacles_group.add(obstacle)
    camera.setObject(obstacle)

    obstacle2 = Obstacle(2000, 490, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle2)
    camera.setObject(obstacle2)



    obstacle4 = Obstacle(2000, 190, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle4)
    camera.setObject(obstacle4)


    obstacle5 = Obstacle(2000, 90, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle5)
    camera.setObject(obstacle5)

    obstacle6 = Obstacle(2000, -10, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle6)
    camera.setObject(obstacle6)


    #Créer un objet magnétique
    magneticObject2 = MagneticObject(2200, 50, "assets/objets_interactibles/objetMagnetique_2.png", 1, 400, 2, ["down"])
    camera.setObject(magneticObject2)
    all_sprites.add(magneticObject2)




       # #Creer une filon de minerai
    ore_vein = OreVein(2400, 600, "assets/objets_interactibles/Minerai_Lune.png", "crystal", 6)
    camera.setObject(ore_vein)
    all_sprites.add(ore_vein)

    #Créer un objet magnétique
    magneticObject3 = MagneticObject(2900, 600, "assets/objets_interactibles/objetMagnetique.png", 1, 400, 2, ["up"])
    camera.setObject(magneticObject3)
    all_sprites.add(magneticObject3)

    obstacle7 = Obstacle(3000, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle7)
    camera.setObject(obstacle7)

    obstacle8 = Obstacle(3000, 490, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle8)
    camera.setObject(obstacle8)



    obstacle9= Obstacle(3000, 390, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle9)
    camera.setObject(obstacle9)


    obstacle10 = Obstacle(3000, 290, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle10)
    camera.setObject(obstacle10)

        # #Creer une filon de minerai
    ore_vein2 = OreVein(3030, 95, "assets/objets_interactibles/Minerai_Lune.png", "crystal", 6)
    camera.setObject(ore_vein2)
    all_sprites.add(ore_vein2)

    obstacle11 = Obstacle(3000, -10, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle11)
    camera.setObject(obstacle11)


    plateform = Obstacle(3200, 530, "assets/obstacles/plateforme.png",200,50)
    obstacles_group.add(plateform)
    camera.setObject(plateform)

    plateform2 = Obstacle(3550, 200, "assets/obstacles/plateforme.png",200,50)
    obstacles_group.add(plateform2)
    camera.setObject(plateform2)

    plateform3 = Obstacle(3800, 400, "assets/obstacles/plateforme.png",200,50)
    obstacles_group.add(plateform3)
    camera.setObject(plateform3)

 



        #Créer un objet magnétique
    magneticObject6 = MagneticObject(4700, 300, "assets/objets_interactibles/objetMagnetique.png", 1, 400, 2, ["up"])
    camera.setObject(magneticObject6)
    all_sprites.add(magneticObject6)

    plateform4 = Obstacle(4900, 100, "assets/obstacles/plateforme.png",300,50)
    obstacles_group.add(plateform4)
    camera.setObject(plateform4)

            # #Creer une filon de minerai
    ore_vein3 = OreVein(5000, 20, "assets/objets_interactibles/Minerai_Lune.png", "crystal", 6)
    camera.setObject(ore_vein3)
    all_sprites.add(ore_vein3)

        
    obstacle12 = Obstacle(6000, 590, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle12)
    camera.setObject(obstacle12)

    obstacle13 = Obstacle(6000, 490, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle13)
    camera.setObject(obstacle13)



    obstacle14= Obstacle(6000, 390, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle14)
    camera.setObject(obstacle14)


    obstacle15 = Obstacle(6000, 290, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle15)
    camera.setObject(obstacle15)

    obstacle16 = Obstacle(6000, 190, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle16)
    camera.setObject(obstacle16)

    obstacle17 = Obstacle(6000, 90, "assets/obstacles/big_box.png",100,100)
    obstacles_group.add(obstacle17)
    camera.setObject(obstacle17)


    plateform4 = Obstacle(6400, 400, "assets/obstacles/plateforme.png",200,50)
    obstacles_group.add(plateform4)
    camera.setObject(plateform4)

    ore_vein4 = OreVein(6450, 350, "assets/objets_interactibles/Minerai_Lune.png", "crystal", 6)
    camera.setObject(ore_vein4)
    all_sprites.add(ore_vein4)


    #Créer un objet magnétique
    magneticObject4 = MagneticObject(6700, 50, "assets/objets_interactibles/objetMagnetique_2.png", 1, 400, 2, ["down"])
    camera.setObject(magneticObject4)
    all_sprites.add(magneticObject4)

    #Créer un objet magnétique
    magneticObject5 = MagneticObject(6700, 600, "assets/objets_interactibles/objetMagnetique.png", 1, 400, 2, ["up"])
    camera.setObject(magneticObject5)
    all_sprites.add(magneticObject5)


    plateform6 = Obstacle(6900, 500, "assets/obstacles/plateforme.png",400,50)
    obstacles_group.add(plateform6)
    camera.setObject(plateform6)

    consomable3 = UpsideDown(7100, 480, "assets/objets_interactibles/consomable.png")
    camera.setObject(consomable3)
    all_sprites.add(consomable3)

    plateform7 = Obstacle(7900, 100, "assets/obstacles/plateforme.png",100,50)
    obstacles_group.add(plateform7)
    camera.setObject(plateform7)

    ore_vein5 = OreVein(7910, 20, "assets/objets_interactibles/Minerai_Lune.png", "crystal", 6)
    camera.setObject(ore_vein5)
    all_sprites.add(ore_vein5)


    # Création des groupes de sprites
    player = Player(obstacles_group)
    all_sprites.add(player)







    # Chargement de l'image de fond
    fond = pygame.image.load("assets/backgrounds/niveau2.png")
    earth = pygame.image.load("assets/planets/Terran.png")
    earth = pygame.transform.scale(earth, (earth.get_width()*4, earth.get_height()*4 ))
    sol = pygame.image.load("assets/backgrounds/sol.png")
    new_width = int((SCREEN_HEIGHT / fond.get_height()) * fond.get_width())
    fond = pygame.transform.scale(fond, (new_width, SCREEN_HEIGHT))
    sol = pygame.transform.scale(sol, (new_width, SCREEN_HEIGHT))
    background_surface = pygame.Surface((fond.get_width(), fond.get_height()))

    background_surface.blit(fond, (0, 0))
    background_surface.blit(earth, ((SCREEN_WIDTH/2) - earth.get_width(),(SCREEN_HEIGHT/2) - earth.get_height()))
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

    player.jump_power = -5

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

        # magneticObject.interact(player)
        magneticObject2.interact(player)
        magneticObject3.interact(player)
        magneticObject4.interact(player)
        magneticObject5.interact(player)
        magneticObject6.interact(player)



        is_consume2 = consomable3.consume(player)
        if is_consume2:
            all_sprites.remove(consomable3)

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
        show_ore_screen(screen, font, pygame.image.load("assets/objets_interactibles/Minerai_Lune.png"), player.numberOre  )

        # Dessinez l'obstacle
        obstacles_group.update()
        obstacles_group.draw(screen)

        # Affichage
        all_sprites.draw(screen)

        if(player.numberOre == 5):
            win_menu_2()

        if(ore_vein5.rect.x == 0 and player.numberOre != 5):
            death_menu(niveau2, True)

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
        player.is_dead = True
        if(player.is_dead == True):
            pygame.mixer.stop()
            pygame.mixer.Sound.play(player.death_sound)
            pygame.time.wait(1000)
            death_menu(niveau2, False)
        return True
# Boucle de jeu

