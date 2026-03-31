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

def to3d(pos4d):
    x, y, z, w = pos4d[0], pos4d[1], pos4d[2], pos4d[3]
    X, Y, Z = x/(1-w), y/(1-w), z/(1-w)
    return (X,Y,Z)

def to2d(pos3D):
    x, y, z = pos3D[0], pos3D[1], pos3D[2]
    # X, Y = x/z, y/z
    X, Y = x/z, y/z
    return (X,Y)


def rotation(pos4d,angle,rot_plane):
    Pos4d = []
    Cos, Sin = cos(angle), sin(angle)
    for i in range(4):
        if rot_plane[0] == i:
            Pos4d.append(Cos*pos4d[rot_plane[0]]+Sin*pos4d[rot_plane[1]])
        elif rot_plane[1] == i:
            Pos4d.append(-Sin*pos4d[rot_plane[0]]+Cos*pos4d[rot_plane[1]])
        else:
            Pos4d.append(pos4d[i])

    return Pos4d






class Vertex:
    def __init__(self,pos) -> None:
        self.pos = pos
    def draw(self, origin, angle, rot_plane):
        Pos = self.pos
        for plane in rot_plane:
            Pos = rotation(Pos, angle, plane)
        Pos = vec_add(Pos,origin)
        Pos = to3d(Pos)
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
            for plane in rot_plane:
                pos = rotation(pos, angle, plane)
            pos = vec_add(pos,orgin)
            pos = to3d(pos)
            vertexPos.append(to2d(pos))
        for i in range(len(self.vertexIndexs)):
            pygame.draw.line(screen, toRGB(self.color), toScreen(vertexPos[i]), toScreen(vertexPos[(i+1)%len(self.vertexIndexs)]), 10)

class Object:
    def __init__(self, vs, fs, origin) -> None:
        self.vs = vs
        self.fs = fs
        self.origin = origin
        self.angle = 0
        self.rot_plane = [(0,2), (0,3), (1,3)]
    def draw(self):
        # for v in self.vs:
        #     v.draw(self.origin,self.angle,self.rot_plane)
        for f in self.fs:
            f.draw(self.origin, self.vs, self.angle, self.rot_plane)

# Cube
cube = Object(
    [
        # front face (z = +0.5)
        Vertex([-0.5, -0.5,  0.5, 0]),  # bottom-left
        Vertex([ 0.5, -0.5,  0.5, 0]),  # bottom-right
        Vertex([ 0.5,  0.5,  0.5, 0]),  # top-right
        Vertex([-0.5,  0.5,  0.5, 0]),  # top-left

        # back face (z = -0.5)
        Vertex([-0.5, -0.5, -0.5, 0]),  # bottom-left
        Vertex([ 0.5, -0.5, -0.5, 0]),  # bottom-right
        Vertex([ 0.5,  0.5, -0.5, 0]),  # top-right
        Vertex([-0.5,  0.5, -0.5, 0])   # top-left
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
    [0, 0, 1.5, 0]
)


tesseract_vs = [
        # --- w = +0.5 cube ---
        Vertex([-0.5, -0.5,  0.5,  0.5]),  # 0
        Vertex([ 0.5, -0.5,  0.5,  0.5]),  # 1
        Vertex([ 0.5,  0.5,  0.5,  0.5]),  # 2
        Vertex([-0.5,  0.5,  0.5,  0.5]),  # 3

        Vertex([-0.5, -0.5, -0.5,  0.5]),  # 4
        Vertex([ 0.5, -0.5, -0.5,  0.5]),  # 5
        Vertex([ 0.5,  0.5, -0.5,  0.5]),  # 6
        Vertex([-0.5,  0.5, -0.5,  0.5]),  # 7

        # --- w = -0.5 cube ---
        Vertex([-0.5, -0.5,  0.5, -0.5]),  # 8
        Vertex([ 0.5, -0.5,  0.5, -0.5]),  # 9
        Vertex([ 0.5,  0.5,  0.5, -0.5]),  # 10
        Vertex([-0.5,  0.5,  0.5, -0.5]),  # 11

        Vertex([-0.5, -0.5, -0.5, -0.5]),  # 12
        Vertex([ 0.5, -0.5, -0.5, -0.5]),  # 13
        Vertex([ 0.5,  0.5, -0.5, -0.5]),  # 14
        Vertex([-0.5,  0.5, -0.5, -0.5])   # 15
    ]
tesseract_fs = [
        # --- faces of w = +0.5 cube ---
        Face([0, 1, 2, 3]),
        Face([4, 5, 6, 7]),
        Face([0, 3, 7, 4]),
        Face([1, 2, 6, 5]),
        Face([3, 2, 6, 7]),
        Face([0, 1, 5, 4]),

        # --- faces of w = -0.5 cube ---
        Face([8, 9,10,11]),
        Face([12,13,14,15]),
        Face([8,11,15,12]),
        Face([9,10,14,13]),
        Face([11,10,14,15]),
        Face([8, 9,13,12]),

        # --- connections between cubes (along w axis) ---
        Face([0, 1, 9, 8]),
        Face([1, 2,10, 9]),
        Face([2, 3,11,10]),
        Face([3, 0, 8,11]),

        Face([4, 5,13,12]),
        Face([5, 6,14,13]),
        Face([6, 7,15,14]),
        Face([7, 4,12,15])
    ]
tesseract_origin = [0, 0, 1.5, 0]
# Tesseract (4D cube)
tesseract = Object(tesseract_vs,tesseract_fs,tesseract_origin)
# tesseract1 = Object(tesseract_vs,tesseract_fs,tesseract_origin)





class Window:
    def __init__(self) -> None:
        self.running = False
        self.isRotating = 1
        self.rotSpeed = 1
    def leftClick(self,Mousepos):
        match self.isRotating:
            case 0:
                self.isRotating = 1
            case 1:
                self.isRotating = 0
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
            
            self.update([tesseract])
            
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