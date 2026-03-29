import pygame

# Colors
BackgroundColor = "#333333"
PointColor = "#E3DC1D"

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


def lerp(min, max, t):
    return min+t*(max-min)


def toScreen(pos):
    return (((pos.real+1)/2)*width, 
            ((1-pos.imag)/2)*height)

a = complex(0.5,2/3)
b = complex(-1,1)

class Game:
    def __init__(self):
        self.running = True
        self.t = 0
    def run(self):
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
            self.update()
            pygame.display.flip() # Update Screen

    def update(self):
        pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
        LerpedPoint = lerp(a,b,self.t)
        print(toScreen(LerpedPoint))
        pygame.draw.circle(Screen, PointColor, toScreen(LerpedPoint), 5)
    
    def leftClick(self,MousePos):
        return
    
    def rightClick(self,MousePos):
        return

    def mwheel(self,e):
        self.t = max(min(self.t + e.y*0.05,1),0)

game = Game()
game.run()