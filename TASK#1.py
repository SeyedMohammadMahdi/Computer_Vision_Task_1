import cv2
import numpy as np
from skimage.metrics import mean_squared_error

# level numbers
levels = [2, 4, 8, 64, 128]
# list to hold mse values for each level number
mse = [0, 0, 0, 0, 0]
# reading image
img = cv2.imread('./images/Lena.bmp')

# converting image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# mapping pixel values to new values but with specific number of levels
# for example if we want 128 levels then each 2 steps in the range of 0-255
# will be one step to achieve 128 levels
# the following variable is for iterating over mse list
i = 0
# here we loop over levels list
for level in levels:
    # make change on the original gary scale image to create 
    # an image with desired number of levels
    # here we get the floor for each step
    # for example if the value is 101 and the step is 2
    # then the step with new number of levels should be dividable 
    # by 2 so the new value is 100.
    # we first divide this value by the step size, here it is 2,
    # so we have 101 / 2 = 50.5,
    # as it was mentioned we get the floor of this number,
    # so we have: floor(50.0) = 50.
    # to remove the effect of division by step size (here it's 2),
    # we multiply the number we got by step size(2),
    # so we have: 50 * 2 = 100.
    newImg = (np.floor(gray/(256/level))*(256/level))
    # calculatin mean squared error using the function mentioned in the 
    # TASK pdf
    mse[i] = mean_squared_error(gray, newImg)
    i += 1
    # saving the result in the results_1 directory
    # NOTE:the directory should be created before the execution of this program
    cv2.imwrite(f"./results_1/{level}-1.jpg", newImg)

# showing mean squared errors
# as it is clear from the result the more the number of levels are the less the mse is
# this is because the image gets closer to original image
print(mse)
