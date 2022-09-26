from ast import main
from turtle import mainloop
import numpy as np
from math import radians
import pygame 
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN

# configuraciones
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500


class App:
    def __init__(self, screen_width, screen_height, bg_color=(0, 0, 0)):
        self.width = screen_width
        self.height = screen_height
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        self.polygons = []
    
    def update(self):
        self.screen.fill(self.bg_color)
        for poly in self.polygons:
            pygame.draw.polygon(self.screen, (0, 255, 0), poly, 3)

        pygame.display.flip()

    def add_polygon(self, polygon):
        self.polygons.append(polygon)

    def transform_poly(self, poly_idx, t_matrix):
        pass

    def run(self):
        self.is_running = True

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        pass
                        # self.polygons[0].translate(100, 100)
                    if event.key == K_UP:
                        pass
                        # self.polygons[0].translate(-100, -100)
                    if event.key == K_LEFT:
                        pass
                        # self.polygons[0].rotate(radians(20))
                    

            self.update()
        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    # definir poligono
    poly1 = [(5, 5),(250, 5), (250, 250), (5, 250)]
    # definir matriz de transformacion
    M_t = np.array([[1, 0, 40], [0, 1, 60], [0, 0, 1]])
    # transformar poligono a forma matricial (coordenadas homogeneas)
    poly1_l = [[p[0], p[1], 1] for p in poly1]
    poly1_m = np.transpose(np.array(poly1_l))
    # transformar vertices
    poly2_m = np.dot(M_t, poly1_m)

    print(poly2_m)
    # convertir poligono transformado a lista de tuplas
    poly2 = [(p[0], p[1]) for p in np.transpose(poly2_m)]
    print(poly2)
    app.add_polygon(poly1)
    app.add_polygon(poly2)
    
    app.run()
