import matplotlib.pyplot as plt
import random

def random_color(color,deviance):
    if color+deviance > 0xFFFFFF:
        upperbound = 0xFFFFFF
    else:
        upperbound = color+deviance
    if color-deviance < 0:
        lowerbound = 0
    else:
        lowerbound = color-deviance
    
    
    return "#{:06x}".format(random.randint(lowerbound, upperbound))

def plot_colors():
    """Plot a list of colors as a horizontal bar."""
    fig, ax = plt.subplots(figsize=(3, 4))
    for i in range(4):
        for y in range(3):
            ax.add_patch(plt.Rectangle((i,y),1,1, color=random_color(0x23D074,0xFF)))
    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3)
    ax.axis('off')
    plt.show()
    
plot_colors()