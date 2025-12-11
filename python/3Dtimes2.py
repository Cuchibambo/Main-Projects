from MathScripts import *
from pythonOBJparser import *
import pygame

class Point():
    def __init__(self, pos:tuple):
        self.pos = pos

pygame.init()
width,height = 500, 500
Surface = pygame.display.set_mode((width,height))
backgroundColor = (50, 50, 50)
PointColor = (255, 100, 100)
FaceColor = (20, 100, 100)
pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()

def PlacePointInFront():
    Points.append(Point((-Center[0],
                         -Center[1],
                         -Center[2])))

Center = (0,0,0)
CameraDistance = 1
vec1 = NormalizeVector((1,0,0))
vec2 = NormalizeVector((0,0,1))
Points = []

OBJImport = r'3DModels\Ultrakill Peircer.obj'

PointsVertexPos = GetVerteciesFromOBJ(OBJImport,1)
Faces = GetFacesFromOBJ(OBJImport)

for i in range(len(Faces)):
    Faces[i] = [Faces[i],0]


for pos in PointsVertexPos:
    Points.append(Point(pos))

FPS = 120
HorizontalMoveSpeed, DepthMoveSpeed, VerticalMoveSpeed = 0.05, 0.05, 0.05
X_RotationSpeed, Y_RotationSpeed, Z_RotationSpeed = 0.03, 0.03, 0.03
MovementVector = (0, 0, 0)
RotationVector = (0, 0, 0)
isZpressed, isSpressed, isQpressed, isDpressed, isLEFTpressed, isRIGHTpressed, isUPpressed, isDOWNpressed, isSPACEpressed, isSHIFTpressed = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
X_Rotation, Z_Rotation = 0, 0
clock = pygame.time.Clock()

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
            if event.key == pygame.K_SPACE:
                isSPACEpressed = 1
            if event.key == pygame.K_LSHIFT:
                isSHIFTpressed = 1
                
            if event.key == pygame.K_e:
                PlacePointInFront()

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
            if event.key == pygame.K_SPACE:
                isSPACEpressed = 0
            if event.key == pygame.K_LSHIFT:
                isSHIFTpressed = 0
            
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:
        #         PlacePointInFront()
            
    # game loop
    clock.tick(FPS)
    pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height)) # empty
    
    # Handle Movement Vector
    MovementVector = (
        isQpressed-isDpressed,
        isSpressed-isZpressed,
        isSPACEpressed-isSHIFTpressed
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
    
    # Rotation Amounts
    Z_Rotation += Z_RotationSpeed*RotationVector[2]
    X_Rotation += X_RotationSpeed*RotationVector[0]

    # Handle Up-Down Rotation
    Rotatedvec1 = X_RotationMatrix(vec1,X_Rotation)
    Rotatedvec2 = X_RotationMatrix(vec2,X_Rotation)
    
    # Handle Left-Right rotation
    Rotatedvec1 = Z_RotationMatrix(Rotatedvec1,Z_Rotation)
    Rotatedvec2 = Z_RotationMatrix(Rotatedvec2,Z_Rotation)
    

    # Get Normal and Camera Pos
    Normal = GetNormalVector(Rotatedvec1,Rotatedvec2)
    Camera = (Normal[0] * CameraDistance, 
            Normal[1] * CameraDistance,
            Normal[2] * CameraDistance)

    # Draw points
    PointsPos = [None for _ in range(len(Points))]

    CenteredPointsPos = []
    
    for point in Points:
        CenteredPointPos = (point.pos[0] + Center[0],
                            point.pos[1] + Center[1],
                            point.pos[2] + Center[2])
        CenteredPointsPos.append(CenteredPointPos)
        
        # Culling
        if ProduitScalaire(NormalizeVector(CenteredPointPos),Normal) < 0:

            NormalPosPoint3D = FindIntersectionBetweeenLineAndPlane(Normal,CenteredPointPos,Camera)
            NormalPointPos2D = GetLinearCoeficientsRepresentationOfPointOnPlane(Rotatedvec1,Rotatedvec2,NormalPosPoint3D)
            PointPos2D = (ChangeRange(NormalPointPos2D[0],-1,1,0,width),
                        ChangeRange(NormalPointPos2D[1],-1,1,0,height))

            PointsPos[Points.index(point)] = PointPos2D # type: ignore
            
    for i in range(len(Faces)):
        Faces[i] = [Faces[i][0],GetMagnitude((Average([CenteredPointsPos[Faces[i][0][0]-1][0],
                                                    CenteredPointsPos[Faces[i][0][1]-1][0],
                                                    CenteredPointsPos[Faces[i][0][2]-1][0]]),
                                            Average([CenteredPointsPos[Faces[i][0][0]-1][1],
                                                    CenteredPointsPos[Faces[i][0][1]-1][1],
                                                    CenteredPointsPos[Faces[i][0][2]-1][1]]),
                                            Average([CenteredPointsPos[Faces[i][0][0]-1][2],
                                                    CenteredPointsPos[Faces[i][0][1]-1][2],
                                                    CenteredPointsPos[Faces[i][0][2]-1][2]]),))]
    
    Faces.sort(key= lambda x : x[1], reverse=True)
    
    # for pos in PointsPos:
    #     try:
    #         pygame.draw.circle(Surface, PointColor, pos, 5) # type: ignore
    #     except:
    #         pass
    
    for face in Faces:
        FaceColor = int(ChangeRange(face[1],Faces[-1][1],Faces[0][1],0,255))
        try:
            pygame.draw.polygon(Surface, (FaceColor,FaceColor,FaceColor), (PointsPos[face[0][0]-1],
                                                     PointsPos[face[0][1]-1],
                                                     PointsPos[face[0][2]-1]))
        except:
            pass
        
    pygame.display.flip()