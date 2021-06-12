import tkinter
import tkinter
from tkinter.constants import NW
import cv2
import PIL.Image  
import PIL.ImageTk
from functools import partial
import threading
import imutils
import time


SET_WIDTH =700
SET_HEIGHT=350

stream=cv2.VideoCapture("Video.mp4")

def play(speed):
    print(f"You clicked on play{speed}")
    
    fram1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,fram1+speed)

    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)
    
    
    
def pending(decision):
    frame=cv2.cvtColor(cv2.imread("stadium-des.png"), cv2.COLOR_BGR2RGB )
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)

    time.sleep(1)
    
    frame=cv2.cvtColor(cv2.imread("Such a goat.jpg"), cv2.COLOR_BGR2RGB )
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)
    
    time.sleep(1.5)
    
    if decision=='out':
        decisionImg='stadium-out.png'
    else:
        decisionImg="stadium-notout.png"
    
    frame=cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB )
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW,image=frame)
        
    
    
def out():
    
    thread=threading.Thread(target=pending,args=("out",))
    thread.daemon=1
    thread.start()
    print("Player is out")
    
def notout():
    
    thread=threading.Thread(target=pending,args=("not out",))
    thread.daemon=1
    thread.start()
    print("Player is not out")
    
    
window=tkinter.Tk()
window.title('DRS')
cv_img=cv2.cvtColor(cv2.imread("stadium-welcome.png"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack() 

#Buttons

btn=tkinter.Button(window,text="<<Previous(slow)",width=50,command=partial(play,-2))
btn.pack()
btn=tkinter.Button(window,text="<<Previous(fast)",width=50, command=partial(play,-50))
btn.pack()
btn=tkinter.Button(window,text="Next(slow)>>",width=50,command=partial(play,2))
btn.pack()
btn=tkinter.Button(window,text="Next(fast)>>",width=50,command=partial(play,50))
btn.pack()
btn=tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()
btn=tkinter.Button(window,text="Give Not Out",width=50,command=notout)
btn.pack()
window.mainloop()






