import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg='#151515')  # Set the background of the main window to black
root.bind("<Escape>", lambda event: root.destroy())
CanvasSize = 500

# Create a canvas with a white background and a grey border in the middle of the window
canvas = tk.Canvas(root, width=CanvasSize, height=CanvasSize, bg='#aaaaaa', highlightthickness='0')
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Make var
Radius = 50
Diameter = Radius * 2
x = Radius
y = Radius
MoveSpaces = int(CanvasSize/Diameter)
BottomLeft = CanvasSize - Radius
ButtonsPressed = 0
PlayerOnButton = False
BoxOnButton = False

# Box
xBox = BottomLeft - Diameter
yBox = BottomLeft - Diameter

# Wall
xWall = Diameter+Radius
yWall = Diameter+Radius

# Button
xBut = CanvasSize/2
yBut = CanvasSize/2

# Initial Obj
Button = canvas.create_oval(xBut - Radius, yBut - Radius, xBut + Radius, yBut + Radius,fill='#c94d4d',outline='')
Box = canvas.create_rectangle(xBox-Radius,yBox-Radius,xBox+Radius,yBox+Radius,fill='#66360b',outline='')
Rect = canvas.create_rectangle(x-Radius,y-Radius,x+Radius,y+Radius,fill='#702055',outline='')
Wall = canvas.create_rectangle(xWall - Radius, yWall - Radius, xWall + Radius, yWall + Radius,fill='#757575',outline='')

# Func to help change an obj pos
def SetObjPos(x,y,obj):
    NewPos = [x-Radius, y-Radius, x+Radius, y+Radius]
    canvas.coords(obj,NewPos)

# Checks for a box in front of the player. Takes a Direction as input
def BoxInFront(Direction):
    global x, y, xBox, yBox
    
    Diretor = {
        'Left' : -1,
        'Right' : 1,
        'Up' : -1,
        'Down' : 1
    }
    
    dir = Diretor.get(Direction,'FUCK!!!!!!')
    
    if (Direction in ('Left', 'Right')) and y == yBox: 
        if x + dir * Diameter == xBox:
            return True
        else:
            return False
    elif (Direction in ('Up', 'Down')) and x == xBox:
        if y + dir * Diameter == yBox:
            return True
        else:
            return False

# Checks for a Wall in front of the player. Takes a Direction as input
def WallInFront(x,y,Direction):
    global xWall, yWall
    
    Diretor = {
        'Left' : -1,
        'Right' : 1,
        'Up' : -1,
        'Down' : 1
    }
    
    dir = Diretor.get(Direction,'FUCK!!!!!!')
    
    if (Direction in ('Left', 'Right')) and y == yWall: 
        if x + dir * Diameter == xWall:
            return True
        else:
            return False
    elif (Direction in ('Up', 'Down')) and x == xWall:
        if y + dir * Diameter == yWall:
            return True
        else:
            return False

# Checks if an obj is on Button
def OnButton(x,y):
    global xBut, yBut
    
    if x == xBut or y == yBut:
        return True
    else:
        return False
    
def ButtonLogic():
    global ButtonsPressed, PlayerOnButton, BoxOnButton, x, y, xBox, yBox
    if OnButton(x,y):
        print('Player on button')
        if PlayerOnButton:
            pass
        else:
            PlayerOnButton = True
            ButtonsPressed += 1
    else:
        if PlayerOnButton:
            PlayerOnButton = False
            ButtonsPressed += -1
    if OnButton(xBox,yBox):
        print('Box on button')
        if BoxOnButton:
            pass
        else:
            BoxOnButton = True
            ButtonsPressed += 1
    else:
        if BoxOnButton:
            BoxOnButton = False
            ButtonsPressed += -1
    if ButtonsPressed >= 1:
        root.destroy

# Move player Left
def MoveLeft():
    global x, y, xBox, yBox
    
    if x - Diameter >= Radius: # Prevents going outside the map
        if WallInFront(x,y,'Left'): # Checks for a Wall in front
            pass # Don't move
        else:
            if BoxInFront('Left'): # Checks for box
                if WallInFront(xBox,yBox,'Left'): # Check for wall in front of box
                    pass # Don't move
                elif x - Diameter * 2 >= Radius: # Accounts for Box movments
                    x += -Diameter # Moves
                    xBox += -Diameter # Moves Box
            else:
                x += -Diameter # Moves
    else:
        x = Radius # Snaps back before the wall
    
    SetObjPos(x,y,Rect)
    SetObjPos(xBox,yBox,Box)
    ButtonLogic()

# Move player Right
def MoveRight():
    global x, y, xBox, yBox
    
    if x + Diameter <= BottomLeft: # Prevents going outside the map
        if WallInFront(x,y,'Right'): # Checks for a Wall in front
            pass # Don't move
        else:
            if BoxInFront('Right'): # Checks for box
                if WallInFront(xBox,yBox,'Right'): # Check for wall in front of box
                    pass # Don't move
                elif x + Diameter * 2 <= BottomLeft: # Accounts for Box movments
                    x += Diameter # Moves
                    xBox += Diameter # Moves Box
            else:
                x += Diameter # Moves
    else:
        x = BottomLeft # Snaps back before the wall
    
    SetObjPos(x,y,Rect)
    SetObjPos(xBox,yBox,Box)
    ButtonLogic()
    
# Move player Up
def MoveUp():
    global x, y, xBox, yBox
    
    if y - Diameter >= Radius: # Prevents going outside the map
        if WallInFront(x,y,'Up'): # Checks for a Wall in front
            pass # Don't move
        else:
            if BoxInFront('Up'): # Checks for box
                if WallInFront(xBox,yBox,'Up'): # Check for wall in front of box
                    pass # Don't move
                elif y - Diameter * 2 >= Radius: # Accounts for Box movments
                    y += -Diameter # Moves
                    yBox += -Diameter # Moves Box
            else:
                y += -Diameter # Moves
    else:
        y = Radius # Snaps back before the wall
    
    SetObjPos(x,y,Rect)
    SetObjPos(xBox,yBox,Box)
    ButtonLogic()

# Move player Down
def MoveDown():
    global x, y, xBox, yBox
    
    if y + Diameter <= BottomLeft: # Prevents going outside the map
        if WallInFront(x,y,'Down'): # Checks for a Wall in front
            pass # Don't move
        else:
            if BoxInFront('Down'): # Checks for box
                if WallInFront(xBox,yBox,'Down'): # Check for wall in front of box
                    pass # Don't move
                elif y + Diameter * 2 <= BottomLeft: # Accounts for Box movments
                    y += Diameter # Moves
                    yBox += Diameter # Moves Box
            else:
                y += Diameter # Moves
    else:
        y = BottomLeft # Snaps back before the wall
    
    SetObjPos(x,y,Rect)
    SetObjPos(xBox,yBox,Box)
    ButtonLogic()



# Bind the arrow keys to move the rectangle
root.bind("<Left>", lambda event: MoveLeft())
root.bind("<Right>", lambda event: MoveRight())
root.bind("<Up>", lambda event: MoveUp())
root.bind("<Down>", lambda event: MoveDown())

# Grid lines
for i in range(1,MoveSpaces):
    canvas.create_line(Radius*2*i, 0, Radius*2*i, CanvasSize, fill="#151515")
    canvas.create_line(0, Radius*2*i, CanvasSize, Radius*2*i, fill="#151515")

# Start the main loop
root.mainloop()