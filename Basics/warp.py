import cv2
import  numpy as np

img = cv2.imread("Resources/card.jpg")
# resizedimg = cv2.resize(img,(400,700))
#define four corner point
width, height = 250,350
point1 = np.float32([[265,61],[504,108],[178,339],[442,402]])
point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(point1,point2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("card image",img)
cv2.imshow("output",imgOutput)
cv2.waitKey(0)
