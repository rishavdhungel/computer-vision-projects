import  cv2
import numpy as np

img = cv2.imread("Resources/card.jpg")
height, width, channels = img.shape
print(height,width,channels)

def showimg(name,resizedimg):
    cv2.imshow(name, resizedimg)
    cv2.waitKey(0)
def resize(): #image resize using custom width and height

    cv2.imshow("Original",img)

    imgResize = cv2.resize(img,(400,500))
    showimg("custom wxh",imgResize)
def crop():
    imgCropped = img[0:200,300:700]
    showimg("Cropped", imgCropped)

# crop()
# resize()

#reducing the size require resampling of the pixels
#increasing size requires the reconstruction of the image(i.e interpolate new pixels)

#resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    #dsize:desired size
    #fx:Scale factor along the horizontal axis
    #fy:Scale factor along the vertical axis
    #interpolation: gives different methods of resizing image

#downscale
def downscale():
    d_width = 300
    d_height = 200
    d_points = (d_width,d_height)
    d_resized = cv2.resize(img, d_points,interpolation = cv2.INTER_LINEAR)
    showimg("downsized image", d_resized)

#Upscale
def upscale():
    u_width = 500
    u_height = 700
    u_points = (u_width,u_height)
    u_resized = cv2.resize(img,u_points,interpolation=cv2.INTER_LINEAR)
    showimg("Upscaled Image", u_resized)

#resizing with scale factor
def scalefactor():
    s_up = 1.2
    s_down = 0.6
    scaledup = cv2.resize(img, None, fx=s_up, fy=s_up,interpolation=cv2.INTER_LINEAR)
    scaledown = cv2.resize(img,None, fx=s_down, fy=s_down, interpolation= cv2.INTER_LINEAR)
    showimg("Scaled up by 1.2", scaledup)
    showimg("Scaled down by 0.6",scaledown)

def interpolationscale():
        s_up = 1.2
        s_down = 0.6
        inter_area = cv2.resize(img, None, fx=s_up, fy=s_up, interpolation=cv2.INTER_AREA)
        inter_cubic = cv2.resize(img, None, fx=s_down, fy=s_down, interpolation=cv2.INTER_CUBIC)
        inter_linear = cv2.resize(img, None, fx=s_up, fy=s_up, interpolation=cv2.INTER_LINEAR)
        inter_nearest = cv2.resize(img, None, fx=s_up, fy=s_up, interpolation=cv2.INTER_NEAREST)
        # showimg("INTER_AREA", inter_area)
        # showimg("INTER_CUBIC", inter_cubic)
        # showimg("INTER_LINEAR", inter_linear)
        # showimg("INTER_NEAREST", inter_nearest)

        #concatnate images
        vertical = np.concatenate((inter_nearest,inter_linear,inter_area),axis = 0)
        cv2.imshow("Interpolation",vertical)
        cv2.waitKey(0)

interpolationscale()
