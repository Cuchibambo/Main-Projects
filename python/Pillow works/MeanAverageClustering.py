from PIL import Image

def CalculateRange(List,index):
    List.sort(key=lambda k: k[index])
    range = List[-1][index]-List[0][index]
    return range

def GetMean(List,index):
    List. 

original_img = Image.open(r'python\Pillow works\example.jpg')
image_size = original_img.size
Colors = []
for x in range(image_size[0]):
    for y in range(image_size[1]):
        Colors.append(original_img.getpixel((x,y)))
Rrange = CalculateRange(Colors,0)
Grange = CalculateRange(Colors,1)
Brange = CalculateRange(Colors,2)








# new_img = Image.new(original_img.mode,
#           original_img.size)

# new_img.show()