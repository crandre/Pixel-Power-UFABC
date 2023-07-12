import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


images = ['adinan', 'enzo', 'giovanna', 'randre', 'tabuleiro']
extention = 'png'

for image in images:
  img = cv.imread(f'./images/{image}.{extention}')
  gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

  corners = cv.goodFeaturesToTrack(gray,25,0.01,10)
  corners = np.int0(corners)

  for i in corners:
   x,y = i.ravel()
   cv.circle(img,(x,y),3,255,-1)

  cv.imwrite(f'./labs/lab6/lab6b/{image}.{extention}',img)
