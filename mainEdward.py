import pygame
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

#screen setup
screenWidth = 700
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))
win.fill(white)
pygame.display.set_caption("The Maze")

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

class Player(object):
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = x
        self.color = red
        self.radius = radius
        self.velocity = 5

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
    
level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]


clock = pygame.time.Clock()
walls = []
circle = Player(100,100,red,12)


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
    pygame.draw.rect(screen, green, end_rect)
    pygame.display.update()

run = True

while run:
    clock.tick(144)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pressed = pygame.key.get_pressed()
    if (pressed[pygame.K_UP] or pressed[pygame.K_w]) and circle.y > circle.radius: 
        circle.y -= circle.velocity
    if (pressed[pygame.K_DOWN] or pressed[pygame.K_s]) and circle.y < screenHeight - circle.radius: 
        circle.y += circle.velocity
    if (pressed[pygame.K_LEFT] or pressed[pygame.K_a]) and circle.x > circle.radius: 
        circle.x -= circle.velocity
    if (pressed[pygame.K_RIGHT] or pressed[pygame.K_d]) and circle.x < screenWidth - circle.radius: 
        circle.x += circle.velocity
    #print("x", x, "y", y)
    redrawGameWindow()