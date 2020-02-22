import pygame
pygame.init()

screenWidth = 700
screenHeight = 500
x = 100
y = 100

win = pygame.display.set_mode((screenWidth,screenHeight))
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
win.fill(white)
radius = 12
pygame.display.set_caption("The Maze")

clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and y > radius: 
        y -= 5
    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and y < screenHeight - radius: 
        y += 5
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and x > radius: 
        x -= 5
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and x < screenWidth - radius: 
        x += 5
    #print("x", x, "y", y)
    win.fill(white)
    pygame.draw.circle(win, red, (x,y), radius)

    pygame.display.flip()
    clock.tick(144)