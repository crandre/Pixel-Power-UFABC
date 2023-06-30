import cv2 as cv
import os
import numpy as np
cap = cv.VideoCapture(0)

# Get current width of frame
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT) # float
# Define Video Frame Rate in fps
fps = cap.get(cv.CAP_PROP_FPS)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out1 = cv.VideoWriter('saidaX_blur.mp4', fourcc, fps, (int(width),int(height)) )
out2 = cv.VideoWriter('saidaY_blur.mp4', fourcc, fps, (int(width),int(height)) )
out3 = cv.VideoWriter('saidaZ_blur.mp4', fourcc, fps, (int(width),int(height)) )


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Blur
    frame = cv.bilateralFilter(frame,9,75,75)
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV (VSH)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    out1.write(frame)
    out2.write(mask)
    out3.write(res)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    if cv.waitKey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out1.release()
out2.release()
out3.release()
cv.destroyAllWindows()