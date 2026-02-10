import pygame

def drawSquare(pos,size,color):
    pygame.draw.rect(Screen, color, (pos[0]-size/2,pos[1]-size/2,size,size))

def drawBoard(board):
    for x in range(8):
        for y in range(8):
            X, Y = x-3, y-3
            if (x+y)%2 == 0:
                pygame.draw.rect(Screen, LightCellColor, (width/2-X*CellSize,height/2-Y*CellSize,CellSize,CellSize))
            else:
                pygame.draw.rect(Screen, DarkCellColor, (width/2-X*CellSize,height/2-Y*CellSize,CellSize,CellSize))
            Number = font.render(str(board[8*y+x]), True, TextColor)
            Screen.blit(Number, ((width/2-X*CellSize),(height/2-Y*CellSize)))

# Chess Stuff
CellSize = 50
Board = [i for i in range(64)]

# Colors
backgroundColor = "#414141"
DarkCellColor = "#649654"
LightCellColor = "#ECEED4"
TextColor = "#1A1A1A"

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
width,height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time and delta time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    
    clock.tick(FPS) # appply fps
    pygame.draw.rect(Screen, backgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
    
    drawBoard(Board)
    
    pygame.display.flip() # Update Screen