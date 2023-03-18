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
        self.center = (self.width / 2, self.height / 2)

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
            settings.WHITE
        )

    def degrees_to_radians(self, degrees: int):
        self.rad = round(radians(degrees), 4)

    def calculate_trig_funcs(self):
        self.sin = round(sin(self.rad), 4)
        self.cos = round(cos(self.rad), 4)
        if self.cos != 0:
            self.tan = round(self.sin / self.cos, 4)
            self.sec = round(1 / self.cos, 4)
        if self.sin != 0:
            self.cosec = round(1 / self.sin, 4)
            self.cotan = round(self.cos / self.sin, 4)
    
    def calculate_points(self):
        cos_x = self.center[0] + self.cos * settings.RADIUS * settings.SCALE
        sin_y = self.center[1] - self.sin * settings.RADIUS * settings.SCALE
        self.point_pos = (cos_x, sin_y)
        self.tan_point = self.center[0] + self.sec * settings.RADIUS * settings.SCALE
        self.cotan_point = self.center[1] - self.cosec * settings.RADIUS * settings.SCALE

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

    def draw_trig_func(self, func: str, color: tuple):
        start, end = self.line_points(func)
        pygame.draw.line(
            self.screen,
            color,
            start,
            end,
            settings.LINE_WIDTH * settings.SCALE
        )
    
    def draw_func_tags(self, func: str, color: tuple):
        center_point = self.func_tag_center(func)
        text = self.font.render(
            f'{func} θ',
            True,
            color
        )
        text_rect = text.get_rect(
            center=center_point
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

    def line_points(self, func: str):
        if func == 'sin':
            return (self.point_pos[0], self.center[1]), self.point_pos
        if func == 'cos':
            return (self.center[0], self.point_pos[1]), self.point_pos
        if func == 'tan':
            return self.point_pos, (self.tan_point, self.center[1])
        if func == 'sec':
            return self.center, (self.tan_point, self.center[1])
        if func == 'cosec':
            return self.center, (self.center[0], self.cotan_point)
        if func == 'cotan':
            return self.point_pos, (self.center[0], self.cotan_point)

    def func_tag_center(self, func: str):
        if func == 'sin':
            return self.point_pos[0] + 30, self.height * 0.25 + self.point_pos[1] * 0.5
        if func == 'cos':
            return self.width * 0.25 + self.point_pos[0] * 0.5, self.point_pos[1] + 15
        if func == 'tan':
            tag_pos = 30
            if self.tan_point < self.center[0]:
                tag_pos = -tag_pos
            return self.point_pos [0] * 0.5 + self.tan_point * 0.5 + tag_pos, self.center[1] * 0.5 + self.point_pos[1] * 0.5
        if func == 'sec':
            return self.center[0] * 0.5 + self.tan_point * 0.5, self.center[1] + 15
        if func == 'cosec':
            return self.center[0] - 40, self.center[1] * 0.5 + self.cotan_point * 0.5
        if func == 'cotan':
            tag_pos = 50
            if self.point_pos[0] < self.center[0]:
                tag_pos = -tag_pos
            return self.center[0] * 0.5 + self.point_pos[0] * 0.5 + tag_pos, self.point_pos[1] * 0.5 + self.cotan_point * 0.5