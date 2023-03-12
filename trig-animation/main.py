import pygame
import settings
import utils

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
center = (width // 2, height // 2)

degrees = 0
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                exit()
    
    utils.draw_background(screen, width, height)
    
    degrees += 1
    if degrees > 360:
        degrees = 0
    utils.draw_point(screen, degrees, height, width)


    
    
    
    
    
    
    clock.tick(settings.FPS)
    pygame.display.update()