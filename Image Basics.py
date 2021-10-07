import cv2 as cv

img = cv.imread('test.jpg')
# cv.imshow('Output', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

import inspect
print(inspect.getmro(type(gray)))
print(gray)
cv.waitKey(0)
cv.destroyAllWindows()

from PIL import Image

image = Image.fromarray(gray, 'L')
# image.show()
import numpy as np

one_dim = np.array([20,50,25,10,30])
double_dim = np.array([one_dim])
print(double_dim) #an image is a 2D array 1 row = height and 5 columns = width

img1 = Image.fromarray(double_dim, 'L')
# img1.show()

image1 = np.reshape(gray, (1, gray.shape[0]*gray.shape[1]))
print(image1)
image1 = Image.fromarray(image1, 'L')
# image1.show()

news = cv.imread('news.png')
gray_news = cv.cvtColor(news, cv.COLOR_BGR2GRAY)
print(gray_news[2:4, 1:3])

print(np.count_nonzero(gray_news[2:4, 1:3]))

white_matrix = np.full((12,12), 255, dtype=nIp.uint8)
white_image = Image.fromarray(white_matrix, 'L')
white_image.show()

print(white_matrix)

white_matrix[:,6] = np.full((1,12), 0, dtype=np.uint8)
print(white_matrix)
white_image = Image.fromarray(white_matrix, 'L')
white_image.show()