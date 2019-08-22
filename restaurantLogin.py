
from mainWindow import *
from kitchenScreen1 import *
from kitchenScreen2 import *
from tkinter import *
from connection import *
from tkinter.messagebox import *
from PIL import ImageTk,Image
from pygame import mixer

class restaurantLogin:
    def loginFun(self):
        print("LOGIN")
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        username=self.userText.get().strip()
        password=self.passwordText.get().strip()

        cur=con.cursor()
        query="select * from staff where email='"+username+"' and password='"+password+"'"
        print(query)

        cur.execute(query)
        data=cur.fetchone()
        print(data)


        if data!=None:


            if data[4]=="CASHIER":
                #self.root.destroy()
                obj = mainWindow(self.root,username,password)


            else:
                #self.root.destroy()
                obj=kitchenScreen1(self.root)


        else:
            showinfo("","Invalid Username or Password")








    def __init__(self):

        self.root=Tk()
        self.root.geometry('600x300')
        self.root.title("LOGIN PAGE")
        self.root.iconbitmap("sign.ico")
        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.resizable(0, 0)
        #self.root.attributes("-fullscreen", True)
        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")



        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: sys.exit())


        '''ADD RESTAURANT CANVAS'''
        '''CANVAS'''
        self.canvas = Canvas(self.root,width=300, height=200, bg='#9c004f',relief="raised")
        self.canvas.pack(expand=YES, fill=BOTH)
        gif1 = PhotoImage(file="splashScreen/indianSpice.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)



        loginLabel=Label(self.canvas,text="LOG IN",bg="#89105f",fg="white",font=("calibri",25),width=30)

        space=Label(self.canvas)
        space1 = Label(self.canvas)

        usernameLabel=Label(self.canvas,text="Username",bg="#89105f",fg="white",font=("calibri",25),width=20)
        passwordLabel=Label(self.canvas,text="Password",bg="#89105f",fg="white",font=("calibri",25),width=20)

        self.userText=Entry(self.canvas,bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)
        self.passwordText=Entry(self.canvas,show="*",bd=1,relief="groove",bg="white",fg="#89105f",font=("calibri",15),width=20)

        button=Button(self.canvas,text="Login",command=self.loginFun,bg="white",fg="#89105f",width=20,font=("SystemButtonFace",25,"bold"),padx=8,pady=8)

        space.grid(row=0, column=0,padx=120)
        space.grid(row=0, column=0,pady=40)
        loginLabel.grid(row=1, column=2, padx=40, pady=10)
        usernameLabel.grid(row=2,column=1,padx=40,pady=10)
        self.userText.grid(row=2, column=2,padx=30,pady=10)
        passwordLabel.grid(row=3,column=1,padx=30,pady=10)
        self.passwordText.grid(row=3,column=2,padx=30,pady=10)

        button.grid(row=4,column=2)
        self.canvas.pack()

        self.root.mainloop()


