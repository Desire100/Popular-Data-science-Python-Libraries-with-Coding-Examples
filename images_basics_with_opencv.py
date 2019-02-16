# Image basics with opencv

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dog_backpack.png')

# Wrong RGB Order!
plt.imshow(img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

new_img = img_rgb
new_img = cv2.flip(new_img,0)
plt.imshow(new_img)
plt.imshow(img_rgb)

cv2.rectangle(img_rgb,pt1=(200,380),pt2=(600,700),color=(255,0,0),thickness=10)
plt.imshow(img_rgb)

"""
Draw a BLUE TRIANGLE in the middle of the image. The size 
and angle should be a triangle (three sides) in any orientation.

"""
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
vertices = np.array([[250,700],[425,400],[600,700]],np.int32)
pts = vertices.reshape((-1,1,2))

cv2.polylines(img_rgb,[pts],isClosed=True,color=(0,0,255),thickness=20)
plt.imshow(img_rgb)

# Fill in this triangle

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
vertices = np.array([[250,700],[425,400],[600,700]],np.int32)
pts = vertices.reshape((-1,1,2))

cv2.fillPoly(img_rgb,[pts],color=(0,0,255))
plt.imshow(img_rgb)

"""
Create a script that opens the picture and 
allows you to draw empty red circles whever
you click the RIGHT MOUSE BUTTON DOWN.

"""
# Create a function based on a CV2 Event (Right button click)
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),10)
        
  
# Open Image
img = cv2.imread("dog_backpack.png")    
# This names the window so we can reference it 
cv2.namedWindow(winname='dog')
# Connects the mouse button to our callback function
cv2.setMouseCallback('dog',draw_circle)

while True: #Runs forever until we break with Esc key on keyboard
    # Shows the image window
    cv2.imshow('dog',img)
    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    if cv2.waitKey(20) & 0xFF == 27:
        break
# Once script is done, its usually good practice to call this line
# It closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()




