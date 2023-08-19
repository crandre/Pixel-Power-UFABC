# Feature - Introduction to SIFT (Scale-Invariant Feature Transform)
import numpy as np
import cv2 as cv

images = ['adinan', 'enzo', 'giovanna', 'randre', 'tabuleiro']
extention = 'png'

for image in images:
    img = cv.imread(f'./images/{image}.{extention}')
    gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    sift = cv.SIFT_create()
    kp = sift.detect(gray,None)

    img=cv.drawKeypoints(gray,kp,img)

    cv.imwrite(f'./labs/lab6/lab6c/{image}.{extention}',img)
