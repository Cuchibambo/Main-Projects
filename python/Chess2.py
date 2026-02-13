import pygame

# Colors
BackgroundColor = "#333333"
LightSquareColor = "#faf8dd"
DarkSquareColor = "#72a945"
HighlightedSquareColor = "#99d55c"
WhiteTextColor = "#595a50"
BlackTextColor = "#45463E"
MovementSquareColor = "#accfd8"
TakeSquareColor = "#d8acac"

class Game:
    def __init__(self):
        self.running = False
        self.board = Board()
        self.cellSize = None
        self.turn = 0
        self.whiteCaptures = []
        self.blackCaptures = []
        self.SlectedIndex = None
        self.TargetIndex = None
        self.SelectedPiece = None
    def ChessPos_to_Index(self,pos):
        x, y = pos[0], pos[1]
        return (y*8)+x
    def ScreenPos_to_ChessPos(self,pos):
        x, y = pos[0], pos[1]
        X = round((x/self.cellSize)-1.5)
        Y = round((y/self.cellSize)-1.5)
        return (X,Y)
    def Index_to_ChessPos(self,index):
        x = index % 8
        y = index // 8
        return (x,y)
    def isValidChessPos(self,pos):
        x, y = pos[0], pos[1]
        return (x in range(8)) and (y in range(8))
    def KingMovement(self,pos,color):
        x, y = pos[0], pos[1]
        for X in [-1,0,1]:
            for Y in [-1,0,1]:
                if (X,Y) != (0,0):
                    moveindex = self.ChessPos_to_Index((x+X,y+Y))
                    if self.isValidChessPos((x+X,y+Y)):
                        if self.board.GetCell(moveindex).piece == None:
                            self.board.setCellMovable(moveindex,True)
                        elif self.board.GetCell(moveindex).piece.color != color:
                            self.board.setCellMovable(moveindex,True)
    def KnightMovement(self,pos,color):
        x, y = pos[0], pos[1]
        for dx in (-1,1):
            for dy in (-2,2):
                moveindex = self.ChessPos_to_Index((x+dx,y+dy))
                if self.isValidChessPos((x+dx,y+dy)):
                    if self.board.GetCell(moveindex).piece == None:
                        self.board.setCellMovable(moveindex,True)
                    elif self.board.GetCell(moveindex).piece.color != color:
                        self.board.setCellMovable(moveindex,True)
        for dx in (-2,2):
            for dy in (-1,1):
                moveindex = self.ChessPos_to_Index((x+dx,y+dy))
                if self.isValidChessPos((x+dx,y+dy)):
                    if self.board.GetCell(moveindex).piece == None:
                        self.board.setCellMovable(moveindex,True)
                    elif self.board.GetCell(moveindex).piece.color != color:
                        self.board.setCellMovable(moveindex,True)
    def HorizontalMovement(self,pos,color):
        x, y = pos[0], pos[1]
        for isX in (True,False):
            for mult in (-1,1):
                for dy in range(1,8):
                    if isX: movepos = (x+(dy*mult),y)
                    else: movepos = (x,y+(dy*mult))
                    moveindex = self.ChessPos_to_Index(movepos)
                    if not self.isValidChessPos(movepos):
                        break
                    if self.board.GetCell(moveindex).piece == None:
                        self.board.setCellMovable(moveindex,True)
                    elif self.board.GetCell(moveindex).piece.color == color:
                        break
                    else: 
                        self.board.setCellMovable(moveindex,True)
                        break
    def DiagonalMovement(self,pos,color):
        x, y = pos[0], pos[1]
        for Xmult in (-1,1):
            for Ymult in (-1,1):
                for d in range(1,8):
                    moveindex = self.ChessPos_to_Index((x+(d*Xmult),y+(d*Ymult)))
                    if not self.isValidChessPos((x+(d*Xmult),y+(d*Ymult))):
                        break
                    if self.board.GetCell(moveindex).piece == None:
                        self.board.setCellMovable(moveindex,True)
                    elif self.board.GetCell(moveindex).piece.color == color:
                        break
                    else: 
                        self.board.setCellMovable(moveindex,True)
                        break
    def SelectionLogic(self,index):
        WhoseTurn = self.turn%2
        ChessPos = self.Index_to_ChessPos(index)
        x, y = ChessPos[0], ChessPos[1]
        if self.board.isSelecting:
            self.TargetIndex = index
            if self.board.GetCell(self.TargetIndex).isPossibleMove:
                self.board.MovePieces(self.SlectedIndex,self.TargetIndex)
                self.Unselect()
                self.board.isSelecting = False
                self.turn += 1
        else:
            if self.board.GetCell(index).piece != None:
                PieceColor = self.board.GetCell(index).piece.color
            else:
                return
            if (WhoseTurn == 0 and PieceColor == "WHITE") or (WhoseTurn == 1 and PieceColor == "BLACK"):
                self.SlectedIndex = index
                self.board.SelectPos(index)
                self.SelectedPiece = self.board.GetCell(index).piece
            else:
                return
            # Possible moves
            if self.SelectedPiece.rank == "ROOK":
                self.HorizontalMovement(ChessPos,self.SelectedPiece.color)
            elif self.SelectedPiece.rank == "KNIGHT":
                self.KnightMovement(ChessPos,self.SelectedPiece.color)
            elif self.SelectedPiece.rank == "BISHOP":
                self.DiagonalMovement(ChessPos,self.SelectedPiece.color)
            elif self.SelectedPiece.rank == "QUEEN":
                self.HorizontalMovement(ChessPos,self.SelectedPiece.color)
                self.DiagonalMovement(ChessPos,self.SelectedPiece.color)
            elif self.SelectedPiece.rank == "KING":
                self.KingMovement(ChessPos,self.SelectedPiece.color)
            elif self.SelectedPiece.rank == "PAWN":
                if self.SelectedPiece.color == "WHITE":
                    # Move 1
                    X, Y = x-0, y-1
                    moveindex = self.ChessPos_to_Index((X,Y))
                    if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece == None):
                        self.board.setCellMovable(moveindex,True)
                    # Move 2
                    X, Y = x-1, y-1
                    moveindex = self.ChessPos_to_Index((X,Y))
                    if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece != None):
                        if self.board.GetCell(moveindex).piece.color == "BLACK":
                            self.board.setCellMovable(moveindex,True)
                    # Move 3
                    X, Y = x+1, y-1
                    moveindex = self.ChessPos_to_Index((X,Y))
                    if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece != None):
                        if self.board.GetCell(moveindex).piece.color == "BLACK":
                            self.board.setCellMovable(moveindex,True)
                    # Move 4
                    if y == 6:
                        X, Y = x-0, y-2
                        moveindex = self.ChessPos_to_Index((X,Y))
                        if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece == None):
                            self.board.setCellMovable(moveindex,True)
                else:
                    # Move 1
                    X, Y = x-0, y+1
                    moveindex = self.ChessPos_to_Index((X,Y))
                    if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece == None):
                        self.board.setCellMovable(moveindex,True)
                    # Move 2
                    X, Y = x-1, y+1
                    moveindex = self.ChessPos_to_Index((X,Y))
                    if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece != None):
                        if self.board.GetCell(moveindex).piece.color == "WHITE":
                            self.board.setCellMovable(moveindex,True)
                    # Move 3
                    X, Y = x+1, y+1
                    moveindex = self.ChessPos_to_Index((X,Y))
                    if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece != None):
                        if self.board.GetCell(moveindex).piece.color == "WHITE":
                            self.board.setCellMovable(moveindex,True)
                    # Move 4
                    if y == 1:
                        X, Y = x-0, y+2
                        moveindex = self.ChessPos_to_Index((X,Y))
                        if self.isValidChessPos((X,Y)) and (self.board.GetCell(moveindex).piece == None):
                            self.board.setCellMovable(moveindex,True)
    def Unselect(self):
        if self.board.isSelecting:
            self.board.isSelecting = False
            self.board.GetCell(self.SlectedIndex).isSelected = False
            self.SelectedPiece = None
            self.SlectedIndex = None
            self.TargetIndex = None
            for cell in self.board.board:
                cell.isPossibleMove = False
    def run(self):
        self.running = True
        self.board = Board()
        self.board.GenerateBoard()
        self.cellSize = self.board.board[0].cellSize
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.Unselect()
                    elif event.button == 1:
                        MousePos = pygame.mouse.get_pos()
                        MouseIndex = self.ChessPos_to_Index(self.ScreenPos_to_ChessPos(MousePos))
                        if 0 <= MouseIndex and MouseIndex <= 63:
                            self.SelectionLogic(MouseIndex)
            clock.tick(FPS) # appply fps
            pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
            self.Update()
            pygame.display.flip() # Update Screen
    def Update(self):
        self.board.drawBoard()

