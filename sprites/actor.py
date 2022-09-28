import pygame
import random
from pygame.sprite import Sprite
from pygame.locals import K_LEFT, K_RIGHT


class Player(Sprite):
    def __init__(self):
        # invocar la inicializacion del padre
        super().__init__()
        # crear una superficie
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect()
    
    def update(self, keys):
        if keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            

class Enemy(Sprite):
    def __init__(self):
        # invocar la inicializacion del padre
        super().__init__()
        # crear una superficie
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(
            random.randint(700, 750),
            random.randint(0, 750)
        ))

    def update(self):
        pass
    