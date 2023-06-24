import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
# img = cv.imread('./labs/lab2/codigos/imagens/opencv_logo.png')
img = cv.imread(f"{os.getcwd()}/labs/lab2/codigos/imagens/foto164.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
assert img is not None, "file could not be read, check with os.path.exists()"
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.savefig(f"{os.getcwd()}/labs/lab2/codigos/imagens/codigo_1.png", bbox_inches='tight', dpi=300)
plt.show()