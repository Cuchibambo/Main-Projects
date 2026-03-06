import pygame

class Sim:
    def __init__(self) -> None:
        pass
    
    def start(self):
        pass

class Floor:
    def __init__(self,pos=(250,450),rotation=0) -> None:
        self.pos = pos
        self.rotation = rotation
    
class Object:
    def __init__(self, mass=1,pos=(250,250),speed=(0,0),acceleration=(0,0)) -> None:
        self.mass = mass
        self.pos = pos
        self.speed = speed
        self.acceleration = acceleration
        

sim = Sim()
sim.start()