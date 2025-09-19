import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg='#151515')  # Set the background of the main window to black
root.bind("<Escape>", lambda event: root.destroy())

Border = 5

# Create a canvas with a white background and a grey border in the middle of the window
canvas = tk.Canvas(root, width=500, height=500, bg='#aaaaaa', highlightthickness=Border, highlightbackground='#505050')
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Make var
Radius = 50
x = Radius + Border
y = Radius + Border
MoveSpeed = Radius * 2

# Box
xBox = 250 + Border
yBox = 250 + Border

Box = canvas.create_rectangle(xBox-Radius,yBox-Radius,xBox+Radius,yBox+Radius,fill='#66360b')

# Initial Rect
Rect = canvas.create_rectangle(x-Radius,y-Radius,x+Radius,y+Radius,fill='#702055')

def MoveLeft():
    global x, y, xBox, yBox
    
    if x - MoveSpeed >= Radius + Border:
        x += -MoveSpeed        
    else:
        x = Radius + Border
    
    SetObjPos(x,y,Rect)

def MoveRight():
    global x, y
    
    if x + MoveSpeed + Radius + Border <= 500 + 9:
        x += MoveSpeed
    else:
        x = 500 - Radius - Border + 9
    
    SetObjPos(x,y,Rect)
    
def MoveUp():
    global x, y
    
    if y - MoveSpeed >= Radius + Border:
        y += -MoveSpeed
    else:
        y = Radius + Border
    
    SetObjPos(x,y,Rect)
    
def MoveDown():
    global x, y
    
    if y + MoveSpeed + Radius + Border <= 500 + 9:
        y += MoveSpeed
    else:
        y = 500 - Radius - Border + 9
    
    SetObjPos(x,y,Rect)

def SetObjPos(x,y,obj):
    NewPos = [x-Radius, y-Radius, x+Radius, y+Radius]
    canvas.coords(obj,NewPos)

# Bind the arrow keys to move the rectangle
root.bind("<Left>", lambda event: MoveLeft())
root.bind("<Right>", lambda event: MoveRight())
root.bind("<Up>", lambda event: MoveUp())
root.bind("<Down>", lambda event: MoveDown())

# GridLines
canvas.create_line(Radius*2 + Border, 0, Radius*2 + Border, 509, fill="#151515")
canvas.create_line(Radius*4 + Border, 0, Radius*4 + Border, 509, fill="#151515")
canvas.create_line(Radius*6 + Border, 0, Radius*6 + Border, 509, fill="#151515")
canvas.create_line(Radius*8 + Border, 0, Radius*8 + Border, 509, fill="#151515")

canvas.create_line(0, Radius*2 + Border, 509, Radius*2 + Border, fill="#151515")
canvas.create_line(0, Radius*4 + Border, 509, Radius*4 + Border, fill="#151515")
canvas.create_line(0, Radius*6 + Border, 509, Radius*6 + Border, fill="#151515")
canvas.create_line(0, Radius*8 + Border, 509, Radius*8 + Border, fill="#151515")

# Start the main loop
root.mainloop()