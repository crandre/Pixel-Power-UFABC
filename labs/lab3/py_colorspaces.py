import cv2 as cv
import os
import numpy as np
cap = cv.VideoCapture(0)

cont = 18

while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV (VSH)
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])

    # filtro verde blusa giovanna
    lower_blue = np.array([50,60,70])
    upper_blue = np.array([90,180,180])

    # #filtro verde e cor da pele
    # lower_blue = np.array([10,20,30])
    # upper_blue = np.array([120,180,180])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    key = cv.waitKey(5) & 0xFF
    if key == ord('x'):
        cv.imwrite(f"{os.getcwd()}/labs/lab3/fotos/{cont}_frame.png", frame)
        cv.imwrite(f"{os.getcwd()}/labs/lab3/fotos/{cont}_mask.png", mask)
        cv.imwrite(f"{os.getcwd()}/labs/lab3/fotos/{cont}_res.png", res)
        cont+=1
    if key == ord('q'):
        break
    # if k == 27:
    #     break
cv.destroyAllWindows()