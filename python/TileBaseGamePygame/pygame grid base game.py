import pygame

class Cell:
    def __init__(self, tile, pos):
        self.tile = tile
        self.pos = pos

class Grid:
    def __init__(self, xCells, yCells):
        self.xCells = xCells
        self.yCells = yCells
        self.grid = []
    
    def generate(self, defaultValue):
        self.grid = [[defaultValue for _ in range(self.xCells)] for _ in range(self.yCells)]

    def draw(self):
        for x in range(self.xCells):
            for y in range(self.yCells):
                try:
                    Texture = self.grid[x][y].tile[0]
                    print(Texture)
                except:
                    Texture = [Screen, pygame.Rect(0,0,width,height)]
                Screen.blit(Texture[0], Texture[1])

# Colors
Background_Color = '#ffffff'

# Tiles texture
Textures = [
    r'python\TileBaseGamePygame\RoadTile.png'
]

# Load Textures
Tiles = [pygame.image.load(texture) for texture in Textures]
Tiles = [[tile, (pos[0],pos[1],0,0)] for tile in Tiles]

# pygame init
pygame.init()
width, height = 500, 500
Screen = pygame.display.set_mode((width, height))
Screen.fill(Background_Color)
pygame.display.flip()

grid = Grid(5, 5)

grid.generate(Cell(Tiles,(0,0)))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    Screen.fill(Background_Color)

    grid.draw()

    pygame.display.flip()