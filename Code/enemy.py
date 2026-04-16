import pygame
from map import TILE_SIZE



class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        self.image = pygame.transform.scale(
            pygame.image.load('../project/PNGs/enemy1.png').convert_alpha(), 
            (TILE_SIZE, TILE_SIZE)
        )
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-20, -20)

        self.obstacle_sprites = obstacle_sprites
        self.direction = pygame.math.Vector2()
        self.speed = 3
        self.health = 300
        self.alive = True

    def chase_player(self, player):
        if player is None or not hasattr(player, 'rect'):
            return
            
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        
        if abs(dx) > 5 or abs(dy) > 5:
            self.direction.x = 1 if dx > 0 else -1 if dx < 0 else 0
            self.direction.y = 1 if dy > 0 else -1 if dy < 0 else 0
            
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

    def move(self):
        
        if self.direction.magnitude() != 0:
            self.rect.x += self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed
               
    def take_damage(self, amount):
        self.health -= amount
        print(f"Enemy took {amount} damage! Remaining health: {self.health}")
        
        if self.health <= 0:
            self.alive = False
            
            
            for group in self.groups():
                for sprite in group:
                    
                    if hasattr(sprite, 'level') and hasattr(sprite.level, 'add_score'):
                        sprite.level.add_score(100)   
                        break
            
            self.kill()
            print("Enemy defeated!")

    def update(self, player):
        self.chase_player(player)
        self.move()
        self.attack_player(player)

    def attack_player(self, player):
        attack_distance = 50
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = (dx**2 + dy**2)**0.5

        if distance < attack_distance:
            player.take_damage(0.1)   
            print("Enemy attacked player!")
