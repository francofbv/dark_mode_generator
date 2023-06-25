import cv2 as cv
import numpy as np

path = input("Enter the path to the image you would like to convert: ")
image = cv.imread(path)
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
grayscale_image = np.multiply(grayscale_image, .05).astype(np.uint8)
equalized_image = cv.equalizeHist(grayscale_image)
dark_mode_image = cv.bitwise_not(equalized_image)

cv.imshow('grayscale image', dark_mode_image)
cv.waitKey(0)
cv.destroyAllWindows()
