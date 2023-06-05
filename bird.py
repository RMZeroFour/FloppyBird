import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Bird:
    def __init__(self, color):
        self.radius = 10
        self.x = SCREEN_WIDTH / 5
        self.y = SCREEN_HEIGHT / 2
        self.v = 0
        self.a = 0
        self.color = color

    def update(self, dt):
        self.a += 0.0001
        self.v += self.a * dt
        self.y += self.v * dt
        self.a = 0
       
    def process(self, event):
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.a += -0.02

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        