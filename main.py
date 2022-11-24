import pygame
from pygame.locals import *
import json
import random

navios = []
options = [70, 116, 162, 208, 254, 300, 346, 392, 438, 484]
coordenadas = [[70, 70], [70, 116], [70, 162], [70, 208], [70, 254], [70, 300], 
[70, 346], [70, 392], [70, 438], [70, 484], [116, 70], [116, 116], [116, 162], 
[116, 208], [116, 254], [116, 300], [116, 346], [116, 392], [116, 438], 
[116, 484], [162, 70], [162, 116], [162, 162], [162, 208], [162, 254], 
[162, 300], [162, 346], [162, 392], [162, 438], [162, 484], [208, 70], 
[208, 116], [208, 162], [208, 208], [208, 254], [208, 300], [208, 346], 
[208, 392], [208, 438], [208, 484], [254, 70], [254, 116], [254, 162], 
[254, 208], [254, 254], [254, 300], [254, 346], [254, 392], [254, 438], 
[254, 484], [300, 70], [300, 116], [300, 162], [300, 208], [300, 254], 
[300, 300], [300, 346], [300, 392], [300, 438], [300, 484], [346, 70], 
[346, 116], [346, 162], [346, 208], [346, 254], [346, 300], [346, 346], 
[346, 392], [346, 438], [346, 484], [392, 70], [392, 116], [392, 162], 
[392, 208], [392, 254], [392, 300], [392, 346], [392, 392], [392, 438], 
[392, 484], [438, 70], [438, 116], [438, 162], [438, 208], [438, 254], 
[438, 300], [438, 346], [438, 392], [438, 438], [438, 484], [484, 70], 
[484, 116], [484, 162], [484, 208], [484, 254], [484, 300], [484, 346], 
[484, 392], [484, 438], [484, 484]]

#for x in options: #utilizado para definir todas as coordenadas possíveis
#    for y in options:
#        coordenadas.append([x, y])


def evita_colisao(tam, orient, x_inicial, y_inicial):
    while tam > 0:
        if(orient == 1):
            coordenadas.remove(tam*x_inicial, y_inicial)
        else:
            coordenadas.remove(x_inicial, tam*y_inicial)
        tam -=1


def criar_navios(tamanho):
    orientacao = random.choice([1, 2])
    #x_inicial = random.choice(options)
    #y_inicial = random.choice(options)
    coord = random.choice(coordenadas)
    x_inicial = coord[0]
    y_inicial = coord[1]
    if orientacao == 1:
        navio = Rect(x_inicial, y_inicial, 46*tamanho, 46) # 46 é eo tamanho de cada quadrado
    else:                                                  # tanto na horizontal quanto na vertical
        navio = Rect(x_inicial, y_inicial, 46, 46*tamanho)
    navios.append(navio)


def main():
    f = open('coordenadas.json')
    data = json.load(f)

    pygame.init()

    x = 600
    y = 600

    x_pos = ""
    y_pos = ""

    screen = pygame.display.set_mode((x, y))
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Batalha Naval")

    bg = pygame.image.load('images/fundo.jpg').convert()
    bg = pygame.transform.scale(bg, (x, y))

    mar = pygame.image.load('images/mar.png').convert()
    mar = pygame.transform.scale(mar, (46, 46))

    acerto = pygame.image.load('images/acerto.png').convert()
    acerto = pygame.transform.scale(acerto, (46, 46))

    screen.blit(bg, (0, 0))
    running = True

    while running:
        primeiro_quadrado = Rect(70, 70, 46, 46)
        segundo_quadrado = Rect(116, 70, 184, 46)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print(mouse_pos[0])
                if primeiro_quadrado.collidepoint(mouse_pos):
                    screen.blit(mar, (70, 70))
                if segundo_quadrado.collidepoint(mouse_pos):
                    for i in range(len(options) - 1):
                        print(mouse_pos[0], options[i+1])
                        if mouse_pos[0] < options[i + 1]:
                            x_pos = options[i]
                            break
                        else:
                            x_pos = 484
                    for i in range(len(options) - 1):
                        if mouse_pos[1] < options[i + 1]:
                            y_pos = options[i]
                            break
                        else:
                            y_pos = 484
                    screen.blit(acerto, (x_pos, y_pos))

        pygame.display.update()


if __name__ == "__main__":
    main()
