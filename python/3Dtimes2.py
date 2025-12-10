from MathScripts import *
import time
import pygame

pygame.init()

width,height = 500, 500

CameraDistance = 10
vec1 = (1,-1,0)
vec2 = (0,0,1)
Point1 = (6,5,-3)
Camera = GetNormalVector(vec1,vec2) * CameraDistance

timenow = time.time()
print(GetLinearCoeficientsRepresentationOfPointOnPlane(vec1,vec2,FindIntersectionBetweeenPointAndPlane(GetNormalVector(vec1,vec2),Point1,Camera)))
timeafter = time.time()
print(f'the process took : {(timeafter-timenow)*100} ms')
