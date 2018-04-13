from PIL import Image
import os
import numpy as np

def balance_levels(red_channel, blue_channel, green_channel):
    red_vector = []
    blue_vector = []
    green_vector = []

    red_pixels = red_channel.load()
    blue_pixels = blue_channel.load()
    green_pixels = green_channel.load()

    for i in range(red_channel.size[0]):
        for j in range(red_channel.size[1]):
            red_vector.append(red_pixels[i,j])
            blue_vector.append(blue_pixels[i,j])
            green_vector.append(green_pixels[i,j])

    red_max = sum(red_vector)/len(red_vector)
    blue_max = sum(blue_vector)/len(blue_vector)
    green_max = sum(green_vector)/len(green_vector)
    print(red_max,blue_max,green_max)

    total_max = max(red_max, blue_max, green_max)
    print(total_max)

    red_weight = 5 * red_max/total_max
    blue_weight = 5 * blue_max/total_max
    green_weight = 5 * green_max/total_max

    red_brightness = (128 - red_max)*red_max/total_max
    blue_brightness = (128 - blue_max)*blue_max/total_max
    green_brightness = (128 - green_max)*green_max/total_max

    for i in range(red_channel.size[0]):
        for j in range(red_channel.size[1]):
            red_pixels[i,j] = int(red_pixels[i,j] * red_weight + red_brightness)
            blue_pixels[i,j] = int(blue_pixels[i,j] * blue_weight + blue_brightness)
            green_pixels[i,j] = int(green_pixels[i,j] * green_weight + green_brightness)

    return red_pixels, green_pixels, blue_pixels


results_folder = 'image_decomp'

if not os.path.exists(results_folder):
    os.makedirs(results_folder)

#image_name = input("Enter Image Name") + '.png'

name_1 = 'images/band_1.png'
name_2 = 'images/band_2.png'
name_3 = 'images/band_3.png'
name_4 = 'images/band_4.png'
name_5 = 'images/band_5.png'
name_6 = 'images/band_6.png'
name_7 = 'images/band_7.png'

band_1 = Image.open(name_1)
band_2 = Image.open(name_2)
band_3 = Image.open(name_3)
band_4 = Image.open(name_4)
band_5 = Image.open(name_5)
band_6 = Image.open(name_6)
band_7 = Image.open(name_7)


blue = band_2.split()[0]
green = band_3.split()[0]
red = band_4.split()[0]
NIR = band_5.split()[0]
IR1 = band_6.split()[0]
IR2 = band_7.split()[0]

"""red_values = red.load()
blue_values = blue.load()
green_values = green.load()"""
#red_values, blue_values, green_values = balance_levels(red,blue,green)

NIR_values,IR1_values,IR2_values = balance_levels(NIR,IR1,IR2)

small_im_size = (7000,7000)

#search_image = Image.open(image_name)
#im_size = search_image.size


"""color_im = Image.new('RGB', small_im_size)
pixels = color_im.load()
for i in range(small_im_size[0]):
    for j in range(small_im_size[1]):
        pixels[i,j] = (red_values[i,j], green_values[i,j], blue_values[i,j])

color_im.save('images/test_color.png')"""

IR_im = Image.new('RGB', small_im_size)
pixels = IR_im.load()
for i in range(small_im_size[0]):
    for j in range(small_im_size[1]):
        pixels[i,j] = (NIR_values[i,j], IR1_values[i,j], IR2_values[i,j])

IR_im.save('images/test_IR.png')


"""for i in range(1,im_size(1)//small_im_size(1)):
    for j in range(1,im_size(2)//small_im_size(2)):"""
