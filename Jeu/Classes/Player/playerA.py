import pygame

class Player(pygame.sprite.Sprite):
    _SCREEN_WIDTH = 1024
    _SCREEN_HEIGHT = 768

    def __init__(self, obstacles_group):
        super().__init__()
        self.images_right = []  # Liste pour stocker les images d'animation orientées vers la droite
        self.images_left = []   # Liste pour stocker les images d'animation orientées vers la gauche
        self.images_jump = []   # Liste pour stocker les images d'animation de saut
        self.image_index = 0    # Indice de l'image actuelle

        # Attributs pour gérer l'animation de mort
        self.images_death = []  # Liste des images de l'animation de mort
        self.death_image_index = 0  # Index de l'image de l'animation de mort
        self.is_dead = False  # Booléen pour déterminer si le joueur est mort
        self.death_animation_speed = 0.2  # Vitesse de l'animation de mort

        # Compteur de temps pour l'animation de mort
        self.death_animation_timer = 0

        self.load_images()     # Chargez les images dans les listes
        self.image = self.images_right[self.image_index]  # Par défaut, utilisez les images orientées vers la droite
        self.rect = self.image.get_rect()
        # self.rect.width = 30  Largeur réduite à 30 pixels
        self.rect.center = (self._SCREEN_WIDTH // 2, self._SCREEN_HEIGHT // 2)
        self.numberOre = 0


        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.04
        self.jump_power = -3
        self.speed = 1.5
        self.on_ground = False
        self.animation_delay = 100  # Délai entre les images en millisecondes
        self.last_animation_time = pygame.time.get_ticks()  # Temps du dernier changement d'image
        self.direction = "right"  # Par défaut, le personnage regarde vers la droite
        # Ajoutez ces deux attributs pour suivre la position précédente
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.obstacles_group = obstacles_group  # Passer le groupe d'obstacles à la classe Player
        self.on_platforme = False
        # Sons des actions du joueur
        self.step_sound = pygame.mixer.Sound("assets/sound/footsteps1.mp3")
        self.jump_sound = pygame.mixer.Sound("assets/sound/jump1.wav")
        self.attack_sound = pygame.mixer.Sound("assets/sound/attack.mp3")
        self.death_sound = pygame.mixer.Sound("assets/sound/death.mp3")
        self.jump_sound.set_volume(0.5)



        # Attributs pour gérer l'animation d'attaque
        self.image_index_attack = 0
        self.attacking = False
        self.attack_counter = 0  # Compteur pour la temporisation de l'animation
        



    def load_images(self):
            idle_image = pygame.image.load("assets/robots/OrangeRobot/SeparetedImages/OrangeRobot1.png")
            idle_image = pygame.transform.scale(idle_image, (70, 70))  # Redimensionnez à la taille souhaitée
            self.images_right.append(idle_image)
            self.images_left.append(pygame.transform.flip(idle_image, True, False))
            
            # Chargez toutes les images d'animation et ajoutez-les à la liste
            for i in range(6, 12):  # Supposons que vous ayez 3 images numérotées
                image = pygame.image.load(f"assets/robots/OrangeRobot/SeparetedImages/OrangeRobot{i}.png")  # Remplacez par vos noms d'image
                image = pygame.transform.scale(image, (70, 70))  # Redimensionnez à la taille souhaitée
                self.images_right.append(image)
                # Inversez et ajoutez les images orientées vers la gauche
                image_left = pygame.transform.flip(image, True, False)
                self.images_left.append(image_left)

                    # Chargez les images d'animation de saut (images 12 à 15)
            for i in range(12, 16):
                image_jump = pygame.image.load(f"assets/robots/OrangeRobot/SeparetedImages/OrangeRobot{i}.png")
                image_jump = pygame.transform.scale(image_jump, (70, 70))  # Redimensionnez à la taille souhaitée
                self.images_jump.append(image_jump)

            # Chargez les images pour l'animation d'attaque à droite
            self.images_attack_right = [pygame.transform.scale(pygame.image.load(f"assets/robots/OrangeRobot/SeparetedImages/OrangeRobot{i}.png"),(70,70)) for i in range(20, 28)]
            # Chargez les images pour l'animation d'attaque à gauche (en inversant horizontalement)
            self.images_attack_left = [pygame.transform.flip(img, True, False) for img in self.images_attack_right]
            # Chargez les images de l'animation de mort
            for i in range(29, 34):
                image_death = pygame.image.load(f"assets/robots/OrangeRobot/SeparetedImages/OrangeRobot{i}.png")
                image_death = pygame.transform.scale(image_death, (70, 70))  # Redimensionnez à la taille souhaitée
                self.images_death.append(image_death)       
  
    def attack(self):
        # Cette méthode est appelée lorsque le joueur attaque
        self.attacking = True
        self.image_index_attack = 0
        # Déterminez quelles images d'attaque utiliser en fonction de la direction
        if self.direction == "right":
            self.attack_images = self.images_attack_right
        else:
            self.attack_images = self.images_attack_left

    def jump(self):
        if self.on_ground:
            pygame.mixer.Sound.play(self.jump_sound)
            self.velocity.y = self.jump_power
            self.on_ground = False  # Définir le joueur comme étant en l'air

    def update(self):
                # Sauvegardez la position actuelle comme position précédente
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(self.step_sound)
            self.velocity.x = -self.speed
            self.direction = "left"  # Définissez la direction vers la gauche
        elif keys[pygame.K_RIGHT]:
            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(self.step_sound)
            self.velocity.x = self.speed
            self.direction = "right"  # Définissez la direction vers la droite
        else:
            self.step_sound.stop()
            self.velocity.x = 0

        if keys[pygame.K_SPACE]:  # Gestion de la touche Espace pour le saut
            self.jump()
        if keys[pygame.K_e]:
            channel = self.attack_sound.get_num_channels()
            if not self.attacking:
                pygame.mixer.Sound.play(self.attack_sound)
            self.attack()  # Appel de la méthode d'attaque lorsque la touche "e" est pressée


        if not self.on_ground:
            self.velocity.y += self.gravity
        else:
            self.velocity.y = 0



        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self._SCREEN_WIDTH:
            self.rect.right = self._SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self._SCREEN_HEIGHT - 90:
            self.rect.bottom = self._SCREEN_HEIGHT
            self.on_ground = True  # Le joueur touche le sol

        # Si le joueur est en collision avec l'obstacle uniquement sur l'axe vertical, réinitialisez sa position horizontale
        collisions = pygame.sprite.spritecollide(self, self.obstacles_group, False)
        if collisions:
            self.rect.x = self.prev_x
            self.on_ground = True

        if not collisions and self.rect.bottom < self._SCREEN_HEIGHT - 90:
            self.on_ground = False


        if self.rect.bottom > self._SCREEN_HEIGHT - 90:
            self.on_ground = True  # Le joueur touche le sol
            self.rect.bottom = self._SCREEN_HEIGHT - 90


        if self.attacking:
            self.attack_counter += 1  # Incrémente le compteur de temporisation
            # Si le compteur a atteint un seuil, changez l'image
            if self.attack_counter >= 10:  # Vous pouvez ajuster ce seuil pour contrôler la vitesse de l'animation
                self.attack_counter = 0  # Réinitialisez le compteur
                self.image_index_attack += 1
                if self.image_index_attack >= len(self.attack_images) - 1:
                    self.attacking = False  # Arrêtez l'animation une fois qu'elle est terminée
            # Changer d'image pour l'animation d'attaque
            self.image = self.attack_images[self.image_index_attack]
        else:

            now = pygame.time.get_ticks()
            if now - self.last_animation_time > self.animation_delay:
                self.last_animation_time = now

                if self.on_ground == False:
                    # Animation de saut
                    self.image_index += 1
                    if self.image_index < len(self.images_jump):
                        if self.direction == "right":
                            self.image = self.images_jump[self.image_index]
                        else:
                            self.image = pygame.transform.flip(self.images_jump[self.image_index], True, False)
                    else:
                        self.image_index = len(self.images_jump) - 1
                elif self.velocity.x != 0:
                    self.image_index += 1
                    if self.image_index >= len(self.images_right):
                        self.image_index = 0
                    if self.direction == "right":
                        self.image = self.images_right[self.image_index]
                    else:
                        self.image = self.images_left[self.image_index]

                else:
                    self.image_index = 0
                    # Si le personnage ne se déplace pas, utilisez l'image actuelle
                    if self.direction == "right":
                        self.image = self.images_right[self.image_index]
                    else:
                        self.image = self.images_left[self.image_index]
                
        if self.is_dead:
            # Si le joueur est mort, jouez l'animation de mort lentement
            self.death_animation_timer += 1  # Ajustez la valeur pour ralentir ou accélérer l'animation

            if self.death_image_index < len(self.images_death):
                # Affichez l'image de l'animation de mort correspondante
                self.image = self.images_death[self.death_image_index]

                # Vérifiez si l'animation de mort est prête pour l'image suivante
                if self.death_animation_timer >= self.death_animation_speed:
                    self.death_image_index += 1
                    self.death_animation_timer = 0
            else:
                # L'animation de mort est terminée
                self.is_dead = False
                # Réinitialisez l'animation
                self.death_image_index = 0
                self.death_animation_timer = 0
            
            









            
