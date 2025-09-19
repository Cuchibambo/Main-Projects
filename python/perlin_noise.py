import matplotlib.pyplot as plt



"""Perlin noise implementation."""
# Licensed under ISC
from itertools import product
import math
import random

pic = [1]

for i in range(1):
    for j in range(105):
        pic.append(i*j)

plt.imshow(pic, cmap='grey')
plt.show()