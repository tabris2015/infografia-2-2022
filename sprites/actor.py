import pygame
import random
from pygame.sprite import Sprite
from pygame.locals import K_UP, K_DOWN, RLEACCEL


class Player(Sprite):
    def __init__(self):
        # invocar la inicializacion del padre
        super().__init__()
        # crear una superficie
        # self.surf = pygame.Surface((50, 50))
        # self.surf.fill((0, 0, 255))
        self.surf = pygame.image.load("sprites/assets/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.projectiles = pygame.sprite.Group()
    
    def update(self, keys):
        self.projectiles.update()
        if keys[K_UP]:
            self.rect.move_ip(0,-5)
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)

    def shoot(self):
        self.projectiles.add(Projectile(self.rect.x, self.rect.y))
        print("shoot!")
            

class Projectile(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.surf = pygame.Surface((5, 2))
        self.surf.fill((255, 255, 0))
        self.rect = self.surf.get_rect(center=(pos_x, pos_y))
        self.speed = 15

    def update(self):
        self.rect.move_ip(self.speed, 0)

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
        self.speed = random.randint(2, 8)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
    