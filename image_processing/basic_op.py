import numpy as np    
import cv2  
import matplotlib.pyplot as plt

image = cv2.imread('./images/lena.jpeg') ## returns an image file
print(image.shape,type(image)) ## stored as a numpy image


cv2.imshow('Hello World',image) ## title , image

cv2.waitKey() ## waits until any key is pressed
cv2.destroyAllWindows() ## closes all the windows