import pygame
import numpy as np
from MathScripts import ChangeRange, toRGB

iterations = 100
def GetNextValue(z,c):
    i = 0
    while i < iterations and abs(z) < 2:
        i += 1
        z = z*z+c
    return i

pygame.init()
width, height = 500, 500
Surface = pygame.display.set_mode((width, height))
BackgroundColor = "#474747"
pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))
pygame.display.flip()                                                

ranges = 1.5

isLEFT, isRIGHT, isUP, isDOWN, isP, isM = 0, 0, 0, 0, 0, 0

Xoffset, Yoffset = 2, 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                quit()

            elif event.key == pygame.K_LEFT:
                isLEFT = 1
            elif event.key == pygame.K_RIGHT:
                isRIGHT = 1
            elif event.key == pygame.K_UP:
                isUP = 1
            elif event.key == pygame.K_DOWN:
                isDOWN = 1
            elif event.key == pygame.K_p:
                isP = 1
            elif event.key == pygame.K_m:
                isM = 1
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                isLEFT = 0
            elif event.key == pygame.K_RIGHT:
                isRIGHT = 0
            elif event.key == pygame.K_UP:
                isUP = 0
            elif event.key == pygame.K_DOWN:
                isDOWN = 0
            elif event.key == pygame.K_p:
                isP = 0
            elif event.key == pygame.K_m:
                isM = 0

    MovementVector = (
        isLEFT-isRIGHT,
        isUP-isDOWN
    )

    Zoom = isP-isM
    Xoffset += MovementVector[0]*0.1
    Yoffset += MovementVector[1]*0.1
    ranges += Zoom*0.1


    pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))

    for x in range(width):
        for y in range(height):
            pixelDependent = complex(ChangeRange(x,0,width,-ranges,ranges)-Xoffset,ChangeRange(y,0,height,-ranges,ranges)-Yoffset)
            Static = complex(-0.5251993,-0.5251993)
            i = GetNextValue(pixelDependent,Static)
            color = toRGB((i*6,1,1))
            pygame.draw.rect(Surface, color, pygame.Rect(x,y,1,1))

    pygame.display.flip()