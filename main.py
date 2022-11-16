import pygame
from pygame.locals import *


def main():
    pygame.init()

    x = 600
    y = 600

    screen = pygame.display.set_mode((x, y))
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Batalha Naval")
    bg = pygame.image.load('images/fundo.jpg').convert()
    bg = pygame.transform.scale(bg, (x, y))
    mar = pygame.image.load('images/mar.png').convert()
    mar = pygame.transform.scale(mar, (46, 46))
    screen.blit(bg, (0, 0))
    running = True

    while running:
        primeiro_quadrado = Rect(70, 70, 46, 46)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if primeiro_quadrado.collidepoint(mouse_pos):
                    screen.blit(mar, (70,70))

        pygame.display.update()


if __name__ == "__main__":
    main()
