from fnmatch import translate
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
        translate_matrix = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
        self.transform(translate_matrix)

    def rotate(self, theta, xr=None, yr=None):
        if xr is None and yr is None:
            xr, yr = self.vertices[0]
        
        translate1_m = np.array([[1, 0, xr], [0, 1, yr], [0, 0, 1]])
        rotate_m = np.array([[np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0, 0, 1]])
        # print(rotate_m)
        translate2_m = np.array([[1, 0, -xr], [0, 1, -yr], [0, 0, 1]])

        trans_matrix = np.dot(np.dot(translate1_m, rotate_m), translate2_m)
        # print(trans_matrix)
        self.transform(trans_matrix)
        

    def scale(self, sx, sy, xr=None, yr=None):
        if xr is None and yr is None:
            xr, yr = self.vertices[0]
        translate1_m = np.array([[1, 0, xr], [0, 1, yr], [0, 0, 1]])
        scale_m = np.array([[sx, 0, 0],
                            [0, sy, 0],
                            [0, 0, 1]])
        # print(scale_m)
        translate2_m = np.array([[1, 0, -xr], [0, 1, -yr], [0, 0, 1]])

        trans_matrix = np.dot(np.dot(translate1_m, scale_m), translate2_m)
        # print(trans_matrix)
        self.transform(trans_matrix)