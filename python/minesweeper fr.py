import math
import random
import pygame

class Cell():
    def __init__(self, pos:tuple[int,int], isBomb:bool, num:int, isUncovered:bool, isFlag:bool):
        self.pos = pos
        self.isBomb = isBomb
        self.num = num
        self.isUncovered = isUncovered
        self.isFlag = isFlag
    def __str__(self):
        if self.isUncovered:
            return str(self.num)
        else:
            return ''

XCellCount, YCellCount = 30, 30
Grid = [[0 for _ in range(XCellCount)] for _ in range(YCellCount)]

nbBombs = int(XCellCount*YCellCount*0.2)

ColorsDict = {
    0 : "#a6a6a6",
    1 : "#3fc32b",
    2 : "#2b65c3",
    3 : "#cde81f",
    4 : "#e81f1f",
    5 : "#e81fdb",
    6 : "#e88a1f",
    7 : "#1db4bc",
    8 : "#127311",
    9 : "#421173"
}

for x in range(XCellCount):
    for y in range(YCellCount):
        Grid[y][x] = Cell((x,y), False, 0, False, False)

def GetBombNum(pos:tuple[int,int],grid) -> int:
    X_bounds, Y_bounds = len(grid[0]), len(grid)
    count = 0
    for x in [-1,0,1]:
        for y in [-1,0,1]:
            if not (x == 0 and y == 0):
                if (y+pos[1] <= Y_bounds-1 and y+pos[1] >= 0) and (x+pos[0] <= X_bounds-1 and x+pos[0] >= 0):
                    if grid[y+pos[1]][x+pos[0]].isBomb:
                        count += 1
    return count

def PlaceBombs(posClicked:tuple[int,int], grid, nbBombs): 
    bombsToPlace = nbBombs
    X_bounds, Y_bounds = len(grid[0]), len(grid)
    while bombsToPlace > 0:
        Xpos = random.randint(0,X_bounds-1)
        Ypos = random.randint(0,Y_bounds-1)
        if not grid[Ypos][Xpos].isBomb:
            if Xpos != posClicked[0] and Ypos != posClicked[1]:
                grid[Ypos][Xpos].isBomb = True
                bombsToPlace -= 1
    return grid

def drawSquare(pos:tuple[int,int],color,radius:int):
    pygame.draw.rect(Surface, color, pygame.Rect(pos[0]-radius,pos[1]-radius,radius,radius))

def DrawGrid(grid):
    for x in range(XCellCount):
        for y in range(YCellCount):
            posOnScree = ((((x/XCellCount)*width)+(width/(XCellCount*4))),
                          ((y/YCellCount)*height)+(height/(YCellCount*4)))
            color = ColorsDict.get(grid[y][x].num)
            if grid[y][x].isUncovered: label = font.render(str(grid[y][x].num), 1, color, BackgroundColor)
            elif not grid[y][x].isFlag:
                label = font.render('', 1, BackgroundColor)
                pygame.draw.rect(Surface, "#2a572e", pygame.Rect(posOnScree[0]-(width/(XCellCount*6)), posOnScree[1]-(height/(YCellCount*6)), width/XCellCount, height/XCellCount))
            elif grid[y][x].isFlag: label = font.render('F', 1, "#b62424", BackgroundColor)
            Surface.blit(label, posOnScree)

def GetCellFromPos(pos:tuple[int,int]) -> tuple[int,int]:
    return (math.floor((pos[0]/width)*XCellCount),
            math.floor((pos[1]/height)*YCellCount))

def WinCheck(grid):
    for x in range(XCellCount):
        for y in range(YCellCount):
            if grid[y][x].isUncovered == False and grid[y][x].isBomb == False:
                return False
    return True

pygame.init()
width, height = 720, 720
Surface = pygame.display.set_mode((width, height))
BackgroundColor = "#000000"
pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))
pygame.display.flip()
font = pygame.font.SysFont('Times new roman', 20)

FirstPlay = True
running = True
while running:
    isMouseDown = False
    isFlagButtonDown = False
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: isMouseDown = True
            elif event.button == 3: isFlagButtonDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: isMouseDown = False
            elif event.button == 3: isFlagButtonDown = False

    pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))

    for x in range(XCellCount):
        for y in range(YCellCount):
            Grid[y][x].num = GetBombNum((x,y),Grid)
            if Grid[y][x].num == 0 and Grid[y][x].isUncovered:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if x+dx <= XCellCount-1 and x+dx >= 0 and y+dy <= YCellCount-1 and y+dy >= 0:
                            Grid[y+dy][x+dx].isUncovered = True
    
    if FirstPlay and isMouseDown:
        pos = GetCellFromPos(mousePos)
        Grid[pos[1]][pos[0]].isUncovered = True
        Grid = PlaceBombs(pos,Grid,nbBombs)
        FirstPlay = False
    elif isMouseDown:
        pos = GetCellFromPos(mousePos)
        if Grid[pos[1]][pos[0]].isBomb:
            pygame.quit()
            running = False
            quit()
        else:
            Grid[pos[1]][pos[0]].isUncovered = True
    elif isFlagButtonDown:
        pos = GetCellFromPos(mousePos)
        if Grid[pos[1]][pos[0]].isFlag:
            Grid[pos[1]][pos[0]].isFlag = False
        else:
            Grid[pos[1]][pos[0]].isFlag = True

    if WinCheck(Grid):
        label = font.render('You WIN!!!', 1, "#c05757")
        Surface.blit(label, (width/2, height/2))
    DrawGrid(Grid)

    pygame.display.flip()