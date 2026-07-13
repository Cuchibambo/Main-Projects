import pygame

# colors
cp_color = "#fafaf6"
bg_color = "#1b1b1b"

class controlPoint:
    def __init__(self, pos) -> None:
        self.pos = pos
    
    def draw(self):
        pygame.draw.circle(screen,cp_color,self.pos,5)




class Game:
    def lerp(self,min,max,t):
        return (max[0] + t*(min[0]-max[0]),
                max[1] + t*(min[1]-max[1]))
    def __init__(self) -> None:
        self.running = False
        self.cp_amount = 5
        self.control_points = [[controlPoint((250,250)),controlPoint((250,350)),controlPoint((150,350)),controlPoint((150,250)),controlPoint((100,450))]]
        for j in range(1,4):
            cps = [controlPoint(self.control_points[0][i].pos) for i in range(self.cp_amount-j)]
            self.control_points.append(cps)
        self.t = 0
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()
                    pygame.quit()
                if event.type == pygame.MOUSEWHEEL:
                    self.t += event.y*0.1
                    self.t = max(min(self.t,1),0)
                    
            self.update()
    def updateCps(self, level):
        for i,cp in enumerate(self.control_points[level]):
            cp.pos = self.lerp(self.control_points[level-1][i].pos,self.control_points[level-1][i+1].pos,self.t)
    def update(self):
        screen.fill(bg_color)
        for level,cps in enumerate(self.control_points):
            for cp in cps:
                if level != 0: self.updateCps(level)
                cp.draw()
        pygame.display.flip()



# pygame
pygame.init()
res = 500
screen = pygame.display.set_mode((res,res))

# Game settings
game = Game()
game.run()