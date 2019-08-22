from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from connection import *
from pygame import mixer

class searchMenu:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)


    def searchFun(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        search=self.menuText.get()
        cur=con.cursor()
        query='select * from menu where name like "'+search+'%"'
        print(query)
        cur.execute(query)
        self.data=cur.fetchall()
        self.insertData()

    def insertData(self):
        self.reset()

        for i in range(0, len(self.data)):
            self.treeview.insert("", i, values=self.data[i])



    def __init__(self,parent):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent = parent
        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()

        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.config(bg="#89105f", highlightthickness=20, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.resizable(0, 0)

        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())


        self.root.title("Search Menu")
        self.root.iconbitmap("i.ico")

        self.framea = PanedWindow(self.root)
        space=Label(self.root,padx=120,pady=60,bg="#89105f")
        self.framea.config(bg="#89105f")
        space.pack()
        self.framea.pack()

        '''IMAGE ON LABEL'''

        self.frame1=PanedWindow(self.root)
        photo=PhotoImage(file="splashScreen/Search1.png")

        searchLabel = Label(self.frame1, image=photo,bg="#89105f")
        menuLabel=Label(self.frame1,text="ENTER MENU",bg="white",fg="#89105f",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)
        self.menuText=Entry(self.frame1,bd=1,relief="groove",bg="#ffffff",font=("calibri",15),width=20)

        searchBtn=Button(self.frame1,text="Search",command=self.searchFun,bg="white",fg="#89105f",width=10,font=("SystemButtonFace",15,"bold"),padx=8,pady=8)

        searchLabel.grid(row=0, column=0)
        menuLabel.grid(row=0,column=1)
        self.menuText.grid(row=0,column=2,padx=10)
        searchBtn.grid(row=0,column=3,padx=10,pady=10)

        self.frame2=PanedWindow(self.root)
        self.treeview=ttk.Treeview(self.frame2,columns=("menuid", "name","description","price"))
        self.treeview.heading("menuid", text="MENU ID")

        self.treeview.heading("name", text="NAME")
        self.treeview.heading("description", text="DESCRIPTION")
        self.treeview.heading("price", text="PRICE")

        '''TREEVIEW '''
        style = ttk.Style()
        scroll = Scrollbar(self.frame2, orient="vertical", command=self.treeview.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.treeview.configure(yscrollcommand=scroll.set)

        '''TREEVIEW STYLING'''

        style.configure("Treeview.Heading", font=("Script MT Bold", 12), yscrollcommand=scroll.set, bg="black",
                        fg="red")
        style.configure("Treeview", font=("calibri", 12))

        self.treeview["show"] = "headings"
        self.treeview.pack()
        self.frame1.pack()
        self.frame1.config(bg="#89105f")
        self.frame2.pack()
        self.frame2.config(bg="#89105f")
        self.root.mainloop()



#obj=searchMenu()