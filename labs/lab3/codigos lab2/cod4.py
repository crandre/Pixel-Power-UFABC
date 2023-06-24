import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
# img = cv.imread('./labs/lab2/codigos/imagens/opencv_logo.png')
img = cv.imread(f"{os.getcwd()}/labs/lab2/codigos/imagens/foto164.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
assert img is not None, "file could not be read, check with os.path.exists()"
median = cv.medianBlur(img,5)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median Blurring')
plt.xticks([]), plt.yticks([])
plt.savefig(f"{os.getcwd()}/labs/lab2/codigos/imagens/codigo_4.png", bbox_inches='tight', dpi=300)
plt.show()
