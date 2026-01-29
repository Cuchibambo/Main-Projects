from PIL import Image
from io import BytesIO
import requests

res = 500

print('Getting Image...')
url = f"https://picsum.photos/{str(res)}"
response = requests.get(url)
img_data = response.content
Original_Image = Image.open(BytesIO(img_data))
print('Image Gotten!')

def AverageColor(cols):
    sum = [0,0,0]
    for col in cols:
        sum[0] += col[0]
        sum[1] += col[1]
        sum[2] += col[2]
    sum[0] = int(sum[0])
    sum[1] = int(sum[1])
    sum[2] = int(sum[2])
    return sum

BoxBlur_Kernel5x5 = [
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

Sharpen_Kernel = [
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
]

GaussianBlur_Kernel_3x3 = [
    [1,2,1],
    [2,4,2],
    [1,2,1]
]

GaussianBlur_Kernel_5x5 = [
    [1,4,7,4,1],
    [4,16,26,16,4],
    [7,26,41,26,7],
    [4,16,26,16,4],
    [1,4,7,4,1]
]

Test_Kernel = [
    [1,1,1],
    [1,-1,1],
    [1,1,1]
]

def Convolution(img,kernel,autodiv,customdiv):
    print(f"Convolution Started!")
    new_img = Image.new(img.mode, img.size, (0,0,0)) # type: ignore
    kernelmax = 0
    for i in range(len(kernel)):
        for j in range(len(kernel[0])):
            kernelmax += kernel[i][j]
    for x in range(res):
        for y in range(res):
            colors = []
            xOffset = len(kernel)//2
            yOffset = len(kernel[0])//2
            for dx in range(len(kernel)):
                dx -= xOffset
                for dy in range(len(kernel[0])):
                    try:
                        dy -= yOffset
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
    print(f'Convolution Done!')
    return new_img

Original_Image.save('Original_Image.png')

# EdgeDetection_Image = Convolution(Original_Image,EdgeDetection_Kernel_Horizontal,False,2)
# EdgeDetection_Image = Convolution(EdgeDetection_Image,EdgeDetection_Kernel_Vertical,False,2)
# EdgeDetection_Image.save('EdgeDetection_Image.png')

# BowBlured_Image5x5 = Convolution(Original_Image,BoxBlur_Kernel5x5,True,None)
# BowBlured_Image5x5.save('BowBlured_Image5x5.png')

# Sharpened_Image = Convolution(Original_Image, Sharpen_Kernel, False, 1)
# Sharpened_Image.save('Sharpened_Image.png')

# GaussianBlur3x3_Image = Convolution(Original_Image, GaussianBlur_Kernel_3x3, True, None)
# GaussianBlur3x3_Image.save('GaussianBlur3x3_Image.png')

# GaussianBlur5x5_Image = Convolution(Original_Image, GaussianBlur_Kernel_5x5, True, None)
# GaussianBlur5x5_Image.save('GaussianBlur5x5_Image.png')

# Test_Image = Convolution(Original_Image, Test_Kernel, True, None)
# Test_Image.save('Test_Image.png')