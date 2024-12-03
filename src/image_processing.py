'''Module designed for image processing and enable the cropping the chest area'''

# code to read an image an transform into grayscale
import cv2
import numpy as np

img_path = "hello.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
cv2.imsave("out/img.png", img)

