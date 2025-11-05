import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

root = tk.Tk()

ScreenX, ScreenY = 400, 300
# ScreenX, ScreenY = 1920, 1080
CameraXYZ = (ScreenX/2, ScreenY/2, -200)
LightXYZ = CameraXYZ

canvas = tk.Canvas(root, width=ScreenX, height=ScreenY)
canvas.pack()
canvas.configure(bg="#6C5876")

img = Image.new("RGB", (ScreenX, ScreenY), (108, 88, 118))

# Screen is at z = 0 with x and y as 400, 300
# Camera is at z = -10 with x and y as 200, 150 

# Point in 3D space Coords = (200, 150, 10)
# (x,y,z) = (x1​, y1​, z1​) + t(x2​−x1​, y2​−y1​, z2​−z1​)

# t = (-z1)/(z2-z1)

# (x1, y1, z1) + ((-z1)/(z2-z1))*(x2​−x1​, y2​−y1​, z2​−z1​)

def drawPoint(x,y,radius):
    canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill='#202020',outline='white')

def drawProjectedPoint(x,y,z):

    P1 = np.array([x, y, z])
    IpXYZ = np.zeros(3)
    
    IpXYZ = CameraXYZ + ((-CameraXYZ[2])/(P1[2]-CameraXYZ[2]))*(P1-CameraXYZ)

    drawPoint(IpXYZ[0], IpXYZ[1], 5)

def middleOfFace(P1,P2,P3):
    out = np.zeros(3)
    out[0] = (P1[0]+P2[0]+P3[0])/3
    out[1] = (P1[1]+P2[1]+P3[1])/3
    out[2] = (P1[2]+P2[2]+P3[2])/3
    return out

def to_hex(n):
    return f"{n:02x}"

def drawFaceDeprecated(P1,P2,P3,P4,col):
    canvas.create_polygon(P1[0],P1[1],P2[0],P2[1],P3[0],P3[1],P4[0],P4[1],fill=f'#{col}{col}{col}')
    
def drawFace(Points,col):
    canvas.create_polygon(Points[0][0],Points[0][1],Points[1][0],Points[1][1],Points[2][0],Points[2][1],fill=f'#{col}{col}{col}')

