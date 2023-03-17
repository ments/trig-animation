from math import sin, cos, radians
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
        self.center = self.center_point()
    
    def center_point(self):
        return (self.width / 2, self.height / 2)

    def draw_axis(self):
        pygame.draw.line(
            self.screen,
            settings.WHITE,
            (0, self.center[1]),
            (self.width, self.center[1])
        )
        pygame.draw.line(
            self.screen,
            settings.WHITE,
            (self.center[0], 0),
            (self.center[0], self.height)
        )
        
    def draw_circle(self):
        pygame.gfxdraw.aacircle(
            self.screen,
            int(self.center[0]),
            int(self.center[1]),
            settings.RADIUS * settings.SCALE,
            settings.WHITE,
        )

    def calculate_point(self, degrees: int):
        self.rad = radians(degrees)
        self.point_pos = (
            self.center[0] + cos(self.rad) * settings.RADIUS * settings.SCALE,
            self.center[1] - sin(self.rad) * settings.RADIUS * settings.SCALE
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
            self.center,
            self.point_pos
        )

    def draw_sin(self):
        pygame.draw.line(
            self.screen,
            settings.RED,
            (self.point_pos[0], self.center[1]),
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
            (self.center[0], self.point_pos[1]),
            self.point_pos,
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
                self.point_pos[1] + 15
            )
        )
        self.screen.blit(
            text,
            text_rect
        )

    def draw_angle(self, degrees: int):
        pygame.gfxdraw.arc(
            self.screen,
            int(self.center[0]),
            int(self.center[1]),
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
                self.center[0] + cos(self.rad / 2)* (settings.ANGLE_RADIUS + 8) * settings.SCALE,
                self.center[1] - sin(self.rad / 2) * (settings.ANGLE_RADIUS + 8) * settings.SCALE
            )
        )
        self.screen.blit(
            text,
            text_rect
        )
        
    def draw_tan(self):
        self.tan_point = self.center[0] + (1 / cos(self.rad)) * settings.RADIUS * settings.SCALE
        pygame.draw.line(
            self.screen,
            settings.YELLOW,
            self.point_pos,
            (self.tan_point, self.center[1]),
            settings.LINE_WIDTH * settings.SCALE
        )
        text = self.font.render(
            'tan θ',
            True,
            settings.YELLOW
        )
        tag_pos = 30
        if self.tan_point < self.center[0]:
            tag_pos = -tag_pos
        text_rect = text.get_rect(
            center=(
                self.point_pos [0] * 0.5 + self.tan_point * 0.5 + tag_pos,
                self.center[1] * 0.5 + self.point_pos[1] * 0.5
            )
        )
        self.screen.blit(
            text,
            text_rect
        )

    def draw_sec(self):
        pygame.draw.line(
            self.screen,
            settings.ORANGE,
            self.center,
            (self.tan_point, self.center[1]),
            settings.LINE_WIDTH * settings.SCALE
        )
        text = self.font.render(
            'sec θ',
            True,
            settings.ORANGE
        )
        text_rect = text.get_rect(
            center=(
                self.center[0] * 0.5 + self.tan_point * 0.5,
                self.center[1] + 15
            )
        )
        self.screen.blit(
            text,
            text_rect
        )
    
    def draw_cosec(self):
        if sin(self.rad) != 0:
            self.cotan_point = self.center[1] - (1 / sin(self.rad)) * settings.RADIUS * settings.SCALE
        pygame.draw.line(
            self.screen,
            settings.PINK,
            self.center,
            (self.center[0], self.cotan_point),
            settings.LINE_WIDTH * settings.SCALE
        )
        text = self.font.render(
            'cosec θ',
            True,
            settings.PINK
        )
        text_rect = text.get_rect(
            center=(
                self.center[0] - 40,
                self.center[1] * 0.5 + self.cotan_point * 0.5
            )
        )
        self.screen.blit(
            text,
            text_rect
        )
    
    def draw_cotan(self):
        pygame.draw.line(
            self.screen,
            settings.LIGHT_BLUE,
            self.point_pos,
            (self.center[0], self.cotan_point),
            settings.LINE_WIDTH * settings.SCALE
        )
        text = self.font.render(
            'cotan θ',
            True,
            settings.LIGHT_BLUE
        )
        text_rect = text.get_rect(
            center=(
                self.center[0] * 0.5 + self.point_pos[0] * 0.5,
                self.point_pos[1] * 0.5 + self.cotan_point * 0.5
            )
        )
        self.screen.blit(
            text,
            text_rect
        )