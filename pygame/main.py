import pygame

#initilizacija pygame
pygame.init()

#definicija velikosti zaslona
screen = pygame.display.set_mode((800,600))

#Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#game loop
running = True
while running:
    #iščemo evente
    for event in pygame.event.get():
        #če je event da pritisnemo gumb za zapiranje programa se program zapre.
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,25,127))
    pygame.display.update()