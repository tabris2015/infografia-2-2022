from numpy import rec
import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(screen, space, draw_options):
    screen.fill("white")
    space.debug_draw(draw_options)
    pygame.display.flip()


def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.elasticity = 0.9
    shape.friction = 0.4
    shape.color = (255, 0, 0, 100)
    space.add(body, shape)
    return shape

def create_boundaries(space, width, height):
    rects = [
        # center, size
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2), (20, height)],
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def run(screen, width, height):
    is_running = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    space = pymunk.Space()
    space.gravity = (0, 981)

    ball = create_ball(space, 30, 10)
    create_boundaries(space, width, height)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball.body.apply_impulse_at_local_point((10000, 0), (0, 0))

        draw(screen, space, draw_options)
        space.step(dt)
        clock.tick(fps)
    pygame.quit()

if __name__ == "__main__":
    run(screen, WIDTH, HEIGHT)