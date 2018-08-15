from __future__ import print_function
import os, sys
from PIL import Image
import numpy as np

ASCII_VALS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_VAL = 255

def load(filename):
    return Image.open(filename)

def get_size(inp):
    if isinstance(inp, (list, tuple, np.ndarray)):
        dim = ( len(inp[0]), len(inp))
    else:
        dim = list(inp.size)
    return (dim[0], dim[1])

def resize(image, ratio):
    r, c = get_size(image)
    image = image.resize([int(ratio*r), int(ratio*c)], Image.ANTIALIAS)
    return image

def image_to_array(image):
    return np.array(image)

def generate_brightness_array(arr, bright_type):
    dim = get_size(arr)
    b_arr = [[ 0 for i in range(dim[0])] for j in range(dim[1])] #brightness_array
    for x in range(dim[1]):
        for y in range(dim[0]):
            pixel = arr[x][y] #rgb tuple
            r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
            avg = (r + g + b) / 3
            lightness = (max(r,g,b) + min(r,g,b)) / 2
            luminosity = int(0.21*r + 0.72*g + 0.07*b)
            if (bright_type == 1):
                b_arr[x][y] = avg
            elif (bright_type == 2):
                b_arr[x][y] = lightness
            elif (bright_type == 3):
                b_arr[x][y] = luminosity
    return b_arr

def generate_char_array(arr):
    dim = get_size(arr)
    ascii_arr = [[ None for i in range(dim[0])] for j in range(dim[1])]
    interval = int(MAX_VAL/len(ASCII_VALS))
    for x in range(dim[1]):
        for y in range(dim[0]):
            bright_val = int(arr[x][y])
            index = int(bright_val/MAX_VAL*len(ASCII_VALS)) - 1
            ascii_arr[x][y] = ASCII_VALS[index]
    return ascii_arr

def print_ascii_image(arr):
    for r in arr:
        line = [ i + i + i for i in r]
        print("".join(line))

if __name__ == "__main__":
    # import image
    filename = input("Which file would you like to convert to ASCII?: ")
    im = load(filename)
    dim = get_size(im)
    print("Current image size: " + str(dim[0]) + " x " + str(dim[1]))
    ratio = int(input("Resize your image by percentage! Please enter a number between 0 and 100: "))/100
    im = resize(im, ratio)
    resize_dim = get_size(im)
    print("New image size: " + str(resize_dim[0]) + " x " + str(resize_dim[1]))
    a_arr = image_to_array(im)
    brightness_type = int(input("Do you want to map brightness using average (1), lightness (2), or luminosity (3)?: "))
    b_arr = generate_brightness_array(a_arr, brightness_type)
    c_arr = generate_char_array(b_arr)
    print_ascii_image(c_arr)
