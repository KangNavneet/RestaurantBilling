from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from pygame import mixer
from PIL import ImageTk,Image

from connection import *
from tkinter.font import *
import tkinter as tki
import tkinter.scrolledtext as scroll

class updateMenu:

    def fetchDataCombo(self):
        cur = con.cursor()
        query = "select * from menu "

        cur.execute(query)
        data = cur.fetchall()
        print(data)

        self.menuList = []

        for record in data:
            print(record)
            self.menuList.append(record[1])

        self.menuList=tuple(self.menuList)

    def reset(self):
        self.itemText.delete(0,500)
        self.descText.delete(0.0, 500.0)
        self.priceText.delete(0, 100)

    def getDetail(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.reset()
        self.cb=self.comboBox.get()
        if len(str(self.cb))<1:
            showinfo("Message","Combobox Not Selected",bg="red",fg="green")
        else:
            cur=con.cursor()
            query="select * from menu where name='"+self.cb+"'"
            cur.execute(query)
            data=cur.fetchall()
            print(data[0][1])

            print(data[0][3])
            self.itemText.insert(0,data[0][1])

            self.priceText.insert(0,data[0][3])
            self.descText.insert(0.0, str(data[0][2]))
            print(data[0][2])



    def updateMenu(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.item = self.itemText.get()
        self.description = self.descText.get(0.0, END)
        self.price = self.priceText.get()

        self.priceStrip=str(self.price).split(".")
        print("Price")

        '''VALIDATION'''
        if len(self.item)<1 and len(self.description)<1 and self.price=="":
            showinfo("", "Fill The ADD MENU FORM!")
        elif len(self.item) < 1:
            showinfo("", "Fill Item!")
        elif len(self.description) < 1:
            showinfo("", "Fill Description!")
        elif len(str(self.price)) < 1:
            showinfo("", "Fill Price Field!")

        else:
            self.flag = True
            for i in range(0, len(self.priceStrip)):

                if not str(self.priceStrip[i]).isdigit():
                    self.flag=False
            if self.flag or str(self.price).isdigit():

                cur=con.cursor()
                query='Update menu set name="'+self.item+'",description="'+self.description+'",price='+str(self.price) +' where name="'+self.cb+'"'
                print(query)
                cur.execute(query)
                con.commit()
                showinfo("Message ","Data Updated")

            else:
                showinfo("Message","Price should be Numeric")


    def comboStyling(self):
        '''COMBOBOX STYLING'''
        '''
        self.style.map('TCombobox', activeforeground=[('readonly', 'red')])

        self.style.map('TCombobox', selectbackground=[('readonly', '#89105f')])
        self.style.map('TCombobox', fieldbackground=[('readonly', '#ffffff')])
        self.style.map('TCombobox', background=[('readonly', '#89105f')])
        '''
        self.style.map('TCombobox', activebackground=[('readonly', '#89105f')],fieldbackground=[('readonly', '#89105f')])




    def __init__(self,parent):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent

        self.root.title("UPDATE MENU")
        self.root.config(bg="#89105f", highlightthickness=20, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.resizable(0, 0)
        self.root.iconbitmap("glass.ico")
        self.root.resizable(0, 0)

        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)
        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())

        '''UPDATE LABEL PHOTO'''
        self.frame0=PanedWindow(self.root)
        self.frame0.config(bg="#89105f")
        image = Image.open("splashScreen/updateMenu.jpg")
        photo=ImageTk.PhotoImage(image)
        updateLabel = Label(self.frame0, image=photo, bg="#89105f")
        updateLabel.grid(row=0, column=0, padx=10, pady=10)
        self.frame0.pack()

        self.frame1=PanedWindow(self.root)
        self.frame1.config(bg="#89105f")
        self.fetchDataCombo()


        self.comboBox=ttk.Combobox(self.frame1, values=self.menuList, state="readonly",width=45)
        self.style = ttk.Style()
        '''
        REDUNDANCY STYLING !!!!
        self.style.theme_use('vista')
        self.style.configure("btn", bg="white",fg="#89105f",relief="raised",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)
        self.style.configure("label", bg="#89105f",fg="#ffffff",font=("calibri",22),width=15)
        self.style.configure("textEntry",bd=1,relief="groove",bg="#ffffff",font=("calibri",15),width=30)
        '''
        getDetailBtn=Button(self.frame1,text="Get Detail",command=self.getDetail,bg="white",fg="#89105f",relief="raised",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)
        itemLabel=Label(self.frame1,text="Item Name",bg="#89105f",fg="#ffffff",font=("calibri",22),width=15)
        self.itemText=Entry(self.frame1,bd=1,relief="groove",bg="#ffffff",font=("calibri",15),width=30)
        descLabel=Label(self.frame1,text="Description",bg="#89105f",fg="#ffffff",font=("calibri",22),width=15)
        self.descText=scroll.ScrolledText(self.frame1,bd=1,relief="groove",bg="#ffffff",font=("calibri",15),width=30,height=10)
        priceLabel=Label(self.frame1,text="Price",bg="#89105f",fg="#ffffff",font=("calibri",22),width=15)
        self.priceText=Entry(self.frame1,bd=1,relief="groove",bg="#ffffff",font=("calibri",15),width=30)
        updateBtn=Button(self.frame1,text="Update Menu",command=self.updateMenu,bg="white",fg="#89105f",relief="raised",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)
        menuLabel=Label(self.frame1,text="Select Menu",bg="#89105f",fg="#ffffff",font=("calibri",22),width=15)

        self.comboBox.bind('<<ComboboxSelected>>',lambda event: self.comboStyling())


        menuLabel.grid(row=0,column=0,padx=10,pady=10)
        self.comboBox.grid(row=0,column=1,padx=20,pady=20)
        getDetailBtn.grid(row=0,column=2,padx=10,pady=10)
        itemLabel.grid(row=1,column=0,padx=10,pady=10)
        self.itemText.grid(row=1, column=1,padx=10,pady=10)
        descLabel.grid(row=2, column=0,padx=10,pady=10)
        self.descText.grid(row=2, column=1,padx=10,pady=10)

        priceLabel.grid(row=3, column=0,padx=10,pady=10)
        self.priceText.grid(row=3, column=1,padx=10,pady=10)

        updateBtn.grid(row=4, column=1,padx=10,pady=10)
        self.frame1.pack()
        self.root.mainloop()

#obj=updateMenu()