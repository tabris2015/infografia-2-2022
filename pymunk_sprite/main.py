import math
import random
from typing import List

import pygame

import pymunk
from pymunk.pygame_util import DrawOptions
from pymunk import Vec2d


class PhysicsActor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surf = pygame.image.load("assets/ball3.png").convert_alpha()
        # self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (80, 80))
        self.rect = self.surf.get_rect()
        self.speed = 5
        self.mass = 5
        moment = pymunk.moment_for_circle(self.mass, 0, 40, (0, 0))
        self.body = pymunk.Body(self.mass, moment)
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, 40)
        self.shape.mass = self.mass
        self.shape.elasticity = 0.6
        self.friction = 1
        self.shape.color = (255, 0, 0, 1)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.shape.body.apply_force_at_world_point((-5000, 0), (0, 0))
        if keys[pygame.K_RIGHT]:
            self.shape.body.apply_force_at_world_point((5000, 0), (0, 0))

        self.rect.centerx = self.body.position.x
        self.rect.centery = self.body.position.y
        # self.surf = pygame.transform.rotate(self.surf, math.degrees(self.body.angle) + 180)

    def jump(self):
        self.body.apply_impulse_at_world_point((0, -1000), (0, 0))

class App:
    def __init__(self, screen_width, screen_height, bg_color=(0, 0, 0)):
        self.width = screen_width
        self.height = screen_height
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        self.sprites = pygame.sprite.Group()
        self.player: PhysicsActor = None
        self.clock = pygame.time.Clock()
        self.fps = 30
        # phys
        self.space = pymunk.Space()
        self.space.gravity = Vec2d(0, 980)

        self.dt = 1 / self.fps
        self.static_lines = []
        self.draw_options = DrawOptions(self.screen)

    def add_walls(self):
        rects = [
            # center, size
            [(self.width / 2, self.height - 10), (self.width, 20)],
            [(self.width / 2, 10), (self.width, 20)],
            [(10, self.height / 2), (20, self.height)],
            [(self.width - 10, self.height / 2), (20, self.height)],
        ]

        for pos, size in rects:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = pos
            shape = pymunk.Poly.create_box(body, size)
            shape.elasticity = 0.4
            shape.friction = 1
            self.space.add(body, shape)


    def add_lines(self):
        self.static_lines = [
            pymunk.Segment(self.space.static_body, (11.0, 280.0), (407.0, 346.0), 1.0),
            pymunk.Segment(self.space.static_body, (407.0, 346.0), (407.0, 147.0), 1.0),
        ]
        for line in self.static_lines:
            line.elasticity = 0.5
            line.friction = 0.5

        self.space.add(*self.static_lines)

    def draw_lines(self):
        # print("draw lines")
        for line in self.static_lines:
            body = line.body
            p1 = body.position + line.a.rotated(body.angle)
            p2 = body.position + line.b.rotated(body.angle)

            pygame.draw.lines(self.screen, pygame.Color("lightgray"), False, [p1, p2], 2)

    def add_player(self, player: PhysicsActor):
        self.player = player
        self.sprites.add(player)
        self.space.add(self.player.body, self.player.shape)

    def update(self, keys):
        self.player.update(keys)
        self.screen.fill(self.bg_color)
        self.space.debug_draw(self.draw_options)
        # draw lines
        self.draw_lines()
        # draw sprites
        for sprite in self.sprites:
            self.screen.blit(sprite.surf, sprite.rect)

        pygame.display.flip()
        self.space.step(self.dt)
        self.clock.tick(self.fps)

    def run(self):
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.body.apply_impulse_at_world_point((0, -1000), (0, 0))
            keys = pygame.key.get_pressed()
            self.update(keys)

        pygame.quit()

def flipy(y):
    """Small hack to convert chipmunk physics to pygame coordinates"""
    return -y + 600


def main():

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    running = True

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = Vec2d(0.0, -900.0)

    ## logo
    logo_img = pygame.image.load("assets/pymunk_logo_googlecode.png")
    logos: List[pymunk.Shape] = []

    ### Static line
    static_lines = [
        pymunk.Segment(space.static_body, (11.0, 280.0), (407.0, 246.0), 0.0),
        pymunk.Segment(space.static_body, (407.0, 246.0), (407.0, 343.0), 0.0),
    ]
    for l in static_lines:
        l.friction = 0.1
    space.add(*static_lines)

    ticks_to_next_spawn = 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.image.save(screen, "using_sprites.png")

        ticks_to_next_spawn -= 1
        if ticks_to_next_spawn <= 0:
            ticks_to_next_spawn = 100
            x = random.randint(20, 400)
            y = 500
            angle = random.random() * math.pi
            vs = [(-23, 26), (23, 26), (0, -26)]
            mass = 10
            moment = pymunk.moment_for_poly(mass, vs)
            body = pymunk.Body(mass, moment)
            shape = pymunk.Poly(body, vs)
            shape.friction = 0.5
            shape.elasticity = 0.6
            body.position = x, y
            body.angle = angle

            space.add(body, shape)
            logos.append(shape)

        ### Update physics
        dt = 1.0 / 60.0
        for x in range(1):
            space.step(dt)

        ### Draw stuff
        screen.fill(pygame.Color("black"))

        for logo_shape in logos:
            # image draw
            p = logo_shape.body.position
            p = Vec2d(p.x, flipy(p.y))

            # we need to rotate 180 degrees because of the y coordinate flip
            angle_degrees = math.degrees(logo_shape.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(logo_img, angle_degrees)

            offset = Vec2d(*rotated_logo_img.get_size()) / 2
            p = p - offset

            screen.blit(rotated_logo_img, (round(p.x), round(p.y)))

            # debug draw
            ps = [
                p.rotated(logo_shape.body.angle) + logo_shape.body.position
                for p in logo_shape.get_vertices()
            ]
            ps = [(round(p.x), round(flipy(p.y))) for p in ps]
            ps += [ps[0]]
            pygame.draw.lines(screen, pygame.Color("red"), False, ps, 1)

        for line in static_lines:
            body = line.body

            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = round(pv1.x), round(flipy(pv1.y))
            p2 = round(pv2.x), round(flipy(pv2.y))
            pygame.draw.lines(screen, pygame.Color("lightgray"), False, [p1, p2], 2)

        ### Flip screen
        pygame.display.flip()
        clock.tick(50)
        pygame.display.set_caption("fps: " + str(clock.get_fps()))


if __name__ == "__main__":
    # main()
    app = App(800, 800)
    app.add_player(PhysicsActor(40, 10))
    app.add_lines()
    app.add_walls()
    app.run()