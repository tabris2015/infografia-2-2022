# inicializacion
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.sprite import Sprite
from bresenham import get_line

# constantes y configuraciones
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
PIXEL_SIZE = 10

def draw_points(screen, points, color=(0, 255, 0)):
    for point in points:
        pygame.draw.rect(
            screen, 
            color, 
            (
                point[0] * PIXEL_SIZE, 
                point[1] * PIXEL_SIZE, 
                PIXEL_SIZE, 
                PIXEL_SIZE
            )
        )


def draw_line(screen, x0, y0, x1, y1, color=(255, 0, 0)):
    pygame.draw.line(
        screen, 
        color, 
        (x0 * PIXEL_SIZE, y0 * PIXEL_SIZE),
        (x1 * PIXEL_SIZE, y1 * PIXEL_SIZE),
        3
    )


def draw_grid(screen, color=(70, 70, 70)):
    for i in range(0, SCREEN_WIDTH, PIXEL_SIZE):
        pygame.draw.line(screen, color, (i, 0), (i, SCREEN_HEIGHT))
        pygame.draw.line(screen, color, (0, i), (SCREEN_WIDTH, i))


pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
is_running = True

# points = [(0,0), (1,1), (2,2)]

x0, y0 = 5, 20
x1, y1 = 30, 5

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        # if event.type == pygame.locals.KEYDOWN:
        #     if event.key == K_UP:
    
    screen.fill((0, 0, 0))
    draw_grid(screen, (0, 60, 60))

    points = get_line(x0, y0, x1, y1)

    draw_points(screen, get_line(0,0,20,30))
    draw_points(screen, points)
    
    draw_line(screen, x0, y0, x1, y1)

    #actualizar pantalla
    pygame.display.flip()

pygame.quit()