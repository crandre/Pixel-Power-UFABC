import cv2 as cv
import os
from matplotlib import pyplot as plt
images = ['adinan.png', 'enzo.png', 'giovanna.png', 'randre.png']

for image in images:
    img = cv.imread(f'./images/{image}', cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    hist = cv.calcHist([img],[0],None,[256],[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.savefig(f"{os.getcwd()}/labs/lab4/hist_{image.split('.')[0]}.pdf", bbox_inches='tight', dpi=300)
    plt.show()