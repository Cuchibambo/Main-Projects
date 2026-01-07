import pygame
import random
from MathScripts import *
import json

# Food Class
class Food():
    def __init__(self, pos) -> None:
        self.pos = pos

# Blob Class
class Blob():
    def __init__(self, pos, speed, maxhunger, color, size, hunger, TurnsSurvived) -> None:
        self.pos = pos
        self.speed = speed
        self.maxhunger = maxhunger
        self.hunger = hunger
        self.target = pos
        self.color = color
        self.size = size
        self.TurnsSurvived = TurnsSurvived

# Start pygame
pygame.init()
width, height = 1920, 1080
Surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
FPS = 30

# Colors
BackgroundColor = "#3D552D"
FoodColor = "#C14949"
BlobColor = "#2172e3"

pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height))
pygame.display.flip()

# Toggles
BlobColorDependSpeed = True
BlobSizeDependsMaxHunger = True

# Variables
tick = 0
turn = 0
secondsPerTurn = 3
Foods = []
SecondsBetweenFoodSpawn = 2
nbFoodPerSpawn = 20
Blobs = []
StartingBlobs = 10
StartSpeed = 5
StartMaxHunger = 3
StartHunger = 1+1
BaseSize = 5
reproductionCost = 1

# Interactible widgets


# Averages
AverageSpeedPerTurn = []
AverageSurvivalRate = []
nbBlobsPerTurn = []

# Make First Blobs
for i in range(StartingBlobs):
    if BlobColorDependSpeed: currentColor = "#ff0000"
    else: currentColor = BlobColor
    Blobs.append(Blob(0, StartSpeed, StartMaxHunger, currentColor, BaseSize, StartHunger, 0))

def Save(data):
    try:
        with open("python\EvoSims\Stats.json", "w") as file:
            json.dump(data, file, indent=4)
            print("JSON file saved successfully!")
    except Exception as e:
        print(f"Error saving file: {e}")

# Start loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Stats = [AverageSpeedPerTurn, nbBlobsPerTurn, AverageSurvivalRate]
            Save(Stats)
            pygame.quit()
            running = False
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Stats = [AverageSpeedPerTurn, nbBlobsPerTurn, AverageSurvivalRate]
                Save(Stats)
                pygame.quit()
                running = False
                quit()

    clock.tick(FPS) # FPS handling
    pygame.draw.rect(Surface, BackgroundColor, pygame.Rect(0,0,width,height)) # Erase screen

    # Start turn
    if tick % (FPS*secondsPerTurn) == 0:
        Foods = []
        AverageSpeedPerTurn.append(0)
        AverageSurvivalRate.append(0)
        nbBlobsPerTurn.append(0)
        for _ in range(nbFoodPerSpawn):
            Foods.append(Food((random.randint(0,width),random.randint(0,height))))
        for blob in Blobs:
            blob.hunger -= 1
            if blob.hunger <= 0:
                Blobs.remove(blob)
            elif blob.hunger == blob.maxhunger-1:
                blob.TurnsSurvived += 1
                blob.hunger -= reproductionCost
                newSpeed = blob.speed + (random.random()*2) - 1
                if BlobColorDependSpeed: currentColor = Convert_HSV_to_RGB((int((newSpeed/StartSpeed)*20),1,1))
                else: currentColor = BlobColor
                if BlobSizeDependsMaxHunger: currentSize = (blob.maxhunger*BaseSize)/StartMaxHunger
                else: currentSize = BaseSize
                Blobs.append(Blob(blob.pos, newSpeed, blob.maxhunger, currentColor, currentSize, 1, 0))
            blob.pos = (random.randint(0,width),random.randint(0,height))
            AverageSpeedPerTurn[-1] += blob.speed
            AverageSurvivalRate[-1] += blob.TurnsSurvived
        AverageSpeedPerTurn[-1] = AverageSpeedPerTurn[-1]/len(Blobs)
        AverageSurvivalRate[-1] = AverageSurvivalRate[-1]/len(Blobs)
        nbBlobsPerTurn[-1] = len(Blobs)

    # Get closest food to every blob
    for blob in Blobs:
        if blob.hunger != blob.maxhunger:
            if blob.target in Foods:
                pass
            else:
                if len(Foods) != 0:
                    distances = []
                    for food in Foods:
                        distances.append((GetMagnitude(TupleSubtract(blob.pos,food.pos)),Foods.index(food)))
                    distances.sort()
                    chosenFood = random.choice(distances[:2])
                    blob.target = Foods[chosenFood[1]]
        else:
            blob.target = None
    
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

    # Draw Foods
    for food in Foods:
        pygame.draw.circle(Surface, FoodColor, food.pos, 8)

    # Draw Blobs
    for blob in Blobs:
        pygame.draw.circle(Surface, blob.color, blob.pos, blob.size)

    tick += 1
    pygame.display.flip() # Update Screen