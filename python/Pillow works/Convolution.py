from PIL import Image, ImageDraw
import random
import math
from io import BytesIO
import requests

res = 500

url = f"https://picsum.photos/{str(res)}"
response = requests.get(url)
img_data = response.content
img = Image.open(BytesIO(img_data))


def AverageColor(cols):
    sum = [0,0,0]
    for col in cols:
        sum[0] += col[0]
        sum[1] += col[1]
        sum[2] += col[2]
    if sum[0] >5 : col[0] =5
    if sum[1] >5 : col[1] =5
    if sum[2] >5 : col[2] =5
    sum[0] = int(sum[0])
    sum[1] = int(sum[1])
    sum[2] = int(sum[2])
    return sum

BoxBlur_Kernel = [
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
]

EdgeDetection_Kernel_Horizontal = [
    [-1,0,1],
    [-1,0,1],
    [-1,0,1]
]

EdgeDetection_Kernel_Vertical = [
    [1,1,1],
    [0,0,0],
    [-1,-1,-1]
]

def Convolution(img,kernel,autodiv,customdiv):
    new_img = Image.new(img.mode, img.size, (0,0,0))
    kernelmax = 0
    for i in range(len(kernel)):
        for j in range(len(kernel[0])):
            kernelmax += kernel[i][j]
    for x in range(res):
        for y in range(res):
            colors = []
            for dx in range(len(kernel)):
                for dy in range(len(kernel[0])):
                    try:
                        dx -= len(kernel)//2
                        dy -= len(kernel[0])//2
                        pending_color = img.getpixel((x+dx,y+dy))
                        prossesed_color = [0,0,0]
                        if autodiv:
                            prossesed_color[0] = pending_color[0]*kernel[dy][dx]/kernelmax
                            prossesed_color[1] = pending_color[1]*kernel[dy][dx]/kernelmax
                            prossesed_color[2] = pending_color[2]*kernel[dy][dx]/kernelmax
                        else:
                            prossesed_color[0] = pending_color[0]*kernel[dy][dx]/customdiv
                            prossesed_color[1] = pending_color[1]*kernel[dy][dx]/customdiv
                            prossesed_color[2] = pending_color[2]*kernel[dy][dx]/customdiv
                        colors.append(prossesed_color)
                    except Exception as e:
                        pass
            color = AverageColor(colors)
            new_img.putpixel((x,y),tuple(color))
    print('done!')
    return new_img

edgeDetection_img = Convolution(img,EdgeDetection_Kernel_Horizontal,False,2)
edgeDetection_img = Convolution(edgeDetection_img,EdgeDetection_Kernel_Vertical,False,2)
# blured_img = Convolution(img,BoxBlur_Kernel,True,None)
img.show()
edgeDetection_img.show()
# blured_img.show()