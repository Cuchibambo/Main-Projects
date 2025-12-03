import numpy as np
import pygame

pygame.init()

WindowDimensions = (500,500)
bg_color = (32,32,32)

window = pygame.display.set_mode(WindowDimensions)
window.fill(bg_color)
pygame.display.flip()

def rotationMatrix():
    return np.matrix(
        [np.cos(theta),-np.sin(theta)],
        [np.sin(theta),np.cos(theta)]
    )

def setpixelcol(x,y,col):
    x += WindowDimensions[0]//2
    y += WindowDimensions[1]//2
    window.set_at((x,y),col)

def drawPoint(x,y,col,radius,outline_radius,outline_col):
    for y1 in range(radius*2):
        for x1 in range(radius*2):
            if np.sqrt((x1)**2 + (y1)**2) <= radius:
                setpixelcol(x+x1,y+y1,col)

theta = np.pi*1

v = (np.sin(theta),np.cos(theta))
A = ()


# Update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill(bg_color)
    
    theta += 0.01
    # setpixelcol(int(theta),0,(255,255,255))
    drawPoint(int(theta),0,(255,255,255),5,1,1)
    
    # Set pixel using:
    # window.set_at(x,y,col)

    pygame.display.update()