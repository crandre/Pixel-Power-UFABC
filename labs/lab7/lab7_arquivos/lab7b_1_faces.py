import cv2 
import numpy as np 
import common #some useful opencv functions

test_image = cv2.imread('test.jpg')
grey = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Carrega a cascade treinada e na imagem cinza aplica Detecção de FACES:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(grey, 1.3, 5)

# na imagem de entrada desenha retangulos nos pontos detectados
for (x,y,w,h) in faces:
     cv2.rectangle(test_image,(x,y),(x+w,y+h),(255,0,0),2)

# Definir nome da janela para re-dimensionar a janela
height, width, ch = test_image.shape
W2 = int(width/1.5)
H2 = int(height/1.5)
cv2.namedWindow("Faces Detection", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Faces Detection", W2, H2)
cv2.imshow("Faces Detection", test_image)


if cv2.waitKey(0) & 0xff == 27:
 cv2.destroyAllWindows()
