from MathScripts import *
import time
import pygame

class Point():
    def __init__(self, pos:tuple):
        self.pos = pos

pygame.init()
width,height = 1000, 1000
Surface = pygame.display.set_mode((width,height))
backgroundColor = (50, 50, 50)
PointColor = (182, 100, 100)
pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

Center = (0,0,0)
CameraDistance = 1
vec1 = NormalizeVector((1,0,0))
vec2 = NormalizeVector((0,0,1))
Points = [Point((-0.5,0.5,-0.5)),
          Point((0.5,0.5,-0.5)),
          Point((0.5,0.5,0.5)),
          Point((-0.5,0.5,0.5)),
          Point((-0.5,1.5,-0.5)),
          Point((0.5,1.5,-0.5)),
          Point((0.5,1.5,0.5)),
          Point((-0.5,1.5,0.5))]

HorizontalMoveSpeed, DepthMoveSpeed, VerticalMoveSpeed = 0.001, 0.001, 0.001
X_RotationSpeed, Y_RotationSpeed, Z_RotationSpeed = 0.001, 0.001, 0.001
MovementVector = (0, 0, 0)
RotationVector = (0, 0, 0)
isZpressed, isSpressed, isQpressed, isDpressed, isLEFTpressed, isRIGHTpressed, isUPpressed, isDOWNpressed = 0, 0, 0, 0, 0, 0, 0, 0
Z_Rotation = 0

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
        isDOWNpressed-isUPpressed,
        0,
        isRIGHTpressed-isLEFTpressed
    )
    
    # Get Normal and Camera Pos
    Normal = GetNormalVector(vec1,vec2)
    Camera = (Normal[0] * CameraDistance, 
            Normal[1] * CameraDistance,
            Normal[2] * CameraDistance)
    
    # Handle Movement
    MovementVector = NormalizeVector(MovementVector)
    MovementVector = Z_RotationMatrix(MovementVector,Z_Rotation)
    Center = (Center[0] + HorizontalMoveSpeed*MovementVector[0],
              Center[1] + DepthMoveSpeed*MovementVector[1], 
              Center[2] + VerticalMoveSpeed*MovementVector[2])
    
    Z_Rotation += Z_RotationSpeed*RotationVector[2]
    
    # Handle Left-Right rotation
    vec1 = Z_RotationMatrix(vec1,Z_RotationSpeed*RotationVector[2])
    vec2 = Z_RotationMatrix(vec2,Z_RotationSpeed*RotationVector[2])
    
    # Handle Up-Down Rotation
    vec1 = X_RotationMatrix(vec1,X_RotationSpeed*RotationVector[0])
    vec2 = X_RotationMatrix(vec2,X_RotationSpeed*RotationVector[0])
    
    # Draw points
    for point in Points:
        CenteredPointPos = (point.pos[0] + Center[0],
                            point.pos[1] + Center[1],
                            point.pos[2] + Center[2])
        NormalPosPoint3D = FindIntersectionBetweeenPointAndPlane(Normal,CenteredPointPos,Camera)
        NormalPointPos2D = GetLinearCoeficientsRepresentationOfPointOnPlane(vec1,vec2,NormalPosPoint3D)
        PointPos2D = (ChangeRange(NormalPointPos2D[0],-1,1,0,width),
                      ChangeRange(NormalPointPos2D[1],-1,1,0,height))
        
        pygame.draw.circle(Surface, PointColor, PointPos2D, 5)
    
    pygame.display.flip()
    
    
# TODO Up-Down Rotation