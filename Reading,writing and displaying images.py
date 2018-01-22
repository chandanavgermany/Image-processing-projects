import cv2
import numpy as np


##Reading images 

# Load an image using 'imread' specifying the path to image
input = cv2.imread('./images/input.jpg')


# To display our image variable, we use 'imshow'
# The first parameter will be title shown on image window
# The second parameter is the image varialbe
cv2.imshow('Hello World', input)

# 'waitKey' allows us to input information when a image window is open
# By leaving it blank it just waits for anykey to be pressed before 
# continuing. By placing numbers (except 0), we can specify a delay for
# how long you keep the window open (time is in milliseconds here)
cv2.waitKey()

# This closes all open windows 
# Failure to place this will cause your program to hang
cv2.destroyAllWindows()


##images dimensions

print input.shape  #prints image's height,width,RGB

print 'Height of Image:', int(input.shape[0]), 'pixels'
print 'Width of Image: ', int(input.shape[1]), 'pixels'


##writing image

# Simply use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('output1.jpg', input)
cv2.imwrite('output1.png', input)