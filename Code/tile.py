import pygame
from map import *
full_path = 'PNGs/pixel rock.png'

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type='object', surface=None):
        super().__init__(groups)
        
        if surface:
            self.image = surface
        else:
            raw_image = pygame.image.load(full_path).convert_alpha()
            self.image = pygame.transform.scale(raw_image, (TILE_SIZE, TILE_SIZE))
        
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -40)
        self.sprite_type = sprite_type
