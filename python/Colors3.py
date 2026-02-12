import pygame
import random

# Colors
BackgroundColor = "#ffffff"
BaseColor = "#874444"

def RGB_from_Hex(hex:str):
    hex = hex[1:]
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
BaseColor = RGB_from_Hex(BaseColor)
pygame.init()
width, height = 500, 500
Screen = pygame.display.set_mode((width,height))
pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
    
    pygame.draw.rect(Screen, BackgroundColor, pygame.Rect(0, 0, width, height))
    BaseColor1 = (BaseColor[0]+random.randint(0,10),BaseColor[1]+random.randint(0,10),BaseColor[2]+random.randint(0,10))
    BaseColor2 = (BaseColor[0]+random.randint(0,10),BaseColor[1]+random.randint(0,10),BaseColor[2]+random.randint(0,10))
    BaseColor3 = (BaseColor[0]+random.randint(0,10),BaseColor[1]+random.randint(0,10),BaseColor[2]+random.randint(0,10))
    BaseColor4 = (BaseColor[0]+random.randint(0,10),BaseColor[1]+random.randint(0,10),BaseColor[2]+random.randint(0,10))
    if BaseColor1[0] > 255: BaseColor1[0] = 255
    elif BaseColor1[0] < 0: BaseColor1[0] = 0
    if BaseColor1[1] > 255: BaseColor1[1] = 255
    elif BaseColor1[1] < 0: BaseColor1[1] = 0
    if BaseColor1[2] > 255: BaseColor1[2] = 255
    elif BaseColor1[2] < 0: BaseColor1[2] = 0
    
    if BaseColor1[0] > 255: BaseColor1[0] = 255
    elif BaseColor1[0] < 0: BaseColor1[0] = 0
    if BaseColor1[1] > 255: BaseColor1[1] = 255
    elif BaseColor1[1] < 0: BaseColor1[1] = 0
    if BaseColor1[2] > 255: BaseColor1[2] = 255
    elif BaseColor1[2] < 0: BaseColor1[2] = 0

    if BaseColor1[0] > 255: BaseColor1[0] = 255
    elif BaseColor1[0] < 0: BaseColor1[0] = 0
    if BaseColor1[1] > 255: BaseColor1[1] = 255
    elif BaseColor1[1] < 0: BaseColor1[1] = 0
    if BaseColor1[2] > 255: BaseColor1[2] = 255
    elif BaseColor1[2] < 0: BaseColor1[2] = 0
    pygame.draw.rect(Screen, BaseColor1, (0,0,width/2,height/2))
    pygame.draw.rect(Screen, BaseColor2, (width/2,0,width/2,height/2))
    pygame.draw.rect(Screen, BaseColor3, (0,height/2,width/2,height/2))
    pygame.draw.rect(Screen, BaseColor4, (width/2,height/2,width/2,height/2))

    key = random.randint(0,3)
    if key == 0: BaseColor = BaseColor1
    elif key == 1: BaseColor = BaseColor2
    elif key == 2: BaseColor = BaseColor3
    elif key == 3: BaseColor = BaseColor4

    pygame.display.flip()