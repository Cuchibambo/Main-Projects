import pygame

G = (6.67*(10**(-11)))

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
        self.potentials = self.evaPotentialOnScreen()
        
    def start(self):
        self.running = True
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
    
    def EvaluatePotential(self,pos,body):
        Mass = body.mass
        dx, dy = body.pos[0]-pos[0], body.pos[1]-pos[1]
        r = (((dx**2)+(dy**2))**(1/2))
        if r == 0: return 0
        else: return G*Mass/r
    
    def EvaluateGravity(self,pos):
        for v in self.potentials:
            if v[0] == pos:
                dx, dy = self.bodies[0].pos[0]-pos[0], self.bodies[0].pos[1]-pos[1]
                r2 = (dx**2)+(dy**2)
                if r2 == 0: return (0,0)
                else:
                    g = (v[1]*dx/r2,v[1]*dy/r2)
                    print(g)
                    return g
    
    def displayPotentialOnScreen(self):
        for v in self.potentials:
            color = (v[1]*(10**13),0,0)
            if color[0] > 255: color = (255,0,0)
            pygame.draw.rect(Screen,color,(v[0][0],v[0][1],1,1))
    
    def evaPotentialOnScreen(self):
        Potentials = []
        for x in range(width):
            for y in range(height):
                phi = 0
                for body in self.bodies:
                    if not body.isMovable:
                        phi += self.EvaluatePotential((x,y),body)
                Potentials.append(((x,y),phi))
        return Potentials
    
    def Update(self):
        pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
        self.displayPotentialOnScreen()
        for body in self.bodies:
            body.draw()
            if body.isMovable:
                g = self.EvaluateGravity(body.pos)
                body.updatePos(g)
            
    def leftClick(self,MousePos):
        self.bodies.append(Body(
            True,
            MousePos,
            self.mass
        ))
    
    def rightClick(self,MousePos):
        self.bodies.append(Body(
            False,
            MousePos,
            self.mass
        ))
        self.potentials = self.evaPotentialOnScreen()
        
    def mwheel(self,e):
        self.mass += e.y
        print(f'mass = {self.mass}')
    
class Body:
    def __init__(self, isMovable=False, pos=(0,0), mass=1) -> None:
        self.isMovable = isMovable
        self.pos = pos
        self.mass = mass
    
    def draw(self):
        pygame.draw.circle(Screen,BodyColor,self.pos,(self.mass**0.5)+2)
        
    def updatePos(self,g):
        newpos = (self.mass*g[0]+self.pos[0], self.mass*g[1]+self.pos[0])
        self.pos = newpos
        
sim = Sim()
sim.start()