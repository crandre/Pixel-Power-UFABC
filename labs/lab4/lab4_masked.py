import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
images = ['adinan.png', 'enzo.png', 'giovanna.png', 'randre.png']

# for image in images:
img = cv.imread(f'./images/foto_Randre.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
hist = cv.calcHist([img],[0],None,[256],[0,256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'cyan')
plt.hist(img.flatten(),256,[0,256], color = 'magenta')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.savefig(f"{os.getcwd()}/labs/lab4/hist_masked_foto_Randre.pdf", bbox_inches='tight', dpi=300)
plt.show()