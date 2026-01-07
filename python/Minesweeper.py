import pygame
import random
import math

class Cell():
    def __init__(self, pos, isBomb, number) -> None:
        self.pos = pos
        self.isBomb = isBomb

def DrawRect(CenterPos:tuple[int,int], Radius:int) -> None:
    pygame.draw.rect(Surface, CellColor, pygame.Rect(CenterPos[0]-Radius,CenterPos[1]-Radius,Radius*2,Radius*2))

XGridCells, YGridCells = 10, 10
Offset = 10
Grid = [[0 for _ in range(XGridCells)] for _ in range(YGridCells)]

for x in range(XGridCells):
    for y in range(YGridCells):
        Grid[y][x] = Cell((x,y), False, 0)
print(Grid)

pygame.init()
width, height = 500, 500
Surface = pygame.display.set_mode((width, height))

BackgroundColor = "#474747"
CellColor = "#A3A3A3"
NumberColorsDict = {
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

pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))
pygame.display.flip()                                                

running = True
while running:
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

        mousePos = pygame.mouse.get_pos()
        print((mousePos[0]/width)*XGridCells)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f'Clicked on square: {(math.floor(mousePos[0]/width)*XGridCells), math.floor((mousePos[1]/height)*YGridCells)}')

    pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height)) # Erase screen

    xGap = (width/(XGridCells+1))
    yGap = (height/(YGridCells+1))
    for x in range(XGridCells):
        for y in range(YGridCells):
            DrawRect((xGap*(x+1/2)*1.2,yGap*(y+1/2)*1.2),(xGap/2)-Offset)
    
    

    pygame.display.flip()