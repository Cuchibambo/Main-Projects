import pygame
import random
from MathScripts import *

# Food Class
class Food():
    def __init__(self, pos) -> None:
        self.pos = pos

# Blob Class
class Blob():
    def __init__(self, pos, speed, maxhunger, hungerdecay, color, size) -> None:
        self.pos = pos
        self.speed = speed
        self.maxhunger = maxhunger
        self.hunger = maxhunger//2
        self.hungerdecay = hungerdecay
        self.target = pos
        self.color = color
        self.size = size

# Start pygame
pygame.init()
width, height = 500, 500
Surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
FPS = 30

# Colors
BackgroundColor = "#434343"
FoodColor = "#C14949"
BlobColor = "#2172e3"

pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))
pygame.display.flip()

# Toggles
BlobColorDependSpeed = True
BlobSizeDependsMaxHunger = True

# Variables
tick = 0
Foods = []
SecondsBetweenFoodSpawn = 2
nbFoodPerSpawn = 20
Blobs = []
StartingBlobs = 10
StartSpeed = 5
StartMaxHunger = 5
StartHungerDecay = 2
BaseSize = 5
reproductionCost = 3

# Interactible widgets


# Make First Blobs
for i in range(StartingBlobs):
    if BlobColorDependSpeed: currentColor = "#ff0000"
    else: currentColor = BlobColor
    Blobs.append(Blob((random.randint(0,width),random.randint(0,height)), StartSpeed, StartMaxHunger, StartHungerDecay, currentColor, BaseSize))

# Start loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()

    clock.tick(FPS) # FPS handling
    pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height)) # Erase screen

    # Spawn nb Food every Seconds
    if tick % (FPS*SecondsBetweenFoodSpawn) == 0:
        for _ in range(nbFoodPerSpawn):
            Foods.append(Food((random.randint(0,width),random.randint(0,height))))

    # Starve Blobs every Seconds
    for blob in Blobs:
        if blob.hungerdecay != 0:
            if tick % (FPS*blob.hungerdecay) == 0:
                blob.hunger -= 1
                if blob.hunger <= 0:
                    Blobs.remove(blob)
        else:
            Blobs.remove(blob)

    # Get closest food to every blob
    for blob in Blobs:
        if blob.target in Foods:
            pass
        else:
            if len(Foods) != 0:
                distances = []
                for food in Foods:
                    distances.append((GetMagnitude(TupleSubtract(blob.pos,food.pos)),Foods.index(food)))
                distances.sort()
                chosenFood = random.choice(distances[:3])
                blob.target = Foods[chosenFood[1]]
    
    # Make blobs go to target and eat
    for blob in Blobs:
        if blob.target in Foods:
            movementVector = TupleSubtract(blob.target.pos,blob.pos)
            if GetMagnitude(movementVector) > blob.speed:
                movementVector = NormalizeVector(movementVector)
                movementVector = (movementVector[0]*blob.speed,movementVector[1]*blob.speed)
                newpos = (movementVector[0]+blob.pos[0],movementVector[1]+blob.pos[1])
                blob.pos = newpos
            else:
                if blob.hunger < blob.maxhunger:
                    try:
                        Foods.remove(blob.target)
                        blob.hunger += 1
                    except:
                        pass
    
    # Reproduction
    for blob in Blobs:
        if blob.hunger == blob.maxhunger:
            blob.hunger -= reproductionCost
            newSpeed = blob.speed + (random.random()*2) - 0.5
            newMaxhunger = blob.maxhunger + random.randint(-1, 1)
            newHungerdecay = blob.hungerdecay + random.randint(-1, 1)
            if BlobColorDependSpeed: currentColor = Convert_HSV_to_RGB((int((newSpeed/StartSpeed)*20),1,1))
            else: currentColor = BlobColor
            if BlobSizeDependsMaxHunger: currentSize = (blob.maxhunger*BaseSize)/StartMaxHunger
            else: currentSize = BaseSize
            Blobs.append(Blob(blob.pos, newSpeed, newMaxhunger, newHungerdecay, currentColor, currentSize))

    # Draw Foods
    for food in Foods:
        pygame.draw.circle(Surface, FoodColor, food.pos, 8)

    # Draw Blobs
    for blob in Blobs:
        pygame.draw.circle(Surface, blob.color, blob.pos, blob.size)

    tick += 1
    pygame.display.flip() # Update Screen