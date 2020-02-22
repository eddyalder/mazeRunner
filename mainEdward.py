import pygame
pygame.init()

screenWidth = 700
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))
white = (255,255,255)
black = (0,0,0)
win.fill(white)
pygame.display.set_caption("First Game")
pygame.draw.rect(win, black, (200,150,100,50))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()    