from ast import main
from turtle import mainloop
import numpy as np
from math import radians
import pygame 
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN
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
        self.is_running = True

        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.polygons[0].translate(100, 100)
                    if event.key == K_UP:
                        self.polygons[0].translate(-100, -100)
                    if event.key == K_LEFT:
                        self.polygons[0].rotate(radians(20))
                    

            self.update()
        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    app.add_polygon(Polygon(
        [
            (5, 5), 
            (70, 5),
            (95, 45), 
            (180, 80), 
            (5, 80)
        ]
    ))
    
    app.run()
