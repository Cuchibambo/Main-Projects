import numpy as np
import matplotlib.pyplot as plt
import cmath

def f(x):
    return np.cos(0.1*x)

a = np.array([f(i) for i in range(100)])

N = 100
k = 10

sum = 0
for n in range(N):
    sum += (a[n]*cmath.exp((-2*cmath.pi*k*n)/N))

x = np.linspace()

print(sum.real)