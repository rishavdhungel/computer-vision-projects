import cv2

path = "Resources/video.mp4"
video_capture = cv2.VideoCapture(path)

#checking if the video is opened using isOpened() func
if(video_capture.isOpened()==False):
    print("Error in opening the video file")
else:
    fps = int(video_capture.get(5)) #5 corresponds to CAP_PROP_FPS
    print("Frame Rate: ", fps, "frames per second")

    frame_count = video_capture.get(7)#7 corresponds to CAP_PROP_FRAME_COUNT numeric value or name can be supplied
    #The get() method does not apply for the web cameras

    print("Frame Count: ",frame_count)

while(video_capture.isOpened()):
    #returns two tuple element, first is boolean and second is frame
    success, frame = video_capture.read()
    if success == True:
        cv2.imshow("Frame",frame)
        cv2.waitKey(1)
        if 0xFF == ord('q'):
            break


#release the object
video_capture.release()
cv2.destroyAllWindows()


