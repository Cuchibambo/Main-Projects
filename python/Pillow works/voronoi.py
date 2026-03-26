from PIL import Image
import random
import math

class Node():
    def __init__(self, pos, color) -> None:
        self.pos = pos
        self.color = color

width, height = 500, 500

Voronoi = Image.new('RGB', (width, height))

nbNodes = 5

Nodes = [Node((random.randint(0,width),random.randint(0,height)),(random.randint(0,255),random.randint(0,255),random.randint(0,255))) for _ in range(nbNodes)]

def GetDistance(P1,P2):
    return math.sqrt(((P1[0]-P2[0])**2)+((P1[1]-P2[1])**2))

for x in range(width):
    for y in range(height):
        distances = []
        for node in Nodes:
            distances.append((GetDistance(node.pos,(x,y)),len(distances)))
        distances.sort(reverse=True)
        Voronoi.putpixel((x,y),Nodes[distances[0][1]].color)

        
Voronoi.show()
