from unit_circle import UnitCircle
import settings
import pygame

def show_func_values():
    values = [
        f'rad: {unit_circle.rad}',
        f'sin: {unit_circle.sin}',
        f'cos: {unit_circle.cos}',
        f'tan: {unit_circle.tan}',
        f'sec: {unit_circle.sec}',
        f'cosec: {unit_circle.cosec}',
        f'cotan: {unit_circle.cotan}'
    ]
    y_cord = 30
    for value in values:
        y_cord += 20
        text = font.render(
            value,
            True,
            settings.WHITE
        )
        text_rect = text.get_rect(
            topleft = (50, y_cord)
        )
        screen.blit(
            text,
            text_rect
        )

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
font = pygame.font.Font('assets/liberation_mono.ttf', settings.FONT_SIZE)

unit_circle = UnitCircle(screen, width, height, font)

degrees = 0
pause = False
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause

    if not pause:
        print(pause)
        degrees += 1
        if degrees > 360:
            degrees = 0
    
    screen.fill(settings.DARK_GREY)
    unit_circle.draw_axis()
    unit_circle.draw_circle()
    
    unit_circle.degrees_to_radians(degrees)
    unit_circle.calculate_trig_funcs()
    unit_circle.calculate_points()
    
    unit_circle.draw_hypotenuse()
    unit_circle.draw_angle(degrees)

    for func, color in settings.TRIG_FUNCS.items():
        unit_circle.draw_trig_func(func, color)
        unit_circle.draw_func_tags(func, color)

    show_func_values()
    
    unit_circle.show_degrees(degrees)
    unit_circle.draw_point()
    
    clock.tick(settings.FPS)
    pygame.display.update()