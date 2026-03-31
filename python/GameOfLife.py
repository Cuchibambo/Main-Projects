import pygame

# Colors
BackgroundColor = "#222328" # Grid line color
DeadCellColor = "#2c2e2f"
AliveCellColor = "#dadfe3"

# Rules
# 1 or no alive dies
# 4 or more alive dies
# 2 or 3 stays alive
# 3 born



class Cell:
    def __init__(self,gridSize) -> None:
        self.state = False
        self.gridSize = gridSize
        self.cellSize = resolution/gridSize
    
    # def updateState(self,localGrid):
    #     aliveCount = 0
    #     for x in range(3):
    #         for y in range(3):
    #             if x != 1 or y != 1:
    #                 if localGrid[x][y].state: aliveCount += 1
    #                 if (x,y) == (1,1):
    #                     print(aliveCount)
    #     if 1 >= aliveCount or 4 <= aliveCount:
    #         self.state = False
    #     elif aliveCount == 3:
    #         self.state = True
            
    
    def draw(self,pos):
        if self.state: color = AliveCellColor
        else: color = DeadCellColor
        gap = gridLineSize/2
        pygame.draw.rect(screen,color,((resolution+self.cellSize*(pos[0]-self.gridSize))+gap,
                                       (resolution+self.cellSize*(pos[1]-self.gridSize))+gap,
                                       self.cellSize-gap,
                                       self.cellSize-gap))
                


class Grid:
    def __init__(self,size) -> None:
        self.grid = []
        self.size = size
    def generateGrid(self):
        self.grid = [[Cell(self.size) for _ in range(self.size)] for _ in range(self.size)]
    
    def updateGrid(self):
        grid_copy = [[self.grid[x][y].state for y in range(self.size)] for x in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                aliveCount = 0
                for X in [-1, 0, 1]:
                    for Y in [-1, 0, 1]:
                        if X != 0 or Y != 0:
                            if grid_copy[(x+X)%self.size][(y+Y)%self.size]: aliveCount += 1
                if lowerLimit >= aliveCount or aliveCount >= upperLimit:
                    self.grid[x][y].state = False
                if aliveCount == creationAmount:
                    self.grid[x][y].state = True
                            
                
    def drawGrid(self):
        for y, line in enumerate(self.grid):
            for x, cell in enumerate(line):
                cell.draw((x, y))


class Game:
    def __init__(self, size=20) -> None:
        self.running = False
        self.size = size
        self.grid = Grid(self.size)
        
    def leftClick(self,Mousepos):
        gridPos = (int(Mousepos[0]*gridSize/resolution),int(Mousepos[1]*gridSize/resolution))
        self.grid.grid[gridPos[1]][gridPos[0]].state = not self.grid.grid[gridPos[1]][gridPos[0]].state
    def rightClick(self,Mousepos):
        self.play = not self.play
    def mwheel(self,e):
        pass
    def run(self):
        self.running = True
        self.grid.generateGrid()
        self.play = False
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
                elif event.type == UPDATEEVENT:
                    if self.play: self.update()
                    
            pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, resolution, resolution)) # empty
            self.grid.drawGrid()
            pygame.display.flip()
            
    def update(self):
        self.grid.updateGrid()
            
        
# Pygame  
pygame.init()
resolution = 500
screen = pygame.display.set_mode((resolution, resolution))
pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, resolution, resolution))
pygame.display.flip()

# Time 
UPDATEEVENT = pygame.USEREVENT+1


# Start
gridSize = 25
gridLineSize = 0
secondsPerUpdate = 0.1
pygame.time.set_timer(UPDATEEVENT,int(secondsPerUpdate*1000))

# Game settings
lowerLimit = 1
upperLimit = 4
creationAmount = 3

game = Game(gridSize)
game.run()