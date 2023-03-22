import numpy as np
from skimage.metrics import mean_squared_error
import cv2

# reading image
img = cv2.imread("./images/Lena.bmp")

# convert image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# bits wanted 
bits = [1, 2, 4, 6]
mse = [0, 0, 0, 0]

i = 0
for bit in bits:
    newImg = (gray * (2**bit / 255))
    cv2.imwrite(f"{bit}.jpg", newImg)
    mse[i] = mean_squared_error(gray, newImg)
    i += 1


print(mse)