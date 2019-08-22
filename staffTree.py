from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

from PIL import ImageTk,Image
from pygame import mixer

from connection import *

class staffTree:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)


    def delItem(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()

        if len(str(self.treeview.item(self.treeview.focus())['values'])) <1:
            showinfo("Message","Select The Item First To Delete!")
        else:
            self.treeClick= self.treeview.item(self.treeview.focus())['values']
            self.email=self.treeClick[1]
            #self.mobile=str(self.treeClick[2])


            confirm = askyesno("Confirmation Window", "Are You Sure To Delete?")
            if confirm:
                cur = con.cursor()
                query = 'delete from staff where email="' + self.email+'"'
                print(query)
                cur.execute(query)
                con.commit()
                self.insertData()
                showinfo("","Item Deleted!")
                self.insertData()


    def fullDataFetchQuery(self):
        cur = con.cursor()
        query = "Select * from staff"
        cur.execute(query)
        self.data = cur.fetchall()


    def insertData(self):
        self.reset()
        self.fullDataFetchQuery()
        for i in range(0, len(self.data)):
            self.treeview.insert("", i, values=self.data[i])


    def __init__(self,parent):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent


        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value,height_value))
        self.root.config(bg="#89105f", highlightthickness=20, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.resizable(0, 0)
        #self.root.attributes("-fullscreen", True)


        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())

        self.root.title("STAFF DETAILS TREE")
        self.root.iconbitmap("chef.ico")

        '''CANVAS'''
        self.frameCanvas=PanedWindow(self.root)

        canvas = Canvas(self.frameCanvas,width=width_value, height=height_value, bg='#9c004f',relief="raised")
        canvas.pack(expand=YES, fill=BOTH)
        gif1 = PhotoImage(file="splashScreen/food1.png")
        canvas.create_image(50, 10, image=gif1, anchor=NW)




        '''ADD STAFF DETAIL PHOTO'''
        self.frame0 = PanedWindow(self.root)
        self.frame0.config(bg="#89105f")
        image = Image.open("splashScreen/staffDetails.jpg")
        photo = ImageTk.PhotoImage(image)
        updateLabel = Label(self.frame0, image=photo, bg="#89105f")
        updateLabel.grid(row=0, column=0, padx=10, pady=10)
        self.frame0.pack()

        self.frame1=PanedWindow(self.root)
        self.treeview = ttk.Treeview(self.frame1, columns=("Name", "Email","Mobile","Password","Type"))
        self.treeview.heading("Name", text="NAME")

        self.treeview.heading("Email", text="EMAIL")
        self.treeview.heading("Mobile", text="MOBILE")
        self.treeview.heading("Password", text="PASSWORD")
        self.treeview.heading("Type", text="TYPE")

        self.treeview["show"] = "headings"
        ttk.Style().configure(".", font=('serif', 8), foreground="red",background="black",activebackground="green" )


        '''TREEVIEW SCROLL '''
        style = ttk.Style()
        scroll=Scrollbar(self.frame1,orient="vertical",command=self.treeview.yview)
        scroll.pack(side=RIGHT,fill=Y)
        self.treeview.configure(yscrollcommand=scroll.set)
        '''TREEVIEW STYLING'''
        style.configure("Treeview.Heading", font=("Script MT Bold ", 20), yscrollcommand=scroll.set, background="black",foreground="#9c004f")


        style.configure("Treeview", bg="black",rowheight = 35,
                              fg="#9c004f", fieldbackground="red")
        self.treeview.pack()

        self.insertData()
        self.frame2=PanedWindow(self.root)
        self.frame2.config(bg="#89105f")
        space=Label(self.frame2,text="",bg="#89105f",fg="#89105f")
        space.grid(row=0,column=0)
        delBtn=Button(self.frame2,text="Delete Item",command=self.delItem,bg="#89105f",fg="white",relief="raised",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)
        delBtn.grid(row=1,column=0)



        self.frame1.pack()
        self.frame2.pack()

        self.frameCanvas.pack()
        self.root.mainloop()



#obj=staffTree()