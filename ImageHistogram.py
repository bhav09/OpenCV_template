import cv2
import numpy as np
#from skimage.util import random_noise
import matplotlib.pyplot as plt

img = cv2.imread('chess.jpg')
cv2.imshow('Original',img)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#plt.hist(img_gray.ravel(),bins=256,  fc='k', ec='k')
#plt.show()

gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

# Add the Gaussian noise to the image
img_gauss = cv2.add(img,gauss)
cv2.imshow('Gaussian Noise',img_gauss)
cv2.waitKey(0)
gray_gauss = cv2.cvtColor(img_gauss,cv2.COLOR_BGR2GRAY)
plt.hist(img_gray.ravel(),bins=256,  fc='blue', ec='k',label='Original Image')
plt.hist(gray_gauss.ravel(),bins=256,  fc='orange', ec='k',label='Gaussian Noise')
plt.title('Histogram Comparison')
plt.legend()
plt.show()

#original image

