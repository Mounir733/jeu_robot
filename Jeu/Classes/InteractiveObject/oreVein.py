import pygame
from Classes.InteractiveObject.interactiveObject import InteractiveObject

class OreVein(InteractiveObject):
    def __init__(self, x, y, sprite_image, ore_name, collecting_hit):
        super().__init__(x, y, sprite_image)
        self.ore_name = ore_name
        self.collecting_hit = collecting_hit
        self.collectable = True

    def interact(self, player):
        if self.collecting_hit > 0 and self.collectable and player.attack_counter == 1:
            self.collecting_hit -= 1
        elif self.collecting_hit == 0:
            self.collectable = False
            self.collecting_hit -= 1
            player.numberOre += 1
    def link(self,player,all_sprites,keys):
        if keys[pygame.K_e]:
            if player.rect.colliderect(self.rect):
                self.interact(player)

            if self.collectable == False:
                all_sprites.remove(self)
        
