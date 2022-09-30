import math
import pygame
import pymunk
from pymunk import Vec2d
from pygame.sprite import Sprite
from pygame.locals import RLEACCEL


def flipy(y):
        return -y + 600

class Actor(Sprite):
    def __init__(self, pos_x, pos_y, angle, mass=10):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle
        self.mass = mass
        self.surf = pygame.image.load("sprites/assets/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.body = pymunk.Body()
        self.size = (40, 40)
        self.shape = pymunk.Poly.create_box(self.body, self.size)
        self.shape.friction = 0.5
        self.body.position = pos_x, pos_y
        self.body.angle = self.angle
        self.img_pos = None

    

    def update(self):
        self.img_pos = self.shape.body.position
        # self.img_pos = Vec2d(self.img_pos.x, flipy(self.img_pos.y))
        angle_degrees = math.degrees(self.shape.body.angle) + 180
        self.surf = pygame.transform.rotate(self.surf, angle_degrees)

        offset = Vec2d(*self.surf.get_size()) / 2
        self.img_pos = self.img_pos - offset
        print(self.img_pos)