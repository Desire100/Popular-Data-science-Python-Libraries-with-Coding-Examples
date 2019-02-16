# Image basics with opencv

import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_img(img,cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

img = cv2.imread('giraffes.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
display_img(img)

"""
Apply a binary threshold onto the image. Note:
What happens when you run this on a non
grayscale image vs a grayscale image

"""
img = cv2.imread('giraffes.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
display_img(thresh1,cmap='gray')

img = cv2.imread('giraffes.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
display_img(img)

"""
 Create a low pass filter with a 4 by 4 Kernel 
 filled with values of 1/10 (0.01)
 and then use 2-D Convolution to blur 
 the giraffer image (displayed in normal RGB)
 
"""
kernel = np.ones(shape=(4,4),dtype=np.float32)/10
img = cv2.imread('../DATA/giraffes.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
dst = cv2.filter2D(img,-1,kernel)
display_img(dst)

"""
: Create a Horizontal Sobel Filter (sobelx from our lecture) 
with a kernel size of 5 to the grayscale version of the giaraffes 
image and then display the resulting
gradient filtered version of the image.

"""

img = cv2.imread('giraffes.jpg',0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display_img(sobelx,cmap='gray')

"""
Plot the color histograms for the RED, BLUE, 
and GREEN channel of the giaraffe image. 
Pay careful attention to the ordering of 
the channels.

"""
img =cv2.imread('giraffes.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Giaraffes Histograms')
plt.show()



