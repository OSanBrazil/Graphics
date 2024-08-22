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

# Defines variables

PI = 3.141592
PI2 = PI * 2
xcentral = ScreenWidth / 2
ycentral = ScreenHeight / 2
tamanho = ScreenHeight * .5
frequencia = 1
init_deg = 0
sides_glob = 3
sides_inc = 1
cor_da_borda = (255, 1, 1)
cor_da_linha = (1, 1, 255)


# Functions

def desenha():
    x_ant = xcentral
    y_ant = ycentral
    x_init = 0
    y_init = 0
    sides = 360 / sides_glob
    deg = init_deg
    while deg <= init_deg + 360:
        rad = deg * PI2 / 360
        x = xcentral + math.sin(rad) * tamanho_atual
        y = ycentral + math.cos(rad) * tamanho_atual
        if y_ant != ycentral:
            pygame.draw.line(screen, cor_da_borda, (x_ant, y_ant), (x, y), 4)
            pygame.draw.line(screen, cor_da_linha, (xcentral, ycentral), (x, y), 4)
            if x_init == 0:
                x_init = x_ant
                y_init = y_ant
        x_ant = x
        y_ant = y
        deg += sides
    pygame.draw.line(screen, cor_da_borda, [x_ant, y_ant], [x_init, y_init], 4)
    pygame.draw.line(screen, cor_da_linha, (xcentral, ycentral), (x_init, y_init), 4)


while True:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    pygame.display.set_caption(f'GRAPHICS / FPS: {frame_counter} / SIDES: {sides_glob}/ mouse: X-{mouse_x} Y-{mouse_y}')

    # pygame.draw.line(screen,[255,255,255],[2, 2],[200, 200])

    # Detecção de eventos (teclado etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Desenha todos os elementos
    screen.fill((0, 0, 0))
    if init_deg < 360:
        init_deg += fps_rate * 3 / fps_rate
        tamanho_atual = tamanho * math.sin(init_deg * PI / 360)
        desenha()

    if init_deg >= 360:
        init_deg = 0
        sides_glob += sides_inc
        if sides_glob > 15 or sides_glob < 4:
            sides_inc = -sides_inc

    # Atualiza tudo
    pygame.display.update()
    frame_counter += 1
    if frame_counter > fps_rate - 1:
        frame_counter = 0
    clock.tick(fps_rate)

# FIM DO LOOP PRINCIPAL
