import random

rows, cols = (10, 10)

cells = [[0 for i in range(cols)] for j in range(rows)]

# Minesweeper
class cell:
    def __init__(self, isBomb, nbBombs):
        self.isBomb = isBomb
        self.nbBombs = nbBombs
    def __str__(self):
        return f"{self.isBomb}, {self.nbBombs}"
        

for i in range(1,cols+1):
    for j in range(1,rows+1):
        cells[j-1][i-1] = cell(True,5)
    
# print(cells)

x = cell(True,5)
print(x)