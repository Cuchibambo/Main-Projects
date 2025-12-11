from MathScripts import *
import time
import pygame

class Point():
    def __init__(self, pos:tuple, connectedVertexIndex:list):
        self.pos = pos
        self.connectedVertexIndex = connectedVertexIndex

pygame.init()
width,height = 500, 500
Surface = pygame.display.set_mode((width,height))
backgroundColor = (50, 50, 50)
PointColor = (255, 100, 100)
pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

Center = (0,0,0)
CameraDistance = 1
vec1 = NormalizeVector((1,0,0))
vec2 = NormalizeVector((0,0,1))
Points = [Point((1,1,1),[1,3,4]),
          Point((1,1,-1),[2,5]),
          Point((-1,1,-1),[6,3]),
          Point((-1,1,1),[7]),
          Point((1,3,1),[5,7]),
          Point((1,3,-1),[6]),
          Point((-1,3,-1),[7]),
          Point((-1,3,1),[]),
          Point((0,2,-2),[1,2,5,6])]

HorizontalMoveSpeed, DepthMoveSpeed, VerticalMoveSpeed = 0.001, 0.001, 0.001
X_RotationSpeed, Y_RotationSpeed, Z_RotationSpeed = 0.001, 0.001, 0.001
MovementVector = (0, 0, 0)
RotationVector = (0, 0, 0)
isZpressed, isSpressed, isQpressed, isDpressed, isLEFTpressed, isRIGHTpressed, isUPpressed, isDOWNpressed = 0, 0, 0, 0, 0, 0, 0, 0
X_Rotation, Z_Rotation = 0, 0

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                isZpressed = 1
            if event.key == pygame.K_s:
                isSpressed = 1
            if event.key == pygame.K_q:
                isQpressed = 1
            if event.key == pygame.K_d:
                isDpressed = 1
            if event.key == pygame.K_LEFT:
                isLEFTpressed = 1
            if event.key == pygame.K_RIGHT:
                isRIGHTpressed = 1
            if event.key == pygame.K_UP:
                isUPpressed = 1
            if event.key == pygame.K_DOWN:
                isDOWNpressed = 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                isZpressed = 0
            if event.key == pygame.K_s:
                isSpressed = 0
            if event.key == pygame.K_q:
                isQpressed = 0
            if event.key == pygame.K_d:
                isDpressed = 0
            if event.key == pygame.K_LEFT:
                isLEFTpressed = 0
            if event.key == pygame.K_RIGHT:
                isRIGHTpressed = 0
            if event.key == pygame.K_UP:
                isUPpressed = 0
            if event.key == pygame.K_DOWN:
                isDOWNpressed = 0
            
    # game loop
    pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height)) # empty
    
    # Handle Movement Vector
    MovementVector = (
        isQpressed-isDpressed,
        isSpressed-isZpressed,
        0
    )
    
    # Handle Rotation Vector
    RotationVector = (
        isUPpressed-isDOWNpressed,
        0,
        isRIGHTpressed-isLEFTpressed
    )
    
    # Handle Movement
    MovementVector = NormalizeVector(MovementVector)
    MovementVector = Z_RotationMatrix(MovementVector,Z_Rotation)
    Center = (Center[0] + HorizontalMoveSpeed*MovementVector[0],
              Center[1] + DepthMoveSpeed*MovementVector[1], 
              Center[2] + VerticalMoveSpeed*MovementVector[2])
    
    Z_Rotation += Z_RotationSpeed*RotationVector[2]
    X_Rotation += X_RotationSpeed*RotationVector[0]
    

    # Handle Left-Right rotation
    Rotatedvec1 = Z_RotationMatrix(vec1,Z_Rotation)
    Rotatedvec2 = Z_RotationMatrix(vec2,Z_Rotation)
    
    # Handle Up-Down Rotation
    Rotatedvec1 = X_RotationMatrix(Rotatedvec1,X_Rotation)
    Rotatedvec2 = X_RotationMatrix(Rotatedvec2,X_Rotation)

    # Get Normal and Camera Pos
    Normal = GetNormalVector(Rotatedvec1,Rotatedvec2)
    Camera = (Normal[0] * CameraDistance, 
            Normal[1] * CameraDistance,
            Normal[2] * CameraDistance)

    # Draw points

    PointsPos = []

    for point in Points:
        
        CenteredPointPos = (point.pos[0] + Center[0],
                            point.pos[1] + Center[1],
                            point.pos[2] + Center[2])
        NormalPosPoint3D = FindIntersectionBetweeenPointAndPlane(Normal,CenteredPointPos,Camera)
        NormalPointPos2D = GetLinearCoeficientsRepresentationOfPointOnPlane(Rotatedvec1,Rotatedvec2,NormalPosPoint3D)
        PointPos2D = (ChangeRange(NormalPointPos2D[0],-1,1,0,width),
                      ChangeRange(NormalPointPos2D[1],-1,1,0,height))

        PointsPos.append(PointPos2D)

        pygame.draw.circle(Surface, PointColor, PointPos2D, 5)
    
    for i in range(len(Points)):
        for vertex in Points[i].connectedVertexIndex:
            pygame.draw.line(Surface,PointColor,PointsPos[i],PointsPos[vertex])

    pygame.display.flip()
    
# TODO Up-Down Rotation