import pymunk
from pymunk import Vec2d
import pygame
import math


class Rectangle:
    def __init__(self, pos, file, space):
        self.img = pygame.image.load(file).convert_alpha()
        size = self.img.get_size()
        moment = 1000
        mass = 5
        body = pymunk.Body(mass, moment)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.color = (0, 0, 255, 10)
        shape.friction = 0.5
        shape.collision_type = 2
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def draw(self):
        screen = pygame.display.get_surface()
        x, y = self.body.position
        angle = self.body.angle

        img = pygame.transform.rotate(self.img, math.degrees(angle))
        w, h = img.get_size()
        x = x - w//2
        y = y - h//2
        screen.blit(img, (x, y))
