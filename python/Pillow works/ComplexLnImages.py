from PIL import Image
from io import BytesIO
import requests
from cmath import log, exp, e

res = 500

print('Getting Image...')
url = f"https://picsum.photos/{str(res)}"
# url = f"https://picsum.photos/id/61/{str(res)}"
response = requests.get(url)
img_data = response.content
Original_Image = Image.open(BytesIO(img_data))
print('Got the Image!')

print('Makeing new Image')
Warped_Image = Image.new(Original_Image.mode,Original_Image.size)

print('Warping Image')
for x in range(res):
    for y in range(res):
        Warped_pos = exp(complex(((2*x)/res)-1,
                                 ((2*y)/res)-1))
        color = Original_Image.getpixel((int(Warped_pos.real*(500/e)-250%res),
                                         int(Warped_pos.imag*(500/e))%res))
        Warped_Image.putpixel((x,y),color)



Warped_Image.show()
print('Image Warped!')
Original_Image.show()
