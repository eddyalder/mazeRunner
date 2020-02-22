import pygame
from random import *
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

#screen setup
screenWidth = 800
screenHeight = 800

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
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)

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
#print(arr)
x = randint(1,rows-2)
y = randint(1,cols-2)
while(arr[x-1][y] != 0 or arr[x+1][y] != 0):
    x = randint(1,rows-2)
    y = randint(1,cols-2)
arr[x][y] = 2
level = []
for i in range(rows):
    wString = ""
    for j in range(cols):
        if(arr[i][j] == 1):
            wString += "W"
        elif(arr[i][j] == 2):
            wString += "E"
        else:
            wString += " "
    level.append(wString)


clock = pygame.time.Clock()
walls = []
circle = Player(100,100,red,4)


x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

def redrawGameWindow():
    win.fill(white)
    circle.draw(win)
    for wall in walls:
        pygame.draw.rect(win, black, wall.rect)
    pygame.draw.rect(win, green, end_rect)
    pygame.display.update()

run = True

while run:
    clock.tick(144)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and circle.y > circle.radius: 
        circle.move(0, -1 * circle.velocity)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                circle.rect.top = wall.rect.bottom
                circle.y = wall.rect.bottom + circle.radius
    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and circle.y < screenHeight - circle.radius: 
        circle.move(0, circle.velocity)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                circle.rect.bottom = wall.rect.top
                circle.y = wall.rect.top - circle.radius
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and circle.x > circle.radius: 
        circle.move(-1 * circle.velocity, 0)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                circle.rect.left = wall.rect.right
                circle.x = wall.rect.right + circle.radius
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and circle.x < screenWidth - circle.radius: 
        circle.move(circle.velocity, 0)
        for wall in walls:
            if (circle.rect.colliderect(wall.rect)):
                circle.rect.right = wall.rect.left
                circle.x = wall.rect.left - circle.radius

    if circle.rect.colliderect(end_rect):
        print("Yessir")
        raise SystemExit("You win!")
    #print("real x", circle.x, "real y", circle.y)
    #print("x", circle.rect.x, "y", circle.rect.y)
    redrawGameWindow()


# for wall in walls:
#             if self.rect.colliderect(wall.rect):
#                 if dx > 0: # Moving right; Hit the left side of the wall
#                     self.rect.right = wall.rect.left
#                 if dx < 0: # Moving left; Hit the right side of the wall
#                     self.rect.left = wall.rect.right
#                 if dy > 0: # Moving down; Hit the top side of the wall
#                     self.rect.bottom = wall.rect.top
#                 if dy < 0: # Moving up; Hit the bottom side of the wall
#                     self.rect.top = wall.rect.bottom