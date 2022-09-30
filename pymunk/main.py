import pygame 
from pygame.locals import K_SPACE
import random

import pymunk
from actor import Actor, flipy

# configuraciones
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class App:
    def __init__(self, screen_width, screen_height, bg_color=(0, 0, 0)):
        self.width = screen_width
        self.height = screen_height
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        # self.sprites es para renderizar
        self.sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.actor: Actor = None
        self.fps = 60
        self.dt = 1 / self.fps

        # fisica
        self.space = pymunk.Space()
        self.space.gravity = (0.0, 900.0)
        ### Static line
        self.static_lines = [
            pymunk.Segment(self.space.static_body, (11.0, 280.0), (407.0, 246.0), 0.0),
            pymunk.Segment(self.space.static_body, (407.0, 246.0), (407.0, 343.0), 0.0),
        ]
        for l in self.static_lines:
            l.friction = 0.1
        self.space.add(*self.static_lines)

    def add_actor(self, actor):
        self.actor = actor

    def update(self, keys):
        # sprite group
        self.screen.fill(self.bg_color)
        # dibujar todos los sprites
        for line in self.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            p1 = round(pv1.x), round(flipy(pv1.y))
            p2 = round(pv2.x), round(flipy(pv2.y))
            pygame.draw.lines(self.screen, pygame.Color("lightgray"), False, [p1, p2], 2)

        self.actor.update()
        self.screen.blit(self.actor.surf, self.actor.img_pos)
        self.space.step(self.dt)
        pygame.display.flip()
        # para mantener 30 frames por segundo
        self.clock.tick(30)

    def run(self):
        self.is_running = True
        # pygame.time.set_timer(self.ADD_ENEMY_EVENT, 250)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                # if event.type == pygame.KEYDOWN:
                #     if event.key == K_SPACE:
                #         self.player.shoot()

            keys = pygame.key.get_pressed()
            self.update(keys)

        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    # app.add_player(Player())
    app.add_actor(Actor(40, 0, 0))
    app.run()
