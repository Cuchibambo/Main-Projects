class Object:
    def __init__(self,pos=(0,0),color="#ffffff") -> None:
        self.pos = pos
        self.color = color
    def draw(self):
        print(f"draw at {self.pos} with color {self.color}")
    
class Ball(Object):
    def __init__(self, pos=(0, 0), color="#ffffff") -> None:
        super().__init__(pos, color)
        self.speed = 10
        self.move_dir = (0,1)
    def move(self):
        self.pos = (self.pos[0]+(self.speed*self.move_dir[0]),self.pos[1]+(self.speed*self.move_dir[1]))

ball = Ball()

while True:
    ball.move()
    ball.draw()