from tkinter import *
from tkinter.messagebox import showinfo

from PIL import ImageTk,Image
from pygame import mixer

from connection import *
class changePassword:
    def changePassFun(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        if len(self.oldText.get())>1:
            if len(self.newText.get())>1:
                if self.newText.get()!=self.confirmText.get():
                    showinfo("","NEW PASSWORD DOESNOT MATCH WITH CONFIRM PASSWORD")
                    self.root.destroy()
                else:

                    self.newPassword = self.newText.get()
                    if self.oldText.get()==self.oldPassword:


                        if len(self.newPassword) < 6:
                            showinfo("", "NEW PASSWORD MUST BE OF Atleast 6 Character")
                            self.root.destroy()
                        else:
                            cur = con.cursor()
                            query = 'update staff set  password="' + str(self.newPassword) + '"' + ' where email="' + str(
                                self.email) + '"'
                            print(query)
                            cur.execute(query)
                            con.commit()
                            showinfo("", "PASSWORD CHANGED")
                            self.root.destroy()
                    else:

                      showinfo("", "OLD PASSWORD WRONG!")
                      self.root.destroy()
            else:
                showinfo("","NEW PASSWORD NOT ENTERED")
                self.root.destroy()

        else:
            showinfo("","OLD PASSWORD EMPTY!")
            self.root.destroy()


    def __init__(self,parent,username,password):

        self.root = Toplevel()
        self.root.transient(parent)
        self.root.parent = parent

        self.root.iconbitmap("mail.ico")
        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value,height_value))
        self.root.title("CHANGE PASSWORD")
        self.root.resizable(0, 0)

        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())


        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")
        '''ADD RESTAURANT CANVAS'''
        '''CANVAS'''
        self.frameCanvas=PanedWindow(self.root)
        self.canvas = Canvas(self.frameCanvas,width=200, height=100,relief="raised")


        gif1 = PhotoImage(file="splashScreen/foodFruit.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)

        space = Label(self.canvas)
        space1 = Label(self.canvas)
        space.grid(row=0, column=0, padx=110)
        space.grid(row=0, column=0, pady=300)
        frame1 = PanedWindow(self.canvas)

        frame1.config(bg="#9c004f")
        frame1.config(width=1200)

        '''CANVAS ENDS HERE'''
        self.email=username
        self.oldPassword=password

        oldPassword=Label(frame1,text="OLD PASSWORD",bg="#89105f",fg="white",font=("calibri",15),width=20)

        newPassword=Label(frame1,text="NEW PASSWORD",bg="#89105f",fg="white",font=("calibri",15),width=20)

        confirmPassword=Label(frame1,text="CONFIRM PASSWORD",bg="#89105f",fg="white",font=("calibri",15),width=20)

        self.oldText=Entry(frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)
        self.newText=Entry(frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)
        self.confirmText=Entry(frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)

        changeBtn=Button(frame1,text="CHANGE",command=self.changePassFun,bg="white",fg="#89105f",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)


        oldPassword.grid(row=1,column=0,padx=20,pady=10)
        self.oldText.grid(row=1,column=1,padx=20,pady=10)

        newPassword.grid(row=2,column=0,padx=20,pady=10)
        self.newText.grid(row=2,column=1,padx=20,pady=10)

        confirmPassword.grid(row=3,column=0,padx=20,pady=10)
        self.confirmText.grid(row=3,column=1,padx=20,pady=10)

        changeBtn.grid(row=4,column=1,padx=20,pady=10)




        frame1.grid(row=0,column=0)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.frameCanvas.pack()
        self.root.mainloop()

#obj=changePassword("","")
