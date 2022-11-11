import cv2
import numpy as  np

path = "Resources/card.jpg"

image = cv2.imread(path)

#contour helps to detect the borders of the objects, localize them easily
#can be implemented by using findContours() and drawContours()
    #algorithm for contour detection are
        #CHAIN_APPROX_SIMPLE
        #CHAIN_APPROX_NONE

#stepsL
#1. convert image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#2. apply binary thresholding
ret, thresh = cv2.threshold(image_gray,150,255, cv2.THRESH_BINARY)
# cv2.imshow("Binary Thresholding",thresh)
#3. Find contours
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_NONE)
#4. Draw contours on original RGB
image_copy = image.copy()
cv2.drawContours(image=image_copy,contours=contours,contourIdx=-1,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)
cv2.imshow("None approximation", image_copy)
cv2.imwrite("contourIMage.jpg",image_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()

