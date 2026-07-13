from typing import Any

import pygame
from math import pi, cos, sin
from MathScripts import toRGB


# Colors
BackgroundColor = "#81abc0"
PointColor = "#35085c"
EdgeColor = [208,0.9,0.84]


def toScreen(pos):
    x, y = pos[0], pos[1]
    X = ((x+1)*width)/2
    Y = ((1-y)*height)/2
    return (X,Y)

def vec_add(vec, vec1):
    vec2 = []
    for i in range(len(vec)):
        vec2.append(vec[i]+vec1[i])
    return vec2

def to2d(pos3D):
    x, y, z = pos3D[0], pos3D[1], pos3D[2]
    # X, Y = x/z, y/z
    X, Y = x/z, y/z
    return (X,Y)


# def rotation(pos3d,angle,rot_plane):
#     Pos3d = []
#     Cos, Sin = cos(angle), sin(angle)
#     for i in range(4):
#         if rot_plane[0] == i:
#             Pos3d.append(Cos*pos3d[rot_plane[0]]+Sin*pos3d[rot_plane[1]])
#         elif rot_plane[1] == i:
#             Pos3d.append(-Sin*pos3d[rot_plane[0]]+Cos*pos3d[rot_plane[1]])
#         else:
#             Pos3d.append(pos3d[i])

#     return Pos3d


class Matrix:
    def __init__(self,lines,columns) -> None:
        self.lines = lines
        self.columns = columns
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(1,args)
        print(2,*args)
        print(3,kwds)
        print(4,*kwds)
        print(5,**kwds)


class Vertex:
    def __init__(self,pos) -> None:
        self.pos = pos
    def draw(self, origin, angle, rot_plane):
        Pos = self.pos
        # for plane in rot_plane:
        #     Pos = rotation(Pos, angle, plane)
        Pos = vec_add(Pos,origin)
        pos2d = to2d(Pos)
        pygame.draw.circle(screen, PointColor, toScreen(pos2d), 5)


class Face:
    def __init__(self,vertexIndexs) -> None:
        self.vertexIndexs = vertexIndexs
        self.color = EdgeColor
    def draw(self, orgin, vs, angle, rot_plane):
        # self.color[0] += dt
        vertexPos = []
        for vIndex in self.vertexIndexs:
            pos = vs[vIndex].pos
            # for plane in rot_plane:
            #     pos = rotation(pos, angle, plane)
            pos = vec_add(pos,orgin)
            vertexPos.append(to2d(pos))
        for i in range(len(self.vertexIndexs)):
            pygame.draw.line(screen, toRGB(self.color), toScreen(vertexPos[i]), toScreen(vertexPos[(i+1)%len(self.vertexIndexs)]), 10)

class Object:
    def __init__(self, vs, fs, origin) -> None:
        self.vs = vs
        self.fs = fs
        self.origin = origin
        self.angle = 0
        self.rot_axis = [0]
    def draw(self):
        # for v in self.vs:
        #     v.draw(self.origin,self.angle,self.rot_plane)
        for f in self.fs:
            f.draw(self.origin, self.vs, self.angle, self.rot_axis)

# Cube
cube = Object(
    [
        # front face (z = +0.5)
        Vertex([-0.5, -0.5,  0.5]),  # bottom-left
        Vertex([ 0.5, -0.5,  0.5]),  # bottom-right
        Vertex([ 0.5,  0.5,  0.5]),  # top-right
        Vertex([-0.5,  0.5,  0.5]),  # top-left

        # back face (z = -0.5)
        Vertex([-0.5, -0.5, -0.5]),  # bottom-left
        Vertex([ 0.5, -0.5, -0.5]),  # bottom-right
        Vertex([ 0.5,  0.5, -0.5]),  # top-right
        Vertex([-0.5,  0.5, -0.5])   # top-left
    ],
    [
        # each face uses indices into the vertex list

        # front
        Face([0, 1, 2, 3]),

        # back
        Face([4, 5, 6, 7]),

        # left
        Face([0, 3, 7, 4]),

        # right
        Face([1, 2, 6, 5]),

        # top
        Face([3, 2, 6, 7]),

        # bottom
        Face([0, 1, 5, 4])
    ],
    [0, 0, 1.5]
)




class Window:
    def __init__(self) -> None:
        self.running = False
        self.isRotating = False
        self.rotSpeed = 1
        self.idk = Matrix(1,1)
    def leftClick(self,Mousepos):
        self.isRotating = not self.isRotating
        self.idk('Hello',['hi',2,3],self.idk)
    def rightClick(self,Mousepos):
        pass
    def mwheel(self,e):
        self.rotSpeed += e.y 
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
            pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, width, height)) # empty
            
            self.update([cube])
            
            pygame.display.flip()
    def update(self, objs):
        for obj in objs:
            obj.draw()
            obj.angle += dt*pi*0.5*self.isRotating*self.rotSpeed
            
        
# Pygame  
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.draw.rect(screen, BackgroundColor, pygame.Rect(0, 0, width, height))
pygame.display.flip()


# Time 
FPS = 60
clock = pygame.time.Clock()
dt = 1/FPS

# Start
window = Window()
window.run()