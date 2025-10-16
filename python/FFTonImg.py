import numpy as np
import cv2
import matplotlib.pyplot as plt
import requests
from PIL import Image, ImageFilter
from io import BytesIO

# Image URL
url = "https://picsum.photos/2000"

# Fetch the image from the URL
response = requests.get(url)
img_data = response.content

# Open the image using PIL
img = Image.open(BytesIO(img_data))

# Convert the image to grayscale
img_gray = np.array(img.convert('L'))  # Convert to grayscale

# Compute FFT
f = np.fft.fft2(img_gray)
fshift = np.fft.fftshift(f)

# Define a 5x5 convolution kernel
kernel_5x5 = [
    -2,  0, -1,  0,  0,
    0, -2, -1,  0,  0,
    -1, -1,  1,  1,  1,
    0,  0,  1,  2,  0,
    0,  0,  1,  0,  2
]

# Compute magnitude spectrum
magnitude_spectrum = 20 * np.log(np.abs(fshift))
convoluted_image = img_gray.filter(ImageFilter.Kernel((5, 5), kernel_5x5, 1, 0))

# Display the original image and its magnitude spectrum
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(img_gray, cmap='gray'), plt.title('Original Image')
# plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray'), plt.title('Magnitude Spectrum')
plt.subplot(122), plt.imshow(convoluted_image, cmap='gray'), plt.title('Convoluted Image')
plt.show()