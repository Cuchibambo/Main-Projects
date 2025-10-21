import tkinter as tk
from tkinter import ttk
import random
import numpy as np

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, bg="#202020")
canvas.pack(fill='both', expand=True)
radius = 20
fx, fy = 100, 100
tx, ty = 100, 100
px, py = 300, 500
FinalPos = canvas.create_oval(fx - radius, fy - radius, fx + radius, fy + radius, fill="#446d7b", outline="")
Target = canvas.create_oval(tx - radius, ty - radius, tx + radius, ty + radius, fill="#78bfd8", outline="white")
Projectile = canvas.create_oval(px - radius, py - radius, px + radius, py + radius, fill="#52228a", outline="white")
acceleration = np.array([0.0,0.0])
speed = np.array([50.0,0.0])
def move_target():
    global tx, ty, speed, acceleration, txdisplay
    speed += acceleration
    interval = 1
    dx = speed[0] * (interval / 1000.0)
    dy = speed[1] * (interval / 1000.0)
    canvas.move(Target, dx, dy)
    tx += dx
    ty += dy
    canvas.after(interval, move_target)
def update_finalPos():
    global fx, fy, tx, ty, px, py, speed
    interval = 1
    fx = tx + speed[0] * 2
    fy = ty + speed[1] * 2
    print(fx,fy)
    canvas.moveto(FinalPos, fx-radius, fy-radius)
    canvas.after(interval, update_finalPos)
move_target()
update_finalPos()
root.mainloop()