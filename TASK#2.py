import numpy as np
from skimage.metrics import mean_squared_error
import cv2

# reading image
img = cv2.imread("./images/Lena.bmp")

# convert image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# bits wanted 
bits = [1, 2, 4, 6]
# list to hold mse values for each number of bits
mse = [0, 0, 0, 0]

# here we map each value between 0-255,
# to a value between 0-2**bit.
# for example if the number of bit is 6,
# we map the values in the range of [0,255],
# to a value in the range of [0-64]
i = 0
for bit in bits:
    # here we calculate the new value for each pixel
    # for exanple consider we have a pixel with the value of 100
    # in the range of [0, 255],
    # find the new value, we multiply the current value bye the ratio of decrease.
    # the ratio is calculated by dividing the new number of levels by 255
    # for instance, we want to show each pixel by only 6 bits, so the number of
    # levels is 2**6 = 64 levels.
    # the ratio = 64 / 255 = 1 / 4 = 0.25
    # so the new value for the pixel if the current value is 100 
    # will be: 100 * 0.25 = 25
    newImg = (gray * (2**bit / 255))
    # calulating the mean squared error for each new image
    mse[i] = mean_squared_error(gray, newImg)
    i += 1
    # saving new images to results_2 directory
    # NOTE: the directory should be created before the execution of program
    # othewise the results won't be saved
    cv2.imwrite(f"./results_2/{bit}-2.jpg", newImg)

# show mse in terminal
print(mse)