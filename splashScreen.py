from tkinter.font import BOLD
import time
from restaurantLogin import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from shutil import copyfile
from os import path
from pathlib import Path
# pip install pyttsx3 pypiwin32
from tkinter import ttk
from pygame import mixer


class splashscreen:
    def start(self):
        self.progress1["value"] = 0
        self.maxbytes = 100
        self.progress1["maximum"] = 100
        self.read_bytes()
    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 1
        abc = "Loading.... (" + str(self.bytes // 1) + "%)"
        self.lb_blank.config(text=abc)
        self.progress1["value"] = self.bytes
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.root.after(50, self.read_bytes)
        else:
            #mixer.music.stop()

            if __name__ == '__main__':
                self.root.destroy()
                obj=restaurantLogin()


    def __init__(self):
        self.root=Tk()

        print("Start Time")
        print(time.time())
        # self.root.geometry("{0}x{0}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        # self.root.resizable(0, 0)
        self.root.attributes('-fullscreen',True)
        mixer.init()
        mixer.music.load('audio/fireSoundTrim.mp3')
        mixer.music.play()
        self.root.config(background="#ccffcc")
        self.a = Image.open("splashScreen/indianSpice.png").resize((1400, 680), Image.ANTIALIAS)
        dp = ImageTk.PhotoImage(self.a)
        self.lbphoto=Label(self.root,image=dp,bg='#9c004f')
        self.lb_blank = Label(self.root, text="",bg="white")
        self.progress1 = ttk.Progressbar(self.root, orient="horizontal", length=500, mode="determinate")
        self.ls=Label(self.root,text="Restaurant Mania",bg="white")
        self.ls.configure(font=("Helvetica", 18))
        self.lbphoto.grid(row=0,column=0,columnspan=7)
        self.ls.grid(row=6,column=0)
        self.lb_blank.grid(row=8,column=1)
        self.progress1.grid(row=9,column=0)

        self.bytes = 0
        self.start()
        print("TIME:")
        print(time.time())
        self.root.mainloop()
obj=splashscreen()