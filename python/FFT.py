import math
import numpy as np
import matplotlib.pyplot as plt

# try:
#     a = float(a)
#     b = float(b)
#     c = float(c)
# except:
#     print("Invalid input. Please enter numeric values.")
#     exit()

a= 1
b= 2
c= 10

N = 1000
n = np.arange(0,N,1000)

x = np.cos(a * n) + np.cos(b * n) + np.cos(c * n)
    
def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n]*np.exp(-2j * np.pi * k * n / N)
    return X
    # ans = 0
    # for n in range(N):
    #     # pass
    #     ans += originalfunc(n)*np.cos((omega*x*n)/(N))
    # return ans

# plt.plot(toplotx,fftfunc(toplotx), 'b-')

X = DFT(x)

# Frequency bins
k = np.arange(N)

# Plot the results
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(n[:200], x[:200], 'r-')
plt.title("Original Signal (first 200 samples)")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.grid(True)

plt.subplot(2,1,2)
plt.stem(k[:N//2], np.abs(X[:N//2]), linefmt='b-', markerfmt='bo', basefmt=' ')
plt.title("Magnitude of DFT")
plt.xlabel("Frequency bin k")
plt.ylabel("|X[k]|")
plt.grid(True)

plt.tight_layout()
plt.show()