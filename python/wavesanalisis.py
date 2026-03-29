import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
from numpy import pi, cos, sin

def f(x, freq):
    return cos(x)

def onSliderChange(val):
    line.set_ydata(f(x, slider.val))
    fig.canvas.draw_idle()

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(-2*pi,2*pi,0.001)
freq_0 = 5
[line] = ax.plot(x, f(x, freq_0))

slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03])
slider = Slider(slider_ax, 'Slider', 0.1, 10, valinit=freq_0)
slider.on_changed(onSliderChange)

plt.show()