import cv2
import numpy as np
from skimage.metrics import mean_squared_error

# level numbers
levels = [4, 8, 64, 128]
mse = [0, 0, 0, 0]
# newImg = []
# reading image
img = cv2.imread('./images/Lena.bmp')

# converting image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# mapping pixel values to new values but with specific number of levels
# for example if we want 128 levels then each 2 steps in the range of 0-255
# will be one step to achieve 128 levels
i = 0
for level in levels:
    newImg = (np.floor(gray/(256/level))*(256/level))
    mse[i] = mean_squared_error(gray, newImg)
    i += 1

# showing mean squared errors
print(mse)
