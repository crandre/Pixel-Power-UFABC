
# import the opencv module
import cv2 as cv

# capturing video
# capture = cv.VideoCapture("./labs/lab5/lab5_arquivos/vtest.avi")

# movimento lento foreground mask
capture = cv.VideoCapture("./labs/lab1/saida2.avi")
print(capture.get(cv.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv.CAP_PROP_FRAME_HEIGHT))


# movimento rápido foreground mask
# capture = cv.VideoCapture("./labs/lab1/saida7.avi")

backSub = cv.createBackgroundSubtractorMOG2()

#backSub = cv.createBackgroundSubtractorKNN()

if not capture.isOpened():
 print('Unable to open: ' + args.input)
 exit(0)

while True:
 ret, frame = capture.read()
 if frame is None:
   break
 
 fgMask = backSub.apply(frame)
 
 cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
 cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
 cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
 
 cv.imshow('Frame', frame)
 cv.imshow('FG Mask', fgMask)
 
 keyboard = cv.waitKey(30)
 if keyboard == ord('q') or keyboard == 27:
   break
