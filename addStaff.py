from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from PIL import ImageTk,Image
from pygame import mixer

from connection import *
import re

class addStaff:
    def isValidEmail(self,email):
        if len(email) > 5 and len(email)<200:

                return True
        return False

    def reset(self):
       self.nameText.delete(0,END)
       self.emailText.delete(0,END)
       self.mobileText.delete(0,END)
       self.passwordText.delete(0,END)
       self.passwordText1.delete(0, END)
       self.staffCombo.set("")




    def insertData(self):

        '''INSERT INTO STAFF DATABASE'''

        cur=con.cursor()
        query='insert into staff values("'+self.name+'","'+self.email+'","'+self.mobile+'","'+self.password+'","'+self.staffType+'")'
        print(query)
        cur.execute(query)
        con.commit()
        showinfo("","Data Inserted")

        self.reset()


    def duplicateCheck(self):
        cur=con.cursor()
        query='Select * from staff where email="'+self.email+'"'
        cur.execute(query)
        self.check=cur.fetchone()
        if self.check==None:
            self.insertData()
        else:
            message=self.email +" ALREADY EXISTS!"
            showinfo("",message)

    def addStaffFun(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.name=self.nameText.get()
        self.email=self.emailText.get()
        self.mobile=self.mobileText.get()
        self.password=self.passwordText.get()
        self.staffType=self.staffCombo.get()

        '''VALIDATION'''
        if len(self.name)<1 :
            showinfo("","Name Not Filled")

            if  str(self.name).isnumeric() or str(self.name).isalnum():
                showinfo("","Invalid Name!")
        else:
            if len(self.email)<1 :
                showinfo("","Email Field Is Empty")
            else:
                if self.isValidEmail(self.email) == False:
                   showinfo("","Invalid Email!")
                else:
                    if len(self.mobile)<1:
                        showinfo("","Fill Mobile No.")
                    else:
                        if len(self.mobile)!=10:
                            showinfo("","Invalid Mobile Number")
                        else:
                            if len(self.password)<1:
                                showinfo("","Fill Password!")
                            else:
                                if len(self.password)<6:
                                    showinfo("","Password Must Be Atleast 6 Letter Long! ")
                                else:
                                    if self.password!=self.passwordText1.get():
                                        showinfo("","Confirm Password Doesnot Match with Password")
                                    else:
                                        if len(self.staffType)<1:
                                            showinfo("","Staff Type Not Selected")
                                        else:
                                            self.duplicateCheck()

    def comboStyling(self):
        self.style.map('TCombobox', activebackground=[('readonly', '#89105f')],
                       fieldbackground=[('readonly', '#89105f')])

    def __init__(self,parent):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent
        #self.root.attributes("-fullscreen", True)

        self.root.iconbitmap("chef.ico")
        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.config(bg="#89105f", highlightthickness=20, highlightbackground="#89105f", highlightcolor="#89105f")
        self.root.title("ADD STAFF")
        self.root.resizable(0, 0)
        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())

        '''CANVAS'''
        self.frameCanvas=PanedWindow(self.root)

        self.canvas = Canvas(self.frameCanvas,width=width_value, height=height_value, bg='#9c004f',relief="raised")
        self.canvas.pack(expand=YES, fill=BOTH)


        '''ADD STAFF PHOTO'''
        self.frame0 = PanedWindow(self.canvas)
        self.frame0.config(bg="#89105f",relief="raised")
        image = Image.open("splashScreen/addStaff.jpg")
        photo = ImageTk.PhotoImage(image)
        updateLabel = Label(self.frame0, image=photo, bg="#89105f")
        updateLabel.grid(row=0, column=0, padx=10, pady=10)

        self.frame1=PanedWindow(self.canvas)
        self.frame1.config(bg="#89105f")
        nameLabel=Label(self.frame1,text="NAME",bg="#89105f",fg="white",font=("calibri",25),width=20)
        emailLabel = Label(self.frame1, text="EMAIL",bg="#89105f",fg="white",font=("calibri",25),width=20)
        mobileLabel = Label(self.frame1, text="MOBILE",bg="#89105f",fg="white",font=("calibri",25),width=20)
        passwordLabel = Label(self.frame1, text="PASSWORD",bg="#89105f",fg="white",font=("calibri",25),width=20)
        passwordLabel1 = Label(self.frame1, text="CONFIRM PASSWORD",bg="#89105f",fg="white",font=("calibri",25),width=20)
        staffTypeLabel = Label(self.frame1, text="STAFF TYPE",bg="#89105f",fg="white",font=("calibri",25),width=20)

        self.nameText=Entry(self.frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=25)
        self.emailText=Entry(self.frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=25)
        self.mobileText=Entry(self.frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=25)
        self.passwordText=Entry(self.frame1,show="*",bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=25)
        self.passwordText1=Entry(self.frame1,show="*",bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=25)
        self.staffCombo=ttk.Combobox(self.frame1,values=["CASHIER","KITCHEN"],state="readonly",width=30)
        self.style = ttk.Style()
        self.staffCombo.bind('<<ComboboxSelected>>',lambda event: self.comboStyling())

        addStaffBtn=Button(self.frame1,text="ADD STAFF",command=self.addStaffFun,bg="white",fg="#89105f",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)
        self.frame1.config(bg="#89105f")




        nameLabel.grid(row=0,column=0,padx=10,pady=10)
        emailLabel.grid(row=1,column=0,padx=10,pady=10)
        mobileLabel.grid(row=2,column=0,padx=10,pady=10)
        passwordLabel.grid(row=3,column=0,padx=10,pady=10)
        passwordLabel1.grid(row=4,column=0,padx=10,pady=10)
        staffTypeLabel.grid(row=5,column=0,padx=10,pady=10)
        self.nameText.grid(row=0,column=1,padx=10,pady=10)
        self.emailText.grid(row=1,column=1,padx=10,pady=10)
        self.mobileText.grid(row=2,column=1,padx=10,pady=10)
        self.passwordText.grid(row=3,column=1,padx=10,pady=10)
        self.passwordText1.grid(row=4,column=1,padx=10,pady=10)
        self.staffCombo.grid(row=5,column=1,padx=10,pady=10)

        addStaffBtn.grid(row=6,column=1,padx=10,pady=10)

        self.frame0.grid(row=0,column=0,padx=85,pady=85)
        self.frame1.grid(row=0,column=0,padx=85,pady=85)

        self.canvas.pack(expand=YES, fill=BOTH)
        self.frameCanvas.pack()
        self.root.mainloop()


#obj=addStaff()