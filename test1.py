from tkinter import *
from test2 import *
class demo1:
    def callpage(self):
        self.obj=demo2(self.root)
    def __init__(self):
        self.root=Tk()
        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))

        Button(self.root,text="Press", width=20,command=self.callpage).pack()

        self.root.mainloop()
if __name__ == '__main__':
    demo1( )