def DrawCube(x,y,z,SideLength,thetaX,thetaY,thetaZ):
    # Gets all points x,y and z coords for the cube
    radius = SideLength/2
    xp = x+radius
    xm = x-radius
    yp = y+radius
    ym = y-radius
    zp = z+radius
    zm = z-radius
    # Rotates every point
    P1 = rotatePointIn3D(xm,ym,zm,x,y,z,thetaX,thetaY,thetaZ) # Bottom Left close
    P2 = rotatePointIn3D(xp,ym,zm,x,y,z,thetaX,thetaY,thetaZ) # Bottom right close
    P3 = rotatePointIn3D(xm,yp,zm,x,y,z,thetaX,thetaY,thetaZ) # Top Left close
    P4 = rotatePointIn3D(xp,yp,zm,x,y,z,thetaX,thetaY,thetaZ) # Top right close
    P5 = rotatePointIn3D(xm,ym,zp,x,y,z,thetaX,thetaY,thetaZ) # Bottom Left far
    P6 = rotatePointIn3D(xp,ym,zp,x,y,z,thetaX,thetaY,thetaZ) # Bottom right far
    P7 = rotatePointIn3D(xm,yp,zp,x,y,z,thetaX,thetaY,thetaZ) # Top Left far
    P8 = rotatePointIn3D(xp,yp,zp,x,y,z,thetaX,thetaY,thetaZ) # Top right far
    # Face 1 : P1 P2 P3 P4 'Close Face'
    # Face 2 : P1 P3 P5 P7 'Left Face'
    # Face 3 : P2 P4 P6 P8 'Right Face'
    # Face 4 : P3 P4 P7 P8 'Top Face'
    # Face 5 : P1 P2 P5 P6 'Bottom Face'
    # Face 6 : P5 P6 P7 P8 'Far Face'
    # Gets coords on screen for each point
    p1 = GetProjectedPoint(P1)
    p2 = GetProjectedPoint(P2)
    p3 = GetProjectedPoint(P3)
    p4 = GetProjectedPoint(P4)
    p5 = GetProjectedPoint(P5)
    p6 = GetProjectedPoint(P6)
    p7 = GetProjectedPoint(P7)
    p8 = GetProjectedPoint(P8)
    # Gets the point at the middle of each face
    Face1 = middleOfFace(P1, P2, P3, P4)
    Face2 = middleOfFace(P1, P3, P5, P7)
    Face3 = middleOfFace(P2, P4, P6, P8)
    Face4 = middleOfFace(P3, P4, P7, P8)
    Face5 = middleOfFace(P1, P2, P5, P6)
    Face6 = middleOfFace(P5, P6, P7, P8)
    # Calculates the distance between middle of face and camera
    FaceDisctance1 = distanceBetweenPoints(Face1, np.array([CameraXYZ[0],CameraXYZ[1],CameraXYZ[2]]))
    FaceDisctance2 = distanceBetweenPoints(Face2, np.array([CameraXYZ[0],CameraXYZ[1],CameraXYZ[2]]))
    FaceDisctance3 = distanceBetweenPoints(Face3, np.array([CameraXYZ[0],CameraXYZ[1],CameraXYZ[2]]))
    FaceDisctance4 = distanceBetweenPoints(Face4, np.array([CameraXYZ[0],CameraXYZ[1],CameraXYZ[2]]))
    FaceDisctance5 = distanceBetweenPoints(Face5, np.array([CameraXYZ[0],CameraXYZ[1],CameraXYZ[2]]))
    FaceDisctance6 = distanceBetweenPoints(Face6, np.array([CameraXYZ[0],CameraXYZ[1],CameraXYZ[2]]))
    # Function to draw each face
    def drawFace1(col):
        drawFaceDeprecated(p1,p2,p4,p3,col)
    def drawFace2(col):
        drawFaceDeprecated(p1,p3,p7,p5,col)
    def drawFace3(col):
        drawFaceDeprecated(p2,p4,p8,p6,col)
    def drawFace4(col):
        drawFaceDeprecated(p3,p4,p8,p7,col)
    def drawFace5(col):
        drawFaceDeprecated(p1,p2,p6,p5,col)
    def drawFace6(col):
        drawFaceDeprecated(p5,p6,p8,p7,col)
    # adds these distance along with their coresponding funciton to draw them in a list of tuples
    FaceDistances = [(FaceDisctance1,drawFace1), 
                     (FaceDisctance2,drawFace2), 
                     (FaceDisctance3,drawFace3), 
                     (FaceDisctance4,drawFace4), 
                     (FaceDisctance5,drawFace5), 
                     (FaceDisctance6,drawFace6)]
    # Sort the list according to the distances in descending order
    FaceDistances.sort(key=lambda x: x[0], reverse=True)
    # Draw every Face from far to close
    for i in FaceDistances:
        i[1]((int((np.sin((0.01*i[0]))**2)*255)))

def drawTri(P1,P2,P3,col):
    ProjectedPoints = np.array([GetProjectedPoint(P1), GetProjectedPoint(P2), GetProjectedPoint(P3)])
    drawFace(ProjectedPoints,col)

def GetProjectedPoint(P1):
    # P1 = np.array([x, y, z])
    IpXYZ = np.zeros(3)
    
    IpXYZ = CameraXYZ + ((-CameraXYZ[2])/(P1[2]-CameraXYZ[2]))*(P1-CameraXYZ)
    
    return IpXYZ[0], IpXYZ[1]

def distanceBetweenPoints(P1,P2):
    return np.sqrt(((P2[0]-P1[0])**2)+((P2[1]-P1[1])**2)+((P2[2]-P1[2])**2))

