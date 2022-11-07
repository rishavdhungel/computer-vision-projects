import  cv2
import numpy as np
# img = cv2.imread("Resources/flower.jpg")
# resizedimg = cv2.resize(img, 500,700)

def showimg(imgname,finalimg):
    cv2.imshow(imgname,finalimg)
    cv2.waitKey(0)


#creating our own image
def createimg(x,y,channel,color):
    img = np.zeros((x,y,channel),np.uint8)
    #uint8: 8-bit unsigned integer (0 to 255). Most often this is used for arrays representing images, with the 3 color channels having small integer values (0 to 255)
    img[:] = color #whole image color
    cv2.line(img,(0,0),(600,600),(0,255,0),2)
    cv2.line(img,(0,600),(600,0),(0,255,0),2)
    cv2.line(img,(0,300),(600,300),(0,255,0),2)
    cv2.line(img,(300,0),(300,600),(0,255,0),2)
    cv2.line(img,(300,0),(600,300),(0,255,0),2)
    cv2.line(img,(0,300),(300,600),(0,255,0),2)

    cv2.rectangle(img,(300,300),(500,500),(255,0,0),2)
    cv2.rectangle(img,(100,100),(300,300),(255,0,0),cv2.FILLED)

    cv2.circle(img,(300,300),300,(0,0,255),2)

    cv2.putText(img,"OPEN CV",(120,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    showimg("image", img)


createimg(600,600,3,(0,0,0))

