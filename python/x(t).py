import pygame
import cmath

# Class and Function Definitions
class Ball:
    def __init__(self,pos,color,size) -> None:
        self.pos = pos
        self.color = color
        self.size = size

def drawBall(screen,ball:Ball):
    pygame.draw.circle(screen,ball.color,ball.pos,ball.size)
    
def MovementFunction(t):
    # x(t) = e^st
    return cmath.exp(s1*t)+cmath.exp(s2*t)

def Pypos_to_worldpos(pos):
    Xmult, Ymult = width/2, height/2
    X, Y = pos[0], pos[1]
    x, y = (X/Xmult)-1, -((Y/Ymult)-1)
    return (x,y)
    
def Worldpos_to_pypos(pos):
    Xmult, Ymult = width/2, height/2
    x, y = pos[0], pos[1]
    X, Y = (x+1)*Xmult, (-y+1)*Ymult
    return (X, Y)

def CalcDiffEqua(a,b,c):
    # ay''+by'+cy=0
    sqrt = cmath.sqrt((b**2)-(4*a*c))
    s1 = (-b+sqrt)/(2*a)
    s2 = (-b-sqrt)/(2*a)
    return s1, s2

def AskForInput():
    global a, b, c, t
    SelectedVar = input("Change a, b, c or t: ")
    Value = None
    while Value == None:
        try:
            Value = float(input("New value: "))
        except:
            print('Invalid value input')
    if SelectedVar == 'a':
        a = Value
    elif SelectedVar == 'b':
        b = Value
    elif SelectedVar == 'c':
        c = Value
    elif SelectedVar == 't':
        t = Value
    else:
        print('invalid var')
    
# Colors
backgroundColor = "#414141"
redColor = "#ac3a3a"
blackColor = "#1b1b1b"

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
width,height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time and delta time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

# Objects
t = 0
a, b, c = -0.02, -0.005, -0.25
s1, s2 = CalcDiffEqua(a,b,c)
redBall = Ball(Worldpos_to_pypos((0,0)),redColor,10)
blackBall = Ball((0.0,0.0),blackColor,12)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                AskForInput()
    
    clock.tick(FPS) # appply fps
    pygame.draw.rect(Screen, backgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
    
    # Udate loop
    ComplexPos = MovementFunction(t)
    RealPos = ComplexPos.real
    pyPos = Worldpos_to_pypos((RealPos,0))
    redBall.pos = pyPos
    blackBall.pos = redBall.pos
    
    # Draw Balls
    drawBall(Screen,blackBall)
    drawBall(Screen,redBall)
    
    t += dt # update time
    pygame.display.flip() # Update Screen
    
