import cv2
import numpy as np
# getting image ready for process

# reading original image
img = cv2.imread("./images/Lena.bmp")

# converting to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


# 3rd TASK

# making image darken by subtacting 128 from each pixel
# the pixels that are less than 128 or euqual to, are mapped to zero
darken = np.where(128 >= gray, 0, gray - 128)
cv2.imwrite("./results/darken.jpg", darken)

# making image lighten by adding 128 to each pixel
# the pixels that are more or equal to 128 are mapped to 255
lighten = np.where(128 <= gray, 255, gray + 128)
cv2.imwrite("./results/lighten.jpg", lighten)

# lower contrast by dividing each pixel by 2 (first way)
# non-linear lower contrast (second way) (used here)
lowerContrast = (gray / 255.0)**0.33 * 255.0
cv2.imwrite("./results/LowerContrast.jpg", lowerContrast)


# raise contrast by multiplying each pixel by 2 (first way)
# non-linear raise contrast
raiseContrast = (gray / 255.0)**2 * 255.0
cv2.imwrite("./results/RaiseContrast.jpg", raiseContrast)

# inverting image by subtracting each pixel from 255
inverted = 255 - gray
cv2.imwrite("./results/inverted.jpg", inverted)

# END OF 3rd TASK