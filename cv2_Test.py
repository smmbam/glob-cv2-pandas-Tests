import cv2
import numpy as np
from matplotlib import pyplot as plt

# reads kean logo image and turns it grayscale
img = cv2.imread('kean.png',cv2.IMREAD_GRAYSCALE)

# plots and displays image among basic image manipulation tools
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
