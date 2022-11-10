import cv2
import numpy as np
path = "Resources/card.jpg"
img = cv2.imread(path)
height, width = img.shape[:2]


#image rotation

#takes center,angle,scale as a parameter
#warpAffine() applies affine transformation to image
#warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]])
def rotate():

    center = (width/2,height/2)
    rotate_matrix = cv2.getRotationMatrix2D(center = center, angle=45, scale=1)

    #rotating the image using warpaffine matrix
    rotated_image = cv2.warpAffine(src=img,M=rotate_matrix, dsize=(width,height))
    cv2.imshow("original image",img)
    cv2.imshow("Rotated image",rotated_image)

    cv2.waitKey(0)

    cv2.imwrite("Resources/rotatedcard.jpg",rotated_image)

# rotate()

def translate():
    img = cv2.imread(path)
    tx,ty = width/4, height/4
    translation_matrix = np.array([
        [1,0,tx],
        [0,1,ty]],dtype=np.float32)
    translated_image = cv2.warpAffine(src=img,M=translation_matrix,dsize=(width,height))
    cv2.imshow("original image", img)
    cv2.imshow("Translated image", translated_image)

    cv2.waitKey(0)

    cv2.imwrite("Resources/translatedcard.jpg", translated_image)

# translate()