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

# na imagem de entrada desenha retangulos nos pontos detectados
for (x,y,w,h) in smiles:
     cv2.rectangle(test_image,(x,y),(x+w,y+h),(0,255,0),2)
     
# Definir nome da janela para re-dimensionar a janela
height, width, ch = test_image.shape
W2 = int(width/2)
H2 = int(height/2)
cv2.namedWindow("All Smiles", cv2.WINDOW_NORMAL)
cv2.resizeWindow("All Smiles", W2, H2)
cv2.imshow("All Smiles", test_image)

# Restringir Sorrisos dentro das Faces
test_image = cv2.imread('test.jpg')
for (x,y,w,h) in faces:
  for (x_s,y_s,w_s,h_s) in smiles:
    if( (x <= x_s) and (y <= y_s) and ( x+w >= x_s+w_s) and ( y+h >= y_s+h_s)):
      cv2.rectangle(test_image, (x_s,y_s),(x_s+w_s,y_s+h_s),(0,255,0),2)

cv2.namedWindow("Smiles of Faces Only", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Smiles of Faces Only", W2, H2)
cv2.imshow("Smiles of Faces Only", test_image)

if cv2.waitKey(0) & 0xff == 27:
 cv2.destroyAllWindows()
