import pygame
from math import cos, sin, sqrt

# Colors
BackgroundColor = "#333333"
ObjectColor = "#A63434"
FloorColor = "#464646"

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
pygame.font.init()
Textfont = pygame.font.SysFont('Segoe UI Symbol', 45, bold=False)
width,height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time and delta time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS
PI = 3.141592654

class Sim:
    def __init__(self):
        self.running = True
        self.g = 9.8
        self.objects = []
        self.floor = Floor()

    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.leftClick(pygame.mouse.get_pos())
                        case 3:
                            self.rightClick(pygame.mouse.get_pos())
            clock.tick(FPS) # appply fps
            self.update()
            pygame.display.flip() # Update Screen

    def update(self):
        pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
        self.floor.draw()
        for o in self.objects:
            o.updatePos(self.g)
            o.draw()
    
    def leftClick(self,MousePos):
        self.objects.append(Object(
            pos=MousePos
        ))
    
    def rightClick(self,MousePos):
        return

class Floor:
    def __init__(self,pos=(250,450),rotation=0) -> None:
        self.pos = pos
        self.rotation = rotation
    
    def clampPos(self,pos,range):
        x, y = pos[0], pos[1]
        up, down = range[0], range[1]
        if x > up: x = up
        if x < down: x = down
        if y > up: y = up
        if y < down: y = down
        return (x,y)
    
    def verifyPoint(self,pos,a,b,c):
        return a*pos[0]+b*pos[1]+c>0
    
    def getPoints(self):
        points = []
        self.rotation %= 2*PI
        corners = [(500,500),(500,0),(0,0),(0,500)]
        # if 0 < self.rotation and self.rotation < PI/4:
        #     points.append(corners[1])
        #     points.append(corners[4])
        # elif self.rotation < 5*PI/4:
        #     points.append(corners[2])
        #     points.append(corners[1])
        # elif self.rotation < 9*PI/4:
        #     points.append(corners[3])
        #     points.append(corners[2])
        # elif self.rotation < 13*PI/4:
        #     points.append(corners[4])
        #     points.append(corners[3])
        cirlce_radius = sqrt(2*(width**2))
        angleCos, angleSin = cos(self.rotation), sin(self.rotation)
        points.append(self.clampPos((cirlce_radius*angleCos+self.pos[0], 
                                     cirlce_radius*angleSin+self.pos[1]),(0,width)))
        points.append(self.clampPos((cirlce_radius*cos(self.rotation+PI)+self.pos[0], 
                                     cirlce_radius*sin(self.rotation+PI)+self.pos[1]),(0,width)))
        c = -angleSin*self.pos[0]-angleCos*self.pos[1]
        for corner in corners:
            if self.verifyPoint(corner,angleSin,angleCos,c):
                points.append(corner)
        return points
    
    def draw(self):
        pygame.draw.polygon(Screen,FloorColor,[(0,450),(500,450),(500,500),(0,500)])
    
class Object:
    def __init__(self, mass=1,pos=(250,250),speed=(0,0),acceleration=(0,0)) -> None:
        self.mass = mass
        self.pos = pos
        self.speed = speed
        self.acceleration = acceleration
    
    def updatePos(self,g):
        self.pos = (self.pos[0] + self.speed[0]*dt, self.pos[1] + self.speed[1]*dt)
        self.speed = (self.speed[0] + self.acceleration[0]*dt, self.speed[1] + self.acceleration[1]*dt)
        self.acceleration = (0,g)
    
    def draw(self):
        pygame.draw.circle(Screen,ObjectColor,self.pos,5)
        

sim = Sim()
sim.start()