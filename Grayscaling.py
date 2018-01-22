'''
Grayscaling

Grayscaling is process by which an image is converted from a full color to shades of grey (black & white)

In OpenCV, many functions grayscale images before processing. This is done because it simplifies the image,
 acting almost as a noise reduction and increasing processing time as there is less information in the image.
'''

import cv2

#Method 1
# Load our input image
image = cv2.imread('./images/input.jpg')
cv2.imshow('Original', image)
cv2.waitKey()

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()


#Method 2
#Another method faster method

img = cv2.imread('./images/input.jpg',0) #0 -> gray

cv2.imshow('Grayscale', img)
cv2.waitKey()
cv2.destroyAllWindows()