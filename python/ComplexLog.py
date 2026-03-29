import pygame
import math
import cmath
backgroundColor = "#2f2f2f"



def clamp(a):
    return max(min(a,1),0)

def lerp(min,max,t):
    return max+t*(min-max)

def getPixelColor(z,size):
    x, y = clamp((z.real/size)+0.5), clamp((z.imag/size)+0.5)
    R = x
    G = y
    B = 1
    return (R*255,G*255,B*255)

def MakeScreen(func,size):
    for x in range(width):
        for y in range(height):
            z = complex(((x/width)*2)-1,(((height-y)/height)*2)-1)
            try:
                z = func(z)
            except:
                z = 0
            color = getPixelColor(z,size)
            pygame.draw.rect(screen,color,(x,y,1,1))


width, height = 500, 500
pygame.init()
screen = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS



func = lambda x:x
size = 2
MakeScreen(func,size)
pygame.display.flip()

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            runing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            match event.button:
                case 1:
                    func = lambda x:cmath.log(x)
                    MakeScreen(func,size)
                    pygame.display.flip()
                case 3:
                    func = lambda x:cmath.exp(x)
                    MakeScreen(func,size)
                    pygame.display.flip()
        elif event.type == pygame.MOUSEWHEEL:
            size += event.y
            if size == 0: size = 1
            print(f'size = {size}')
            MakeScreen(func,size)
            pygame.display.flip()
    clock.tick(FPS)
    pygame.display.flip()
