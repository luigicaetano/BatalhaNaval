import pygame
from pygame.locals import *
import json
import random


def criar_navios(tamanho):
    x_inicial = random.choice(options)
    y_inicial = random.choice(options)
    navio = Rect(x_inicial, y_inicial, 46, 46*tamanho)
    navios.append(navio)

#def conferir_navio():


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


navios = []
options = [70, 116, 162, 208, 254, 300, 346, 392, 438, 484]

if __name__ == "__main__":
    main()
