import numpy as np
import random

class Match():
    def __init__(self, pos, rotation):
        self.pos = pos
        self.rotation = rotation
    
    def __str__(self):
        return f'position: {self.pos}, rotation: {self.rotation}'

# Floor is 500x500
# Match is 10 long 
# Line at top, line at bottom, 51 lines in horizontal tot

N = 100000

Matches = []

intersections = 0
non_intersections = 0

for i in range(N):
    Matches.append(Match((random.randint(0,500),random.randint(0,500)),random.random()*2*np.pi))

for match in Matches:
    PosY = match.pos[1]
    RelativePosY = PosY-((PosY//10)*10)
    Rotation = match.rotation
    p1y = (np.sin(Rotation)*5)+RelativePosY
    p2y = (np.sin(Rotation+np.pi)*5)+RelativePosY
    if p1y <= 0 or p1y >= 10 or p2y <= 0 or p2y >= 10:
        intersections += 1
    else:
        non_intersections += 1



print(f'Number of Matches: {N}\nIntersections: {intersections}\nNon Intersections: {non_intersections}')
print(f'Ratio should approch pi: {(N*2)/(intersections)}')
