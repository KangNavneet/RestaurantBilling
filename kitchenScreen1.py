from kitchenScreen2 import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
from connection import *
from pygame import mixer

class kitchenScreen1:
    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def fullDataFetchQuery(self):
        cur = con.cursor()
        query = 'Select * from bill where status="PENDING"'
        cur.execute(query)
        self.data = cur.fetchall()

    def insertData(self):
        self.reset()
        self.fullDataFetchQuery()
        if self.data != None:
            for i in range(0, len(self.
                                          data)):
                self.treeview.insert("", i, values=self.data[i])
        else:
            showinfo("", "Status is Done!")

    def viewDetail(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        print("View Details KitchenScreen 2")
        print(self.treeview.item(self.treeview.focus())['values'])
        print(len(self.treeview.item(self.treeview.focus())['values']))
        if self.treeview.item(self.treeview.focus())['values']=="":
            showinfo("Message", "Select Item First!")
        else:
            self.treeClick = self.treeview.item(self.treeview.focus())['values']
            self.billid = self.treeClick[0]
            print(self.treeClick)


            print("I am In MAIN")
            self.root.destroy()
            print("KitchenScreen 2")

            self.root.destroy()
            obj = kitchenScreen2(self.root,self.billid)



    def __init__(self,parent):

        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent
        #self.root=Tk()


        self.root.title("Kitchen Screen 1")

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
        self.canvas.pack(expand=YES, fill=BOTH)
        gif1 = PhotoImage(file="splashScreen/foodItem.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)

        '''LABEL FRAME'''
        self.frame0 = PanedWindow(self.canvas)
        #        self.frame0.config(bg="#89105f")
        treeLabel = Label(self.frame0, text="Kitchen Screen", width=120)
        treeLabel.pack(pady=20, padx=20)


        '''Treeview Frame'''
        self.frame1 = PanedWindow(self.canvas)
        self.treeview = Treeview(self.frame1, columns=(
        "billid", "typeoforder", "address", "modeofpayment", "cashCollected", "cashReturned", "mobileno", "netamount",
        "gst", "status", "date"))
        self.treeview.heading("billid", text="BILL ID")

        self.treeview.heading("typeoforder", text="TYPE OF ORDER")
        self.treeview.heading("address", text="ADDRESS")
        self.treeview.heading("modeofpayment", text="MODE")
        self.treeview.heading("cashCollected", text="COLLECTED")

        self.treeview.heading("cashReturned", text="RETURNED")
        self.treeview.heading("mobileno", text="MOBILE NUMBER")
        self.treeview.heading("netamount", text="NET AMOUNT")

        self.treeview.heading("gst", text="GST")
        self.treeview.heading("status", text="STATUS")
        self.treeview.heading("date", text="DATE")

        self.treeview["show"] = "headings"
        ttk.Style().configure(".", font=('serif', 8), foreground="red", background="black", activebackground="green")

        '''TREEVIEW SCROLL '''
        style = ttk.Style()
        scroll = Scrollbar(self.frame1, orient="vertical", command=self.treeview.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.treeview.configure(yscrollcommand=scroll.set)
        '''TREEVIEW STYLING'''
        style.configure("Treeview.Heading", font=("Script MT Bold italic", 8), yscrollcommand=scroll.set,
                        background="black", foreground="#9c004f")

        style.configure("Treeview", bg='#89105f', rowheight=35,
                        fg="#9c004f", fieldbackground="red")

        self.treeview.column("billid", width=130)
        self.treeview.column("typeoforder", width=130)
        self.treeview.column("address", width=130)
        self.treeview.column("modeofpayment", width=120)
        self.treeview.column("cashCollected", width=120)

        self.treeview.column("cashReturned", width=120)
        self.treeview.column("mobileno", width=120)
        self.treeview.column("netamount", width=120)

        self.treeview.column("gst", width=120)
        self.treeview.column("status", width=120)
        self.treeview.column("date", width=140)

        self.frame2 = PanedWindow(self.canvas)

        self.addDetailBtn = Button(self.frame2, text="View Details", command=self.viewDetail, bg="white", fg="#89105f",
                                   width=15, font=("Harlow Solid", 20, "bold"))
        self.addDetailBtn.pack()
        self.insertData()

        self.frame0.pack()
        self.frame0.config(bg='#89105f')
        self.canvas.pack()
        self.frame1.pack()
        self.frame1.config(bg='#89105f')
        self.frame2.pack(pady=10)
        self.frame2.config(bg='white')
        self.treeview.pack()
        self.root.mainloop()




