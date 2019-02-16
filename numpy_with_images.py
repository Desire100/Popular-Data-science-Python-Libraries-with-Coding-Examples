
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

pic = Image.open('desire.jpg') # import your pic name
type(pic_arr)

pic_arr =np.asanyarray(pic)  # transforming it to an array 
plt.imshow(pic_arr)
pic_arr.shape


pic_red = pic_arr.copy()
plt.imshow(pic_red[:,:,0], cmap = 'gray')
plt.imshow(pic_red[:,:,1], cmap = 'gray')
plt.imshow(pic_red[:,:,2], cmap = 'gray')
