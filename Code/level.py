import pygame
from map import TILE_SIZE
from tile import Tile
from player import Player
from support import *
from enemy import *

class Level :
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = RPG_Camera()
        self.obstacle_sprites = pygame.sprite.Group()

        self.game_over = False          
        self.spawn_timer = 0
        self.spawn_interval = 1000
        self.player = None

        self.score = 0                 
        self.kill_count = 0
        self.attack_effect_group = pygame.sprite.Group()
        self.visible_sprites.attack_effect_group = self.attack_effect_group

        self.create_map()

    def add_score(self, points=100):
        self.score += points
        self.kill_count += 1
        print(f"Enemy defeated! +{points} points | Total Score: {self.score} | Kills: {self.kill_count}")

    def create_map(self):
        self.visible_sprites.empty()
        self.obstacle_sprites.empty()
        layouts = {
             'boundary' : import_csv_layout('../project/PNGs/map/CSVfile/map_floorblock.csv'),
        }
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1' :
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE
                        if style == 'boundary' :
                            Tile((x,y),[ self.obstacle_sprites],'invisible')

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == 'X':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], sprite_type='object')
                
                if cell == 'p':
                    self.player = Player((x, y), self.visible_sprites, self.obstacle_sprites)
                    self.player.level = self

        if self.player is None:
            self.player = Player((1150, 1000), self.visible_sprites, self.obstacle_sprites)
            self.player.level = self
            self.player.attack_effect_group = self.attack_effect_group

    def spawn_enemies(self, count=1):
        for _ in range(count):
            x = 200 + pygame.math.Vector2().x * (1920 - 400)   
            y = 200 + pygame.math.Vector2().y * (1280 - 400)
            spawn_x = 300 + (pygame.time.get_ticks() % 1400)
            spawn_y = 300 + (pygame.time.get_ticks() % 800)
            Enemy((spawn_x, spawn_y), self.visible_sprites, self.obstacle_sprites)

    def run(self, events):
        if self.game_over:
            self.show_game_over_screen(events)
            return
        
        self.attack_effect_group.update()

        for sprite in list(self.visible_sprites):
            if isinstance(sprite, Player):
                sprite.update(events)
            elif isinstance(sprite, Enemy):
                sprite.update(self.player)

        self.visible_sprites.custom_draw(self.player)
        current_enemies = len([s for s in self.visible_sprites if isinstance(s, Enemy)])

        if current_enemies < 6:
            self.spawn_timer += 16
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_enemies(1)
                self.spawn_timer = 0
        else:
            self.spawn_timer = 0

        self.draw_score()

    def show_game_over_screen(self, events):
        
        self.display_surface.fill((0, 0, 0))  

        font_title = pygame.font.SysFont("Arial", 80, bold=True)
        font_big = pygame.font.SysFont("Arial", 50)
        font_small = pygame.font.SysFont("Arial", 36)

       
        title_text = font_title.render("GAME OVER", True, (255, 0, 0))
        self.display_surface.blit(title_text, 
            (self.display_surface.get_width()//2 - title_text.get_width()//2, 150))

        
        score_text = font_big.render(f"FINAL SCORE: {self.score}", True, (255, 255, 255))
        kill_text = font_big.render(f"TOTAL KILLS: {self.kill_count}", True, (255, 255, 100))

        self.display_surface.blit(score_text, 
            (self.display_surface.get_width()//2 - score_text.get_width()//2, 280))
        self.display_surface.blit(kill_text, 
            (self.display_surface.get_width()//2 - kill_text.get_width()//2, 350))

        
        restart_text = font_small.render("Press R to Restart", True, (200, 200, 200))
        quit_text = font_small.render("Press Q to Quit", True, (200, 200, 200))

        self.display_surface.blit(restart_text, 
            (self.display_surface.get_width()//2 - restart_text.get_width()//2, 480))
        self.display_surface.blit(quit_text, 
            (self.display_surface.get_width()//2 - quit_text.get_width()//2, 530))

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:      
                    self.reset_level()
                elif event.key == pygame.K_q:    
                    pygame.quit()
                    exit()

    def reset_level(self):
        
        self.__init__()   
    
    def draw_score(self):
        font = pygame.font.SysFont("Arial", 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        kill_text = font.render(f"Kills: {self.kill_count}", True, (255, 255, 255))
        self.display_surface.blit(score_text, (20, 70))   
        self.display_surface.blit(kill_text, (20, 110))


class RPG_Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2
        self.floor_surf = pygame.image.load('../project/PNGs/map/mapAllLayers.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        
        self.offset = pygame.math.Vector2(
            player.rect.centerx - self.display_surface.get_width() // 2,
            player.rect.centery - self.display_surface.get_height() // 2
        )
        
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.copy()
            offset_rect.topleft -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)

        offset_rect = player.rect.copy()
        offset_rect.topleft -= self.offset
        self.display_surface.blit(player.image, offset_rect)
        
        player.draw_health_bar(self.display_surface)

        for effect in self.attack_effect_group:
            offset_rect = effect.rect.copy()
            offset_rect.topleft -= self.offset
            self.display_surface.blit(effect.image, offset_rect)
