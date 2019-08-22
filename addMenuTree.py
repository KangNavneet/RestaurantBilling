from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from connection import *
from pygame import mixer


class addMenuTree:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def doubleClick(self, event):

        if len(self.treeview.item(self.treeview.focus())['values'])<1:
            showinfo("","Select Item First Which You Want To Delete!")
        else:
            self.treeClick = self.treeview.item(self.treeview.focus())['values']
            menuid = self.treeClick[0]
            name = str(self.treeClick[1])
            confirm = askyesno("Confirmation Window", "Are You Sure To Delete?")
            if confirm:
                cur = con.cursor()
                query = 'delete from menu where menuid=' + str(menuid)
                print(query)
                cur.execute(query)
                con.commit()
                showinfo("", "Item Deleted!")

                self.insertData()

    def delItem(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        if len(self.treeview.item(self.treeview.focus())['values'])<1:
            showinfo("","Select Item First Which You Want To Delete!")
        else:
            self.treeClick = self.treeview.item(self.treeview.focus())['values']
            menuid = self.treeClick[0]
            name = str(self.treeClick[1])
            print(menuid)
            print(name)

            confirm = askyesno("Confirmation Window", "Are You Sure To Delete?")
            if confirm:
                cur = con.cursor()
                query = 'delete from menu where menuid=' + str(menuid)
                print(query)
                cur.execute(query)
                con.commit()
                showinfo("", "Item Deleted!")

                self.insertData()

    def fullDataFetchQuery(self):
        cur = con.cursor()
        query = "Select * from menu"
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
        #self.root.attributes("-fullscreen", True)

        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.iconbitmap("i.ico")
        self.root.config(bg="#89105f", highlightthickness=20, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.resizable(0, 0)


        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())



        #self.root.attributes('-alpha', 1.0)




        self.root.title("FULL MENU DATABASE")
        '''CANVAS'''

        self.canvas = Canvas(self.root,width=300, height=200, bg='#9c004f',relief="raised")
        self.canvas.pack(expand=YES, fill=BOTH)
        gif1 = PhotoImage(file="splashScreen/foodItem.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)



        self.frame0=PanedWindow(self.canvas)

        self.menuTitle=Label(self.frame0,text="MENU DETAILS",bg="#9c004f",fg="white",width=60,height=1 ,font=("Harlow Solid ",25,"bold"))
        self.menuTitle.grid(row=0,column=1,padx=20,pady=20)
        self.frame1=PanedWindow(self.canvas)

        self.treeview = ttk.Treeview(self.frame1, columns=("menuid", "name", "description", "price"))
        '''TREEVIEW SCROLL '''
        style = ttk.Style()
        scroll=Scrollbar(self.frame1,orient="vertical",command=self.treeview.yview)
        scroll.pack(side=RIGHT,fill=Y)
        self.treeview.configure(yscrollcommand=scroll.set)
        self.treeview.heading("menuid", text="MENU ID")
        self.treeview.heading("name", text="NAME")
        self.treeview.heading("description", text="DESCRIPTION")
        self.treeview.heading("price", text="PRICE")
        self.treeview["show"] = "headings"

        '''TREEVIEW STYLING'''
        style.configure("Treeview.Heading", font=("Script MT Bold ", 20), yscrollcommand=scroll.set, background="black",foreground="#9c004f")
        style.configure("Treeview", bg="black",rowheight = 34,
                              fg="#9c004f", fieldbackground="red")



        self.insertData()

        self.frame2 = PanedWindow(self.canvas)
        delBtn = Button(self.frame2, text="Delete Item", command=self.delItem,bg="white",fg="#9c004f",width=10,font=("SystemButtonFace",20,"bold"),padx=10,pady=10)
        delBtn.grid(row=0, column=0,padx=20,pady=20)


        self.frame0.pack()
        self.frame0.config(bg="#9c004f")
        self.frame1.pack()
        self.frame1.config(bg="#9c004f")
        self.treeview.pack()
        self.frame2.pack()
        self.frame2.config(bg="#9c004f")





        self.root.mainloop()


#obj=addMenuTree()
