import numpy as np

vector1 = (1,1,1)
vector2 = (1,-1,-1)
vector3 = (5,1,1)

def IsCoplanar(v1,v2,v3):
    x = (v3[0] - y*v2[0])/v1[0]
    v3[1] = (v3[0]*v1[1])/v1[0] - (y*v2[0]*v1[1])/v1[0] + y*v2[1]