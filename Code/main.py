import pygame
from level import Level

pygame.init()
screen = pygame.display.set_mode((64*30, 64*20))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("My RPG Game")
level = Level()


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            running = False       

    screen.fill('black')
    
    level.run(events)
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()


