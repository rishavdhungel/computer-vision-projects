import cv2
import numpy as np

path ="Resources/card.jpg"
img = cv2.imread(path)

cv2.imshow("Origninal Image",img)

#convert to gray
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(grayimg,(7,7),1)
imgcombined = np.hstack((grayimg,imgBlur ))
cv2.imshow("Image",imgcombined)
imgCanny = cv2.Canny(imgBlur,50,50)
cv2.imshow("cannyimg",imgCanny)



cv2.waitKey(0)