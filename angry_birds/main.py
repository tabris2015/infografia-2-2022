import math
import pymunk
from pymunk import Vec2d
from pymunk.pygame_util import DrawOptions
import pygame

from characters import Bird
from world import Rectangle
from utils import vector, unit_vector


class App:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.bg_color = (0, 0, 0)
        pygame.init()
        pygame.font.init()
        font=pygame.font.get_default_font()              
        self.fontsys=pygame.font.SysFont(font, 30)           
        self.text_1 = self.fontsys.render("Score: ", 2, (0,50,0)) 
        self.screen = pygame.display.set_mode((w, h))
        self.bg_img = pygame.image.load("angry_birds/assets/img/background3.png").convert_alpha()
        self.sling_image = pygame.image.load("angry_birds/assets/img/sling-3.png").convert_alpha()
        self.redbird = pygame.image.load("angry_birds/assets/img/red-bird3.png").convert_alpha()
        self.is_running = False
        self.clock = pygame.time.Clock()
        self.fps = 50
        self.dt = 1 / self.fps
        self.space = pymunk.Space()
        self.space.gravity = (0, 700)
        self.mouse_distance = 0
        self.mouse_pressed = False
        self.angle = 0
        self.x_mouse, self.y_mouse = 0, 0
        self.x_sling, self.y_sling = 0, 0
        self.x_sling2, self.y_sling2 = 160, 450
        self.rope_length = 90
        self.score = 0
        self.text_score = self.fontsys.render(str(self.score), 2, (0, 255, 0))
        self.beams = []
        self.columns = []
        self.birds = []
        # capas: (capa1, capa2) ---     (a, b)
        self.space.add_collision_handler(0, 2).post_solve = self.col_bird_wood
        self.init_floor()
        self.draw_options = DrawOptions(self.screen)
        self.beams = [
            Rectangle((980, 500), "angry_birds/assets/img/beam.png", self.space),
            Rectangle((980, 300), "angry_birds/assets/img/beam.png", self.space),
        ]
        self.columns = [
            Rectangle((950, 550), "angry_birds/assets/img/column.png", self.space),
            Rectangle((1010, 550), "angry_birds/assets/img/column.png", self.space),
            Rectangle((950, 350), "angry_birds/assets/img/column.png", self.space),
            Rectangle((1010, 350), "angry_birds/assets/img/column.png", self.space),
        ]
        # self.barra = Rectangle((800, 550), "assets/img/column.png", self.space)

    def init_floor(self):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        line = pymunk.Segment(body, (0, self.height - 20), (1200, self.height - 20), 0)
        line.elasticity = 0.90
        line.friction = 1
        line.collision_type = 3

        body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
        line2 = pymunk.Segment(body2, (1200, self.height - 20), (1200, 0), 0)
        line2.elasticity = 0.90
        line2.friction = 1
        line2.collision_type = 3

        self.space.add(body, line)
        self.space.add(body2, line2)

    # def init_woods(self):
    #     for p in [(950, 550), (1010, self.height - 180), (950, self.height - 320), (1010, self.height - 320)]:
    #         self.columns.append(Rectangle(p, "assets/img/column.png", self.space))
    #     for p in [(980, self.height - 240), (980, self.height - 150)]:
    #         self.beams.append(Rectangle(p, "assets/img/beam.png", self.space))

    def col_bird_wood(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data):
        to_remove = []

        if arbiter.total_impulse.length > 1100:
            a, b = arbiter.shapes
            for beam in self.beams:
                if b == beam.shape:
                    to_remove.append(beam)
            for column in self.columns:
                if b == column.shape:
                    to_remove.append(column)

            for item in to_remove:
                if item in self.beams:
                    self.beams.remove(item)
                elif item in self.columns:
                    self.columns.remove(item)
            space.remove(b, b.body)
            self.score += 100

    def draw_score(self):
        self.screen.blit(self.text_1, (10, 10))
        self.text_score = self.fontsys.render(str(self.score), 2, (0, 50, 0))
        self.screen.blit(self.text_score, (100, 10))

    def draw(self):
        self.screen.fill((130, 200, 100))
        self.screen.blit(self.bg_img, (0, -50))
        self.draw_score()

        # self.barra.draw()
        # resortera parte atras
        rect = pygame.Rect(50, 0, 70, 220)
        self.screen.blit(self.sling_image, (138, 420), rect)

        # resortera
        if self.mouse_pressed:
            self.sling_action()

        for bird in self.birds:
            bird.draw()


        # resortera parte adelante
        rect = pygame.Rect(0, 0, 60, 200)
        self.screen.blit(self.sling_image, (120, 420), rect)

        # estructura
        for column in self.columns:
            column.draw()
        for beam in self.beams:
            beam.draw()

        self.space.step(self.dt)
        # self.space.debug_draw(self.draw_options)
        pygame.display.flip()
        self.clock.tick(self.fps)

    def sling_action(self):
        # fijar ave a cuerda
        v = vector((self.x_sling, self.y_sling), (self.x_mouse, self.y_mouse))
        uvx, uvy = unit_vector(v)

        sling = Vec2d(self.x_sling, self.y_sling)
        mouse = Vec2d(self.x_mouse, self.y_mouse)
        self.mouse_distance = (sling - mouse).length

        pux, puy = (uvx * self.rope_length + self.x_sling, uvy * self.rope_length + self.y_sling)
        bigger_rope = 102
        x_bird = self.x_mouse - 20
        y_bird = self.y_mouse - 20

        if self.mouse_distance > self.rope_length:
            pux -= 20
            puy -= 20
            pul = pux, puy
            self.screen.blit(self.redbird, pul)
            pu2 = (uvx * bigger_rope + self.x_sling, uvy * bigger_rope + self.y_sling)
            pygame.draw.line(self.screen, (0, 0, 0), (self.x_sling2, self.y_sling2), pu2, 5)
            self.screen.blit(self.redbird, pul)
            pygame.draw.line(self.screen, (0, 0, 0), (self.x_sling, self.y_sling), pu2, 5)
        else:
            self.mouse_distance += 10
            pu3 = (uvx * self.mouse_distance + self.x_sling, uvy * self.mouse_distance + self.y_sling)
            pygame.draw.line(self.screen, (0, 0, 0), (self.x_sling2, self.y_sling2), pu3, 5)
            self.screen.blit(self.redbird, (x_bird, y_bird))
            pygame.draw.line(self.screen, (0, 0, 0), (self.x_sling, self.y_sling), pu3, 5)

        # angulo de impulso
        dx = self.x_mouse - self.x_sling
        dy = self.y_mouse - self.y_sling

        if dx == 0:
            dx = 0.000000000001
        self.angle = math.atan(dy / dx)

    def run(self):
        self.is_running = True
        self.mouse_pressed = False
        self.x_sling, self.y_sling = 135, 450
        self.x_sling2, self.y_sling2 = 160, 450
        self.mouse_distance = 0
        self.x_mouse, self.y_mouse = 0, 0
        self.angle = 0
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # rectangulo cercano al sling
                    rect = pygame.Rect(100, 370, 150, 180)
                    if rect.collidepoint(event.pos):
                        print(f"self.mouse_pressed at: ({event.pos})")
                        self.mouse_pressed = True

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.mouse_pressed:
                    # lanzar
                    self.mouse_pressed = False
                    x0 = 154
                    y0 = self.height - 156
                    if self.mouse_distance > self.rope_length:
                        self.mouse_distance = self.rope_length
                    if self.x_mouse < self.x_sling + 5:
                        bird = Bird(self.mouse_distance, self.angle, x0, y0, self.space)
                        print("bird", self.mouse_distance)
                        self.birds.append(bird)
                    else:
                        bird = Bird(-self.mouse_distance, self.angle, x0, y0, self.space)
                        print("bird", self.mouse_distance)
                        self.birds.append(bird)

            self.x_mouse, self.y_mouse = pygame.mouse.get_pos()

            self.draw()
        pygame.quit()


if __name__ == '__main__':
    app = App(1200, 600)
    app.run()