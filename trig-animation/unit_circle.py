from math import sin, cos, tan, radians
import pygame
import pygame.gfxdraw
import settings

class UnitCircle:

    def __init__(
        self,
        screen: object,
        width: int,
        height: int
    ):
        self.screen = screen
        self.width = width
        self.height = height
        self.point_pos = None

    def draw_axis(self):
        pygame.draw.line(
            self.screen,
            settings.WHITE,
            (0, self.height / 2),
            (self.width, self.height / 2)
        )
        pygame.draw.line(
            self.screen,
            settings.WHITE,
            (self.width / 2, 0),
            (self.width / 2, self.height)
        )
        
    def draw_circle(self):
        pygame.gfxdraw.aacircle(
            self.screen,
            self.width // 2,
            self.height // 2,
            settings.RADIUS * settings.SCALE,
            settings.WHITE,
        )

    def calculate_point(self, degrees):
        rad = radians(degrees)
        self.point_pos = (
            self.width / 2 + cos(rad) * settings.RADIUS * settings.SCALE,
            self.height / 2 - sin(rad) * settings.RADIUS * settings.SCALE
        )

    def draw_hypotenuse(self):
        pygame.draw.line(
            self.screen,
            settings.WHITE,
            (self.width / 2, self.height / 2),
            self.point_pos
        )

    def draw_sin(self):
        pygame.draw.line(
            self.screen,
            settings.RED,
            (self.point_pos[0], self.height / 2),
            self.point_pos,
            settings.LINE_WIDTH * settings.SCALE
        )

    def draw_cos(self):
        pygame.draw.line(
            self.screen,
            settings.GREEN,
            (self.width / 2, self.height / 2),
            (self.point_pos[0], self.height / 2),
            settings.LINE_WIDTH * settings.SCALE
        )

    def draw_angle(self, degrees):
        pygame.gfxdraw.arc(
            self.screen,
            self.width // 2,
            self.height // 2,
            10 * settings.SCALE,
            -degrees,
            0,
            settings.WHITE
        )
    
    
    
    def draw_point(self):
        pygame.draw.circle(
            self.screen,
            settings.WHITE,
            self.point_pos,
            5
        )