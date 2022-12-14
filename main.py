import pygame
from pygame.locals import *
import random
import sys
from button import Button

navios = []
navio_acertado = [[1, 1]]
navios_coord = []
mares = []
options = [70, 116, 162, 208, 254, 300, 346, 392, 438, 484]
coordenadas = [[70, 70], [70, 116], [70, 162], [70, 208], [70, 254], [70, 300],
               [70, 346], [70, 392], [70, 438], [70, 484], [
                   116, 70], [116, 116], [116, 162],
               [116, 208], [116, 254], [116, 300], [
                   116, 346], [116, 392], [116, 438],
               [116, 484], [162, 70], [162, 116], [
                   162, 162], [162, 208], [162, 254],
               [162, 300], [162, 346], [162, 392], [
                   162, 438], [162, 484], [208, 70],
               [208, 116], [208, 162], [208, 208], [
                   208, 254], [208, 300], [208, 346],
               [208, 392], [208, 438], [208, 484], [
                   254, 70], [254, 116], [254, 162],
               [254, 208], [254, 254], [254, 300], [
                   254, 346], [254, 392], [254, 438],
               [254, 484], [300, 70], [300, 116], [
                   300, 162], [300, 208], [300, 254],
               [300, 300], [300, 346], [300, 392], [
                   300, 438], [300, 484], [346, 70],
               [346, 116], [346, 162], [346, 208], [
                   346, 254], [346, 300], [346, 346],
               [346, 392], [346, 438], [346, 484], [
                   392, 70], [392, 116], [392, 162],
               [392, 208], [392, 254], [392, 300], [
                   392, 346], [392, 392], [392, 438],
               [392, 484], [438, 70], [438, 116], [
                   438, 162], [438, 208], [438, 254],
               [438, 300], [438, 346], [438, 392], [
                   438, 438], [438, 484], [484, 70],
               [484, 116], [484, 162], [484, 208], [
                   484, 254], [484, 300], [484, 346],
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
            removidos.append([(tam * 46) + x_inicial, y_inicial])
            coordenadas.remove([(tam * 46) + x_inicial, y_inicial])
        else:
            removidos.append([x_inicial, (tam * 46) + y_inicial])
            coordenadas.remove([x_inicial, (tam * 46) + y_inicial])
        tam -= 1
    coordenadas_alteradas()


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
    while conferindo:
        tam2 = tam - 1
        if any(x in navio_atual for x in removidos):
            nova_coord = regras_navios(orient, tam)
            navio_atual = []
            while tam2 >= 0:
                if orient == 1:
                    navio_atual.append(
                        [(tam2 * 46) + nova_coord[0], nova_coord[1]])
                else:
                    navio_atual.append(
                        [nova_coord[0], (tam2 * 46) + nova_coord[1]])
                tam2 -= 1
        else:
            navios_coord.append(navio_atual)
            conferindo = False
    return nova_coord


def criar_navios(tamanho):
    orientacao = random.choice([1, 2])
    coord = confere_colisao(tamanho, orientacao)

    x_inicial = coord[0]
    y_inicial = coord[1]
    if orientacao == 1:
        # 46 ?? o tamanho de cada quadrado
        navio = Rect(x_inicial, y_inicial, 46 * tamanho, 46)
    else:  # tanto na horizontal quanto na vertical
        navio = Rect(x_inicial, y_inicial, 46, 46 * tamanho)
    navios.append(navio)
    evita_colisao(tamanho, orientacao, x_inicial, y_inicial)


def escolher_imagem(tamanho, orientacao):
    imagem = ""
    if orientacao == 2 and tamanho == 2:
        imagem = barco2_2
    elif orientacao == 1 and tamanho == 2:
        imagem = barco2_1
    elif orientacao == 1 and tamanho == 3:
        imagem = barco3_1
    elif orientacao == 2 and tamanho == 3:
        imagem = barco3_2
    elif orientacao == 1 and tamanho == 4:
        imagem = barco4_1
    elif orientacao == 2 and tamanho == 4:
        imagem = barco4_2
    elif orientacao == 1 and tamanho == 5:
        imagem = barco5_1
    elif orientacao == 2 and tamanho == 5:
        imagem = barco5_2
    return imagem


def jogar_novamente():
    global navios
    global navio_acertado
    global navios_coord
    global mares
    global options
    global coordenadas
    global removidos
    global coordenadas2_1
    global coordenadas2_2
    global coordenadas3_1
    global coordenadas3_2
    global coordenadas4_1
    global coordenadas4_2
    global coordenadas5_1
    global coordenadas5_2

    navios = []
    navio_acertado = [[1, 1]]
    navios_coord = []
    mares = []
    options = [70, 116, 162, 208, 254, 300, 346, 392, 438, 484]
    coordenadas = [[70, 70], [70, 116], [70, 162], [70, 208], [70, 254], [70, 300],
                   [70, 346], [70, 392], [70, 438], [70, 484], [
                       116, 70], [116, 116], [116, 162],
                   [116, 208], [116, 254], [116, 300], [
                       116, 346], [116, 392], [116, 438],
                   [116, 484], [162, 70], [162, 116], [
                       162, 162], [162, 208], [162, 254],
                   [162, 300], [162, 346], [162, 392], [
                       162, 438], [162, 484], [208, 70],
                   [208, 116], [208, 162], [208, 208], [
                       208, 254], [208, 300], [208, 346],
                   [208, 392], [208, 438], [208, 484], [
                       254, 70], [254, 116], [254, 162],
                   [254, 208], [254, 254], [254, 300], [
                       254, 346], [254, 392], [254, 438],
                   [254, 484], [300, 70], [300, 116], [
                       300, 162], [300, 208], [300, 254],
                   [300, 300], [300, 346], [300, 392], [
                       300, 438], [300, 484], [346, 70],
                   [346, 116], [346, 162], [346, 208], [
                       346, 254], [346, 300], [346, 346],
                   [346, 392], [346, 438], [346, 484], [
                       392, 70], [392, 116], [392, 162],
                   [392, 208], [392, 254], [392, 300], [
                       392, 346], [392, 392], [392, 438],
                   [392, 484], [438, 70], [438, 116], [
                       438, 162], [438, 208], [438, 254],
                   [438, 300], [438, 346], [438, 392], [
                       438, 438], [438, 484], [484, 70],
                   [484, 116], [484, 162], [484, 208], [
                       484, 254], [484, 300], [484, 346],
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

    coordenadas_alteradas()


def main(n):
    global barco2_1
    global barco2_2
    global barco3_1
    global barco3_2
    global barco4_1
    global barco4_2
    global barco5_1
    global barco5_2
    pygame.init()

    x = 600
    y = 600

    x_pos = ""
    y_pos = ""

    screen = pygame.display.set_mode((x, y))
    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Batalha Naval")

    bg = pygame.image.load('images/fundo.jpg').convert()
    bg = pygame.transform.scale(bg, (x, y))

    mar = pygame.image.load('images/mar.png').convert()
    mar = pygame.transform.scale(mar, (46, 46))

    acerto = pygame.image.load('images/acerto.png').convert()
    acerto = pygame.transform.scale(acerto, (46, 46))

    barco2_1 = pygame.image.load('images/barco2-1.png').convert()
    barco2_1 = pygame.transform.scale(barco2_1, (92, 46))

    barco2_2 = pygame.image.load('images/barco2-2.png').convert()
    barco2_2 = pygame.transform.scale(barco2_2, (46, 92))

    barco3_1 = pygame.image.load('images/barco3-1.png').convert()
    barco3_1 = pygame.transform.scale(barco3_1, (138, 46))

    barco3_2 = pygame.image.load('images/barco3-2.png').convert()
    barco3_2 = pygame.transform.scale(barco3_2, (46, 138))

    barco4_1 = pygame.image.load('images/barco4-1.png').convert()
    barco4_1 = pygame.transform.scale(barco4_1, (184, 46))

    barco4_2 = pygame.image.load('images/barco4-2.png').convert()
    barco4_2 = pygame.transform.scale(barco4_2, (46, 184))

    barco5_1 = pygame.image.load('images/barco5-1.png').convert()
    barco5_1 = pygame.transform.scale(barco5_1, (230, 46))

    barco5_2 = pygame.image.load('images/barco5-2.png').convert()
    barco5_2 = pygame.transform.scale(barco5_2, (46, 230))

    pontos = n
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Erros restantes: " + str(pontos),
                       True, (250, 250, 250), (78, 187, 174))
    textRect = text.get_rect()
    textRect.center = (150, 570)

    navios_acertados = 10

    text_navios = font.render(
        "Navios restantes: " + str(navios_acertados), True, (250, 250, 250), (78, 187, 174))
    naviosRect = text_navios.get_rect()
    naviosRect.center = (450, 570)

    final = pygame.Surface((300, 300))
    final.fill((78, 187, 174))

    text_jogar_novamente = font.render(
        "Jogar novamente?", True, (250, 250, 250), (78, 187, 174))
    jogar_novamenterect = text_jogar_novamente.get_rect()
    jogar_novamenterect.center = (300, 250)

    font2 = pygame.font.Font('freesansbold.ttf', 25)
    text_sim = font2.render("Sim", True, (250, 250, 250), (101, 96, 99))
    sim = text_sim.get_rect()
    sim.center = (250, 350)

    text_nao = font2.render("N??o", True, (250, 250, 250), (101, 96, 99))
    nao = text_nao.get_rect()
    nao.center = (350, 350)

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
    aguardando = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for p in mares:
                    if p.collidepoint(mouse_pos):
                        p.w = 0
                        p.h = 0
                        screen.blit(mar, (p[0], p[1]))
                        pontos = pontos - 1
                        text = font.render(
                            f'Erros restantes: {pontos}', True, (250, 250, 250), (78, 187, 174))
                        if pontos <= 0:
                            screen.fill((78, 187, 174), Rect(0, 550, 600, 50))
                            text = font.render(
                                f'GAME OVER!!', True, (250, 250, 250), (78, 187, 174))
                            screen.blit(text, textRect)
                            for t in mares:
                                t.w = 0
                                t.h = 0
                            for k in navios:
                                k.w = 0
                                k.h = 0
                            screen.blit(final, (150, 150))
                            screen.blit(text_jogar_novamente,
                                        jogar_novamenterect)
                            screen.blit(text_sim, sim)
                            screen.blit(text_nao, nao)
                            pygame.display.update()
                            running = False
                            aguardando = True
                for p in navios:
                    if p.collidepoint(mouse_pos):
                        for i in range(len(options) - 1):
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
                        navio_acertado.append([x_pos, y_pos])
                        screen.blit(acerto, (x_pos, y_pos))
                counter = 0
                x_navio = 1000
                y_navio = 1000
                for i in navios_coord:
                    for k in i:
                        if k in navio_acertado:
                            counter += 1
                    if counter == len(i):
                        for k in i:
                            if k[0] < x_navio:
                                x_navio = k[0]
                            if k[1] < y_navio:
                                y_navio = k[1]
                        for p in navios:
                            if p[0] == x_navio and p[1] == y_navio:
                                if p[2] > p[3]:
                                    orientacao_navio = 1
                                    tamanho_navio = int(p[2]/p[3])
                                else:
                                    orientacao_navio = 2
                                    tamanho_navio = int(p[3]/p[2])
                                p.w = 0
                                p.h = 0
                                barco = escolher_imagem(
                                    tamanho_navio, orientacao_navio)
                                screen.blit(barco, (x_navio, y_navio))
                        navios_coord.remove(i)
                        counter = 0
                        navios_acertados = navios_acertados - 1
                        text_navios = font.render("Navios restantes: " + str(navios_acertados), True,
                                                  (250, 250, 250),
                                                  (78, 187, 174))
                        if navios_acertados == 0:
                            screen.fill((78, 187, 174), Rect(0, 550, 600, 50))
                            screen.blit(text_navios, naviosRect)
                            text = font.render(
                                f'YOU WIN!!', True, (250, 250, 250), (78, 187, 174))
                            screen.blit(text, textRect)
                            for p in mares:
                                p.w = 0
                                p.h = 0
                            for p in navios:
                                p.w = 0
                                p.h = 0
                            screen.blit(final, (150, 150))
                            screen.blit(text_jogar_novamente,
                                        jogar_novamenterect)
                            screen.blit(text_sim, sim)
                            screen.blit(text_nao, nao)
                            pygame.display.update()
                            running = False
                            aguardando = True
                    else:
                        counter = 0

        if running:
            screen.fill((78, 187, 174), Rect(0, 550, 600, 50))
            screen.blit(text, textRect)
            screen.blit(text_navios, naviosRect)
            pygame.display.update()

    while aguardando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aguardando = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if sim.collidepoint(mouse_pos):
                    screen.fill((0, 0, 0))
                    aguardando = False
                    jogar_novamente()
                    main(n)
                if nao.collidepoint(mouse_pos):
                    aguardando = False
                    pygame.quit()


pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/Background.jpg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("images/font.ttf", size)


def printing_text(text, place, tela):
    INSTRUCTION_TEXT = get_font(10).render(text, True, "White")
    INSTRUCTION_RECT = INSTRUCTION_TEXT.get_rect(center=(300, place))
    tela.blit(INSTRUCTION_TEXT, INSTRUCTION_RECT)


def Instruction_menu():
    pygame.init()

    SCREEN = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Batalha Naval")
    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)

    BG = pygame.image.load("images/Background.jpg")
    instruction = True
    while instruction:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(35).render("Instru????es:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        printing_text(
            "H?? 10 navios no mapa, s??o eles 4 navios de tamanho 2", 150, SCREEN)
        printing_text(
            "3 navios de tamanho 3, 2 navios de tamanho 4 e 1 na-", 200, SCREEN)
        printing_text("vio de tamanho 5. Exploda todos eles!", 250, SCREEN)
        printing_text("Escolha a dificuldade desejada", 350, SCREEN)

        PLAY_Facil = Button(image=None, pos=(100, 550),
                            text_input="F??cil", font=get_font(25), base_color="White", hovering_color="Green")
        PLAY_Medio = Button(image=None, pos=(300, 550),
                            text_input="M??dio", font=get_font(25), base_color="White", hovering_color="Green")
        PLAY_Dificil = Button(image=None, pos=(500, 550),
                              text_input="D??ficil", font=get_font(25), base_color="White", hovering_color="Green")

        PLAY_Facil.changeColor(PLAY_MOUSE_POS)
        PLAY_Facil.update(SCREEN)

        PLAY_Medio.changeColor(PLAY_MOUSE_POS)
        PLAY_Medio.update(SCREEN)

        PLAY_Dificil.changeColor(PLAY_MOUSE_POS)
        PLAY_Dificil.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_Facil.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    coordenadas_alteradas()
                    instruction = False
                    main(60)
                if PLAY_Medio.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    coordenadas_alteradas()
                    instruction = False
                    main(45)
                if PLAY_Dificil.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    coordenadas_alteradas()
                    instruction = False
                    main(30)

        if instruction:
            pygame.display.update()


def menu_principal():
    menu = True
    logo = pygame.image.load("images/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Batalha Naval")
    while menu:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("Batalha Naval", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(300, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("images/Play Rect.png"), pos=(300, 200),
                             text_input="Jogar", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("images/Quit Rect.png"), pos=(300, 400),
                             text_input="Sair", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    menu = False
                    Instruction_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    menu = False
                    sys.exit()

        if menu:
            pygame.display.update()


menu_principal()