def rotatePointIn3D(P1, CXYZ, thetaX, thetaY, thetaZ):
    out = np.zeros(3)
    
    x = P1[0] - CXYZ[0]
    y = P1[1] - CXYZ[1]
    z = P1[2] - CXYZ[2]

    out[0] = (np.cos(thetaY) * np.cos(thetaZ) * x) + (np.cos(thetaY) * np.sin(thetaZ) * -y) + (np.sin(thetaY) * z)
    out[1] = ((np.cos(thetaX) * np.sin(thetaZ) + np.sin(thetaX) * np.sin(thetaY) * np.cos(thetaZ)) * x) + ((np.cos(thetaX) * np.cos(thetaZ) - np.sin(thetaX) * np.sin(thetaY) * np.sin(thetaZ)) * y) + (np.sin(thetaX) * np.cos(thetaY) * -z)
    out[2] = ((np.sin(thetaX) * np.sin(thetaZ) - np.cos(thetaX) * np.sin(thetaY) * np.cos(thetaZ)) * x) + ((np.sin(thetaX) * np.cos(thetaZ) + np.cos(thetaX) * np.sin(thetaY) * np.sin(thetaZ)) * y) + (np.cos(thetaX) * np.cos(thetaY) * z)
    
    out[0] += CXYZ[0]
    out[1] += CXYZ[1]
    out[2] += CXYZ[2]
    
    return out

def barycentric_weights(P1, P2, P3, P):
    v0 = np.array(P2) - np.array(P1)
    v1 = np.array(P3) - np.array(P1)
    v2 = np.array(P) - np.array(P1)
    d00 = np.dot(v0, v0)
    d01 = np.dot(v0, v1)
    d11 = np.dot(v1, v1)
    d20 = np.dot(v2, v0)
    d21 = np.dot(v2, v1)
    denom = d00 * d11 - d01 * d01
    if denom == 0:
        return 0,0,0
    v = (d11*d20 - d01*d21) / denom
    w = (d00*d21 - d01*d20) / denom
    u = 1 - v - w
    return u, v, w

Points = np.array([])
Faces = []

def DefineMesh():
    global Points, Faces
    # Cube
    # Points = np.array([(150,200,50),
    #                    (250,200,50),
    #                    (250,100,50),
    #                    (150,100,50),
    #                    (150,200,150),
    #                    (150,100,150),
    #                    (250,200,150),
    #                    (250,100,150)])
    # Faces = [
    #     (0,1,2),
    #     (0,2,3),
    #     (4,0,3),
    #     (4,3,5),
    #     (6,4,5),
    #     (6,5,7),
    #     (1,6,7),
    #     (1,7,2),
    #     (3,2,7),
    #     (3,7,5),
    #     (0,1,6),
    #     (0,6,4),
    # ]
    # # Tétraèdre
    # Points = np.array([(150,200,50),
    #                    (250,200,50),
    #                    (200,200,150),
    #                    (200,100,100)])
    # Faces = [
    #     (0,1,2),
    #     (0,1,3),
    #     (1,2,3),
    #     (2,0,3),
    # ]
    # Octogone
    MAGICNUMBER = (np.sqrt(2)/2)*50
    Points = np.array([
        (200,200,25), # close left
        (200+MAGICNUMBER,150+MAGICNUMBER,25), # close right
        (250,150,25), # kinda far right
        (200+MAGICNUMBER,150-MAGICNUMBER,25), # further right
        (200,100,25), # furthest right
        (200-MAGICNUMBER,150-MAGICNUMBER,25), # furthest left
        (150,150,25), # further left
        (200-MAGICNUMBER,150+MAGICNUMBER,25), # kinda far left
        (200,150,25), # Center top
        # Behind
        (200,200,50), # close left
        (200+MAGICNUMBER,150+MAGICNUMBER,50), # close right
        (250,150,50), # kinda far right
        (200+MAGICNUMBER,150-MAGICNUMBER,50), # further right
        (200,100,50), # furthest right
        (200-MAGICNUMBER,150-MAGICNUMBER,50), # furthest left
        (150,150,50), # further left
        (200-MAGICNUMBER,150+MAGICNUMBER,50), # kinda far left
        (200,150,50) # Center Bottom
    ])
    Faces = [
        (0,1,8),
        (1,2,8),
        (2,3,8),
        (3,4,8),
        (4,5,8),
        (5,6,8),
        (6,7,8),
        (7,0,8),
        # Behind
        (10,9,17),
        (11,10,17),
        (12,11,17),
        (13,12,17),
        (14,13,17),
        (15,14,17),
        (16,15,17),
        (9,16,17),
        # Sides
        (9,10,0),
        (10,1,0),
        (10,11,1),
        (11,2,1),
        (11,12,2),
        (12,3,2),
        (12,13,3),
        (13,4,3),
        (13,14,4),
        (14,5,4),
        (14,15,5),
        (15,6,5),
        (15,16,6),
        (16,7,6),
        (16,9,7),
        (9,0,7),
    ]
    # Points = np.array([
    #     (150,250,100),
    #     (250,250,100),
    #     (150,250,300),
    #     (250,250,300),
    #     (200,350,200),
    #     (200,150,200)
    # ])
    # Faces = [
    #     (0,1,4),
    #     (1,3,4),
    #     (3,2,4),
    #     (2,0,4),
    #     # Under
    #     (0,5,1),
    #     (1,5,3),
    #     (3,5,2),
    #     (2,5,0),
    # ]

