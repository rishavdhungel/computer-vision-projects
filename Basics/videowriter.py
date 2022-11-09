import cv2
import numpy as np

path = "Resources/video.mp4"
outpath = "Resources/output.avi"

video_capture = cv2.VideoCapture(path)
#getting frame size info using .get() 3 is for fame_width and 4 is for frame_height
frame_width = int(video_capture.get(3))
frame_height = int(video_capture.get(4))
frame_size = (frame_width,frame_height)
fps = 20

#VideoWriter() class is used for writing purpose
#takes filename, apiPreference, Fourcc,fps, frameSize[,isColor])
#video codec specifies how video stream is compressed
# AVI = cv2.VideoWriter_fourcc('M','J','P','G')
# MP4 = cv2.VideoWriter_fourcc(*'XVID')

#initializing video writer object
output = cv2.VideoWriter(outpath,cv2.VideoWriter_fourcc('M','J','P','G'),20,frame_size)

while(video_capture.isOpened()):
    success, frame = video_capture.read()
    if success == True:
        output.write(frame)
    else:
        print("Stream disconnected")
        break

