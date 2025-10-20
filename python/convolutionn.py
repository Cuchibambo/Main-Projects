# from PIL import Image, ImageFilter
# from io import BytesIO
# import requests

# # Define a 5x5 convolution kernel
# kernel_5x5 = [
# 1,  0, -1,  0,  0,
# 0,  1, -1,  0,  0,
# -1, -1,  1,  1,  1,
# 0,  0,  1,  1,  0,
# 0,  0,  1,  0, -1
# ]

# def apply_convolution(image_path):
#     # Open the image using PIL
#     img = Image.open(image_path)

#     # Convert the image to grayscale
#     img_gray = img.convert('L')  # Convert to grayscale

#     # Apply convolution using the defined kernel
#     convoluted_image = img_gray.filter(ImageFilter.Kernel((5, 5), kernel_5x5, 1, 0))

#     return convoluted_image

# # Example usage
# if __name__ == "__main__":
    
#     # Download a random 200x200 image and save it as the file used below
#     url = "https://picsum.photos/200"
#     # Fetch the image from the URL
#     response = requests.get(url)
#     img_data = response.content
#     # Open the image using PIL
#     img = Image.open(BytesIO(img_data))

#     result_image = apply_convolution(img)
#     result_image.show()

import math
import time

# print(os.times())
epoch_time = int(time.time())
print(math.factorial(5000))

print(int(time.time())-epoch_time)