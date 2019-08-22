from tkinter import *
from tkinter.messagebox import showinfo

from connection import *
from pygame import mixer
class changeEmail:
    def changeMailFun(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        if len(self.oldText.get())>1:
            if len(self.newText.get())>1:
                if self.newText.get()!=self.confirmText.get():
                    showinfo("","NEW EMAIL DOESNOT MATCH WITH CONFIRM EMAIL")

                else:

                    self.newEmail = self.newText.get()
                    if self.oldEmail==self.oldText.get():


                        if len(self.newEmail) < 3:
                            showinfo("", "NEW Email MUST BE OF Atleast 3 Character")

                        else:
                            cur = con.cursor()
                            query = 'update staff set  email="' + str(self.newEmail) + '"' + ' where password="' + str(
                                self.oldPassword) + '"'
                            print(query)
                            cur.execute(query)
                            con.commit()
                            showinfo("", "EMAIL CHANGED")
                            self.root.destroy()
                    else:

                      showinfo("", "OLD EMAIL WRONG!")

            else:
                showinfo("","NEW EMAIL NOT ENTERED")


        else:
            showinfo("","OLD EMAIL EMPTY!")


    def __init__(self,parent,username,password):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent

        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value,height_value))
        self.root.iconbitmap("mail.ico")
        self.root.config(bg="#89105f", highlightthickness=22, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.title("CHANGE EMAIL")
        self.root.resizable(0, 0)

        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())
        self.oldEmail=username
        self.oldPassword=password
        '''CANVAS'''
        self.frameCanvas=PanedWindow(self.root)
        self.canvas = Canvas(self.frameCanvas,width=200, height=100,relief="raised")


        gif1 = PhotoImage(file="splashScreen/foodFruit.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)
        space=Label(self.canvas)
        space1 = Label(self.canvas)
        space.grid(row=0,column=0,padx=110)
        space.grid(row=0, column=0, pady=300)
        frame1 = PanedWindow(self.canvas)


        frame1.config(bg="#9c004f")
        frame1.config(width=1200)

        oldEmail=Label(frame1,text="OLD EMAIL",bg="#89105f",fg="white",font=("calibri",25),width=20)

        newEmail=Label(frame1,text="NEW EMAIL",bg="#89105f",fg="white",font=("calibri",25),width=20)

        confirmEmail=Label(frame1,text="CONFIRM EMAIL",bg="#89105f",fg="white",font=("calibri",25),width=20)

        self.oldText=Entry(frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)
        self.newText=Entry(frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)
        self.confirmText=Entry(frame1,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)

        changeBtn=Button(frame1,text="CHANGE",command=self.changeMailFun)


        oldEmail.grid(row=1,column=0,padx=30,pady=10)
        self.oldText.grid(row=1,column=1,padx=30,pady=10)

        newEmail.grid(row=2,column=0,padx=30,pady=10)
        self.newText.grid(row=2,column=1,padx=30,pady=10)

        confirmEmail.grid(row=3,column=0,padx=30,pady=10)
        self.confirmText.grid(row=3,column=1,padx=30,pady=10)

        changeBtn.grid(row=4,column=1,padx=30,pady=10)


        frame1.grid(row=0,column=0)
        self.canvas.pack(expand=YES, fill=BOTH)
        self.frameCanvas.pack()
        self.root.mainloop()

#obj=changeEmail("","")
