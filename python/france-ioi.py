TerrainInput = input()
listTerrain = TerrainInput.split(' ')
nbLignes = int(listTerrain[0])
grid = []
squares = []
for _ in range(nbLignes):
    strligne = input()
    listligne = strligne.split(' ')
    grid.append(listligne)

# grid = [
#     [1,0,0,1,0,0,1],
#     [0,0,0,0,0,0,0],
#     [1,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,1,0,0,0,0,1],
#     [1,0,0,0,1,0,1]
# ]

def GetSquareSize(grid,cellpos):
    squareSize = 1
    
    while squareSize < len(grid)-cellpos[1] and squareSize < len(grid[0])-cellpos[0]:
        for dy in range(squareSize+1):
            for dx in range(squareSize+1):
                if int(grid[dy + cellpos[1]][dx + cellpos[0]]) != 0:
                    return squareSize
        squareSize += 1
    return squareSize

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if int(grid[y][x]) == 0:
            squares.append(GetSquareSize(grid,(x,y)))

squares.sort()
print(squares[-1])