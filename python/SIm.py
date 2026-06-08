import pygame
from math import pi, cos, sin
from MathScripts import toRGB


# Colors
BackgroundColor = "#5a7651"

def GetDistance(A,B):
    return (((A[0]-B[0])**2)+((A[1]-B[1])**2)**0.5)

class bear:
    def __init__(self, pos=[0,0], health=100, food=100, age=0, targetPos=[0,0], isCombat=False, agro=None, attackRange=5, damage=10, visionRadius=100, moveSpeed=10) -> None:
        self.living = living("#32251d")
        self.pos = pos
        self.health = health
        self.maxHealth = health
        self.food = food
        self.maxFood = food
        self.age = age
        self.targetPos = targetPos
        self.isCombat = isCombat
        self.agro = agro
        self.attackRange = attackRange
        self.damage = damage
        self.visionRadius = visionRadius
        self.moveSpeed = moveSpeed
        self.potentialEnemies = [bear]
    def draw(self):
        pygame.draw.rect(screen, self.living.color, (self.pos[0], self.pos[1], 3, 3))
    def die(self):
        Objects.remove(self)
    def combatLogic(self):
        if self.health < 10:
            self.retreat()
        else:
            agro_distance = GetDistance(self.pos,self.agro.pos)
            if agro_distance <= self.attackRange:
                self.attack(self.agro)
            else:
                self.targetPos = self.agro.pos
                self.move()
    def retreat(self):
        self.targetPos = []
        self.move()
    def move(self):
        movementVector = [self.targetPos[0]-self.pos[0],self.targetPos[1]-self.pos[1]]
        targetDistance = GetDistance(self.targetPos,self.pos)
        normalizedMovementVector = [movementVector[0]/targetDistance,movementVector[1]/targetDistance]
        self.pos = [self.pos[0]+(normalizedMovementVector[0]*self.moveSpeed),self.pos[1]+(normalizedMovementVector[1]*self.moveSpeed)]
    def update(self):
        if self.health <= 0:
            self.die()
        if self.isCombat and self.agro != None:
            self.combatLogic()
        else:
            self.lookForEnemies()
            self.move()
    def attack(self,target):
        target.health -= self.damage
        if target.health <= 0:
            self.targetPos = [0,0]
    def isPotentialEnemie(self,entity):
        for enemies in self.potentialEnemies:
            if isinstance(entity, enemies):
                return True
        return False
    def lookForEnemies(self):
        for obj in Objects:
            if obj != self and self.isPotentialEnemie(obj):
                distanceToObj = GetDistance(self.pos,obj.pos)
                if distanceToObj < self.visionRadius:
                    self.agro = obj
                    self.isCombat = True
                    print('found enemy')
        
        
        
class living:
    def __init__(self, color="#0000FF") -> None:
        self.color = color

class staticObject:
    def __init__(self, color="#ff00ff", isCollidable=True) -> None:
        self.color = color
        self.isCollidable = isCollidable

class Window:
    def __init__(self) -> None:
        self.running = False
    def leftClick(self,Mousepos):
        pass
    def rightClick(self,Mousepos):
        pass
    def mwheel(self,e):
        pass
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.leftClick(pygame.mouse.get_pos())
                        case 3:
                            self.rightClick(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEWHEEL:
                    self.mwheel(event)
            # main loop
            clock.tick(FPS)
            pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, res, res)) # empty
            
            self.update()
            
            pygame.display.flip()
    def update(self):
        for obj in Objects:
            obj.draw()
            obj.update()
            
Objects=[bear(pos=[250,250]), bear(pos=[100,100], targetPos=[250,250])]
                    
# Pygame  
pygame.init()
res = 500
screen = pygame.display.set_mode((res, res))
pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, res, res))
pygame.display.flip()


# Time
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

# Start
window = Window()
window.run()