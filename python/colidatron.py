import pygame

# Colors
background_color = "#464646"
obj_color = "#A02E2E"

pygame.init()
res = 500
screen = pygame.display.set_mode((res,res))

class Box2D:
    def __init__(self,origin=(res/2,res/2),sizeX=1,sizeY=1,rotation=0,scale=1) -> None:
        self.origin = origin
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.rotation = rotation
        self.scale = scale
    def draw(self):
        pass

class Circle2D:
    def __init__(self,pos=(res/2,res/2),radius=1,scale=1) -> None:
        self.pos = pos
        self.radius = radius
        self.scale = scale
    def draw(self):
        pygame.draw.circle(screen,obj_color,self.pos,self.radius)
    
class Window:
    def __init__(self) -> None:
        self.running = False
        self.rigidBodies = {Circle2D(radius=25)}
    def run(self):
        self.running = True
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    quit()
            screen.fill(background_color)
            self.update()
            pygame.display.flip()
    def update(self):
        for rb in self.rigidBodies:
            rb.draw()

window = Window()
window.run()