class Board:
    def __init__(self):
        self.board = []
        self.isSelecting = False
    def GetCell(self,index):
        return self.board[index]
    def setCellMovable(self,index,state):
        self.GetCell(index).isPossibleMove = state
    def GenerateBoard(self):
        for i in range(64):
            self.board.append(Cell(i,None))
        self.ResetBoard()
    def ResetBoard(self):
        # Black
        # Rooks
        self.board[0] = Cell(0,Piece("ROOK","BLACK"))
        self.board[7] = Cell(7,Piece("ROOK","BLACK"))
        # Knight
        self.board[1] = Cell(1,Piece("KNIGHT","BLACK"))
        self.board[6] = Cell(6,Piece("KNIGHT","BLACK"))
        # Bishop
        self.board[2] = Cell(2,Piece("BISHOP","BLACK"))
        self.board[5] = Cell(5,Piece("BISHOP","BLACK"))
        # Royaltie
        self.board[3] = Cell(3,Piece("QUEEN","BLACK"))
        self.board[4] = Cell(4,Piece("KING","BLACK"))
        # Pawns
        self.board[8] = Cell(8,Piece("PAWN","BLACK"))
        self.board[9] = Cell(9,Piece("PAWN","BLACK"))
        self.board[10] = Cell(10,Piece("PAWN","BLACK"))
        self.board[11] = Cell(11,Piece("PAWN","BLACK"))
        self.board[12] = Cell(12,Piece("PAWN","BLACK"))
        self.board[13] = Cell(13,Piece("PAWN","BLACK"))
        self.board[14] = Cell(14,Piece("PAWN","BLACK"))
        self.board[15] = Cell(15,Piece("PAWN","BLACK"))

        # White
        # Rooks
        self.board[56] = Cell(56,Piece("ROOK","WHITE"))
        self.board[63] = Cell(63,Piece("ROOK","WHITE"))
        # Knight
        self.board[57] = Cell(57,Piece("KNIGHT","WHITE"))
        self.board[62] = Cell(62,Piece("KNIGHT","WHITE"))
        # Bishop
        self.board[58] = Cell(58,Piece("BISHOP","WHITE"))
        self.board[61] = Cell(61,Piece("BISHOP","WHITE"))
        # Royalties
        self.board[59] = Cell(59,Piece("QUEEN","WHITE"))
        self.board[60] = Cell(60,Piece("KING","WHITE"))
        # Pawns
        self.board[48] = Cell(48,Piece("PAWN","WHITE"))
        self.board[49] = Cell(49,Piece("PAWN","WHITE"))
        self.board[50] = Cell(50,Piece("PAWN","WHITE"))
        self.board[51] = Cell(51,Piece("PAWN","WHITE"))
        self.board[52] = Cell(52,Piece("PAWN","WHITE"))
        self.board[53] = Cell(53,Piece("PAWN","WHITE"))
        self.board[54] = Cell(54,Piece("PAWN","WHITE"))
        self.board[55] = Cell(55,Piece("PAWN","WHITE"))
    def drawBoard(self):
        for cell in self.board:
            cell.drawCell()
    def SelectPos(self,index):
        self.isSelecting = True
        self.board[index].isSelected = True
    def MovePieces(self,selectedIndex,targteIndex):
        PieceToMove = self.board[selectedIndex].piece
        CapturedPiece = self.board[targteIndex].piece
        self.board[targteIndex].piece = PieceToMove
        self.board[selectedIndex].piece = None
        # self.isSelecting = False
        # self.board[selectedIndex].isSelected = False
        return CapturedPiece

