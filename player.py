import pygame
from pygame.math import Vector2

class Lemur(object):
    def __init__(self, screen):
        self.screen = screen

        self.fade = 0.95
        self.speed = 0.1

        self.x = 520
        self.y = 125

        self.srcr = "img/player-right.png"

        self.pos = Vector2(self.x, self.y)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def display(self, src):
        texture = pygame.image.load(src)
        self.screen.blit(texture, (self.pos.x,self.pos.y))

    def add_force(self, force):
        self.acc += force

    def move(self):
        press = pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            if self.pos.x>0:
                self.add_force(Vector2(-self.speed,0))
        if press[pygame.K_RIGHT]:
            if self.pos.x<1000:
                self.add_force(Vector2(self.speed,0))

        self.vel *= self.fade
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0
