import turtle
from random import randint, shuffle
from time import sleep

x_max = 9
y_max = 9

myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x=-150
topLeft_y=150

def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)    		  
    myPen.write(message,align="left",font=FONT)

def GenerateEmptyGrid():
    grid = [[0 for _ in range(x_max)] for _ in range(y_max)]
    return grid

def IsGridFull(grid):
    for y in range(y_max):
      for x in range(x_max):
        if grid[y][x] == 0:
            return False
    return True

grid = GenerateEmptyGrid()

def drawGrid(grid):
  intDim=35
  for row in range(0,10):
    if (row%3)==0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)
    myPen.penup()
    myPen.goto(topLeft_x,topLeft_y-row*intDim)
    myPen.pendown()
    myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
  for col in range(0,10):
    if (col%3)==0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)    
    myPen.penup()
    myPen.goto(topLeft_x+col*intDim,topLeft_y)
    myPen.pendown()
    myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

  for row in range (0,9):
      for col in range (0,9):
        if grid[row][col]!=0:
          text(grid[row][col],topLeft_x+col*intDim+9,topLeft_y-row*intDim-intDim+8,18)

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
    global counter
    #Find next empty cell
    for i in range(0,81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            for value in range (1,10):
                #Check that this value has not already be used on this row
                if not(value in grid[row]):
                    #Check that this value has not already be used on this column
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        #Identify which of the 9 squares we are working on
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                            else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
            #Check that this value has not already be used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col]=value
              if IsGridFull(grid):
                counter+=1
                break
              else:
                if solveGrid(grid):
                  return True
      break
  grid[row][col]=0