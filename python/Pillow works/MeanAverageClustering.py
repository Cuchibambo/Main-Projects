from PIL import Image

original_img = Image.open(r'python\Pillow works\example.jpg')
image_size = original_img.size
Colors = []
for x in range(image_size[0]):
    for y in range(image_size[1]):
        Colors.append(original_img.getpixel((x,y)))







new_img = Image.new(original_img.mode,
          original_img.size)

new_img.show()