import pygame

class AttackEffect(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups):
        super().__init__(groups)   
        
        self.direction = direction
        
        try:
            self.images = {
                'up':    pygame.image.load('PNGs/attack_up.png').convert_alpha(),
                'down':  pygame.image.load('PNGs/attack_down.png').convert_alpha(),
                'left':  pygame.image.load('PNGs/attack_left.png').convert_alpha(),
                'right': pygame.image.load('PNGs/attack_right.png').convert_alpha()
            }
            for key in self.images:
                self.images[key] = pygame.transform.scale(self.images[key], (64, 64))
        except:
            print(f"Attack image not found, using placeholder for {direction}")
            self.images = {
                'up': pygame.Surface((64, 64), pygame.SRCALPHA),
                'down': pygame.Surface((64, 64), pygame.SRCALPHA),
                'left': pygame.Surface((64, 64), pygame.SRCALPHA),
                'right': pygame.Surface((64, 64), pygame.SRCALPHA)
            }
            self.images['up'].fill((0, 255, 255, 200))
            self.images['down'].fill((255, 0, 255, 200))
            self.images['left'].fill((0, 200, 255, 200))
            self.images['right'].fill((255, 100, 255, 200))

        dir_map = {'front': 'down', 'back': 'up', 'left': 'left', 'right': 'right'}
        self.image = self.images.get(dir_map.get(direction, 'down'), self.images['down'])
        
        self.rect = self.image.get_rect(center=pos)
        
        self.lifetime = 2      
        self.frame = 0

    def update(self):
        self.frame += 1
        if self.frame >= self.lifetime:
            self.kill()         
