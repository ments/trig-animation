from unit_circle import UnitCircle
import settings
import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
unit_circle = UnitCircle(screen, width, height)

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
    
    screen.fill(settings.DARK_GREY)
    unit_circle.draw_axis()
    unit_circle.draw_circle()
    
    degrees += 1
    if degrees > 360:
        degrees = 0
    unit_circle.calculate_point(degrees)

    unit_circle.draw_angle(degrees)
    unit_circle.draw_hypotenuse()
    unit_circle.draw_sin()
    unit_circle.draw_cos()



   
    
    
    
    unit_circle.draw_point()
    
    clock.tick(settings.FPS)
    pygame.display.update()