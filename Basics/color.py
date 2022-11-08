import cv2
import numpy as np

path = "Resources/flower.jpg"
img = cv2.imread(path)
resizedimg = cv2.resize(img,(400,600))

hsvimg = cv2.cvtColor(resizedimg,cv2.COLOR_BGR2HSV)
# cv2.imshow("Flower Original",resizedimg)
# cv2.imshow("HSV Image",hsvimg)
grayimg = cv2.cvtColor(resizedimg,cv2.COLOR_BGR2GRAY)
combinedhsv = np.hstack((resizedimg,hsvimg))
# combinedgray = np.hstack((resizedimg,grayimg))
# cv2.imshow("Comparision", combinedhsv)
# allcombined = np.vstack((?combinedhsv,combinedgray))
cv2.imshow("allcombined",combinedhsv)
cv2.waitKey(0)