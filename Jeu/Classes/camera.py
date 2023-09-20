import pygame

class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.objects = []

    def setObject(self, object):
        self.objects.append(object)

    def displace_objects(self, player):
        for object in self.objects:
            
            try:
                object.rect.centerx -= 1
                if object.rect.colliderect(player.rect):
                    player.rect.centerx -= 1
                
                    
            except AttributeError:
                object.get_rect().centerx -= 1
        
