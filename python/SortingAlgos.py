import matplotlib.pyplot as plt
import time
import numpy as np

plt.style.use('_mpl-gallery')

N = 10

list = np.arange(N)
np.random.shuffle(list)

def bubblesort():
    global list
    
    plt.ion()
    
    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="black", linewidth=1)

    ax.set(xlim=(0, N), xticks=np.arange(N),
        ylim=(0, N), yticks=np.arange(N))
    
    N = len(list)
    for _ in range(N-1):
        for i in range(N-1):
            if list[i] > list[i+1]:
                list[[i, i+1]] = list[[i+1, i]]
                y = list
                plt.pause(0.05)

# make data:
x = 0.5 + np.arange(N)
bubblesort()

plt.ioff
plt.show()
