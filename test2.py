from tkinter import *
from tkinter import messagebox
class demo2(Toplevel):
    def msg(self):
        messagebox.showwarning("","hello")
    def __init__(self,parent):
        self.win=Toplevel(parent)
        self.win.transient(parent)
        self.win.parent = parent
        Button(self.win,text="Model PopUp",command=self.msg).pack()

        self.win.mainloop()

if __name__ == '__main__':
    demo2()