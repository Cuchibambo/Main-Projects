from MathScripts import X_RotationMatrix,Y_RotationMatrix,Z_RotationMatrix,NormalizeVector,GetNormalVector
import pygame
PI = 3.14159

class Object():
    def __init__(self, vs, fs, origin, name) -> None:
        self.vs = vs
        self.fs = fs
        self.origin = origin
        self.name = name
        self.angle = [0,0,0]
        self.ns = []

class Camera():
    def __init__(self, pos, rotation, fov, speed, sensitivity) -> None:
        self.pos = pos
        self.rotation = rotation
        self.fov = (180-fov)*PI/180
        self.speed = speed 
        self.sensitivity = sensitivity

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
], [0,0,1.5], 'cube')]

camera = Camera([0,0,0], [0,0,0], 110, 1, 0.1)

pygame.display.init() # Might not work if it crashes change this
width,height = 500, 500
Surface = pygame.display.set_mode((width,height))
backgroundColor = (100, 100, 150)
PointColor = (255, 100, 100)
pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

def TranslatePoint(Point:list, Center:list) -> list:
    return [Point[0]-Center[0],
            Point[1]-Center[1],
            Point[2]-Center[2]]

def RotatePoint(Point:list, angle:list) -> list:
    XrotatedPoint = Z_RotationMatrix(Point,-angle[2]) # type: ignore
    XYrotatedPoint = Y_RotationMatrix(XrotatedPoint,-angle[1])
    XYZrotatedPoint = X_RotationMatrix(XYrotatedPoint,-angle[0])
    return XYZrotatedPoint # type: ignore

def ProjectPoints(Point:list) -> list:
    return [(Point[0]*camera.fov)/Point[2], 
            (Point[1]*camera.fov)/Point[2]]

def ChangeRange(Point):
    return [((Point[0]+1)/2)*width,
            ((1-Point[1])/2)*height]

def rotateVertex(v,angle,origin):
    v[0] -= origin[0]
    v[1] -= origin[1]
    v[2] -= origin[2]

    v = list(Z_RotationMatrix(Y_RotationMatrix(X_RotationMatrix(v,angle[0]),angle[1]),angle[2]))
    
    v[0] += origin[0]
    v[1] += origin[1]
    v[2] += origin[2]

    return v

def TriangulateFaces(f):
    fs = []
    for n in range(len(f)-2):
        fs.append([f[0],f[n+1],f[n+2]])
    return fs

for object in Objects:
    fs = []
    for f in object.fs:
        fs += TriangulateFaces(f)
    for i in range(len(fs)):
        vec1 = (
            object.vs[fs[i][0]][0]-object.vs[fs[i][1]][0],
            object.vs[fs[i][0]][1]-object.vs[fs[i][1]][1],
            object.vs[fs[i][0]][2]-object.vs[fs[i][1]][2]
        )
        vec2 = (
            object.vs[fs[i][0]][0]-object.vs[fs[i][2]][0],
            object.vs[fs[i][0]][1]-object.vs[fs[i][2]][1],
            object.vs[fs[i][0]][2]-object.vs[fs[i][2]][2]
        )
        object.ns.append(GetNormalVector(vec1,vec2))
    object.fs = fs

#         z s q d SpSh
Inputs = [0,0,0,0,0,0]

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                Inputs[0] = 1
            elif event.key == pygame.K_s:
                Inputs[1] = 1
            elif event.key == pygame.K_q:
                Inputs[2] = 1
            elif event.key == pygame.K_d:
                Inputs[3] = 1
            elif event.key == pygame.K_SPACE:
                Inputs[4] = 1
            elif event.key == pygame.K_LSHIFT:
                Inputs[5] = 1
                
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                quit()
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                Inputs[0] = 0
            elif event.key == pygame.K_s:
                Inputs[1] = 0
            elif event.key == pygame.K_q:
                Inputs[2] = 0
            elif event.key == pygame.K_d:
                Inputs[3] = 0
            elif event.key == pygame.K_SPACE:
                Inputs[4] = 0
            elif event.key == pygame.K_LSHIFT:
                Inputs[5] = 0
    
    # game loop
    clock.tick(FPS)
    pygame.draw.rect(Surface, backgroundColor, pygame.Rect(0, 0, width, height)) # empty
    
    # First Person Controls
    dMousePos = pygame.mouse.get_rel()
    RotationVector = [
        -dMousePos[1],
        -dMousePos[0],
        0
    ]

    camera.rotation[0] += RotationVector[0] * camera.sensitivity * dt # type: ignore
    camera.rotation[1] += RotationVector[1] * camera.sensitivity * dt # type: ignore
    camera.rotation[2] += RotationVector[2] * camera.sensitivity * dt # type: ignore
    
    # Move camera
    MovmentVector = NormalizeVector([
        Inputs[3]-Inputs[2],
        Inputs[4]-Inputs[5],
        Inputs[0]-Inputs[1],
    ]) # type: ignore
    
    # MovmentVector = X_RotationMatrix(MovmentVector,camera.rotation[0])
    MovmentVector = Y_RotationMatrix(MovmentVector,camera.rotation[1])
    # MovmentVector = Z_RotationMatrix(MovmentVector,camera.rotation[2])
    
    camera.pos[0] += MovmentVector[0]*camera.speed*dt
    camera.pos[1] += MovmentVector[1]*camera.speed*dt
    camera.pos[2] += MovmentVector[2]*camera.speed*dt
    
    for object in Objects:
        vsProjected = []
        o = object.origin
        o = TranslatePoint(o, camera.pos)
        o = list(RotatePoint(o, camera.rotation))
        for v in object.vs:
            v = TranslatePoint(v, camera.pos)
            v = list(RotatePoint(v, camera.rotation))
            v = rotateVertex(v,object.angle, o)
            v = ProjectPoints(v)
            v = ChangeRange(v)
            vsProjected.append(v)
            pygame.draw.circle(Surface, PointColor, tuple(v), 5)
        i=0
        for n in object.ns:
            print(n,object.vs[object.fs[i][0]])
            n = [0.5*n[0]+object.vs[object.fs[i][0]][0],
                 0.5*n[1]+object.vs[object.fs[i][0]][1],
                 0.5*n[2]+object.vs[object.fs[i][0]][2]]
            n = TranslatePoint(n, camera.pos)
            n = list(RotatePoint(n, camera.rotation))
            n = rotateVertex(n,object.angle,object.vs[object.fs[i][0]])
            n = ProjectPoints(n)
            n = ChangeRange(n)
            pygame.draw.circle(Surface, '#ffffff', tuple(n), 5)
            i+=1

        for f in object.fs:
            for v in f:
                pygame.draw.line(Surface, PointColor, vsProjected[v], vsProjected[f[(f.index(v)+1)%len(f)]])
        
        # for x in range(width):
        #     for y in range(height):
                
        
        # object.angle[1] += 0.5*2*PI*dt  # type: ignore 0.5 rotation per second
        # camera.rotation[1]+=1*dt
        
    pygame.display.flip()