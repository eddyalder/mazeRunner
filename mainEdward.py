import pygame
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

#screen setup
screenWidth = 700
screenHeight = 500

win = pygame.display.set_mode((screenWidth,screenHeight))
win.fill(white)
pygame.display.set_caption("The Maze")

class Player(object):
    def __init__(self,x,y,color,radius):
        self.x = x
        self.y = x
        self.color = red
        self.radius = radius
        self.velocity = 5

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)
    

def redrawGameWindow():
    win.fill(white)
    circle.draw(win)
    pygame.display.update()

clock = pygame.time.Clock()
circle = Player(100,100,red,12)
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