# importar e inicializar el motor
import pygame

pygame.init()

# configuracion de la ventana
screen = pygame.display.set_mode([500, 500])

running = True

while running:
    # verificar eventos: teclado, mouse, joystick
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # rellenar el fondo de color blanco
    screen.fill((255, 255, 255))

    # dibujar un circulo en el centro de la pantalla
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # actualizar la pantalla
    pygame.display.flip()

# si salimos del bucle, terminar
pygame.quit()