def middleOfPoints(Points):
    out = np.zeros(3)
    for i in Points:
        out[0] += i[0]
        out[1] += i[1]
        out[2] += i[2]
    out[0] = out[0]/len(Points)
    out[1] = out[1]/len(Points)
    out[2] = out[2]/len(Points)
    return out

def GetNormal(P1,P2,P3):
    u = np.zeros(3)
    v = np.zeros(3)
    for i in range(3):
        u[i] = P2[i] - P1[i]
    for i in range(3):
        v[i] = P3[i] - P1[i]
    Normal = np.zeros(3)
    Normal[0] = (u[1])*(v[2])-(u[2])*(v[1])
    Normal[1] = (u[2])*(v[0])-(u[0])*(v[2])
    Normal[2] = (u[0])*(v[1])-(u[1])*(v[0])
    return Normal

def GetLightVectorFromVertex(P1):
    # Get vector from light to center of face
    lightVector = np.zeros(3)
    for i in range(3):
        lightVector[i] = LightXYZ[i] - P1[i]
    return lightVector

def CosOfDotProd(u,v):
    dot = (u[0]*v[0])+(u[1]*v[1])+(u[2]*v[2])
    uNorm = np.sqrt((u[0]**2)+(u[1]**2)+(u[2]**2))
    vNorm = np.sqrt((v[0]**2)+(v[1]**2)+(v[2]**2))
    out = dot/(uNorm*vNorm)
    return out

def GetVertexNormals(P1,Points):
    vertexIndexInPoints = np.where((Points == P1).all(axis=1))[0][0]
    facesConnectedToVertex = [i for i in Faces if vertexIndexInPoints in i]
    NormalsOfConnectedFaces = []
    for i in facesConnectedToVertex:
        NormalsOfConnectedFaces.append(GetNormal(Points[i[0]],Points[i[1]],Points[i[2]]))
    # Average the normals
    sum = np.zeros(3)
    for Normal in NormalsOfConnectedFaces:
        for i in range(3):
            sum[i] = sum[i] + Normal[i]
    for i in range(3):
        sum[i] = sum[i] / len(NormalsOfConnectedFaces)
    return sum

