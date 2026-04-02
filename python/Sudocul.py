import pygame
import random

# Colors
light_bg_color = "#777777"
dark_bg_color = "#191919"
square_color = "#a5a5a5"
number_color = "#4b4b4b"
placing_number_color = "#677b8b"


class Square:
    def __init__(self, pos, value) -> None:
        self.pos = pos
        self.value = value
        self.placing_value = 0
        self.isHovering = False
        self.possibilities = set()
    def draw(self, board_size):
        square_size = res/board_size
        screen_pos = (self.pos[0]*square_size,
                      self.pos[1]*square_size)
        pygame.draw.rect(screen, square_color, (screen_pos[0]+gridlines_girth,screen_pos[1]+gridlines_girth,square_size-gridlines_girth*2,square_size-gridlines_girth*2))
        if self.isHovering:
            RenderedText = Textfont.render(str(self.placing_value),True,placing_number_color)
            TextRect = RenderedText.get_rect(center=(screen_pos[0]+square_size/2, screen_pos[1]+square_size/2))
            screen.blit(RenderedText,TextRect)
        elif self.value != 0:
            RenderedText = Textfont.render(str(self.value),True,number_color)
            TextRect = RenderedText.get_rect(center=(screen_pos[0]+square_size/2, screen_pos[1]+square_size/2))
            screen.blit(RenderedText,TextRect)


class Sudoku:
    def __init__(self,board_size=9) -> None:
        self.board_size = board_size
        self.running = False
        self.board = []
        self.isPlacing = False
        self.hovering_square = None
        self.placing_value = 1
        self.remaining_numbers = int(81*0.75)
    def run(self):
        self.running = True
        self.generateBoard()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            if self.isPlacing:
                                self.hovering_square.value = self.placing_value
                            else: self.isPlacing = True
                        case 3:
                            if self.isPlacing:
                                if self.hovering_square != None: self.hovering_square.isHovering = False
                                self.hovering_square = None
                                self.isPlacing = False
                        case 2:
                            sudoku.generateSudoku()
                elif event.type == pygame.MOUSEWHEEL:
                    self.placing_value += event.y
                    self.placing_value = max(min(self.placing_value,9),0)
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            self.solve()
            self.drawBg()
            self.update()
            pygame.display.flip()
    def generateBoard(self):
        self.board = [[Square((x,y),0) for x in range(self.board_size)] for y in range(self.board_size)] 
    def generateSudoku(self):
        self.generateBoard()
        try:
            for _ in range(10):
                random_square = self.board[random.randint(0,8)][random.randint(0,8)]
                if random_square.value == 0:
                    self.placeRandomNumber(random_square)
            self.solve()
        except:
            self.generateSudoku()
            
        while 81-self.countZeros() > self.remaining_numbers:
            self.board[random.randint(0,8)][random.randint(0,8)].value = 0
    def placeRandomNumber(self,square):
        square.value = random.randint(1,9)
        if not self.checkSolution(False):
            self.placeRandomNumber(square)
    def countZeros(self):
        sum = 0
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board[y][x].value == 0: sum += 1
        return sum
    def drawBg(self):
        big_square_amount = int(self.board_size**0.5)
        big_square_size = res/big_square_amount
        screen.fill(dark_bg_color)
        for x in range(big_square_amount):
            for y in range(big_square_amount):
                pygame.draw.rect(screen,light_bg_color,(x*big_square_size+gridlines_girth,y*big_square_size+gridlines_girth,big_square_size-gridlines_girth*2,big_square_size-gridlines_girth*2))
    def update(self):
        if self.isPlacing:
            mouse_pos = pygame.mouse.get_pos()
            board_mouse_pos = (int(mouse_pos[0]*self.board_size/res),int(mouse_pos[1]*self.board_size/res))
            hovered_square = self.board[board_mouse_pos[1]][board_mouse_pos[0]]
            if hovered_square != self.hovering_square:
                if self.hovering_square == None:
                    hovered_square.isHovering = True
                    self.hovering_square = hovered_square
                    self.hovering_square.placing_value = self.placing_value
                else:
                    self.hovering_square.isHovering = False
                    hovered_square.isHovering = True
                    self.hovering_square = hovered_square
                    self.hovering_square.placing_value = self.placing_value
            else:
                self.hovering_square.placing_value = self.placing_value

        for line in self.board:
            for square in line:
                square.draw(self.board_size)
    def checkSolution(self, isZeroCount):
        # check lines
        for line in self.board:
            numbers_seen = []
            for square in line:
                if square.value == 0:
                    if isZeroCount: return False
                elif square.value in numbers_seen:
                    return False
                else:
                    numbers_seen.append(square.value)
        # check columns
        for x in range(self.board_size):
            numbers_seen = []
            for y in range(self.board_size):
                if self.board[y][x].value == 0:
                    if isZeroCount: return False
                elif self.board[y][x].value in numbers_seen:
                    return False
                else:
                    numbers_seen.append(self.board[y][x].value)
        # check big square
        big_square_amount = int(self.board_size**0.5)
        for x in range(big_square_amount):
            for y in range(big_square_amount):
                numbers_seen = []
                for X in [0,1,2]:
                    for Y in [0,1,2]:
                        if self.board[Y+y*3][X+x*3].value == 0:
                            if isZeroCount: return False
                        elif self.board[Y+y*3][X+x*3].value in numbers_seen:
                            return False
                        else:
                            numbers_seen.append(self.board[Y+y*3][X+x*3].value)
        return True      
    def solve(self):
        history = []
        for x in range(self.board_size):
            for y in range(self.board_size):
                active_square = self.board[y][x]
                if active_square.value == 0:
                    self.fillaSquare(active_square, True, history)                  
    def fillaSquare(self, square, isFirst, history):
        if isFirst:
            for n in range(1,10):
                square.value = n
                if self.checkSolution(False):
                    square.possibilities.add(n)
        else:
            square.possibilities.pop()
        if len(square.possibilities) == 0:
            square.value = 0
            self.fillaSquare(history.pop(), False, history)
            self.fillaSquare(square,True,history)
        else:
            square.value = next(iter(square.possibilities))
            history.append(square)



pygame.init()
res = 720
Textfont = pygame.font.SysFont('monospace', int(0.07*res), bold=True)
screen = pygame.display.set_mode((res,res))



# Game Settings
gridlines_girth = 0.003*res

# Game Start
sudoku = Sudoku(9)
sudoku.run()