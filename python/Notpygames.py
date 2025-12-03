import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1920, 1080
CELLAMOUNT = 32
CELLSIZE = WIDTH // CELLAMOUNT
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('City Car Simulator')
world = [[0 for _ in range(HEIGHT//CELLSIZE)] for _ in range(CELLAMOUNT)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 0 is empty
    # 1 is road
    # 2 is building
    
    # Get mouse position in grid coordinates
    MouseX, MouseY = pygame.mouse.get_pos()
    GridX = MouseX // CELLSIZE
    GridY = MouseY // CELLSIZE
    
    # Detect mouse clicks and update cell state
    if pygame.mouse.get_pressed()[0]:  # Left mouse button
        if 0 <= GridX < CELLAMOUNT and 0 <= GridY < HEIGHT // CELLSIZE:
            world[GridX][GridY] = 1  # Set to road
    elif pygame.mouse.get_pressed()[2]:  # Right mouse button
        if 0 <= GridX < CELLAMOUNT and 0 <= GridY < HEIGHT // CELLSIZE:
            world[GridX][GridY] = 2  # Set to building
    elif pygame.mouse.get_pressed()[1]:  # Right mouse button
        if 0 <= GridX < CELLAMOUNT and 0 <= GridY < HEIGHT // CELLSIZE:
            world[GridX][GridY] = 0  # Set to building
    
    # Update the world according to the array
    for x in range(CELLAMOUNT):
        for y in range(HEIGHT // CELLSIZE):
            if world[x][y] == 0:
                screen.fill((0, 0, 0), rect=(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
            elif world[x][y] == 1:
                screen.fill((150, 150, 150), rect=(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
            elif world[x][y] == 2:
                screen.fill((200, 155, 144), rect=(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE))
    
    # draw grid
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if x % CELLSIZE == 0:
                screen.set_at((x, y), (255, 255, 255))
            if y % CELLSIZE == 0:
                screen.set_at((x, y), (255, 255, 255))
    
    # Update the display
    pygame.display.flip()

# Clean up and close the window
pygame.quit()
sys.exit()

#32x18