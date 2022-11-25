import pygame
from pygame.locals import *
import random

navios = []
mares = []
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
removidos = []

coordenadas2_1 = []
coordenadas2_2 = []
coordenadas3_1 = []
coordenadas3_2 = []
coordenadas4_1 = []
coordenadas4_2 = []
coordenadas5_1 = []
coordenadas5_2 = []


def coordenadas_alteradas():
    for u in coordenadas:
        if u[0] != 484:
            coordenadas2_1.append(u)
        if u[1] != 484:
            coordenadas2_2.append(u)
        if u[0] != 484 and u[0] != 438:
            coordenadas3_1.append(u)
        if u[1] != 484 and u[1] != 438:
            coordenadas3_2.append(u)
        if u[0] != 484 and u[0] != 438 and u[0] != 392:
            coordenadas4_1.append(u)
        if u[1] != 484 and u[1] != 438 and u[1] != 392:
            coordenadas4_2.append(u)
        if u[0] != 484 and u[0] != 438 and u[0] != 392 and u[0] != 346:
            coordenadas5_1.append(u)
        if u[1] != 484 and u[1] != 438 and u[1] != 392 and u[1] != 346:
            coordenadas5_2.append(u)



def regras_navios(orientacao, tamanho):
    coord = ""
    if orientacao == 1 and tamanho == 1:
        coord = random.choice(coordenadas)
    if orientacao == 1 and tamanho == 2:
        coord = random.choice(coordenadas2_1)
    if orientacao == 2 and tamanho == 2:
        coord = random.choice(coordenadas2_2)
    if orientacao == 1 and tamanho == 3:
        coord = random.choice(coordenadas3_1)
    if orientacao == 2 and tamanho == 3:
        coord = random.choice(coordenadas3_2)
    if orientacao == 1 and tamanho == 4:
        coord = random.choice(coordenadas4_1)
    if orientacao == 2 and tamanho == 4:
        coord = random.choice(coordenadas4_2)
    if orientacao == 1 and tamanho == 5:
        coord = random.choice(coordenadas5_1)
    if orientacao == 2 and tamanho == 5:
        coord = random.choice(coordenadas5_2)
    if orientacao == 2 and tamanho == 1:
        coord = random.choice(coordenadas)
    return coord


def evita_colisao(tam, orient, x_inicial, y_inicial):
    tam -= 1
    while tam >= 0:
        if orient == 1:
            print(f'Tamanho: {tam}, x a remover: {(tam * 46) + x_inicial}, y a remover: {y_inicial}')
            print(f'Coordenadas: {coordenadas}')
            removidos.append([(tam * 46) + x_inicial, y_inicial])
            coordenadas.remove([(tam * 46) + x_inicial, y_inicial])
        else:
            print(f'Tamanho: {tam}, x a remover: {x_inicial}, y a remover: {(tam * 46) + y_inicial}')
            print(f'Coordenadas: {coordenadas}')
            removidos.append([x_inicial, (tam * 46) + y_inicial])
            coordenadas.remove([x_inicial, (tam * 46) + y_inicial])
        tam -= 1
    coordenadas_alteradas()
    print(coordenadas2_1)
    print(coordenadas2_2)
    print(coordenadas3_1)
    print(coordenadas3_2)
    print(coordenadas4_1)
    print(coordenadas4_2)
    print(coordenadas5_1)
    print(coordenadas5_2)
    print(f' Removidos: {removidos}')

def confere_colisao(tam, orient):
    conferindo = True
    navio_coord = regras_navios(orient, tam)
    nova_coord = [navio_coord[0], navio_coord[1]]
    navio_atual = []
    tam1 = tam - 1
    while tam1 >= 0:
        if orient == 1:
            navio_atual.append([(tam1 * 46) + navio_coord[0], navio_coord[1]])
        else:
            navio_atual.append([navio_coord[0], (tam1 * 46) + navio_coord[1]])
        tam1 -= 1
    print(f'Navio atual {navio_atual}')
    while conferindo:
        tam2 = tam - 1
        if any(x in navio_atual for x in removidos):
            print(f'Errado: {navio_atual}')
            nova_coord = regras_navios(orient, tam)
            navio_atual = []
            while tam2 >= 0:
                if orient == 1:
                    navio_atual.append([(tam2 * 46) + nova_coord[0], nova_coord[1]])
                else:
                    navio_atual.append([nova_coord[0], (tam2 * 46) + nova_coord[1]])
                tam2 -= 1
        else:
            print(f'Certo: {navio_atual}')
            conferindo = False
    return nova_coord

def criar_navios(tamanho):
    orientacao = random.choice([1, 2])
    #coord = regras_navios(orientacao, tamanho)
    coord = confere_colisao(tamanho, orientacao)

    x_inicial = coord[0]
    y_inicial = coord[1]
    if orientacao == 1:
        navio = Rect(x_inicial, y_inicial, 46 * tamanho, 46)  # 46 é o tamanho de cada quadrado
    else:  # tanto na horizontal quanto na vertical
        navio = Rect(x_inicial, y_inicial, 46, 46 * tamanho)
    navios.append(navio)
    evita_colisao(tamanho, orientacao, x_inicial, y_inicial)


def main():
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

    pontos = 20
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Erros restantes: " + str(pontos), True, (255, 255, 255), (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (300, 570)

    criar_navios(1)
    criar_navios(1)
    criar_navios(2)
    criar_navios(2)
    criar_navios(2)
    criar_navios(2)
    criar_navios(3)
    criar_navios(3)
    criar_navios(3)
    criar_navios(4)
    criar_navios(4)
    criar_navios(5)

    for i in coordenadas:
        novo_mar = Rect(i[0], i[1], 46, 46)
        mares.append(novo_mar)

    screen.blit(bg, (0, 0))
    running = True

    print(navios)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print(mouse_pos[0])
                for p in mares:
                    if p.collidepoint(mouse_pos):
                        screen.blit(mar, (p[0], p[1]))
                        pontos = pontos - 1
                        text = font.render(f'Pontos restantes: {pontos}', True, (255, 255, 255), (0, 0, 0))
                for p in navios:
                    if p.collidepoint(mouse_pos):
                        for i in range(len(options) - 1):
                            print(mouse_pos[0], options[i + 1])
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
        screen.fill((78, 187, 174), Rect(0, 550, 600, 50))
        screen.blit(text, textRect)
        pygame.display.update()


if __name__ == "__main__":
    main()