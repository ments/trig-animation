from math import sin, cos, tan, radians
import pygame
import pygame.gfxdraw
import settings

class UnitCircle:

    def __init__(
        self,
        screen: object,
        width: int,
        height: int,
        font: object
    ):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = font

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

    def calculate_point(self, degrees: int):
        self.rad = radians(degrees)
        self.point_pos = (
            self.width / 2 + cos(self.rad) * settings.RADIUS * settings.SCALE,
            self.height / 2 - sin(self.rad) * settings.RADIUS * settings.SCALE
        )

    def draw_point(self):
        pygame.draw.circle(
            self.screen,
            settings.WHITE,
            self.point_pos,
            5
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
        text = self.font.render(
            'sin θ',
            True,
            settings.RED
        )
        text_rect = text.get_rect(
            center=(
                self.point_pos[0] + 30,
                self.height * 0.25 + self.point_pos[1] * 0.5
            )
        )
        self.screen.blit(
            text,
            text_rect
        )

    def draw_cos(self):
        pygame.draw.line(
            self.screen,
            settings.GREEN,
            (self.width / 2, self.height / 2),
            (self.point_pos[0], self.height / 2),
            settings.LINE_WIDTH * settings.SCALE
        )
        text = self.font.render(
            'cos θ',
            True,
            settings.GREEN
        )
        text_rect = text.get_rect(
            center=(
                self.width * 0.25 + self.point_pos[0] * 0.5,
                self.height / 2 + 15
            )
        )
        self.screen.blit(
            text,
            text_rect
        )

    def draw_angle(self, degrees: int):
        pygame.gfxdraw.arc(
            self.screen,
            self.width // 2,
            self.height // 2,
            settings.ANGLE_RADIUS * settings.SCALE,
            -degrees,
            0,
            settings.WHITE
        )
    
    def show_degrees(self, degrees: int):
        text = self.font.render(
            f'{degrees}°',
            True,
            settings.WHITE
        )
        text_rect = text.get_rect(
            center=(
                self.width / 2 + cos(self.rad / 2)* (settings.ANGLE_RADIUS + 8) * settings.SCALE,
                self.height / 2 - sin(self.rad / 2) * (settings.ANGLE_RADIUS + 8) * settings.SCALE
            )
        )
        self.screen.blit(
            text,
            text_rect
        )
        
    def draw_tan(self):
        pass