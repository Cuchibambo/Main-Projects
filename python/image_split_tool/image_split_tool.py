from PIL import Image
from math import sqrt, ceil

img = Image.open(r"python\image_split_tool\Toki_pona dict.png")

width = img.width
height = img.height

ratio = sqrt(2)

new_height = round(width * ratio)

Images = []

image_count = ceil(height/new_height)

for i in range(image_count):
    img.crop((0,i*new_height,width,(i+1)*new_height)).save(fr"python\image_split_tool\{i}.png")