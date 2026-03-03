import pygame
import numpy as np
import cmath
import ImageToComplexArray
from PIL import Image

# Colors
BackgroundColor = "#111111"
TraceColor = "#e3c958"

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
pygame.font.init()
Textfont = pygame.font.SysFont('Segoe UI Symbol', 45, bold=False)
width,height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time and delta time
FPS = 360
clock = pygame.time.Clock()
dt = 1/FPS

class Sim:
    def __init__(self):
        self.t = 0
        self.isArrowVisible = False
        self.ArrowsAmount = 100
        self.imagepath = r'Images\Circle.png'
        self.arrowSet = None
        self.ImageData = None
        self.interval = 15*cmath.pi
        self.speed = 1
    def draw(self):
        self.arrowSet.draw(self.isArrowVisible)
    def start(self):
        img = Image.open(self.imagepath)
        self.arrowSet = ArrowSet()
        s = [complex(50,0),
             complex(0,-50),
             complex(-50,0),
             complex(0,100)]
        for n in range(-self.ArrowsAmount,self.ArrowsAmount+1):
            cn = 0
            for i in range(len(s)):
                cn += s[i]*cmath.exp(complex(0,-n*i*2*cmath.pi/self.interval))
            cn = cn/2*cmath.pi
            self.arrowSet.arrows.append(Arrow(cn,n*2*cmath.pi/self.interval,cmath.pi/2))
        
        
        
        
        # self.ImageData = CIC(self.imagepath)


        
        # array = np.fft.fft(self.ImageData).imag
        
        # array = array[array.size//2+1:]
        # array = array[:200]
        # print(array)
        # self.arrowSet.arrows = []
        # for n in range(array.size):
        #     Size =  array[n]/251
        #     f =     n+1
        #     sa =    0
        #     self.arrowSet.arrows.append(Arrow(Size,f,sa))
        
        
        self.arrowSet.arrows = [Arrow(20*3.2,-0.4,3.2),
                                Arrow(20,2,0),
                                Arrow(20,3,0),
                                Arrow(20,4,0),
                                Arrow(20,5,0),
                                Arrow(20,6,0),
                                Arrow(20,7,0),
                                Arrow(20,8,0),
                                Arrow(20,9,0),
                                Arrow(20,10,0),]
        
        
        
        
        
        
        # self.arrowSet.arrows = arrows
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.isArrowVisible = self.isArrowVisible == False
                        pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
                elif event.type == pygame.MOUSEWHEEL:
                    self.speed += event.y
                    print(f'Speed = {self.speed}')
            clock.tick(FPS) # appply fps
            self.Update()
            pygame.display.flip() # Update Screen
    def Update(self):
        if self.isArrowVisible: pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
        self.arrowSet.update(self.t)
        self.draw()
        self.t += dt*self.speed
        
    
class ArrowSet:
    def __init__(self) -> None:
        self.arrows = []
    def update(self,t):
        self.arrows[-1].isTip = True
        pos = [width/2,height/2]
        for arrow in self.arrows:
            arrow.pos = pos
            arrow.update(t)
            pos = [pos[0] + arrow.vec[0], pos[1] + arrow.vec[1]]
    def draw(self,isArrowVisible):
        for arrow in self.arrows:
            arrow.draw(isArrowVisible)

class Arrow:
    def __init__(self, size, frequencie, StartingAngle) -> None:
        self.isTip = False
        self.size = size
        self.frequencie = frequencie
        self.pos = []
        self.vec = [0,0]
        self.StartingAngle = StartingAngle
        self.angle = StartingAngle
    def update(self,t):
        self.angle = (self.frequencie*t)+self.StartingAngle
        vecX = self.size*np.cos(self.angle)
        vecY = self.size*np.sin(self.angle)
        self.vec = [vecX,vecY]
    def draw(self,isArrowVisible):
        if isArrowVisible:
            pygame.draw.line(Screen,TraceColor,self.pos,(self.pos[0]+self.vec[0],self.pos[1]+self.vec[1]))
        if self.isTip:
            pygame.draw.rect(Screen,TraceColor,(self.pos[0]+self.vec[0],self.pos[1]+self.vec[1],1,1))

sim = Sim()
sim.start()