from ast import main
from turtle import mainloop
import numpy as np
from math import radians
import pygame 
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, K_a, K_d
from polygon import Polygon

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
            poly.draw(self.screen)

        pygame.display.flip()

    def add_polygon(self, polygon):
        self.polygons.append(polygon)

    def run(self):
        vx, vy = 2,1
        d_scale = 1.01
        v_theta = radians(0.5)
        self.is_running = True

        while self.is_running:
            pygame.time.delay(10)       # frame rate constante
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
              
            self.update()
            if self.polygons[0].rect[1] > SCREEN_HEIGHT or self.polygons[0].rect[1] < 0:
                vy = -vy
            if self.polygons[0].rect[0] > SCREEN_WIDTH or self.polygons[0].rect[0] < 0:
                vx = -vx
            

            self.polygons[0].translate(vx, vy)  
            poly_rect = self.polygons[0].rect
            # self.polygons[0].rotate(v_theta, poly_rect[0] + poly_rect[2] // 2, poly_rect[1] + poly_rect[3] // 2)      
            if poly_rect[3] > 100:
                d_scale = 0.99
            if poly_rect[3] < 10:
                d_scale = 1.01
            
            self.polygons[0].scale(d_scale, d_scale)

        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    app.add_polygon(Polygon(
        [
            (5, 5), 
            (70, 5),
            (70, 70), 
            (5, 70)
        ]
    ))
    
    app.run()
