import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
images = ['adinan.png', 'enzo.png', 'giovanna.png', 'randre.png']

for image in images:
    img = cv.imread(f'./images/{image}', cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    equ = cv.equalizeHist(img)
    res = np.hstack((img,equ)) #stacking images side-by-side
    cv.imwrite(f"./labs/lab4/{image.split('.')[0]}_equalizated.png",res)
    
    img2 = equ

    hist,bins = np.histogram(img.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.savefig(f"{os.getcwd()}/labs/lab4/hist_{image.split('.')[0]}.pdf", bbox_inches='tight', dpi=300)
    plt.show()

    hist2,bins2 = np.histogram(img2.flatten(),256,[0,256])
    cdf2 = hist2.cumsum()
    cdf_m2 = np.ma.masked_equal(cdf2,0)
    cdf_m2 = (cdf_m2 - cdf_m2.min())*255/(cdf_m2.max()-cdf_m2.min())
    cdf2 = np.ma.filled(cdf_m2,0).astype('uint8')
    cdf_normalized2 = cdf2 * float(hist2.max()) / cdf2.max()
    plt.plot(cdf_normalized2, color = 'cyan')
    plt.hist(img2.flatten(),256,[0,256], color = 'magenta')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.savefig(f"{os.getcwd()}/labs/lab4/hist_equalizated_{image.split('.')[0]}.pdf", bbox_inches='tight', dpi=300)
    plt.show()