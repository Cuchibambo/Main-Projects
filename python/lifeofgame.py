import pygame

# Colors
BackgroundColor = "#2b2c2d"
AliveCellColor = "#f2f3f4"
RedTeamColor = "#bb1c1c"
BlueTeamColor = "#365bbf"
DeadCellColor = "#1C1C1E"

class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.state = False
        self.team = 'RED'
    def draw(self):
        if self.state:
            if self.team == 'RED': color = RedTeamColor
            else: color = BlueTeamColor
        else: color = DeadCellColor
        cellSize = resolution/GridSize
        pygame.draw.rect(screen,color, (resolution+cellSize*(self.pos[0]-GridSize)+GridLinesWidth,
                                        resolution+cellSize*(self.pos[1]-GridSize)+GridLinesWidth,
                                        cellSize-GridLinesWidth,
                                        cellSize-GridLinesWidth))
        


class Game:
    def __init__(self) -> None:
        self.running = False
        self.playing = False
        self.grid = [[Cell((x,y)) for x in range(GridSize)] for y in range(GridSize)]
    def leftClick(self,Mousepos):
        RedCount, BlueCount = self.countColors()
        if RedCount < maxRed:
            GridPos = int(Mousepos[0]*GridSize/resolution),int(Mousepos[1]*GridSize/resolution)
            State = self.grid[GridPos[1]][GridPos[0]].state
            Team = self.grid[GridPos[1]][GridPos[0]].team
            if not State:
                self.grid[GridPos[1]][GridPos[0]].state = not self.grid[GridPos[1]][GridPos[0]].state
                self.grid[GridPos[1]][GridPos[0]].team = 'RED'
            else:
                if Team == 'RED':
                    self.grid[GridPos[1]][GridPos[0]].state = False
                else:
                    self.grid[GridPos[1]][GridPos[0]].team = 'RED'
    def rightClick(self,Mousepos):
        RedCount, BlueCount = self.countColors()
        if BlueCount < maxBlue:
            GridPos = int(Mousepos[0]*GridSize/resolution),int(Mousepos[1]*GridSize/resolution)
            State = self.grid[GridPos[1]][GridPos[0]].state
            Team = self.grid[GridPos[1]][GridPos[0]].team
            if not State:
                self.grid[GridPos[1]][GridPos[0]].state = not self.grid[GridPos[1]][GridPos[0]].state
                self.grid[GridPos[1]][GridPos[0]].team = 'BLUE'
            else:
                if Team == 'BLUE':
                    self.grid[GridPos[1]][GridPos[0]].state = False
                else:
                    self.grid[GridPos[1]][GridPos[0]].team = 'BLUE'
    def play(self):
        self.playing = not self.playing
    def mwheel(self,e):
        pass
    def draw(self):
        screen.fill(BackgroundColor)
        for line in self.grid:
            for cell in line:
                cell.draw()
        
        RedCount, BlueCount = self.countColors()

        RenderedText = Textfont.render(f'Red population : {RedCount} | Blue population : {BlueCount}',True,AliveCellColor)
        TextRect = RenderedText.get_rect(center=(resolution*0.5,resolution*0.1))
        screen.blit(RenderedText,TextRect)

        pygame.display.flip()
        
    def update(self):
        grid_copy = [[(self.grid[y][x].state,self.grid[y][x].team) for x in range(GridSize)] for y in range(GridSize)]
        for x in range(GridSize):
            for y in range(GridSize):
                AliveCount = 0
                BlueCount = 0
                RedCount = 0
                currentCell = self.grid[y][x]
                for X in [-1,0,1]:
                    for Y in [-1,0,1]:
                        if (X != 0 or Y != 0) and grid_copy[(y+Y)%(GridSize-1)][(x+X)%(GridSize-1)][0]:
                            AliveCount += 1
                            if grid_copy[(y+Y)%(GridSize-1)][(x+X)%(GridSize-1)][1] == 'RED':
                                RedCount += 1
                            else: BlueCount += 1
                if overpopulationtrhreashold < AliveCount or AliveCount < underpopulationthreashold:
                    currentCell.state = False
                if AliveCount == birthpopulationamount:
                    currentCell.state = True
                    if RedCount > BlueCount:
                        currentCell.team = 'RED'
                    else: currentCell.team = 'BLUE'
    def countColors(self):
        RedCount = 0
        BlueCount = 0
        for x in range(GridSize):
            for y in range(GridSize):
                if self.grid[y][x].state:
                    if self.grid[y][x].team == 'RED':
                        RedCount += 1
                    elif self.grid[y][x].team == 'BLUE':
                        BlueCount += 1
        return RedCount, BlueCount
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
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            self.play()
                elif event.type == pygame.MOUSEWHEEL:
                    self.mwheel(event)
                elif event.type == UPDATEEVENT and self.playing:
                        self.update()
            self.draw()
            
            

# Game settings
GridSize = 50
GridLinesWidth = 0
updateTime = 0.01

maxRed = 10
maxBlue = 10

underpopulationthreashold = 2
overpopulationtrhreashold = 3
birthpopulationamount = 3
        
# Pygame 
pygame.init()
Textfont = pygame.font.SysFont('Segoe UI Symbol', 20, bold=False)
resolution = 800
screen = pygame.display.set_mode((resolution, resolution))
pygame.draw.rect(screen,BackgroundColor,(0,0,resolution,resolution))
pygame.display.flip()
UPDATEEVENT = pygame.USEREVENT+1
pygame.time.set_timer(UPDATEEVENT,int(updateTime*1000))

# Start
game = Game()
game.run()