import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,500)
waveform =  np.cos(400*x)
frequencyDomain = np.fft.fft(waveform)

plt.plot(x,waveform,'b-')
plt.plot(x,frequencyDomain,'r-')
plt.show()