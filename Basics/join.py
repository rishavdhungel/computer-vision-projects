import cv2
import numpy as np
img = cv2.imread("Resources/card.jpg")
horimg = np.hstack((img,img))
cv2.imshow("horizontal stack", horimg)
verticalimg = np.vstack((horimg,horimg))
cv2.imshow("vertical stack",verticalimg)


cv2.waitKey(0)