import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

prevTime = 0
currentTime = 0

while True:
    passed, cam = capture.read()
    imgRGB = cv2.cvtColor(cam, cv2.COLOR_BGR2RGB)
    output = hands.process(imgRGB)
    print(output.multi_hand_landmarks)
    if output.multi_hand_landmarks:
        for handslms in output.multi_hand_landmarks:
            for id, lm in enumerate(handslms.landmark):
                h,w,c = cam.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id ==0:
                    cv2.putText(cam, "WRIST", (cx,cy), cv2.FONT_HERSHEY_PLAIN,0.6,(50,250,50),1)
                if id ==1:
                    cv2.putText(cam, "THUMB_CMC", (cx,cy), cv2.FONT_HERSHEY_PLAIN,0.6,(50,250,50),1)
                if id ==2:
                    cv2.putText(cam, "THUMB_MCP", (cx,cy), cv2.FONT_HERSHEY_PLAIN,0.6,(50,250,50),1)
                if id ==3:
                    cv2.putText(cam, "THUMB_IP", (cx,cy), cv2.FONT_HERSHEY_PLAIN,0.6,(50,250,50),1)
                if id == 4:
                    cv2.putText(cam, "THUMB_TIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 5:
                    cv2.putText(cam, "INDEX_MCP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 6:
                    cv2.putText(cam, "INDEX_PIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 7:
                    cv2.putText(cam, "INDEX_DIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 8:
                    cv2.putText(cam, "INDEX_TIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 9:
                    cv2.putText(cam, "MIDDLE_MCP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 10:
                    cv2.putText(cam, "MIDDLE_PIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 11:
                    cv2.putText(cam, "MIDDLE_DIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 12:
                    cv2.putText(cam, "MIDDLE_TIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 13:
                    cv2.putText(cam, "RING_MCP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 14:
                    cv2.putText(cam, "RING_PIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 15:
                    cv2.putText(cam, "RING_DIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 16:
                    cv2.putText(cam, "RING_TIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 17:
                    cv2.putText(cam, "PINKY_MCP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 18:
                    cv2.putText(cam, "PINKY_PIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 19:
                    cv2.putText(cam, "PINKY_DIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                if id == 20:
                    cv2.putText(cam, "PINKY_TIP", (cx, cy), cv2.FONT_HERSHEY_PLAIN, 0.6, (50, 250, 50), 1)
                else:
                    print("hello")


            mpDraw.draw_landmarks(cam,handslms, mpHands.HAND_CONNECTIONS)

    currentTime = time.time()
    fps = 1/(currentTime - prevTime)
    prevTime = currentTime
    finalfps = "FPS:" + str(int(fps))

    cv2.putText(cam, finalfps,(10,75), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)
    cv2.imshow("Camera", cam)
    #waitKey(1) display a frame for 1 ms
    #  waitkey(0) will pause your screen as it will wait infinitely for keyPress on keyboard
    cv2.waitKey(1)