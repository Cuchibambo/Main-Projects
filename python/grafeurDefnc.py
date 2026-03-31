import pygame

# Colors
BackgroundColor = "#81abc0"
PointColor = "#35085c"


class Game:
    def __init__(self) -> None:
        self.running = False
    def leftClick(self,Mousepos):
        self.update(lambda x,y:((x-250)**2)+((y-250)**2)-1000)
    def rightClick(self,Mousepos):
        pass
    def mwheel(self,e):
        pass
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.leftClick(pygame.mouse.get_pos())
                        case 3:
                            self.rightClick(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEWHEEL:
                    self.mwheel(event)
            # main loop
            # pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # empty
            
            
            
            pygame.display.flip()
    def update(self, func):
        signs = []
        for y in range(height+1):
            line = []
            for x in range(width+1):
                value = func(x,y)
                if value == 0:
                    pygame.draw.rect(screen, PointColor, (x,y,1,1))
                    sign = 1
                else:
                    sign = abs(value)/value
                line.append(sign)
            signs.append(line)
        # signs = [[abs(func(x,y))/func(x,y) for x in range(width+1)] for y in range(height+1)]
        for x in range(width):
            for y in range(height):
                if not (signs[y][x] == signs[y][x+1]  and signs[y][x] == signs[y+1][x] and signs[y][x] == signs[y+1][x+1]):
                    pygame.draw.rect(screen, PointColor, (x,y,1,1))
                 
                
                
                       
        
# Pygame  
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()


# Start
game = Game()
game.run()