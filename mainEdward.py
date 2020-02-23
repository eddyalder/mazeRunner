import pygame
import time
import math
from random import *
pygame.init()


#Colors
white = (255,255,255)
red = (255,0,0)
gold = (255,215,0)
silver = (155,20,20)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
brown = (210,105,30)

#Screen setup
screenWidth = 800
screenHeight = 800
startingX = 104
startingY = 104

#Difficulty
difficultyChoice = 1
difficultySpeed = 1
deathCounter = 0

fileOpen = open("test.txt", "r")
if fileOpen.mode == 'r':
    difficultyChoice = int(fileOpen.read())

difficultySpeed = difficultyChoice * 4
timeRemaining = math.floor(256 / difficultySpeed)
#Global arr
level = []
walls = []

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
        self.velocity = 1
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
class Enemy(object):
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = y
        self.color = brown
        self.radius = radius
        self.velocity = 4 + difficultyChoice
        self.rect = pygame.Rect(x + radius, y + radius, 5, 5)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
        self.rect.left = self.x
        self.rect.top = self.y

    def move(self, colorChange):
        choice = randint(0,1)
        retColorUp = win.get_at((self.x, self.y - self.velocity))
        retColorDown = win.get_at((self.x, self.y + self.velocity))
        retColorLeft = win.get_at((self.x - self.velocity, self.y))
        retColorRight = win.get_at((self.x + self.velocity, self.y))
        if(circle.x < self.x):
            if(circle.y < self.y):
                if(choice):
                    if (retColorUp == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.y -= self.velocity
                else:
                    if (retColorLeft == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.x -= self.velocity
            else:
                if(choice):
                    if (retColorDown == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.y += self.velocity
                else:
                    if (retColorLeft == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.x -= self.velocity
        else:
            if(circle.y < self.y):
                if(choice):
                    if (retColorUp == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.y -= self.velocity
                else:
                    if (retColorRight == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.x += self.velocity
            else:
                if(choice):
                    if (retColorDown == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.y += self.velocity
                else:
                    if (retColorRight == (255, 255 - colorChange, 255 - colorChange, 255)):
                        self.x += self.velocity

        # if (choice == 1):
        #     if (retColorUp == (255, 255 - colorChange, 255 - colorChange, 255)):
        #         self.y -= self.velocity
        # elif (choice == 2):
        #     if (retColorDown == (255, 255 - colorChange, 255 - colorChange, 255)):
        #         self.y += self.velocity
        # elif (choice == 3):
        #     if (retColorLeft == (255, 255 - colorChange, 255 - colorChange, 255)):
        #         self.x -= self.velocity
        # elif (choice == 4):
        #     if (retColorRight == (255, 255 - colorChange, 255 - colorChange, 255)):
        #         self.x += self.velocity



def eraseMap():
    walls.clear()
    level.clear()
    win.fill(white)

def restart():
    global deathCounter 
    deathCounter += 1
    circle.x = startingX
    circle.y = startingY
    circle.rect.x = startingX
    circle.rect.y = startingY

def loadMap():
    eraseMap()
    restart()
    global deathCounter
    deathCounter = 0
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
			    if(arr[i+1][j] != 1 and arr[i-1][j] != 1 and arr[i][j+1] != 1 and arr[i][j-1] != 1 and arr[i-1][j-1] != 1 and arr[i-1][j+1] != 1 and arr[i+1][j-1] != 1 and arr[i+1][j+1] != 1):
				    if(arr[i-2][j-2]):
				    	arr[i-1][j-1] = 1
				    elif(arr[i-1][j-2]):
				    	arr[i-1][j-1] = 1
				    elif(arr[i-2][j-1]):
				    	arr[i-1][j-1] = 1
				    elif(arr[i-2][j]):
				    	arr[i-1][j] = 1
				    elif(arr[i][j-2]):
				    	arr[i][j-1] = 1
				    elif(arr[i-2][j+1]):
				    	arr[i-1][j] = 1
				    elif(arr[i+1][j-2]):
				    	arr[i][j-1] = 1
				    elif(arr[i-2][j+2]):
				    	arr[i-1][j+1] = 1
				    elif(arr[i+2][j-2]):
				    	arr[i+1][j-1] = 1
				    elif(arr[i+2][j-1]):
				    	arr[i+1][j-1] = 1
				    elif(arr[i-1][j+2]):
				    	arr[i-1][j+1] = 1
				    elif(arr[i+2][j]):
				    	arr[i+1][j] = 1
				    elif(arr[i][j+2]):
				    	arr[i][j+1] = 1
				    elif(arr[i+1][j+2]):
				    	arr[i+1][j+1] = 1
				    elif(arr[i+2][j+1]):
				    	arr[i+1][j+1] = 1
				    elif(arr[i+2][j+2]):
				    	arr[i+1][j+1] = 1


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

    x = randint(1, rows-2)
    y = randint(1, cols-2)
    while(arr[x][y] != 0):
        x = randint(1, rows-2)
        y = randint(1, cols-2)
    arr[x][y] = 4

    x = randint(1, rows-2)
    y = randint(1, cols-2)
    while(arr[x][y] != 0):
        x = randint(1, rows-2)
        y = randint(1, cols-2)
    arr[x][y] = 5

    x = randint(1, rows-2)
    y = randint(1, cols-2)

    l = 6
    for k in range(difficultyChoice):
        while(arr[x][y] != 0):
            x = randint(1, rows-2)
            y = randint(1, cols-2)
        arr[x][y] = l
        l = l + 1
    for i in range(rows):
        wString = ""
        for j in range(cols):
            if(arr[i][j] == 1):
                wString += "W"
            elif(arr[i][j] == 2):
                wString += "E"
            elif(arr[i][j] == 3):
                wString += "S"
            elif(arr[i][j] == 4):
                wString += "O"
            elif(arr[i][j] == 5):
                wString += "P"
            elif(arr[i][j] == 6):
                wString += "T"
            elif(arr[i][j] == 7):
                wString += "Y"
            elif(arr[i][j] == 8):
                wString += "U"
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
            if col == "O":
                portalEntrace_rect = pygame.Rect(x, y, 16, 16)
            if col == "P":
                portalExit_rect = pygame.Rect(x, y, 16, 16)
            if col == "T":
                enemy1 = Enemy(x + 8, y + 8, brown, circle.radius)
            if col == "Y":
                enemy2 = Enemy(x + 8, y + 8, brown, circle.radius)
            if col == "U":
                enemy3 = Enemy(x + 8, y + 8, brown, circle.radius)
            x += 16
        y += 16
        x = 0

    if (difficultyChoice == 1):
        return end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1
    elif (difficultyChoice == 2):
        return end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1, enemy2
    elif (difficultyChoice == 3):
        return end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1, enemy2, enemy3
    

if (difficultyChoice == 1):
    end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1 = loadMap()
elif (difficultyChoice == 2):
    end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1, enemy2 = loadMap()
elif (difficultyChoice == 3):
    end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1, enemy2, enemy3 = loadMap()

clock = pygame.time.Clock()

def redrawGameWindow():
    win.fill(white)
    for wall in walls:
        pygame.draw.rect(win, black, wall.rect)
    pygame.draw.rect(win, green, end_rect)
    pygame.draw.rect(win, blue, start_rect)
    pygame.draw.rect(win, gold, portalEntrace_rect)
    pygame.draw.rect(win, silver, portalExit_rect)
    if (difficultyChoice == 1):
        enemy1.draw(win)
    if (difficultyChoice == 2):
        enemy1.draw(win)
        enemy2.draw(win)
    if (difficultyChoice == 3):
        enemy1.draw(win)
        enemy2.draw(win)
        enemy3.draw(win)
    circle.draw(win)
    pygame.display.update()

def teleport():
    circle.x = portalExit_rect.x + 5
    circle.y = portalExit_rect.y + 5
    circle.rect.x = portalExit_rect.x + 5
    circle.rect.y = portalExit_rect.y + 5

origVelocity = circle.velocity
sprintMult = 3

run = True
t0 = pygame.time.get_ticks()
while run:
    clock.tick(144)
    tfinal = (pygame.time.get_ticks() - t0) / 1000
    pygame.display.set_caption("The Maze: Death Counter: " + str(deathCounter) + " | Difficulty Time - " + str(timeRemaining) + " | Your Time - " + str(tfinal))

    i = math.floor(tfinal) * difficultySpeed
    if (255 - i < 0):
        raise SystemExit("You lose!")
    white = (255, 255 - i, 255 - i)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and circle.y > circle.radius: 
        circle.move(0, -1 * circle.velocity)
        if (difficultyChoice == 1):
            enemy1.move(i)
        elif (difficultyChoice == 2):
            enemy1.move(i)
            enemy2.move(i)
        elif (difficultyChoice == 3):
            enemy1.move(i)
            enemy2.move(i)
            enemy3.move(i)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                #circle.rect.top = wall.rect.bottom
                #circle.y = wall.rect.bottom + circle.radius
    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and circle.y < screenHeight - circle.radius: 
        circle.move(0, circle.velocity)
        if (difficultyChoice == 1):
            enemy1.move(i)
        elif (difficultyChoice == 2):
            enemy1.move(i)
            enemy2.move(i)
        elif (difficultyChoice == 3):
            enemy1.move(i)
            enemy2.move(i)
            enemy3.move(i)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                #circle.rect.bottom = wall.rect.top
                #circle.y = wall.rect.top - circle.radius
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and circle.x > circle.radius: 
        circle.move(-1 * circle.velocity, 0)
        if (difficultyChoice == 1):
            enemy1.move(i)
        elif (difficultyChoice == 2):
            enemy1.move(i)
            enemy2.move(i)
        elif (difficultyChoice == 3):
            enemy1.move(i)
            enemy2.move(i)
            enemy3.move(i)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                #circle.rect.left = wall.rect.right
                #circle.x = wall.rect.right + circle.radius
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and circle.x < screenWidth - circle.radius: 
        circle.move(circle.velocity, 0)
        if (difficultyChoice == 1):
            enemy1.move(i)
        elif (difficultyChoice == 2):
            enemy1.move(i)
            enemy2.move(i)
        elif (difficultyChoice == 3):
            enemy1.move(i)
            enemy2.move(i)
            enemy3.move(i)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                restart()
                #raise SystemExit("You lose!")
                #circle.rect.right = wall.rect.left
                #circle.x = wall.rect.left - circle.radius
    if (pressed[pygame.K_r]):
        if (difficultyChoice == 1):
            end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1 = loadMap()
        elif (difficultyChoice == 2):
            end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1, enemy2 = loadMap()
        elif (difficultyChoice == 3):
            end_rect, start_rect, portalEntrace_rect, portalExit_rect, enemy1, enemy2, enemy3 = loadMap()
        redrawGameWindow()
        t0 = pygame.time.get_ticks()
    if (pressed[pygame.K_LSHIFT]):
        circle.velocity = origVelocity * sprintMult
    
    if (not pressed[pygame.K_LSHIFT]):
        circle.velocity = origVelocity

    if circle.rect.colliderect(end_rect):
        print("You win!")
        run = False
    
    if (difficultyChoice == 1):
        if circle.rect.colliderect(enemy1.rect):
            restart()
    if (difficultyChoice == 2):
        if circle.rect.colliderect(enemy1.rect):
            restart()
        if circle.rect.colliderect(enemy2.rect):
            restart()
    if (difficultyChoice == 3):
        if circle.rect.colliderect(enemy1.rect):
            restart()
        if circle.rect.colliderect(enemy2.rect):
            restart()
        if circle.rect.colliderect(enemy3.rect):
            restart()

    if circle.rect.colliderect(portalEntrace_rect):
        teleport()

    redrawGameWindow()

