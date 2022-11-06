import cv2
# #image capture
def imageCapture():
    img = cv2.imread("Resources/opencvlogo.png")
    cv2.imshow("Opencvlogo",img)
    cv2.waitKey(0)

#video capture
def videoCapture():
    videocap = cv2.VideoCapture("Resources/video.mp4")
    while True:
        success, video = videocap.read()
        cv2.imshow("Video Window",video)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Video by RODNAE Productions: https://www.pexels.com/video/astronauts-looking-around-in-a-desolate-area-8474604/

#webcam capture
def webCamCapture():

    cam = cv2.VideoCapture(0)

    while True:
        success, img = cam.read()
        cv2.imshow("camera", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

webCamCapture()
# videoCapture()
# imageCapture()