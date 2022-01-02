import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
global last_frame1 #global variable to store the last frame
last_frame1 = np.zeros((480,640,3), np.uint8)
global last_frame2 #global variable to store the last frame
last_frame2 = np.zeros((480,640,3), np.uint8)
global cap1 #global variable to store the video capture object
global cap2 #global variable to store the video capture object
cap1=cv2.VideoCapture("./videos/video1.mp4") #Change the path to your video file
cap2=cv2.VideoCapture("./videos/video2.mp4") #Change the path to your video file
def show_vid():
    if not cap1.isOpened():
        print("Error opening video stream or file")
    flag1, frame1 = cap1.read()
    frame1=cv2.resize(frame1,(640,480))
    if flag1 is None:
        print("No frame read")
    elif flag1:
        global last_frame1
        last_frame1=frame1.copy()
        pic=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(pic)
        imgtk=ImageTk.PhotoImage(image=img)
        lmain1.imgtk=imgtk  #Shows frame for first video
        lmain1.configure(image=imgtk)
        lmain1.after(10,show_vid)
def show_vid2():
    if not cap2.isOpened():
        print("Error opening video stream or file")
    flag2, frame2 = cap2.read()
    frame2=cv2.resize(frame2,(640,480))
    if flag2 is None:
        print("No frame read")
    elif flag2:
        global last_frame2
        last_frame2=frame2.copy()
        pic=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(pic)
        imgtk=ImageTk.PhotoImage(image=img)
        lmain2.imgtk=imgtk  #Shows frame for second video
        lmain2.configure(image=imgtk)
        lmain2.after(10,show_vid2)
if __name__ == '__main__':
    root=tk.Tk()
    img=ImageTk.PhotoImage(Image.open("logo.png"))
    heading=Label(root,image=img,bg="black",text="Video Comparison",fg="white",font=("Helvetica",20))
    #heading.pack(background="black",fill=BOTH)
    heading.pack()
    heading2=Label(root,pady=20,text="Video 1",font=("Helvetica",20))

    heading2.configure(background="black",fg="white")
    heading2.pack()
    lmain1=tk.Label(master=root)
    lmain2=tk.Label(master=root)

    lmain1.pack(side=LEFT)
    lmain2.pack(side=RIGHT)
    root.title("Lanne Detector")
    root.geometry("1280x720")

    exitbutton=Button(root,text="Exit",command=root.destroy,font=("Helvetica",20),fg="red").pack(side=BOTTOM)
    show_vid()
    show_vid2()
    root.mainloop()
    cap1.release()