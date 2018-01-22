## Drawing images and shapes using OpenCV

# black square

import cv2
import numpy as np

# Create a black image
image = np.zeros((512,512,3), np.uint8)

# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Black Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()


##line over our black sqare
#cv2.line(image, starting cordinates, ending cordinates, color, thickness)
# Draw a diagonal blue line of thickness of 5 pixels
image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,0), (511,511), (255,127,0), 5)
cv2.imshow("Blue Line", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#rectangle
#cv2.rectangle(image, starting vertex, opposite vertex, color, thickness)

# Draw a Rectangle in
image = np.zeros((512,512,3), np.uint8)

cv2.rectangle(image, (100,100), (300,250), (127,50,127), -1) #-1 fills color inside rectangle
cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Circle
#cv2.cirlce(image, center, radius, color, fill)
image = np.zeros((512,512,3), np.uint8)

cv2.circle(image, (350, 350), 100, (15,75,50), -1) 
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Polygons

image = np.zeros((512,512,3), np.uint8)

# Let's define four points
pts = np.array( [[10,50], [400,50], [90,150], [50,500]], np.int32)

# reshape our points in form  required by polylines
pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True, (0,0,255), 3)
cv2.imshow("Polygon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Adding text with cv2.putText

'''
cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)

FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
FONT_HERSHEY_DUPLEX,FONT_HERSHEY_COMPLEX
FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
FONT_HERSHEY_SCRIPT_SIMPLEX
FONT_HERSHEY_SCRIPT_COMPLEX
'''

image = np.zeros((512,512,3), np.uint8)

cv2.putText(image, 'Chandan loves Sahana', (75,290), cv2.FONT_HERSHEY_COMPLEX, 1, (100,170,0), 3)
cv2.imshow("Hello World!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()