from tkinter import *
from tkinter.messagebox import *
from connection import *
from pygame import mixer
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from PyQt5 import QtGui



class addMenu:
    def reset(self):
        self.itemText.delete(0,END)
        self.descText.delete(0.0, END)
        self.priceText.delete(0,END)


    def preCheck(self):
        cur=con.cursor()
        query="select * from menu where name='"+self.item+"'"
        cur.execute(query)
        data=cur.fetchone()
        if data==None:
            self.insertData()
        else:
            message="Menu "+self.item+" Already Exists!"
            if True:

                showinfo("",message)



    def insertData(self):

        cur=con.cursor()
        query='insert into menu(name,description,price) values("'+self.item+'","'+self.description+'",'+self.price+')'
        print(query)
        cur.execute(query)
        con.commit()
        if True:
            showinfo("","DATA INSERTED!")
        self.reset()





    def addMenuFun(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.item=(self.itemText.get())
        self.description=self.descText.get(0.0,END)
        self.price=self.priceText.get()

        '''VALIDATION'''
        if len(self.item)<1 and len(self.description)<1 and self.price=="":
            showinfo("","Fill The ADD MENU FORM!")



        elif len(str(self.item).strip())<1 :
            showinfo("","Fill Item!")
        elif len(str(self.description).strip())<1:
            showinfo("","Fill Description!")
        elif len(str(self.price).strip())<1:
            showinfo("","Fill Price Field!")
        else:
            if (str(self.price).strip()).isnumeric() :
                self.preCheck() #PRE CHECK BEFORE INSERTING DATA
            else:
                showinfo("","Invalid Price!")






    def __init__(self,parent):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent
        #self.root.attributes("-fullscreen", True)

        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.resizable(0, 0)
        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")

        #self.root.overrideredirect(1)  ---REMOVES ALL ABOVE MINIMIZE MAXIMIZE BUTTON


        '''WINDOW CONSTRUCTION'''


        self.root.title("ADD MENU!")
        self.root.iconbitmap("i.ico")


        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())

        '''FOR MAKING SCREEN TRASPARENT'''
        #self.root.wm_attributes("-transparentcolor", "white")

        '''LABEL IMAGE CONSTRUCTION'''
        '''
        canvas.image = PhotoImage(file="splashScreen/shadow.png")
        addMenuLabel=Label(canvas,fg="white",image=canvas.image ,text="HELLLLLLLLLL",font=("Harlow Solid ",20,"bold"),width=332,height=30)
        label=Label(addMenuLabel,text="Description",bg="#9c004f",font=("Script MT Bold",15,"bold"))
        label.pack()

        addMenuLabel['bg']=addMenuLabel.master['bg']
        self.frame1=PanedWindow(self.root)
        '''



        '''CANVAS'''
        self.frameCanvas=PanedWindow(self.root)
        self.canvas = Canvas(self.frameCanvas,width=200, height=100,relief="raised")


        gif1 = PhotoImage(file="splashScreen/food1.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)


        frame1=PanedWindow(self.canvas)
        frame1.config(bg="#9c004f")
        frame1.config(width=1200)

        space=Label(self.canvas)
        space.grid(row=0,column=0,padx=10,pady=10)

        addMenuLabel=Label(frame1 ,text="ADD MENU",fg="#9c004f",font=("Harlow Solid",20,"bold"),width=40,height=1)

        itemLabel=Label(frame1,text="Item Name",fg="#9c004f" , font=("Script MT Bold",15,"bold"))
        self.itemText=Entry(frame1,bd=1,relief="groove",bg="white",font=("calibri",15),width=60)
        descLabel=Label(frame1,text="Description",fg="#9c004f",font=("Script MT Bold",15,"bold"))
        self.descText=Text(frame1,bd=1,height=8,bg="#ffffff",relief="groove",font=("calibri",15),width=60)
        priceLabel=Label(frame1,text="Price",fg="#9c004f",font=("Script MT Bold",20,"bold"),width=4)
        self.priceText=Entry(frame1,bd=1,bg="#ffffff",relief="groove",font=("calibri",15),width=60)
        addBtn=Button(frame1,text="Add Menu",relief="raised",command=self.addMenuFun,bg="white",fg="#9c004f",font=("Script MT Bold",15,"bold"),activebackground="#9c004f")
        addMenuLabel.grid(row=0,column=1,padx=115,pady=15)
        itemLabel.grid(row=1,column=0,padx=115,pady=25)
        self.itemText.grid(row=1, column=1,padx=115,pady=25)
        descLabel.grid(row=2, column=0,padx=115,pady=25)
        self.descText.grid(row=2, column=1,padx=115,pady=25)

        priceLabel.grid(row=3, column=0,padx=115,pady=25)
        self.priceText.grid(row=3, column=1,padx=115,pady=25)

        addBtn.grid(row=4, column=1,padx=115,pady=25)
        frame1.grid(row=0,column=0,padx=85,pady=85)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.frameCanvas.pack()
        self.root.mainloop()


#obj=addMenu()

