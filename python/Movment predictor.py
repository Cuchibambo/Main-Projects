import pygame
import math

# Initialize pygame
pygame.init()

# Set up the window (width, height)
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Movment Predictor")

Sstartingpos = [250,250]
Rstartingpos = [250,300]

class Sender:
    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)
    

class Receiver:    
    def __init__(self, pos):
        self.pos = pos
    def move(self, vel):
        self.pos[0] += vel[0]
        self.pos[1] += vel[1]

# Main loop
running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=0
    screen.fill('#1F1F1F')
    Sender1 = Sender(Sstartingpos)
    Receiver1 = Receiver(Rstartingpos)
    
    
    
    
    
    
    
    pygame.display.flip() 

# Quit pygame
pygame.quit()