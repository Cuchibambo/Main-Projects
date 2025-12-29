from PIL import Image
import random

HeightMap = Image.open(r"python\Pillow works\HeightMap.png")

# print(HeightMap.format, HeightMap.size, HeightMap.mode)

width, height = HeightMap.size

Noise = Image.new('RGB', (width, height))

for x in range(width):
    for y in range(height):
        Noise.putpixel((x,y),((y%2)*255,255,255))



Noise.show()

# HeightMap.show()
