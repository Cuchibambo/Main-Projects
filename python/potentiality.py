import pygame

# Constants
PI = 3.141592654
g = 9.81

# Colors
background_color = "#333333"

class Main:
    def __init__(self):
        self.running = True
        # Time and delta time
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.dt = 1/self.FPS
    
    def toRGB(self,hsv_color:tuple) -> tuple:
        H = hsv_color[0]
        S = hsv_color[1]
        V = hsv_color[2]
        # H in degrees
        # S in 0-1
        # V in 0-1
        hR, hG, hB = 0, 0, 0
        H %= 360
        if H >= 0 and H < 60:
            hR = 1
            hG = H/60
        elif H >= 60 and H < 120:
            hR = (-H/60)+2
            hG = 1
        elif H >= 120 and H < 180:
            hG = 1
            hB = (H/60)-2
        elif H >= 180 and H < 240:
            hG = (-H/60)+4
            hB = 1
        elif H >= 240 and H < 300:
            hR = (H/60)-4
            hB = 1
        elif H >= 300 and H < 360:
            hR = 1
            hB = (-H/60)+6
            
        R = hR+1-S
        G = hG+1-S
        B = hB+1-S
        if R>1: R=1
        if G>1: G=1
        if B>1: B=1
        R *= V
        G *= V
        B *= V
        return (int(R*255),int(G*255),int(B*255))
        
    def CalculatePotential(self):
        for x in range(self.width):
            for y in range(self.height):
                potential = (y*g)/(self.height*g)
                color = self.toRGB((203,potential,1))
                pygame.draw.rect(self.screen,color,(x,y,1,1))
    
    def run(self):
        # Start Pygame
        pygame.init()
        self.font = pygame.font.SysFont('Monospace', 22, bold=False)
        self.width, self.height = 500, 500
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill(background_color)
        self.CalculatePotential()
        pygame.display.flip()
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
            self.clock.tick(self.FPS) # appply fps
            self.update()
            pygame.display.flip() # Update Screen

    def update(self):
        # self.screen.fill(background_color)
        pass
    
    def leftClick(self,MousePos):
        return
    
    def rightClick(self,MousePos):
        return

main = Main()
main.run()