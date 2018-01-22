### 1. Gaussian Mixture-based Background/Foreground Segmentation Algorithm

# OpenCV 2.4.13 only
import numpy as np
import cv2

cap = cv2.VideoCapture('images/walking.avi')

# Initlaize background subtractor
foreground_background = cv2.BackgroundSubtractorMOG()

while True:
    
    ret, frame = cap.read()

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(1) == 13: 
        break

cap.release()
cv2.destroyAllWindows()

#WebCam

# OpenCV 2.4.13 only
import numpy as np
import cv2

# Intialize Webcam
cap = cv2.VideoCapture(0)

# Initlaize background subtractor
foreground_background = cv2.BackgroundSubtractorMOG()

while True:
    
    ret, frame = cap.read()

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(1) == 13: 
        break

cap.release()
cv2.destroyAllWindows()

###Improved adaptive Gausian mixture model for background subtraction
# OpenCV 2.4.13
import numpy as np
import cv2

cap = cv2.VideoCapture('images/walking.avi')

# Initlaize background subtractor
foreground_background = cv2.BackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(1) == 13: 
        break

cap.release()
cv2.destroyAllWindows()


#Foreground substraction

import cv2
import numpy as np

# Initalize webacam and store first frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Create a flaot numpy array with frame values
average = np.float32(frame)

while True:
    # Get webcam frmae
    ret, frame = cap.read()
    
    # 0.01 is the weight of image, play around to see how it changes
    cv2.accumulateWeighted(frame, average, 0.01)
    
    # Scales, calculates absolute values, and converts the result to 8-bit
    background = cv2.convertScaleAbs(average)

    cv2.imshow('Input', frame)
    cv2.imshow('Disapearing Background', background)
    
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cv2.destroyAllWindows()
cap.release()