from tkinter import *
from PIL import ImageTk,Image
import time
from threading import Thread
wn=""
class imagedemo2:
    def __init__(self):
        self.window = Tk()

        self.window.title("Join")
        self.window.geometry("500x600")
        worker().start()
        self.window.configure(background='grey')
        self.window.mainloop()
class worker(Thread):
    def run(self):
        lst = [ "splashScreen/dish.jpg", "splashScreen/forkFruit.jpg",
               "splashScreen/juice.jpg", "splashScreen/vegBurger.jpg", "splashScreen/vegImage.jpg", "splashScreen/wine.jpg"]
        i = 1


        while(TRUE):
            img = ImageTk.PhotoImage(Image.open(lst[i]))
            i=i+1
            self.lb1 = Label(wn, image=img)
            self.lb1.grid(row=1, column=2)
            self.lb1.place(x=20, y=20)
            time.sleep(2)
            if i==6:
                i=1

x=imagedemo2()
