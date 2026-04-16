import pygame
from map import *
from level import *
from enemy import Enemy
from attackeffect import *

front = 'PNGs/IMG_5469.png'
left = 'PNGs/2_20260406180028.png'
right = 'PNGs/2_20260406180045.png'
back = 'PNGs/2_20260406180052.png'



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.images = {
            'front': pygame.transform.scale(pygame.image.load('PNGs/IMG_5469.png').convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            'back':  pygame.transform.scale(pygame.image.load('PNGs/2_20260406180052.png').convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            'left':  pygame.transform.scale(pygame.image.load('PNGs/2_20260406180028.png').convert_alpha(), (TILE_SIZE, TILE_SIZE)),
            'right': pygame.transform.scale(pygame.image.load('PNGs/2_20260406180045.png').convert_alpha(), (TILE_SIZE, TILE_SIZE))
        }
        
        self.image = self.images['front']
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-30, -15)
        self.obstacle_sprites = obstacle_sprites

        self.max_health = 50
        self.health = self.max_health
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length
        
        self.direction = pygame.math.Vector2()    
        self.speed = 5
       
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0
        self.can_attack = True
        self.attack_effect_group = None   
        
        self.current_direction = 'front'
        self.last_attack_direction = pygame.math.Vector2(0, 1)

    def input(self, events):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.current_direction = 'back'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.current_direction = 'front'
        else:
            self.direction.y = 0 

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.current_direction = 'right'

        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.current_direction = 'left'
        else:
            self.direction.x = 0 

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.can_attack:
                    self.attacking = True
                    self.attack_time = pygame.time.get_ticks()
                    self.can_attack = False
                    print('attack triggered once')

    def attack_enemies(self):
        if not self.attacking:
            return

        if self.direction.magnitude() != 0:
            self.last_attack_direction = self.direction.copy()
        
        attack_offset = self.last_attack_direction * 64
        attack_rect = self.rect.copy()
        attack_rect.center += attack_offset
        attack_rect.inflate_ip(30, 30)   

        for sprite in self.groups()[0]:  
            if isinstance(sprite, Enemy) and attack_rect.colliderect(sprite.rect):
                sprite.take_damage(25)    
                print(f"Hit enemy! Enemy health: {sprite.health}")

        if hasattr(self, 'attack_effect_group') and self.attack_effect_group is not None:
            effect_pos = self.rect.center + self.last_attack_direction * 45
            AttackEffect(effect_pos, self.current_direction, self.attack_effect_group)

    def take_damage(self, amount):
        self.health -= amount
        print(f"Player took {amount} damage! Remaining health: {self.health}")
        
        if self.health <= 0:
            print("Player died! Game Over")
    
            if hasattr(self, 'level'):  
                self.level.game_over = True
            else:
                pygame.quit()
                exit()
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking :
            if current_time - self.attack_time > self.attack_cooldown:
                
                self.attacking = False
                self.can_attack = True

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        if self.attacking == True:
                speed = 0
        else:
            self.hitbox.x += self.direction.x * speed 
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * speed 
            self.collision('vertical')
            self.rect.center = self.hitbox.center
        if self.direction.magnitude() != 0:           
            self.image = self.images[self.current_direction]
      
    def collision(self, direction):
        # x
        if direction == 'horizontal' :
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # to right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # to left
                        self.hitbox.left = sprite.hitbox.right
                      
        # y
        if direction == 'vertical' :
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self, events):
        self.input(events)
        self.move(self.speed)
        self.cooldowns()
        self.attack_enemies()
        
        if self.health <= 0:
            if hasattr(self, 'level'):
                self.level.game_over = True

    def draw_health_bar(self, surface):   
        current_health_length = int(self.health / self.health_ratio)
               
        pygame.draw.rect(surface, (50, 50, 50), (20, 20, self.health_bar_length, 25))          
        pygame.draw.rect(surface, (255, 0, 0), (20, 20, current_health_length, 25))
        pygame.draw.rect(surface, (255, 255, 255), (20, 20, self.health_bar_length, 25), 3)  
        font = pygame.font.SysFont("Arial", 20)
        health_text = font.render(f"HP: {int(self.health)} / {self.max_health}", True, (255, 255, 255))
        surface.blit(health_text, (230, 20))








