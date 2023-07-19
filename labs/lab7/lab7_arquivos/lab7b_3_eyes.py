import cv2 
import numpy as np 
import common #some useful opencv functions

test_image = cv2.imread('test.jpg')
grey = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Carrega a cascade treinada e na imagem cinza aplica Detecção de FACES:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(grey, 1.3, 5)

# Carrega a cascade treinada e na imagem cinza aplica Detecção de SORRISOS:
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
smiles = smile_cascade.detectMultiScale(grey, 1.3, 20)

# Carrega a cascade treinada e na imagem cinza aplica Detecção de OLHOS:
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(grey, 1.3, 1)

# na imagem de entrada desenha retangulos nos pontos detectados
for (x,y,w,h) in eyes:
     cv2.rectangle(test_image,(x,y),(x+w,y+h),(255,255,255),2)
     
# Definir nome da janela para re-dimensionar a janela
height, width, ch = test_image.shape
W2 = int(width/3)
H2 = int(height/3)
cv2.namedWindow("All Eyes", cv2.WINDOW_NORMAL)
cv2.resizeWindow("All Eyes", W2, H2)
cv2.imshow("All Eyes", test_image)

# Restringir Olhos dentro das Faces
test_image = cv2.imread('test.jpg')
for (x,y,w,h) in faces:
  for (x_s,y_s,w_s,h_s) in eyes:
    if( (x <= x_s) and (y <= y_s) and ( x+w >= x_s+w_s) and ( y+h >= y_s+h_s)):
      cv2.rectangle(test_image, (x_s,y_s),(x_s+w_s,y_s+h_s),(255,255,255),2)
      
cv2.namedWindow("Eyes inside Faces Only", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Eyes inside Faces Only", W2, H2)
cv2.imshow("Eyes inside Faces Only", test_image)

if cv2.waitKey(0) & 0xff == 27:
 cv2.destroyAllWindows()