def drawShadedTri(P1,P2,P3,shade1,shade2,shade3):
    global img
    p1 = GetProjectedPoint(P1)
    p2 = GetProjectedPoint(P2)
    p3 = GetProjectedPoint(P3)
    # Gets bounds of tri
    min_x = int(min(p1[0], p2[0], p3[0]))
    max_x = int(max(p1[0], p2[0], p3[0]))
    min_y = int(min(p1[1], p2[1], p3[1]))
    max_y = int(max(p1[1], p2[1], p3[1]))
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            u, v, w = barycentric_weights(p1, p2, p3, (x, y)) # u, v, w are how close the point it to each vertex of the tri 
            if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1: # are we on the tri
                shade = int(u*shade1 + v*shade2 + w*shade3) # goes with the shade apropriate
                img.putpixel((x, y), (shade, shade, shade))

def drawMesh(thetaX, thetaY, thetaZ):
    # Rotate Points
    MiddleOfMesh = middleOfPoints(Points)
    RotatedPoints = Points.copy()
    for i in Points:
        indexofi = np.where((Points == i).all(axis=1))[0][0]
        RotatedPoints[indexofi] = rotatePointIn3D(i,MiddleOfMesh, thetaX, thetaY, thetaZ) # USE RotatedPoints instead of Points from now on
    
    # Gets a list of Furthest tri to closest tri 
    FaceDistances = []
    for i in Faces:
        arr = []
        for j in range(3):
            arr.append(RotatedPoints[i[j]])
        arr = np.array(arr)
        FaceDistances.append(distanceBetweenPoints(middleOfPoints(arr),CameraXYZ))
    FaceDistanceWithIndex = []
    for i in range(len(Faces)):
        FaceDistanceWithIndex.append((FaceDistances[i],i))
    FaceDistanceWithIndex.sort(key= lambda x: x[0], reverse=True)
    
    # Drawing order
    for i in FaceDistanceWithIndex:
        # Points in 3D of the current face
        P1 = RotatedPoints[Faces[i[1]][0]]
        P2 = RotatedPoints[Faces[i[1]][1]]
        P3 = RotatedPoints[Faces[i[1]][2]]
        P1Normal = GetVertexNormals(P1,RotatedPoints)
        P2Normal = GetVertexNormals(P2,RotatedPoints)
        P3Normal = GetVertexNormals(P3,RotatedPoints)
        P1LightIntensity = max(0, CosOfDotProd(P1Normal,GetLightVectorFromVertex(P1)))
        P2LightIntensity = max(0, CosOfDotProd(P2Normal,GetLightVectorFromVertex(P2)))
        P3LightIntensity = max(0, CosOfDotProd(P3Normal,GetLightVectorFromVertex(P3)))
        shade1 = int(P1LightIntensity * 255)
        shade2 = int(P2LightIntensity * 255)
        shade3 = int(P3LightIntensity * 255)
        drawShadedTri(P1,P2,P3,shade1,shade2,shade3)

angleX = 0
angleY = 0
angleZ = 0
step = 0.05
DefineMesh()

def animate():
    global angleX, angleY, angleZ, img
    canvas.delete("all")
    img = Image.new("RGB", (ScreenX, ScreenY), (108, 88, 118))
    
    drawMesh(angleX, angleY, angleZ)
    canvas.img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=canvas.img)
    
    angleX += step * 1
    if angleX > 2 * np.pi:
        angleX = 0
    angleY += step * 0.5
    if angleY > 2 * np.pi:
        angleY = 0
    angleZ += step * 0.2
    if angleZ > 2 * np.pi:
        angleZ = 0
        
    root.after(30, animate)

def Binds(event):
    global angleX, angleY, angleZ
    if event.keysym == 'Up':
        angleX -= 0.1
    if event.keysym == 'Down':
        angleX += 0.1
    if event.keysym == 'Left':
        angleY += 0.1
    if event.keysym == 'Right':
        angleY -= 0.1
    if event.keysym in ('a', 'A'):
        angleZ -= 0.1
    if event.keysym in ('e', 'E'):
        angleZ += 0.1

# root.bind("<KeyPress>", Binds)

animate()
root.mainloop()