class Cell:
    def __init__(self,index,piece):
        self.index = index
        self.piece = piece
        self.isSelected = False
        self.isPossibleMove = False
        self.cellSize = 50
    def Index_to_ChessPos(self,index):
        x = index % 8
        y = index // 8
        return (x,y)
    def ChessPos_to_ScreenPos(self,pos):
        x, y = pos[0], pos[1]
        CenterX, CenterY = width/2, height/2
        X = (x-3.5)*self.cellSize+CenterX
        Y = (y-3.5)*self.cellSize+CenterY
        return (X,Y)
    def drawCell(self):
        ChessPos = self.Index_to_ChessPos(self.index)
        ScreenPos = self.ChessPos_to_ScreenPos(ChessPos)
        if self.isSelected: color = HighlightedSquareColor
        elif self.isPossibleMove and (self.piece != None): color = TakeSquareColor
        elif self.isPossibleMove: color = MovementSquareColor
        elif (ChessPos[1]+ChessPos[0])%2 == 0: color = LightSquareColor
        else: color = DarkSquareColor
        pygame.draw.rect(Screen,color,pygame.Rect(ScreenPos[0]-(self.cellSize/2), ScreenPos[1]-(self.cellSize/2), self.cellSize, self.cellSize))
        if self.piece != None:
            self.piece.drawPiece(ScreenPos)

class Piece:
    def __init__(self,rank,color):
        self.rank = rank
        self.color = color
        self.WhitePieceDict = {
            "ROOK" : 0x2656,
            "KNIGHT" : 0x2658,
            "BISHOP" : 0x2657,
            "QUEEN" : 0x2655,
            "KING" : 0x2654,
            "PAWN" : 0x2659
        }
        self.BlackPieceDict = {
            "ROOK" : 0x265C,
            "KNIGHT" : 0x265E,
            "BISHOP" : 0x265D,
            "QUEEN" : 0x265B,
            "KING" : 0x265A,
            "PAWN" : 0x265F
        }
    def drawPiece(self,pos):
        if self.color == "WHITE": 
            PieceText = self.WhitePieceDict.get(self.rank,0x2800)
            color = WhiteTextColor
        else: 
            PieceText = self.BlackPieceDict.get(self.rank,0x2800)
            color = BlackTextColor
        RenderedText = Textfont.render(chr(PieceText),True,color)
        TextRect = RenderedText.get_rect(center=pos)
        Screen.blit(RenderedText,TextRect)

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
pygame.font.init()
Textfont = pygame.font.SysFont('Segoe UI Symbol', 45, bold=False)
width,height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time and delta time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

# Start
game = Game()
game.run()