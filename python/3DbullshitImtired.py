import numpy as np
import tkinter as tk

root = tk.Tk()

ScreenX, ScreenY = 400, 300
CameraXYZ = (ScreenX/2, ScreenY/2, -100)

canvas = tk.Canvas(root, width=ScreenX, height=ScreenY)
canvas.pack()
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

def DrawCube(x,y,z,SideLength,theta):
    radius = SideLength/2
    xp = x+radius
    xm = x-radius
    yp = y+radius
    ym = y-radius
    zp = z+radius
    zm = z-radius
    P1 = rotatePointIn3DY(xm,ym,zm,x,y,z,theta)
    P2 = rotatePointIn3DY(xp,ym,zm,x,y,z,theta)
    P3 = rotatePointIn3DY(xm,yp,zm,x,y,z,theta)
    P4 = rotatePointIn3DY(xp,yp,zm,x,y,z,theta)
    P5 = rotatePointIn3DY(xm,ym,zp,x,y,z,theta)
    P6 = rotatePointIn3DY(xp,ym,zp,x,y,z,theta)
    P7 = rotatePointIn3DY(xm,yp,zp,x,y,z,theta)
    P8 = rotatePointIn3DY(xp,yp,zp,x,y,z,theta)
    drawProjectedPoint(P1[0],P1[1],P1[2])
    drawProjectedPoint(P2[0],P2[1],P2[2])
    drawProjectedPoint(P3[0],P3[1],P3[2])
    drawProjectedPoint(P4[0],P4[1],P4[2])
    drawProjectedPoint(P5[0],P5[1],P5[2])
    drawProjectedPoint(P6[0],P6[1],P6[2])
    drawProjectedPoint(P7[0],P7[1],P7[2])
    drawProjectedPoint(P8[0],P8[1],P8[2])

def rotatePointIn3DY(x, y, z, cx, cy, cz, theta):
    out = np.zeros(3)
    
    x -= cx
    y -= cy
    z -= cz
    
    out[0] = x * np.cos(theta) + z * np.sin(theta)
    out[1] = y
    out[2] = -x * np.sin(theta) + z * np.cos(theta)

    out[0] += cx
    out[1] += cy
    out[2] += cz
    
    return out

angle = 0  # starting angle
step = 0.05  # how much to increase each frame

def animate():
    global angle
    canvas.delete("all")  # clear previous frame
    DrawCube(200, 150, 250, 200, angle)  # draw cube with current angle
    angle += step
    if angle > 2 * np.pi:
        angle = 0  # loop back
    root.after(30, animate)  # call animate again after 30ms (~33 fps)

animate()  # start the animation
root.mainloop()