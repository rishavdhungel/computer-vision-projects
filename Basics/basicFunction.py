import cv2
import numpy as np

img = cv2.imread("Resources/opencvlogo.png")
kernel = np.ones((5,5),np.uint8)

def showimg(imgname, img):
    cv2.imshow(imgname, img)
    cv2.waitKey(0)


def colorcvt():
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    showimg("Gray Image",imgGray)
def blur():
    imgBlur = cv2.GaussianBlur(img,(5,5),2) # use odd for ksize
    showimg("blurredImage",imgBlur)
def edgeDetect():
    imgCanny = cv2.Canny(img, 100,100)
    showimg("edge detect", imgCanny)

def dilation():
    imgCanny = cv2.Canny(img, 100,100)
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
    showimg("dilation", imgDilation)
def erosen():
    imgCanny = cv2.Canny(img, 100,100)
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
    imgEroded = cv2.erode(imgDilation,kernel,iterations=1)
    showimg("Eroded",imgEroded)
# blur()
# colorcvt()
# edgeDetect()
# dilation()
# erosen()