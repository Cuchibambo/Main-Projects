from PIL import Image
import random

HeightMap = Image.open(r"python\Pillow works\HeightMap.png")

# print(HeightMap.format, HeightMap.size, HeightMap.mode)

width, height = HeightMap.size

Noise = Image.new('1', (width, height))

for x in range(width):
    for y in range(height):
        Noise.putpixel((x,y),random.randint(0,1)*255)



Noise.show()

# HeightMap.show()
