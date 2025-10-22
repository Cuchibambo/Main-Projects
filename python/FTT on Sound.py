import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

y, sr = librosa.load("python\cat-meow-8-fx-306184.mp3", sr=None)
x = np.linspace(0,len(y)/sr,len(y))
ffty = np.fft.fft(y,len(y))
freqs = np.fft.fftfreq(len(ffty), 1/sr)
ffty_filtered = ffty.copy()
ffty_filtered[:1800] = 0
y2 = np.fft.ifft(ffty_filtered).real
plt.plot(x,y,'r-')
# plt.plot(x,ffty,'b-')
plt.plot(x,y2,'g-')
plt.show()
sf.write("output.wav", y2, sr)