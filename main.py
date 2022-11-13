import pygame



def main():
    pygame.init()

    x = 600
    y = 600

    screen = pygame.display.set_mode((x, y))
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    bg = pygame.image.load('images/fundo.jpg')
    bg = pygame.transform.scale(bg, (x, y))


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(bg, (0, 0))
        pygame.display.update()

if __name__ == "__main__":
    main()