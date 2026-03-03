import numpy as np
from PIL import Image

def ComplexImageConverter(f:str):
    img = Image.open(f)
    center = [img.size[0]//2,img.size[1]//2]
    array = np.array([])
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if img.getpixel((x,y)) == (0,0,0,255):
                array = np.append(array, complex(x-center[0],y-center[1]))
    return array