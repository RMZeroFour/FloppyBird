import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Bird:
    def __init__(self, color):
        self.radius = 15
        self.x = SCREEN_WIDTH / 5
        self.y = SCREEN_HEIGHT / 2
        self.v = 0
        self.color = color

    def update(self, dt):
        G = 2000
        self.v += G * dt
        self.v = max(min(self.v, 500), -500)
        self.y += self.v * dt
       
    def process(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.v -= 1000

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        