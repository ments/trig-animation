from math import sin, cos, tan, radians
import pygame
import pygame.gfxdraw
import settings

def draw_background(screen, width, height):
    screen.fill(settings.DARK_GREY)
    pygame.draw.line(
        screen,
        settings.WHITE,
        (0, height / 2),
        (width, height / 2)
    )
    pygame.draw.line(
        screen,
        settings.WHITE,
        (width / 2, 0),
        (width / 2, height)
    )
    pygame.gfxdraw.aacircle(
        screen,
        width // 2,
        height // 2,
        settings.RADIUS * settings.SCALE,
        settings.WHITE,
    )

def draw_point(screen, degrees, height, width):
    rad = radians(degrees)
    point_pos = (
        width / 2 + cos(rad) * settings.RADIUS * settings.SCALE,
        height / 2 - sin(rad) * settings.RADIUS * settings.SCALE
    )
    pygame.draw.circle(
        screen,
        settings.WHITE,
        point_pos,
        5,
    )