from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from connection import *

from pygame import mixer

p=False


class kitchenScreen2:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)


    def fullDataFetchQuery(self,billId):
        cur = con.cursor()
        query = "Select * from billdetail where billid="+str(billId)
        cur.execute(query)
        self.data = cur.fetchall()
        print(self.data)


    def insertData(self,billId):
        self.reset()
        self.fullDataFetchQuery(billId)
        for i in range(0, len(self.data)):
            self.treeview.insert("", i, values=self.data[i])

    def check(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        cur=con.cursor()

        query="select * from bill where billid="+str(self.billId)
        cur.execute(query)
        self.data=cur.fetchone()
        print(self.data)

        print(self.data[9])
        if self.data[9]=="PENDING":

            status="DONE"
            query='update bill set status="'+status+'" where billid='+str(self.billId)
            print(query)
            cur.execute(query)
            con.commit()
            showinfo("","Order Is Done")



            from kitchenScreen1 import kitchenScreen1

            obj = kitchenScreen1(self.root)
            self.root.destroy()

    def __init__(self,parent,x):

        self.root=Toplevel()


        self.root.title("Kitchen Screen 2")
        self.root.iconbitmap("chef.ico")

        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))

        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.resizable(0, 0)
        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())
        self.root.iconbitmap("chef.ico")
        '''CANVAS'''

        self.canvas = Canvas(self.root,width=300, height=200, bg='#89105f',relief="raised")
        gif1 = PhotoImage(file="splashScreen/foodItem.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)
        '''LABEL FRAME'''
        self.frame0 = PanedWindow(self.canvas)
        #        self.frame0.config(bg="#89105f")
        treeLabel = Label(self.frame0, text="Kitchen Screen Details", width=120)
        treeLabel.pack(pady=20, padx=20)


        self.billId=x
        self.frame1=PanedWindow(self.canvas)
        self.treeview = ttk.Treeview(self.frame1, columns=(
        "billdetailid", "billid", "menuid", "price", "quantity", "total"))

        self.treeview.heading("billdetailid", text="BILL DETAIL ID")

        self.treeview.heading("billid", text="BILL ID")
        self.treeview.heading("menuid", text="MENU ID")
        #self.treeview.heading("menuItem", text="MENU ITEM")
        self.treeview.heading("price", text="PRICE")

        self.treeview.heading("quantity", text="QUANTITY")
        self.treeview.heading("total", text="TOTAL")


        self.treeview["show"] = "headings"

        scroll=Scrollbar(self.root,orient="vertical",command=self.treeview.yview)
        scroll.pack(side=RIGHT,fill=Y)
        self.treeview.configure(yscrollcommand=scroll.set)
        self.treeview.pack()



        self.insertData(x)

        self.frame2=PanedWindow(self.canvas)
        self.orderUpdateBtn = Button(self.frame2, text="DONE",command=lambda :self.check(), bg="white", fg="#89105f",
                                   width=15, font=("Harlow Solid ", 20, "bold"))

        self.orderUpdateBtn.pack(padx=20,pady=20)
        self.canvas.pack(expand=YES, fill=BOTH)

        self.frame0.config(bg='#89105f')
        self.frame0.pack()
        self.frame1.pack()
        self.frame1.config(bg='#89105f')
        self.treeview.pack()
        self.frame2.pack()
        self.frame2.config(bg='#89105f')
        self.root.mainloop()

