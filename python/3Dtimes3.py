from MathScripts import X_RotationMatrix,Y_RotationMatrix,Z_RotationMatrix
import pygame

class Object():
    def __init__(self, vs, fs, origin, name) -> None:
        self.vs = vs
        self.fs = fs
        self.origin = origin
        self.name = name
        self.angle = [0,0,0]

Objects = [Object([
    # front face
    [0.5,0.5,1], #top-right
    [-0.5,0.5,1], #top-left
    [-0.5,-0.5,1], #bottom-left
    [0.5,-0.5,1], #bottom-right
    
    # far face
    [0.5,0.5,2],#top-right
    [-0.5,0.5,2], #top-left
    [-0.5,-0.5,2], #bottom-left
    [0.5,-0.5,2] #bottom-right
], [
    [0,1,2,3], # front face
    [4,5,6,7], # far face
    [0,4,5,1], # top face
    [3,7,6,2] # bottom face
], [0,0,1.25], 'cube')]

Center = [0,0,0]
Rotation = [0,0,0]

pygame.display.init() # Might not work if it crashes change this
width,height = 500, 500
Surface = pygame.display.set_mode((width,height))
backgroundColor = (100, 100, 150)
PointColor = (255, 100, 100)
pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()
FPS = 30
clock = pygame.time.Clock()
dt = 1/FPS
PI = 3.14159

def TranslatePoint(Point:list, Center:list) -> list:
    return [Point[0]-Center[0],
            Point[1]-Center[1],
            Point[2]-Center[2]]

def RotatePoint(Point:list, angle:list) -> list:
    XrotatedPoint = X_RotationMatrix(Point,-angle[0]) # type: ignore
    XYrotatedPoint = Y_RotationMatrix(XrotatedPoint,-angle[1])
    XYZrotatedPoint = Z_RotationMatrix(XYrotatedPoint,-angle[2])
    return XYZrotatedPoint # type: ignore

def ProjectPoints(Point:list) -> list:
    return [Point[0]/Point[2], 
            Point[1]/Point[2]]

def ChangeRange(Point):
    return [((Point[0]+1)/2)*width,
            ((1-Point[1])/2)*height]

def rotateVertex(v,angle):
    v[0] -= object.origin[0]
    v[1] -= object.origin[1]
    v[2] -= object.origin[2]
        
    v = list(Z_RotationMatrix(Y_RotationMatrix(X_RotationMatrix(v,angle[0]),angle[1]),angle[2]))
    
    v[0] += object.origin[0]
    v[1] += object.origin[1]
    v[2] += object.origin[2]

    return v
        
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    # game loop
    clock.tick(FPS)
    pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height)) # empty
    
    for object in Objects:
        vsProjected = []
        for v in object.vs:
            v = TranslatePoint(v, Center)
            v = rotateVertex(v,object.angle)
            v = list(RotatePoint(v, Rotation))
            v = ProjectPoints(v)
            v = ChangeRange(v)
            vsProjected.append(v)
            pygame.draw.circle(Surface, PointColor, tuple(v), 5)

        for f in object.fs:
            for v in f:
                pygame.draw.line(Surface, PointColor, vsProjected[v], vsProjected[f[(v+1)%len(f)]])
                
        object.angle[1] += 1*dt # type: ignore
        
    pygame.display.flip()