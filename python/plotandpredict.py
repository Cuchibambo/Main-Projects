import matplotlib.pyplot as plt
import numpy as np
import random
import math

X_MIN = -100
X_MAX = 100
POINTS = 500
Ratio = (max(X_MIN,X_MAX)-min(X_MIN,X_MAX))/POINTS

def f(x):
    ans = x**3
    return ans

# fprime[499] = (f(100+Ratio)-f(100))/Ratio

def derivf(x):
    return (f(x+Ratio)-f(x))/Ratio

def derivderivf(x):
    return (derivf(x+Ratio)-derivf(x))/Ratio

def derivderivderivf(x):
    return (derivderivf(x+Ratio)-derivderivf(x))/Ratio

axx = np.linspace(X_MIN,X_MAX,POINTS)
# axy = f(axx)
axy = f(axx)
fprime = derivf(axx)
fprimeprime = derivderivf(axx)
fprimeprimeprime = derivderivderivf(axx)
plt.plot(axx,axy,'r-')
plt.plot(axx,fprime,'b-')
plt.plot(axx,fprimeprime,'g-')
plt.plot(axx,fprimeprimeprime,'y-')
plt.grid()
plt.xlim(-100, 100)
plt.ylim(-100, 100)
plt.show()