import pygame
import time
import math
from random import *
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)

#screen setup
screenWidth = 800
screenHeight = 800
startingX = 105
startingY = 105

win = pygame.display.set_mode((screenWidth,screenHeight))
win.fill(white)
pygame.display.set_caption("The Maze")

class Wall(object):
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Player(object):
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = y
        self.color = red
        self.radius = radius
        self.velocity = 2
        self.rect = pygame.Rect(x + radius, y + radius, 5, 5)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.rect.left = self.x
        self.rect.top = self.y

    def move(self, dx, dy):
        
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        self.x += dx
        self.y += dy

circle = Player(startingX,startingY,red,4)

def eraseMap():
    walls.clear()
    level.clear()
    win.fill(white)

def restart():
    circle.x = startingX
    circle.y = startingY
    circle.rect.x = startingX
    circle.rect.y = startingY

level = []
walls = []

def loadMap():
    eraseMap()
    restart()
    rows, cols = (50, 50) 
    arr = [[random() for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            if(arr[i][j] < .3):
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    for i in range(cols):
        arr[0][i] = 1
        arr[rows - 1][i] = 1
    for i in range(rows):
        arr[i][0] = 1
        arr[i][cols -1] = 1
    for i in range(1,rows-1):
            for j in range(1,cols-1):
                if(arr[i][j]):
                    if(arr[i+1][j] != 1 and arr[i-1][j] != 1 and arr[i][j+1] != 1 and arr[i][j-1] != 1):
                        x = randint(0,1)
                        if(arr[i-1][j-1]):
                            if(x):
                                arr[i-1][j] = 1
                            else:
                                arr[i][j-1] = 1
                        elif(arr[i-1][j+1]):
                            if(x):
                                arr[i-1][j] = 1
                            else:
                                arr[i][j+1] = 1
                        elif(arr[i+1][j-1]):
                            if(x):
                                arr[i+1][j] = 1
                            else:
                                arr[i][j-1] = 1
                        elif(arr[i+1][j+1]):
                            if(x):
                                arr[i+1][j] = 1
                            else:
                                arr[i][j+1] = 1
    x = randint(1,rows-2)
    y = randint(1,cols-2)
    while(arr[x-1][y] != 0 or arr[x+1][y] != 0):
        x = randint(1,rows-2)
        y = randint(1,cols-2)
    arr[x][y] = 2
    arr[6][6] = 3
    for i in range(rows):
        wString = ""
        for j in range(cols):
            if(arr[i][j] == 1):
                wString += "W"
            elif(arr[i][j] == 2):
                wString += "E"
            elif(arr[i][j] == 3):
                wString += "S"
            else:
                wString += " "
        level.append(wString)

    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
            if col == "E":
                end_rect = pygame.Rect(x, y, 16, 16)
            if col == "S":
                start_rect = pygame.Rect(x, y, 16, 16)
            x += 16
        y += 16
        x = 0
    return end_rect, start_rect
    

end_rect, start_rect = loadMap()

clock = pygame.time.Clock()

def redrawGameWindow():
    win.fill(white)
    for wall in walls:
        pygame.draw.rect(win, black, wall.rect)
    pygame.draw.rect(win, green, end_rect)
    pygame.draw.rect(win, blue, start_rect)
    circle.draw(win)
    pygame.display.update()


run = True
t0 = pygame.time.get_ticks()
while run:
    clock.tick(60)
    tfinal = (pygame.time.get_ticks() - t0) / 1000
    pygame.display.set_caption("The Maze - " + str(tfinal))

    i = math.floor(tfinal) * 16
    if (255 - i < 0):
        raise SystemExit("You lose!")
    white = (255, 255 - i, 255 - i)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and circle.y > circle.radius: 
        circle.move(0, -1 * circle.velocity)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                # circle.rect.top = wall.rect.bottom
                # circle.y = wall.rect.bottom + circle.radius
    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and circle.y < screenHeight - circle.radius: 
        circle.move(0, circle.velocity)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                # circle.rect.bottom = wall.rect.top
                # circle.y = wall.rect.top - circle.radius
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and circle.x > circle.radius: 
        circle.move(-1 * circle.velocity, 0)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                # circle.rect.left = wall.rect.right
                # circle.x = wall.rect.right + circle.radius
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and circle.x < screenWidth - circle.radius: 
        circle.move(circle.velocity, 0)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                # circle.rect.right = wall.rect.left
                # circle.x = wall.rect.left - circle.radius
    if (pressed[pygame.K_r]):
        end_rect, start_rect = loadMap()
        redrawGameWindow()
        t0 = pygame.time.get_ticks()

    if circle.rect.colliderect(end_rect):
        print("You win!")
        run = False
    #print("real x", circle.x, "real y", circle.y)
    #print("x", circle.rect.x, "y", circle.rect.y)
    redrawGameWindow()

