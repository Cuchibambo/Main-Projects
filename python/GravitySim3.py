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
        self.bodies = [
            Body(
                mass = 1000000000000000
            )
        ]
        self.running = False
        self.PlacingMass = 100000
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
    
    def Update(self):
        pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
        for body in self.bodies:
            if body.isDestroyed: self.bodies.remove(body)
        uncheckBodies = self.bodies.copy()
        for body in self.bodies:
            uncheckBodies.remove(body)
            for b in uncheckBodies:
                F1 = body.calculateForce(b)
                F2 = (-F1[0],-F1[1])
                body.forces.append(F1)
                b.forces.append(F2)
            body.updatePos()
            body.draw()
    
    def leftClick(self,MousePos):
        self.bodies.append(
            Body(
                pos = MousePos,
                speed = (0,0),
                mass  = self.PlacingMass
            )
        )
    
    def rightClick(self,MousePos):
        return
        
    def mwheel(self,e):
        self.PlacingMass += e.y
        print(f'mass = {self.PlacingMass}')

class Body:
    def __init__(self,pos=(250,250),speed=(0,0),acceleration=(0,0),mass=1) -> None:
        self.pos = pos
        self.speed = speed
        self.acceleration = acceleration
        self.mass = mass
        self.forces = []
        self.isDestroyed = False
    
    def updatePos(self):
        self.pos = (self.pos[0] + self.speed[0]*dt,
                    self.pos[1] + self.speed[1]*dt)
        self.speed = (self.speed[0] + self.acceleration[0]*dt,
                      self.speed[1] + self.acceleration[1]*dt)
        fX, fY = 0, 0
        for f in self.forces:
            fX += f[0]
            fY += f[1]
        self.acceleration = (fX/self.mass,fY/self.mass)
        if 0 > self.pos[0] or self.pos[0] > width or 0 > self.pos[1] or self.pos[1] > height:
            self.destroy()
        
    def destroy(self):
        self.isDestroyed = True
    
    def draw(self):
        pygame.draw.circle(Screen,BodyColor,self.pos,5)
        
    def calculateForce(self,body):
        dx, dy = body.pos[0]-self.pos[0], body.pos[1]-self.pos[1]
        r = ((dx**2)+(dy**2)**0.5)
        rvec = (dx/r,dy/r)
        F = (self.mass*body.mass*G)/(r**2)
        Fvec = (F*rvec[0],F*rvec[1])
        return Fvec
        

sim = Sim()
sim.start()