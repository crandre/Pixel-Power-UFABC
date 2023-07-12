# Feature - Harris Corner Detection

import numpy as np
import cv2 as cv

images = ['adinan', 'enzo', 'giovanna', 'randre', 'tabuleiro']
extention = 'png'

for image in images:
  img = cv.imread(f'./images/{image}.{extention}')
  gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

  gray = np.float32(gray)
  dst = cv.cornerHarris(gray,2,3,0.04)

  #result is dilated for marking the corners, not important
  dst = cv.dilate(dst,None)

  # Threshold for an optimal value, it may vary depending on the image.
  img[dst>0.01*dst.max()]=[0,0,255]

  cv.imshow('dst',img)
  cv.imwrite(f'./labs/lab6/lab6a/{image}.{extention}',img)
