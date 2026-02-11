import pygame

class Piece:
    def __init__(self,color,type):
        self.color = color
        self.type = type

def drawSquare(pos,size,color):
    pygame.draw.rect(Screen, color, (pos[0]-size/2,pos[1]-size/2,size,size))

def drawBoard(board):
    for y in range(8):
        for x in range(8):
            if SelectedPos == ChessPos_to_Index((x,y)) and isSelected:
                color = HighlightColor
            elif (x+y)%2 == 0:
                color = DarkCellColor
            else:
                color = LightCellColor
            drawSquare(ChessPos_to_ScreenPos((x,y)),CellSize,color)
            # Number = font.render(str(board[ChessPos_to_Index((x,y))]), True, TextColor)
            # Screen.blit(Number, ChessPos_to_ScreenPos((x,y)))

def ChessPos_to_ScreenPos(pos):
    x, y = pos[0], pos[1]
    CenterX, CenterY = width/2, height/2
    X = (x-3.5)*CellSize+CenterX
    Y = (y-3.5)*CellSize+CenterY
    return (X,Y)

def ScreenPos_to_ChessPos(pos):
    x, y = pos[0], pos[1]
    X = round((x/CellSize)-1.5)
    Y = round((y/CellSize)-1.5)
    return (X,Y)

def drawPiece(board,index):
    pos = Index_to_ChessPos(index)
    x, y = pos[0], pos[1]
    pieceType = board[index].type
    pieceColor = board[index].color
    text = PieceDict.get(pieceType,'')
    Colors = PieceDict.get(pieceColor,('#ffffff','#ffffff')) 
    drawTextnOutline(text,Colors[0],Colors[1],ChessPos_to_ScreenPos((x,y)))

def changePiece(board,index,type,color):
    board[index].type = type
    board[index].color = color 

def ChessPos_to_Index(pos):
    x, y = pos[0], pos[1]
    return (y*8)+x

def Index_to_ChessPos(index):
    x = index % 8
    y = index // 8
    return (x,y)

def drawTextnOutline(text,textColor,outlineColor,pos):
    RenderedText = Textfont.render(text, True, textColor)
    TextRect = RenderedText.get_rect(center=pos)
    RenderedOutline = Outlinefont.render(text, True, outlineColor)
    OutlineRect = RenderedOutline.get_rect(center=pos)
    Screen.blit(RenderedOutline, OutlineRect)
    Screen.blit(RenderedText, TextRect)

def ScreenPos_to_Index(pos):
    return ChessPos_to_Index(ScreenPos_to_ChessPos(pos))

# Colors
backgroundColor = "#414141"
DarkCellColor = "#649654"
LightCellColor = "#ECEED4"
BlackTextColor = "#1A1A1A"
WhiteTextColor = "#E8F2F1"
HighlightColor = "#a6dc3b"

# Chess Stuff
CellSize = 50
Board = [Piece(None,None) for _ in range(64)]
TextSize = 30
OutlineSize = 3
Turn = 0
isSelected = False
SelectedPos = None
TargetPos = None
WhitePawnMoves = [-8]
WhitePawnCaptures = [-9,-7]
KnightBehaviour = [-17,-15,-5,11,-11,5,15,17]
KingBehaviour = [-9,-8,-7,-1,1,7,8,9]

# Piece Dict
PieceDict = {
    "PAWN" : "P",
    "KNIGHT" : "C",
    "BISHOP" : "B",
    "ROOK" : "R",
    "QUEEN" : "Q",
    "KING" : "K",
    "WHITE" : (WhiteTextColor,BlackTextColor),
    "BLACK" : (BlackTextColor,WhiteTextColor)
}

PieceMovementDict = {
    ("WHITE","PAWN") : WhitePawnCaptures,
    ("WHITE","KNIGHT") : WhitePawnCaptures
}

# Start Pygame
pygame.display.init() # Might not work if it crashes change this
pygame.font.init()
Textfont = pygame.font.SysFont('Arial', TextSize, bold=False)
Outlinefont = pygame.font.SysFont('Arial', TextSize+OutlineSize, bold=True)
width,height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

# Time and delta time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

changePiece(Board,51,"PAWN","WHITE")

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                MousePos = pygame.mouse.get_pos()
                if isSelected:
                    TargetPos = ScreenPos_to_Index(MousePos)
                    SelectedPiece = Board[SelectedPos]
                    SelectedPiece
                    if 
                    changePiece(Board,TargetPos,SelectedPiece.type,SelectedPiece.color)
                    changePiece(Board,SelectedPos,None,None)
                    isSelected = False
                else:
                    SelectedPos = ScreenPos_to_Index(MousePos)
                    if Board[SelectedPos].type != None:
                        isSelected = True
                    
    clock.tick(FPS) # appply fps
    pygame.draw.rect(Screen, backgroundColor, pygame.Rect(0, 0, width, height)) # Clear Screen
    
    drawBoard(Board)
    for i in range(64):
        drawPiece(Board,i)
    
    
    pygame.display.flip() # Update Screen