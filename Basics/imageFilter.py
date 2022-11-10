import cv2
import numpy as np
path = "Resources/card.jpg"
img = cv2.imread(path)
#convolution kernels
#using kernels to sharpen or blur images
#convolution kernel is a 2D matrix that is used to filete images also known as convolution matrix
#convolution matrix are typically a square MxN matrix, where both M and N are odd integers
#3x3,5x5,7x7

#applying identity kernel to image
def identitykernel():
    #identity kernel has middle element 1 and rest are zero
    #read the image
    #define 3x3 np array
    i_kernel = np.array([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ])
    #use filter2D(src, ddepth, kernel) for linear filter operation
        #ddepth indicated the depth of the resulting image
    i_filtered = cv2.filter2D(src=img,ddepth=-1,kernel=i_kernel)
    cv2.imshow("Original",img)
    cv2.imshow("Identity",i_filtered)
    cv2.waitKey(0)
    #show and write image
    cv2.imwrite("Resources/identityFiltered.jpg",i_filtered)

# identitykernel()

#blur kernel
#5x5 kernel

def blurkernel():
    #define kernel
    blur_kernel = np.ones((5,5),np.float32)/25
    #dividing kernel by 25 ensures that all values are normalized as it ensures all values stays within the range of [0,1]
    blurredimg = cv2.filter2D(src=img,ddepth=-1,kernel=blur_kernel)
    cv2.imshow('Original',img)
    cv2.imshow("Blurred",img)

    cv2.waitKey(0)
    cv2.imwrite("Resources/blurredimage.jpg",blurredimg)

# blurkernel()

#using OpenCV's builtin function to blur
def builtinblur():
    img_blur1 = cv2.blur(src=img,ksize=(5,5))
    #gaussianblur
    img_blur2 = cv2.GaussianBlur(src=img,ksize=(5,5),sigmaX=0,sigmaY=0)
    #medianblur
    img_blur3 = cv2.medianBlur(src=img,ksize=5)

    cv2.imshow("original",img)
    cv2.imshow("blur 1", img_blur1)
    cv2.imshow("Gaussian Blur",img_blur2)
    cv2.imshow("Median Blur", img_blur3)

    cv2.waitKey(0)
    cv2.imwrite("Resources/img_blur1.jpg", img_blur1)
    cv2.imwrite("Resources/Gaussianblur.jpg",img_blur2)
    cv2.imwrite("Resources/Medianblur.jpg",img_blur3)

# builtinblur()

#sharpening an image with custom 2D convolution
def sharpen():
    #commonly used kernels:
        # https: // en.wikipedia.org / wiki / Kernel_(image_processing)
    kernel1 = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
    ])
    sharpen_img = cv2.filter2D(src=img,ddepth=-1,kernel=kernel1)
    cv2.imshow("Oringinal",img)
    cv2.imshow("Sharpened",sharpen_img)

    cv2.waitKey(0)
    cv2.imwrite("Resources/sharp.jpg",sharpen_img)

# sharpen()
#bialateral filtering ...
