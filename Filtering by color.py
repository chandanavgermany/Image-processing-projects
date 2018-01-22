import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# define range of PURPLE color in HSV
lower_purple = np.array([125,0,0])
upper_purple = np.array([175,255,255])

# loop until break statement is exectured
while True:
    
    # Read webcam image
    ret, frame = cap.read()
    
    # Convert image from RBG/BGR to HSV so we easily filter
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Use inRange to capture only the values between lower & upper_blue
    mask = cv2.inRange(hsv_img, lower_purple, upper_purple)

    # Perform Bitwise AND on mask and our original frame
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)  
    cv2.imshow('mask', mask)
    cv2.imshow('Filtered Color Only', res)
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()