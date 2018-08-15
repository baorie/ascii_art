from __future__ import print_function
import os, sys
from PIL import Image
from numpy import array

im = Image.open("meme.jpg")
maxsize = (320, 240)
size = list(im.size)
print("Successfully loaded image!")
print("Image size: " + str(size[0]) + " x " + str(size[1]))
im = im.resize([160,120], Image.ANTIALIAS)
arr = array(im)

light_arr = [[ 0 for i in range(len(arr[0]))] for j in range(len(arr))]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        pixel = arr[x][y]
        pixel_avg = (int(pixel[0]) + int(pixel[1]) + int(pixel[2]) ) / 3 
        light_arr[x][y] = int(pixel_avg)

ascii_arr = [[ None for i in range(len(arr[0]))] for j in range(len(arr))]
ascii_vals = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
print(len(ascii_vals)) # 65 characters

# brightness values are between 0 and 255 (256 total values)
# there are only 65 characters

interval_range = int(255/len(ascii_vals))
print(interval_range)

for x in range(len(light_arr)):
    for y in range(len(light_arr[x])):
        brightness = int(light_arr[x][y]) #makes sure this is an integer between 0 and 255
        ascii_arr[x][y] = ascii_vals[int(brightness/255*len(ascii_vals)) - 1]

for row in ascii_arr:
    row_out = [ i + i + i for i in row]
    print("".join(row_out))
