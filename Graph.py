# Bibliotecas
import math

import pygame
from sys import exit

# Seta as variáveis
ScreenWidth = 1024
ScreenHeight = 760
fps_rate = 60
frame_counter = 0

pygame.init()
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("GRAPHICS")
clock = pygame.time.Clock()

while True:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.display.set_caption(f'GRAPHICS mouse: X-{mouse_x} Y-{mouse_y}')

    # pygame.draw.line(screen,[255,255,255],[2, 2],[200, 200])
    PI = 3.141592
    PI2 = PI * 2
    xcentral = ScreenWidth / 2
    ycentral = ScreenHeight / 2
    tamanho = ScreenHeight * .4
    frequencia = 1
    x_ant = xcentral
    y_ant = ycentral
    x_init = 0
    y_init = 0
    sides = 5
    sides = 360/sides
    deg = 0
    while deg <= 360:
        rad = deg * PI2 / 360
        x = xcentral + math.sin(rad) * tamanho
        y = ycentral + math.cos(rad) * tamanho
        if y_ant != ycentral:
            pygame.draw.line(screen, (16, 255, 16), (x_ant, y_ant), (x, y))
            pygame.draw.line(screen, (255,16,16),(xcentral,ycentral),(x,y))
            if x_init == 0:
                x_init = x_ant
                y_init = y_ant
        x_ant = x
        y_ant = y
        deg += sides
    pygame.draw.line(screen, [255, 255, 255], [x_ant, y_ant], [x_init, y_init])
    # Detecção de eventos (teclado etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Desenha todos os elementos
    # Atualiza tudo
    pygame.display.update()
    frame_counter += 1
    if frame_counter > fps_rate - 1:
        frame_counter = 0
    clock.tick(fps_rate)

# FIM DO LOOP PRINCIPAL
