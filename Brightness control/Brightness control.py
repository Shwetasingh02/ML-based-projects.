import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.Hands()
hands=mpHands.Hands()
mp.Draw=mp.solutions.drawing_utils
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2,COLOR_BGR2RGB)
    result=mpHands.prosess(imgRGB)
    lmList=[]
    if result.multi_hand_landmark:
        for handlandmark in result.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmarks):
                h,w,=img.shape[:2]
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
            mp.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    if lmList!=[]:
        x1,y1=lmList[4][1],lmList[4][2]
        x2,y2=lmList[5][1],lmList[5][2]
        cv2.circle(img,(x1,y1),4,(255,0,0),cv2.FILLED)
        cv2.circle(img,(x2,y2),4,(255,0,0),cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)
        length=hypot(x2-x1,y2-y1)
        bright=np.interp(length,[15,220],[0,100])
        print(bright,length)
        sbc.set_brightness(int(bright))
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
