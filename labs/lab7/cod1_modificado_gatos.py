from __future__ import print_function
import cv2 as cv
import argparse
import os
import time

def detectAndDisplay(frame, image):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)

        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = catsface_cascade.detectMultiScale(faceROI)
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)

    cv.imshow('Image - Face detection', frame)

    cv.waitKey(0) # Wait for any key press to close image window
    cv.destroyAllWindows() # Close image window

    timestamp = time.time()
    output_filename = f'./labs/lab7/output_{timestamp}_' + os.path.basename(image)
    cv.imwrite(output_filename, frame) # Save the image


parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='./labs/lab7/lab7_arquivos/haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='./labs/lab7/lab7_arquivos/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--catsface_cascade', help='Path to cats face cascade.', default='./labs/lab7/lab7_arquivos/haarcascade_frontalcatface.xml')

args = parser.parse_args()

face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
catsface_cascade_name = args.catsface_cascade

face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
catsface_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
if not catsface_cascade.load(cv.samples.findFile(catsface_cascade_name)):
    print('--(!)Error loading cats face cascade')
    exit(0)

#-- 2. Read the image

# image = './labs/lab1/grupo.jpg'
image = './labs/lab7/enxoval-para-gato.jpg'

frame = cv.imread(image)
if frame is None:
    print(f'--(!) No captured frame from {image} -- Break!')

detectAndDisplay(frame, image)
