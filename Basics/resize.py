import  cv2
import numpy as np

img = cv2.imread("Resources/flower.jpg")
print(img.shape)

def resize():

    cv2.imshow("flowere pic",img)

    imgResize = cv2.resize(img,(400,500))
    cv2.imshow("resized",imgResize)
    cv2.waitKey(0)

def crop():
    imgCropped = img[0:200,300:700]
    cv2.imshow("cropped",imgCropped)
    cv2.waitKey(0)
# crop()
# resize()