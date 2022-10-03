import pygame
import pymunk
from pymunk import Vec2d


class Bird:
    def __init__(self, distance, angle, x, y, space):
        self.hp = 20
        mass = 5
        radius = 12
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        body.position = x, y
        power = distance * 53
        impulse = power * Vec2d(1, 0)
        body.apply_impulse_at_local_point(impulse.rotated(angle))
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 0.8
        shape.friction = 1
        # capa para detectar colisiones
        shape.collision_type = 0
        space.add(body, shape)
        self.body = body
        self.shape = shape
        self.img = pygame.image.load("angry_birds/assets/img/red-bird3.png")
        self.rect = self.img.get_rect()

    def draw(self):
        screen = pygame.display.get_surface()
        x, y = self.shape.body.position
        self.rect.center = x, y
        screen.blit(self.img, self.rect)
        r = int(self.shape.radius)
        pygame.draw.circle(screen, pygame.Color("blue"), (x, y), r, 2)


class Pig:
    def __init__(self, x, y, space, hp=20):
        self.hp = hp
        mass = 5
        radius = 14
        inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        body = pymunk.Body(mass, inertia)
        body.position = x, y
        shape = pymunk.Circle(body, radius, (0, 0))
        shape.elasticity = 0.95
        shape.friction = 1
        shape.collision_type = 1
        space.add(body, shape)
        self.body = body
        self.shape = shape