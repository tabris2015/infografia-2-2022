# inicializacion
import pygame
import random
import math
import cmath
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

# constantes y configuraciones
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

def draw_shapes(screen, final_angle=360):

    pygame.draw.circle(
        screen, 
        (200, 200, 200), 
        (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        100
    )
    for angle in range(0, final_angle, 2):
        r = (angle % 60) * 3
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        pygame.draw.circle(
            screen,
            (0, 255 - angle // 4, angle // 4),
            (center_c.real + SCREEN_WIDTH / 2, center_c.imag + SCREEN_HEIGHT / 2),
            5
        )
        pygame.draw.line(screen, (255, 255, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), (center_c.real + SCREEN_WIDTH / 2, center_c.imag + SCREEN_HEIGHT / 2))


pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
is_running = True

final_angle = 60

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.locals.KEYDOWN:
            if event.key == K_UP:
                final_angle += 10
            if event.key == K_DOWN:
                final_angle -= 10
    
    screen.fill((0, 0, 0))

    draw_shapes(screen, final_angle)

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()