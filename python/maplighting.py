from PIL import Image

new_img = Image.new("RGB",(30,30))

def average(values):
    sum = 0
    for v in values:
        sum += v
    return sum/len(values)

for x in range(30):
    for y in range(30):
        height = y
        top_left_average_height = average([y,y-1,y-1])
        height_diffrence = height-top_left_average_height
        print(top_left_average_height,height)
        col_lo = 20
        col_me = 130
        col_hi = 255
        # if 
        # new_img.putpixel((x,y),(col,col,col))
        # new_img.putpixel((x,y),(255,255,255))

new_img.show()