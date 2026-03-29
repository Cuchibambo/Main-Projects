import pygame
import math

# Colors
backgroundColor = "#242424"
penColor = "#f3eb0e"

def toScreen(pos):
    uv = ((pos[0]+2)/4,
          (-pos[1]+2)/4)
    screenPos = (uv[0]*width, uv[1]*height)
    return screenPos


# Objects
class Arrow:
    def __init__(self, startingAngle, frequencie, Amplitude):
        self.startingAngle = startingAngle
        self.frequencie = frequencie
        self.Amplitude = Amplitude
        self.previousPos = self.getPos(0)
        self.isTip = False
    def getPos(self, t):
        localpos = (self.Amplitude*math.cos(self.frequencie*t+self.startingAngle), 
                    self.Amplitude*math.sin(self.frequencie*t+self.startingAngle))
        return localpos
    def draw(self,center,t):
        localPos = self.getPos(t)
        startPos = (center[0]+localPos[0],
                    center[1]+localPos[1])
        if self.isTip:
            pygame.draw.line(screen, penColor, toScreen(startPos), toScreen(self.previousPos))
        self.previousPos = startPos
        return startPos

class Game:
    def __init__(self):
        self.arrows = []
        self.speed = 1
        self.t = 0
    
    def fourierSeries(self):
        for n in range(-10,11):
            frequencie = n
            Amplitude = 
            self.arrows.append(Arrow(0, frequencie, Amplitude))

    def run(self):
        self.arrows[-1].isTip = 1
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    quit()
            # main loop
            clock.tick(FPS)
            # pygame.draw.rect(screen, backgroundColor, pygame.Rect(0, 0, width, height)) # empty
            self.update()
            self.t+=self.speed*dt
            pygame.display.flip()
    def update(self):
        center = [0,0]
        for arrow in self.arrows:
            arrowPos = arrow.draw(center,self.t)
            center[0] += arrowPos[0]
            center[1] += arrowPos[1]

# pygame
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width,height))
pygame.draw.rect(screen, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

game = Game()
game.arrows = [Arrow(0,1,1),
               Arrow(2,2,1/2),
               Arrow(12,21,0.01)]
game.run()