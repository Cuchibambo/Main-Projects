import pygame

# Colors
background_color = "#404040"

pygame.init()
res = 500
screen = pygame.display.set_mode((res,res))

class Window:
    def __init__(self) -> None:
        self.running = False
        self.grid = 
    def run(self):
        self.running = True
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.running = False
            screen.fill(background_color)
            self.update()
            pygame.display.flip()
    def update(self):
        self.draw()
    def draw(self):
        for line in self.grid:
            for item in line:
                
    
class Grid:
    
    