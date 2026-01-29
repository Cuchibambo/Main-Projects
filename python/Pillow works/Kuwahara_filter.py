from PIL import Image
import requests
from io import BytesIO
import MathScripts

# Open an image file
url = "https://picsum.photos/500"
response = requests.get(url)
img_data = response.content
image = Image.open(BytesIO(img_data))


def rgbAverage(cols:list):
    r, g, b = 0, 0, 0
    for col in cols:
        r += col[0]
        g += col[1]
        b += col[2]
    return [r//]
    
image.show()