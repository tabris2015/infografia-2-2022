# inicializacion
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.sprite import Sprite

# constantes y configuraciones
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# objeto del juego
class Player(Sprite):
    def __init__(self):
        super(Sprite, self).__init__() # inicializar clase padre
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        self.pos_x = 0
        self.pos_y = 0
        self.surf.fill((255, 0, 0))
    
    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

pygame.init()
player = Player()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.locals.KEYDOWN:
            if event.key == K_UP:
                if player.pos_y > 0:
                    player.move(0, -10)
            if event.key == K_DOWN:
                if player.pos_y < SCREEN_HEIGHT:
                    player.move(0, 10)
    
    screen.fill((0, 0, 0))
    # dibujar el player en la pantalla
    screen.blit(player.surf, (player.pos_x, player.pos_y))

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()