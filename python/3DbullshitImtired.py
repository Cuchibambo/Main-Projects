import numpy as np
import tkinter as tk

root = tk.Tk()

ScreenX, ScreenY = 400, 300
# ScreenX, ScreenY = 1920, 1080
CameraXYZ = (ScreenX/2, ScreenY/2, -100)

canvas = tk.Canvas(root, width=ScreenX, height=ScreenY)
canvas.pack()
canvas.configure(bg="#6C5876")

def drawPoint(x,y,radius):
    canvas.create_oval(x-radius,y-radius,x+radius,y+radius,fill='#202020',outline='white')

# Screen is at z = 0 with x and y as 400, 300
# Camera is at z = -10 with x and y as 200, 150 

# Point in 3D space Coords = (200, 150, 10)
# (x,y,z) = (x1​, y1​, z1​) + t(x2​−x1​, y2​−y1​, z2​−z1​)

# t = (-z1)/(z2-z1)

# (x1, y1, z1) + ((-z1)/(z2-z1))*(x2​−x1​, y2​−y1​, z2​−z1​)

def drawProjectedPoint(x,y,z):

    P1 = np.array([x, y, z])
    IpXYZ = np.zeros(3)
    
    IpXYZ = CameraXYZ + ((-CameraXYZ[2])/(P1[2]-CameraXYZ[2]))*(P1-CameraXYZ)

    drawPoint(IpXYZ[0], IpXYZ[1], 5)
    
def GetProjectedPoint(P1):
    # P1 = np.array([x, y, z])
    IpXYZ = np.zeros(3)
    
    IpXYZ = CameraXYZ + ((-CameraXYZ[2])/(P1[2]-CameraXYZ[2]))*(P1-CameraXYZ)
    
    return IpXYZ[0], IpXYZ[1]

def middleOfFace(P1,P2,P3,P4):
    out = np.zeros(3)
    out[0] = (P1[0]+P2[0]+P3[0]+P4[0])/4
    out[1] = (P1[1]+P2[1]+P3[1]+P4[1])/4
    out[2] = (P1[2]+P2[2]+P3[2]+P4[2])/4
    return out

def to_hex(n):
    return f"{n:02x}"

def drawFace(P1,P2,P3,P4,col):
    canvas.create_polygon(P1[0],P1[1],P2[0],P2[1],P3[0],P3[1],P4[0],P4[1],fill=f'#{col}{col}{col}')

def distanceBetweenPoints(P1,P2):
    return np.sqrt(((P2[0]-P1[0])**2)+((P2[1]-P1[1])**2)+((P2[2]-P1[2])**2))

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
        drawFace(p1,p2,p4,p3,col)
    def drawFace2(col):
        drawFace(p1,p3,p7,p5,col)
    def drawFace3(col):
        drawFace(p2,p4,p8,p6,col)
    def drawFace4(col):
        drawFace(p3,p4,p8,p7,col)
    def drawFace5(col):
        drawFace(p1,p2,p6,p5,col)
    def drawFace6(col):
        drawFace(p5,p6,p8,p7,col)
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

def rotatePointIn3D(x, y, z, cx, cy, cz, thetaX, thetaY, thetaZ):
    out = np.zeros(3)
    
    x -= cx
    y -= cy
    z -= cz

    out[0] = (np.cos(thetaY) * np.cos(thetaZ) * x) + (np.cos(thetaY) * np.sin(thetaZ) * -y) + (np.sin(thetaY) * z)
    out[1] = ((np.cos(thetaX) * np.sin(thetaZ) + np.sin(thetaX) * np.sin(thetaY) * np.cos(thetaZ)) * x) + ((np.cos(thetaX) * np.cos(thetaZ) - np.sin(thetaX) * np.sin(thetaY) * np.sin(thetaZ)) * y) + (np.sin(thetaX) * np.cos(thetaY) * -z)
    out[2] = ((np.sin(thetaX) * np.sin(thetaZ) - np.cos(thetaX) * np.sin(thetaY) * np.cos(thetaZ)) * x) + ((np.sin(thetaX) * np.cos(thetaZ) + np.cos(thetaX) * np.sin(thetaY) * np.sin(thetaZ)) * y) + (np.cos(thetaX) * np.cos(thetaY) * z)
    
    
    out[0] += cx
    out[1] += cy
    out[2] += cz
    
    return out

# DrawCube(200, 150, 250, 300, 0, np.pi/4, 0)

angleX = 0
angleY = 0
angleZ = 0
step = 0.05

def animate():
    global angle
    canvas.delete("all")
    DrawCube(200, 150, 150, 150, angleX, angleY, angleZ)
    # angle += step
    # if angle > 2 * np.pi:
    #     angle = 0
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

root.bind("<KeyPress>", Binds)

animate()
root.mainloop()