import pygame
import random

# Colors
BackgroundColor = "#5E5E5E"
OutlineColor = "#333333"

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
pygame.font.init()
Textfont = pygame.font.SysFont('Segoe UI Symbol', 45, bold=False)
width,height = 512, 512
screen = pygame.display.set_mode((width,height))
screen.fill(BackgroundColor)
pygame.display.flip()

# Time and delta time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

class L_tetromino:
    def __init__(self) -> None:
        self.color = "#F69230"
        self.cells = [(0,1), (0,-1), (1,1)]
        
class J_tetromino:
    def __init__(self) -> None:
        self.color = "#F16EB9"
        self.cells = [(0,1), (0,-1), (-1,1)]

class O_tetromino:
    def __init__(self) -> None:
        self.color = "#FEF84C"
        self.cells = [(0,1), (1,0), (1,1)]

class I_tetromino:
    def __init__(self) -> None:
        self.color = "#51E1FC"
        self.cells = [(0,-1), (0,1), (0,2)]

class S_tetromino:
    def __init__(self) -> None:
        self.color = "#E93D1E"
        self.cells = [(-1,0), (0,-1), (1,-1)]

class Z_tetromino:
    def __init__(self) -> None:
        self.color = "#4AAA41"
        self.cells = [(1,0), (0,-1), (-1,-1)]

class Cell:
    def __init__(self,board_position) -> None:
        self.board_position = board_position
        self.piece = None
        self.offloaded_piece = None
    def draw(self,outline_size,board_left,board_right,cell_size):
        if self.piece != None: color = self.piece.color
        elif self.offloaded_piece != None: color = self.offloaded_piece.color
        else: color = BackgroundColor
        pygame.draw.rect(screen,color,(outline_size+board_left+self.board_position[0]*cell_size,outline_size+board_right+self.board_position[1]*cell_size,cell_size-outline_size*2,cell_size-outline_size*2))
    def propagatePiece(self,cells):
        if self.piece == None: return

        for cell in self.piece.cells:
            x, y = self.board_position[0]+cell[0], self.board_position[1]+cell[1]
            cells[y][x].offloaded_piece = self.piece
        

class Board:
    def __init__(self) -> None:
        self.size = (10,24)
        self.outline_size = 1
        self.cell_size = 20
        self.board_left = (width-self.size[0]*self.cell_size)/2
        self.board_right = (height-self.size[1]*self.cell_size)/2
        self.cells = [[Cell((x,y)) for x in range(self.size[0])] for y in range(self.size[1])]
        self.cells[5][5].piece = S_tetromino()
    def update(self):
        for row in self.cells:
            for cell in row:
                cell.propagatePiece(self.cells)
        self.draw()
    def draw(self):
        pygame.draw.rect(screen,OutlineColor,(self.board_left,self.board_right,self.size[0]*self.cell_size,self.size[1]*self.cell_size))
        for row in self.cells:
            for cell in row:
                cell.draw(self.outline_size,self.board_left,self.board_right,self.cell_size)
         

class Game:
    def __init__(self):
        self.running = True
        self.board = Board()
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
                elif event.type == pygame.K_LEFT:
                    pass
                elif event.type == pygame.K_RIGHT:
                    pass
            clock.tick(FPS) # appply fps
            self.update()
            pygame.display.flip() # Update Screen

    def update(self):
        screen.fill(BackgroundColor)
        self.board.update()
    
    def leftClick(self,MousePos):
        return
    
    def rightClick(self,MousePos):
        return

game = Game()
game.run()