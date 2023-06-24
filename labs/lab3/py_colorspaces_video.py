import cv2 as cv
import os
import numpy as np
cap = cv.VideoCapture(0)

# Get current width of frame
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # float
# Define Video Frame Rate in fps
fps = 30.0

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out1 = cv.VideoWriter('saida1_blur.avi', fourcc, fps, (int(width),int(height)) )
out2 = cv.VideoWriter('saida2_blur.avi', fourcc, fps, (int(width),int(height)) )
out3 = cv.VideoWriter('saida3_blur.avi', fourcc, fps, (int(width),int(height)) )


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = cv.flip(frame, 0)

    frame = cv.bilateralFilter(cv.flip(frame, 0),9,75,75) # blur
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV (VSH)
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    lower_blue = np.array([50,60,70])
    upper_blue = np.array([90,180,180])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    # cv.imshow('frame',frame)
    # cv.imshow('mask',mask)
    # cv.imshow('res',res)

    out1.write(frame)
    out2.write(mask)
    out3.write(res)

    cv.imshow('frame', frame)
    cv.imshow('frame', mask)
    cv.imshow('frame', res)

    if cv.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()