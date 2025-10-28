import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

y, sr = librosa.load("Sounds\\Test2.mp3", sr=None)
x = np.linspace(0,len(y)/sr,len(y))
ffty = np.fft.fft(y,len(y))
ffty_filtered = ffty.copy()
# ffty_filtered[6300:9000] = 0
# ffty_filtered[453000:455000] = 0
y2 = np.fft.ifft(ffty_filtered).real
plt.plot(x,y,'r-')
plt.plot(x,ffty_filtered,'b-')
plt.plot(x,y2,'g-')
plt.show()
# sf.write("Sounds\\output2.wav", y2, sr)