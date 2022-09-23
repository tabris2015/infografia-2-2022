# inicializacion
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

# constantes y configuraciones
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def draw_shapes(screen):
    pygame.draw.rect(
        screen,
        (100, 100, 100),
        (40, 40, 100, 100)
    )

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        # if event.type == pygame.locals.KEYDOWN:
        #     if event.key == K_UP:
    
    screen.fill((0, 0, 0))

    draw_shapes(screen)

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()