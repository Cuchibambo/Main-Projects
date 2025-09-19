import matplotlib.pyplot as plt
import numpy as np

# Define the Mandelbrot function
def mandelbrot(c, max_iterations):
    z = 0
    iteration = 0
    while abs(z) <= 2 and iteration < max_iterations:
        z = z*z + c
        iteration += 1
    return iteration

# Set up the image size and plot range
width, height = 800, 800  # Image size
xmin, xmax = -2.5, 1.5    # X range (real part)
ymin, ymax = -2.0, 2.0    # Y range (imaginary part)

# # Zoomed in range
# xmin, xmax = -0.75, 0.25  # X range for zoom
# ymin, ymax = -0.5, 0.5    # Y range for zoom

# Create an array to hold the colors for each pixel
image = np.zeros((height, width))

# Maximum number of iterations
max_iterations = 100

# Loop over each pixel in the image
for i in range(width):
    for j in range(height):
        # Map pixel position to a point in the complex plane
        x0 = xmin + (i / width) * (xmax - xmin)
        y0 = ymin + (j / height) * (ymax - ymin)
        c = complex(x0, y0)
        
        # Compute the Mandelbrot function for this point
        iteration = mandelbrot(c, max_iterations)
        
        # Set the color based on the number of iterations
        if iteration == max_iterations:
            color = 0  # Black for points inside the set
        else:
            color = iteration  # Color based on the number of iterations
        
        image[j, i] = color

# Display the Mandelbrot set
plt.imshow(image, extent=[xmin, xmax, ymin, ymax], cmap='inferno')
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
