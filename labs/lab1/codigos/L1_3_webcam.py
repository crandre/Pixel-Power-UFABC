import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

cont = 150

if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
   
    # Display the resulting frame
    cv.imshow('frame', frame)
    
    key = cv.waitKey(1)
    if key == ord('x'):
        cv.imwrite('./foto'+str(cont)+'.png', frame)
        cont+=1
    if key == ord('q'):
        break
    

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
