import cv2
import  numpy as np

img = cv2.imread("Resources/card.jpg")
# resizedimg = cv2.resize(img,(400,700))
#
cv2.imshow("card image",img)
cv2.waitKey(0)
