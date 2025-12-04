import pygame
import math
import random

class Point():
    def __init__(self, folloWho, pos, num, color):
        self.folloWho = folloWho
        self.pos = pos
        self.num = num
        self.color = color
    def __str__(self):
        try:
            return f'Point {self.num} on ({self.pos[0]},{self.pos[1]})'
        except:
            return f'Point {self.num} on ({self.pos[0]},{self.pos[1]}), follows {self.folloWho.num}'

class Food():
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color

def GetVectorMagnitude(vec):
    return math.sqrt((vec[0]**2)+(vec[1]**2))

def NormalizeVector(vec):
    VectorMag = GetVectorMagnitude(vec)
    try:
        return [
            vec[0]/VectorMag,
            vec[1]/VectorMag
        ]
    except:
        return [0,0]


def RandomColor():
    return (
        math.floor(random.random()*255),
        math.floor(random.random()*255),
        math.floor(random.random()*255)
    )

def GetNextPos(center,previousPos):
    previousPos[0] -= center[0]
    previousPos[1] -= center[1]
    pos = NormalizeVector(previousPos)
    pos[0] = pos[0]*Closeness
    pos[1] = pos[1]*Closeness
    return [
        pos[0] + center[0],
        pos[1] + center[1]
    ]

def AddAPoint(color):
    folloWho = Points[-1]
    pos = [0,0]
    num = len(Points)+1
    Points.append(Point(folloWho,pos,num,color))

def AddFood(width,height):
    Foods.append(Food([random.randint(0,width),random.randint(0,height)], (255,0,0)))

def Convert_HSV_to_RGB(color):
    H = color[0]
    S = color[1]
    V = color[2]
    # H in degrees
    # S in percent
    # V in percent
    hR, hG, hB = 0, 0, 0
    H = H%360
    if H >= 0 and H < 60:
        hR = 1
        hG = H/60
        hB = 0
    elif H >= 60 and H < 120:
        hR = (-H/60)+2
        hG = 1
        hB = 0
    elif H >= 120 and H < 180:
        hR = 0
        hG = 1
        hB = (H/60)-2
    elif H >= 180 and H < 240:
        hR = 0
        hG = (-H/60)+4
        hB = 1
    elif H >= 240 and H < 300:
        hR = (H/60)-4
        hG = 0
        hB = 1
    elif H >= 300 and H < 360:
        hR = 1
        hG = 0
        hB = (-H/60)+6
        
    R = hR+1-S
    G = hG+1-S
    B = hB+1-S
    if R>1: R=1
    if G>1: G=1
    if B>1: B=1
    R = R*V
    G = G*V
    B = B*V
    return (int(R*255),int(G*255),int(B*255))
        

nbPoints = 30
PointRadius = 8
Closeness = 30
grow = False
TimeBetweenPointsSpawn = 1000*5
FoodSpawn = True
MaxFood = 1
Foods = []
NotColorsRandom = True
PointsPerRainbow = 30
StartColor = [0,1,1] # HSV in degrees and ratios respectively
RandomBgColor = False

CurrentColor = StartColor
if not NotColorsRandom:
    Points = [Point(None, [0,0], 0, RandomColor())]
    for _ in range(nbPoints-1):
        AddAPoint(RandomColor())
else:
    Points = [Point(None, [0,0], 0, Convert_HSV_to_RGB(StartColor))]
    for i in range(nbPoints-1):
        CurrentColor[0] += 360/(PointsPerRainbow-1)
        AddAPoint(Convert_HSV_to_RGB(CurrentColor))

def main():
    global nbPoints, CurrentColor
    pygame.init()
    width, height = 1920, 1080
    GROW = pygame.USEREVENT+1
    pygame.time.set_timer(GROW, TimeBetweenPointsSpawn)
    if FoodSpawn:
        while len(Foods) < MaxFood:
            AddFood(width,height)
    Surface = pygame.display.set_mode((width,height))
    if RandomBgColor:
        backgroundColor = RandomColor()
    else:
       backgroundColor = (50,50,50) 
    pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
    pygame.display.flip()

    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == GROW:
                if grow:
                    if NotColorsRandom:
                        nbPoints+=1
                        CurrentColor[0] += 360/(PointsPerRainbow-1)
                        AddAPoint(Convert_HSV_to_RGB(CurrentColor))
                    else:
                        nbPoints+=1
                        AddAPoint(RandomColor())
                        
                        
        pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))

        mouse_pos = pygame.mouse.get_pos()
        Points[0].pos = [mouse_pos[0], mouse_pos[1]]
        for i in range(len(Points)-1):
            Points[i+1].pos = GetNextPos(Points[i+1].folloWho.pos,Points[i+1].pos)
            
        for point in Points:
            for food in Foods:
                if (point.pos[0] <= food.pos[0]+PointRadius and
                    point.pos[0] >= food.pos[0]-PointRadius and
                    point.pos[1] <= food.pos[1]+PointRadius and
                    point.pos[1] >= food.pos[1]-PointRadius):
                    if NotColorsRandom:
                        nbPoints+=1
                        CurrentColor[0] += 360/(PointsPerRainbow-1)
                        AddAPoint(Convert_HSV_to_RGB(CurrentColor))
                        Foods.remove(food)
                        AddFood(width,height)
                    else:
                        nbPoints+=1
                        AddAPoint(RandomColor())
                        Foods.remove(food)
                        AddFood(width,height)

        for point in Points:
            pygame.draw.circle(Surface, point.color, (point.pos[0],point.pos[1]), PointRadius)
            
        for food in Foods:
            pygame.draw.circle(Surface, food.color, (food.pos[0],food.pos[1]), PointRadius)

        pygame.display.flip()

if __name__ == '__main__':
    main()