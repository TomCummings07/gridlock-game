import pygame

pygame.init()

size = [700,400]

screen = pygame.display.set_mode(size)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    

pygame.quit()