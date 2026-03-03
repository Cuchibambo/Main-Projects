import pygame

G = (6.67*(10**(-11)))
PI = 3.141592654

# Colors
BackgroundColor = "#111111"
BodyColor = "#e3c958"

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

class Sim:
    def __init__(self) -> None:
        self.bodies = []
        self.running = False
        self.mass = 1
        
    def start(self):
        self.running = True
        self.immovableBody = Body(
            mass=       100000000,
            volume=     5
        )
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.leftClick(pygame.mouse.get_pos())
                        case 3:
                            self.rightClick(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEWHEEL:
                    self.mwheel(event)
            clock.tick(FPS) # appply fps
            self.Update()
            pygame.display.flip() # Update Screen
    
    def Update(self):
        pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
        self.immovableBody.draw()
        for body in self.bodies:
            body.draw()
            g = body.Calculateg(self.immovableBody)
            body.Updatepos(g)
    
    def leftClick(self,MousePos):
        self.bodies.append(
            Body(
                mass=       self.mass,
                pos=        MousePos,
                volume=     1
            )
        )
    
    def rightClick(self,MousePos):
        return
        
    def mwheel(self,e):
        self.mass += e.y
        print(f'mass = {self.mass}')

class Body:
    def __init__(self,mass=1,pos=(250,250),volume=1) -> None:
        self.mass = mass
        self.pos = pos
        self.volume = volume

    def draw(self):
        pygame.draw.circle(Screen,BodyColor,self.pos,self.volume)
        
    def Calculateg(self,attractionBody):
        dx, dy = attractionBody.pos[0]-self.pos[0], attractionBody.pos[1]-self.pos[1]
        ro = attractionBody.mass/attractionBody.volume
        a = 8*PI*G*ro/3
        g = (a*dx, a*dy)
        return g

    def Updatepos(self,vec):
        self.pos = (self.pos[0]+vec[0]*self.mass,
                    self.pos[1]+vec[1]*self.mass)
        

sim = Sim()
sim.start()