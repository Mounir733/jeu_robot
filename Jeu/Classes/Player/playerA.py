import pygame

class Player(pygame.sprite.Sprite):
    _SCREEN_WIDTH = 1024
    _SCREEN_HEIGHT = 768

    def __init__(self):
        super().__init__()
        self.images_right = []  # Liste pour stocker les images d'animation orientées vers la droite
        self.images_left = []   # Liste pour stocker les images d'animation orientées vers la gauche
        self.image_index = 0    # Indice de l'image actuelle
        self.load_images()      # Chargez les images dans les listes
        self.image = self.images_right[self.image_index]  # Par défaut, utilisez les images orientées vers la droite
        self.rect = self.image.get_rect()
        self.rect.center = (self._SCREEN_WIDTH // 2, self._SCREEN_HEIGHT // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.3
        self.jump_power = -10
        self.speed = 2.5
        self.on_ground = False
        self.animation_delay = 100  # Délai entre les images en millisecondes
        self.last_animation_time = pygame.time.get_ticks()  # Temps du dernier changement d'image
        self.direction = "right"  # Par défaut, le personnage regarde vers la droite


    def load_images(self):
            idle_image = pygame.image.load("assets/robots/OrangeRobot/SeparetedImages/OrangeRobot1.png")
            idle_image = pygame.transform.scale(idle_image, (100, 100))  # Redimensionnez à la taille souhaitée
            self.images_right.append(idle_image)
            self.images_left.append(pygame.transform.flip(idle_image, True, False))
            
            # Chargez toutes les images d'animation et ajoutez-les à la liste
            for i in range(6, 12):  # Supposons que vous ayez 3 images numérotées
                image = pygame.image.load(f"assets/robots/OrangeRobot/SeparetedImages/OrangeRobot{i}.png")  # Remplacez par vos noms d'image
                image = pygame.transform.scale(image, (100, 100))  # Redimensionnez à la taille souhaitée
                self.images_right.append(image)
                # Inversez et ajoutez les images orientées vers la gauche
                image_left = pygame.transform.flip(image, True, False)
                self.images_left.append(image_left)
    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False  # Définir le joueur comme étant en l'air

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -self.speed
            self.direction = "left"  # Définissez la direction vers la gauche
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = self.speed
            self.direction = "right"  # Définissez la direction vers la droite
        else:
            self.velocity.x = 0

        if keys[pygame.K_SPACE]:  # Gestion de la touche Espace pour le saut
            self.jump()

        if not self.on_ground:
            self.velocity.y += self.gravity
        else:
            self.velocity.y = 0

        now = pygame.time.get_ticks()
        if now - self.last_animation_time > self.animation_delay:
            self.last_animation_time = now

            if self.velocity.x != 0:
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

        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self._SCREEN_WIDTH:
            self.rect.right = self._SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > self._SCREEN_HEIGHT:
            self.rect.bottom = self._SCREEN_HEIGHT
            self.on_ground = True  # Le joueur touche le sol
