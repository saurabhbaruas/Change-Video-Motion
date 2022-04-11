import ffmpeg
from tkinter import *
from tkinter.filedialog import askopenfile
import tkinter.messagebox
import cv2

content = ""
NAME = ""


def convert_slow():
    flag1 = True
    file = askopenfile(mode='r', title="Choose a Video file.")
    fileName = file.name
    cap = cv2.VideoCapture(fileName)
    if(cap.isOpened() == False):
        print("Error reading video file")
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter(
        NAME.get()+'.avi', cv2.VideoWriter_fourcc(*'MJPG'), 5, size)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            result.write(frame)
           # cv2.imshow('frame',frame)
            if flag1:
                tkinter.messagebox.showinfo(
                    "Task Completed.", "Video Conversion Done.\n\nYour Slow Motion Video is Saved.")
                flag1 = False
            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(0) == 27:
                break
        else:
            break
    cap.release()
    result.release()
    cv2.destroyAllWindows()


def convert_fast():
    flag2 = True
    file = askopenfile(mode='r', title="Choose a Video file.")
    fileName = file.name
    cap = cv2.VideoCapture(fileName)
    if (cap.isOpened() == False):
        print("Error reading video file")
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter(
        NAME.get()+'.avi', cv2.			VideoWriter_fourcc(*'MJPG'), 230, size)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            result.write(frame)
            if flag2:
                tkinter.messagebox.showinfo(
                    "Task Completed.", "Video Conversion Done. \n\nYour Tine-Lapsed video has  been saved successfully.")
                flag2 = False
            if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(0) == 27:
                break
        else:
            break
    cap.release()
    result.release()
    cv2.destroyAllWindows()


window = Tk()
window.title("Video Manupilation Project by SAURABH")
window.geometry('600x400')

lbl2 = Label(window, text=" Slow-Mo & Time-Lapse",
             font=('lato black', 17, 'bold'), fg='red')
lbl2.grid(column=0, row=0)
lbl2 = Label(window, text=" of Vidwo using python",
             font=('lato black', 17, 'bold'), fg="red")
lbl2.grid(column=0, row=1)

lbl2 = Label(window, text="", font=('lato black', 30, 'bold'), fg="red")
lbl2.grid(column=0, row=2)

lbl2 = Label(window, text="Output Video Name: ",
             font=('lato black', 12, 'bold'))
lbl2.grid(column=0, row=3)

NAME = Entry(window, textvariable=NAME, font=('lato black', 12, 'normal'))
NAME.grid(column=1, row=3)

lbl2 = Label(window, text="", font=('lato black', 12, 'normal'))
lbl2.grid(column=0, row=4)

btn = Button(window, font=('lato', 13, 'bold'), text="Convert Slow-Mo",
             padx=2, pady=2, bg="#703c0d", fg="white", command=lambda: convert_slow())
btn.grid(column=0, row=5)
btn2 = Button(window, font=('lato', 13, 'bold'), text="Convert Lime-Lapse",
              padx=2, pady=2, bg="#703c0d", fg="white", command=lambda: convert_fast())
btn2.grid(column=1, row=5)


window.mainloop()
