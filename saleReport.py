from pdfReport import *
from tkinter import *
from tkinter import ttk
from connection import *
from tkcalendar import *
from pygame import mixer



class saleReport:

    def fullDataFetchQuery(self):
        cur = con.cursor()
        query = 'Select * from bill where status="DONE" and  date="'+str(self.getDate)+'"'

        cur.execute(query)
        self.data1 = cur.fetchall()
        self.data = []
        self.total=0
        for i in range(0, len(self.data1)):
            self.data2 = []
            for j in range( len(self.data1[i])-1,-1,-1):
                if not  self.data1[i][j]=="DONE":
                    self.data2.insert(0, self.data1[i][j])


            print(self.data2)
            print(self.total)
            self.data.append(self.data2)
        print(self.data)
        for i in range(0,len(self.data)):
            self.total=self.total+self.data[i][7]
        print(self.total)

        print(self.data)

    def reset(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def printReport(self):
        obj=pdfReport(self.data,self.total)

    def insertData(self):
        self.getDate=self.date.get_date()
        print(self.getDate)
        self.reset()
        self.fullDataFetchQuery()
        for i in range(0, len(self.data)):
            self.treeview.insert("", i, values=self.data[i])




    def __init__(self,parent):
        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent

        self.root.title("LOGIN PAGE")
        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.resizable(0, 0)
        #self.root.attributes("-fullscreen", True)
        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.iconbitmap("pdf.ico")

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)
        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())

        '''CANVAS'''
        self.canvas = Canvas(self.root,width=300, height=200, bg='#9c004f',relief="raised")
        self.canvas.pack(expand=YES, fill=BOTH)
        gif1 = PhotoImage(file="splashScreen/indianSpice.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)


        self.frame0=PanedWindow(self.canvas)
        self.date=DateEntry(self.frame0,bg="#9c004f",fg="white",width=30,height=1 ,font=("Harlow Solid ",25,"bold"))
        self.getReport=Button(self.frame0,text="REPORT DATA",command=self.insertData,bg="#9c004f",fg="white",width=15,height=1 ,font=("Harlow Solid Italic",25,"italic","bold"))
        self.getReport.grid(row=0,column=1)
        self.date.grid(row=0,column=0)



        self.frame0.pack()


        self.frame1 = PanedWindow(self.canvas)
        self.root.title("SALES REPORT")


        self.treeview = ttk.Treeview(self.frame1, columns=(
        "billid", "typeoforder", "address", "modeofpayment", "cashCollected", "cashReturned", "mobileno", "netamount",
        "gst", "date"))

        self.treeview.heading("billid", text="BILL ID")
        self.treeview.heading("typeoforder", text="TYPE OF ORDER")
        self.treeview.heading("address", text="ADDRESS")
        self.treeview.heading("modeofpayment", text="MODE OF PAYMENT")
        self.treeview.heading("cashCollected", text="CASH COLLECTED")
        self.treeview.heading("cashReturned", text="CASH RETURNED")
        self.treeview.heading("mobileno", text="MOBILE NO.")
        self.treeview.heading("netamount", text="NET AMOUNT")
        self.treeview.heading("gst", text="GST")
        self.treeview.heading("date", text="DATE")
        self.treeview["show"] = "headings"

        self.treeview.column("billid",width=120)
        self.treeview.column("typeoforder",width=120)
        self.treeview.column("address",width=120)
        self.treeview.column("modeofpayment",width=120)
        self.treeview.column("cashCollected",width=120)
        self.treeview.column("cashReturned",width=120)
        self.treeview.column("mobileno",width=120)
        self.treeview.column("netamount",width=120)
        self.treeview.column("gst",width=120)
        self.treeview.column("date",width=120)
        self.insertData()


        '''TREEVIEW SCROLL '''
        style = ttk.Style()
        scroll = Scrollbar(self.frame1, orient="vertical", command=self.treeview.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.treeview.configure(yscrollcommand=scroll.set)
        '''TREEVIEW STYLING'''
        style.configure("Treeview.Heading", font=("Script MT Bold italic", 9), yscrollcommand=scroll.set, background="black",foreground="#9c004f")
        style.configure("Treeview", bg="black",rowheight = 30,
                              fg="#9c004f", fieldbackground="red")

        self.treeview.pack()
        self.frame1.pack()

        self.frame2=PanedWindow(self.canvas)
        spaceLabel=Label(self.frame2)
        spaceLabel.grid(row=0,column=0)

        reportPrint=Button(self.frame2,text="PRINT REPORT",bg="#9c004f",fg="white",width=20,font=("SystemButtonFace",20,"bold"))
        reportPrint.grid(row=0, column=0,pady=40)
        self.frame2.config(bg="#9c004f")
        self.frame2.pack()


        self.root.mainloop()


if __name__ == '__main__':

    obj=saleReport()