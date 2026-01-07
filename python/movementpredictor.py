import pygame
from MathScripts import NormalizeVector

# basic object class
class Object():
    def __init__(self) -> None:
        self.pos = [0,0]
        self.dir = [0,1]
        self.speed = 1
        self.color = '000000'

# draw a point on screen to represent the object
def DrawObject(object):
    pygame.draw.circle(Screen, object.color, object.pos, ObjectRadius)

# draw the vizualiser for the direction of an object with lenghth = to its speed
def DrawDirVizualiser(object):
    endPos = [object.pos[0]+(object.dir[0]*object.speed),
              object.pos[1]+(object.dir[1]*object.speed)]
    pygame.draw.line(Screen, DirVizualiserColor, object.pos, endPos)

# Updates direction by using a point on the plane to point towards
def UpdateDir(object, coords):
    dir = (coords[0]-object.pos[0],
           coords[1]-object.pos[1])
    dir = list(NormalizeVector(dir))
    object.dir = dir

# Calculates the direction the projectile object needs to be aiming at to hit the target, here we divide ProjectileSPeed/TargetSpeed and Prejectile.xy-Target.xy
def CalculateProjectileDir(projectile, target):
    speed = projectile.speed/target.speed
    pos = [projectile.pos[0]-target.pos[0],
           projectile.pos[1]-target.pos[1]]
    
    if speed == 1:
        t = ((pos[0]**2)+(pos[1]**2))/((2*target.dir[0]*pos[0])+(2*target.dir[1]*pos[1]))
        if t<0:
            return target.dir
        else:
            return [target.dir[0]-(pos[0]/t),target.dir[1]-(pos[1]/t)]

# Time managment
FPS = 60
dt = 1/FPS
clock = pygame.time.Clock()

# Screen init
pygame.init()
aspectRatio = 16/9
height = 500
width = height*aspectRatio
Screen = pygame.display.set_mode((width, height))

# Colors
BackgroundColor = "#2c2c2c"
TargetColor = "#b43232"
ProjectileColor = "#b383e0"
DirVizualiserColor = '#ffffff'

# Arbitrary settings
ObjectRadius = 5

# bg innit
pygame.draw.rect(Screen, BackgroundColor, (0,0,width,height))
pygame.display.flip()

# Make the target and Projectile objects and give them initial values
Target = Object()
Target.pos = [0,3]
Target.dir = [1,0]
Target.speed = 100 # speed per seconds
Target.color = TargetColor
Projectile = Object()
Projectile.pos = [3, 0]
Projectile.speed = 100 # speed per seconds
Projectile.color = ProjectileColor

# Main loop
SimRuning = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Pauses or unpauses the sim, recalculates the Prejectile.dir every time
                if SimRuning: 
                    SimRuning = False
                else: 
                    SimRuning = True
                    Projectile.dir = CalculateProjectileDir(Projectile, Target) # type: ignore
                    print(Projectile.dir)
    
    # time managment
    clock.tick(FPS)
    pygame.draw.rect(Screen, BackgroundColor, (0,0,width,height))
    
    # When sim is running object should move when it isnt we can move them and change the dir
    if SimRuning:
        DrawDirVizualiser(Projectile)
        Target.pos[0] += Target.dir[0] * Target.speed * dt # type: ignore
        Target.pos[1] += Target.dir[1] * Target.speed * dt # type: ignore
        
        Projectile.pos[0] += Projectile.dir[0] * Projectile.speed * dt # type: ignore
        Projectile.pos[1] += Projectile.dir[1] * Projectile.speed * dt # type: ignore
    else:
        mousePos = pygame.mouse.get_pos()
        
        if pygame.mouse.get_pressed()[0]:
            Target.pos = list(mousePos)
            
        if pygame.mouse.get_pressed()[2]:
            Projectile.pos = list(mousePos)
            
        if pygame.mouse.get_pressed()[1]:
            UpdateDir(Target, mousePos)
            
        DrawDirVizualiser(Target)
    
    # Draw Objects on Screen
    DrawObject(Target)
    DrawObject(Projectile)
    
    # Update display
    pygame.display.flip()