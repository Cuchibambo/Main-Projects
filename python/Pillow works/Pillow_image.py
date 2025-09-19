from PIL import Image, ImageFilter, ImageDraw, ImageFont

# Open an image file
image = Image.open("python\Pillow works\example.jpg")

dithered_image = image.convert('1')
image = dithered_image

image.show()