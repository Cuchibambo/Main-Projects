import matplotlib.pyplot as plt
import numpy as np

x_lim = (-100,100)

x = np.linspace(x_lim[0],x_lim[1],500)
y = ((x**2)-(3*x)+(2))*(np.e**x)
# y = np.sqrt((x**2)+(2*x)+5)

def deriv(x,y):
    run = x[1]-x[0]
    y1 = np.zeros(len(x))
    for i in range(len(x)-1):    
        y1[i] = (y[i+1]-y[i])/(run)

    y1[-1] = y1[-2]
    return y1
    

y1 = deriv(x,y)
y2 = deriv(x,y1)

fig, ax = plt.subplots()
ax.plot(x,y,'r-')
ax.plot(x,y1,'b-')
ax.plot(x,y2,'g-')
ax.set_xlim(x_lim)
ax.set_ylim(-3,5)
plt.grid(True)
plt.show()