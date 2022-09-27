import numpy as np
import pygame
from pygame.sprite import Sprite


class Polygon:
    def __init__(self, vertices, color=(0, 255, 0)):
        self.vertices = vertices
        self.color = color
        self.rect = None

    def draw(self, surface):
        self.rect = pygame.draw.polygon(surface, self.color, self.vertices)

    def transform(self, t_matrix):
        vert_list = [[v[0], v[1], 1] for v in self.vertices] 
        vert_matrix = np.transpose(np.array(vert_list))
        new_matrix = np.transpose(np.dot(t_matrix, vert_matrix))
        new_vertices = [(v[0], v[1]) for v in new_matrix]

        self.vertices = new_vertices

    def translate(self, tx, ty):
        pass

    def rotate(self, theta, xr=None, yr=None):
        pass