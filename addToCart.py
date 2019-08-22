from excelGenration import *

from PIL import ImageTk,Image
from tkinter import ttk
from tkinter.messagebox import *
from connection import *
from datetime import datetime
from pdfdemo import *
from sendsmsdemo import *

from tkinter import *
from pygame import mixer


# import openpyxl module
import openpyxl
# import Font function from openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment
import random




class addToCart:
    def generateexcel(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        if self.flag:
            if __name__ == '__main__':
                obj=excelFile(self.mainList)
                self.allClear()
        else:
            showinfo("","GENERATE BILL FIRST!")


    def fieldReset(self):
        '''NORMAL'''
        self.orderCombo['state']="normal"
        self.payModeCombo['state']="normal"
        self.cashReturnedText['state']="normal"
        self.totalAmt['state']="normal"
        self.gst['state']="normal"
        self.netAmt['state']="normal"


        self.orderCombo.set("")
        self.addressText.delete(0.0, END)
        self.payModeCombo.set("")
        self.cashReturnedText.delete(0, END)
        self.mobileText.delete(0, END)
        self.cashCollectedText.delete(0, END)
        self.menuCombo.set("")
        self.quantCombo.set("")
        self.totalAmt.delete(0, END)
        self.gst.delete(0, END)
        self.netAmt.delete(0,END)


        '''READ ONLY'''
        self.orderCombo['state']="readonly"
        self.payModeCombo['state']="readonly"
        self.cashReturnedText['state']="readonly"
        self.totalAmt['state']="readonly"
        self.gst['state']="readonly"
        self.netAmt['state']="readonly"


    def allClear(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.reset()
        self.fieldReset()
        self.serial = 1
        self.mainList=[]

        # self.getDate()


    def fetchDataCombo(self):
        cur = con.cursor()
        query = "select * from menu "

        cur.execute(query)
        data = cur.fetchall()
        print(data)

        self.menuItem = []

        for record in data:
            print(record)
            self.menuItem.append(record[1])

        self.menuItem=tuple(self.menuItem)

    def quantity(self):
        self.menuQuantity=[]
        for i in range(1,11):
            self.menuQuantity.append(i)

    def reset(self):

        menuItem=""
        self.price=0
        self.quantity=0
        self.totalPrice=0
        self.flag=False

        self.subList =["Serial Number","Item Name","Price","Quantity","Total Price"]
        for i in self.treeview.get_children():
            self.treeview.delete(i)

    def priceClear(self):
        print("ENTRY   PRICE CLEAR!")
        self.totalAmt = Entry(self.frame3, state="readonly")
        self.gst = Entry(self.frame3, state="readonly")
        self.netAmt = Entry(self.frame3, state="readonly")
        self.totalAmt.grid(row=0, column=1)
        self.gst.grid(row=1, column=1)
        self.netAmt.grid(row=2, column=1)

        # self.totalAmt.delete(0,END)
        # self.gst.delete(0,END)
        # self.netAmt.delete(0,END)





    def priceFetchQuery(self):
        cur = con.cursor()
        menuItem=self.menuCombo.get()
        print(menuItem)
        if menuItem=="":
            showinfo("","Menu Item Not Selected")
        else:
            if self.quantCombo.get()=="":
                showinfo("","Quantity Not Selected")
            else:

                query = 'Select * from menu where name="'+menuItem+'"'
                print(query)
                cur.execute(query)
                self.data = cur.fetchone()
                self.price=float(self.data[3])
                print("Price="+str(self.price))
                print(self.data)

    def serialConst(self):
        for i in range(0, len(self.mainList)):
            self.mainList[i][0] = i + 1
        self.serial = len(self.mainList) + 1

    def mainListConst(self):

        flag=False

        for i in range(0,len(self.mainList)):
            if self.subList[1]==self.mainList[i][1]:
                flag=True
                self.mainList[i][0]=i+1
                self.subList[3]=float(self.subList[3])+float(self.mainList[i][3])

                self.quantity=self.subList[3]
                print("Quantity:"+str(self.quantity))
                self.mainList[i][3]=self.quantity
                self.mainList[i][4]=self.mainList[i][3]*self.mainList[i][2]
                print("Total Amount Updated="+str(self.mainList[i][4]))
        if flag==False:


            self.mainList.append(self.subList)

            self.serial=len(self.mainList)+1

    def cashReturn(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.cashReturnedText['state']="normal"
        self.cashReturnedText.delete(0,END)
        if len(str(self.cashCollectedText.get()))<1:
            showinfo("","Collect Cash First!")
        else:
            leftAmt=float(self.cashCollectedText.get())-self.netAmtVar
            print("Left AMount:"+str(leftAmt))
            self.cashReturnedText.insert(0,leftAmt)
            self.cashReturnedText['state']="readonly"
    def treeData(self):
        self.reset()
        '''Tree View Data'''
        for i in range(0, len(self.mainList)):
            self.treeview.insert("", i, values=self.mainList[i])

    def insertCart(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        self.priceClear()
        self.reset()


        self.priceFetchQuery()
        self.quantity=self.quantCombo.get()
        self.menu=self.menuCombo.get()
        print("Quantity:"+self.quantity)
        print("Price:"+str(self.price))
        self.totalPrice=(float(self.price)*float(self.quantity))+self.totalPrice
        print("Total Price:"+str(self.totalPrice))



        '''Sub List and Main List'''
        self.subList=[self.serial,self.menu,self.price,self.quantity,self.totalPrice]

        print(self.subList)

        self.mainListConst()



        self.treeData()

        self.priceFill()


    def priceFill(self):
        ''' INSERT IN FRAME 3 Price Calculation'''
        print(self.mainList)
        self.totalAmtVar = 0
        for i in range(0, len(self.mainList)):
            self.totalAmtVar = self.mainList[i][4] + self.totalAmtVar

            print("Total Amount=" + str(self.totalAmtVar))

        self.gstAmtVar = 5 * (0.01)
        self.netAmtVar = self.totalAmtVar + (self.totalAmtVar * self.gstAmtVar)
        print("Total Net:" + str(self.netAmtVar))

        print(str(self.totalAmtVar))
        print(str(self.gstAmtVar))
        print(str(self.netAmtVar))
        print('Total Amount: ' + str(self.totalAmtVar) + " " + str(self.gstAmtVar) + " " + str(self.netAmtVar))
        self.priceCalculation()


    def priceCalculation(self):

        self.totalAmt['state']="normal"
        self.gst['state']="normal"
        self.netAmt['state']="normal"
        self.totalAmt.insert(0,"Rs. "+str(self.totalAmtVar))
        self.gst.insert(0, str(self.gstAmtVar*100)+"%")
        self.netAmt.insert(0, "Rs. "+str(self.netAmtVar))
        self.totalAmt['state']="readonly"
        self.gst['state']="readonly"
        self.netAmt['state']="readonly"
    def orderBillQuery(self):
        self.orderSubList=[self.orderType,self.address,self.paymentMode,self.cash,self.cashReturn,self.mobileNumber,self.cashReturn,self.mobileNumber,self.netAmtVar,self.gstAmtVar,self.status]
        cur=con.cursor()
        query='insert into bill(typeoforder,address,modeofpayment,cashCollected,cashReturned,mobileno,netamount,gst,status,date) values("'+self.orderType+'","'+self.address+'","'+self.paymentMode+'",'+str(self.cash)+' ,'+str(self.cashReturn)+',"'+self.mobileNumber+'",'+str(self.netAmtVar)+','+str(self.gstAmtVar)+',"'+self.status+'","'+self.date+'")'
        print(query)
        cur.execute(query)
        con.commit()
        showinfo("Message","Data Inserted!")
        self.billDetailQuery()
        self.smsMessage()

        self.flag=True


    def smsMessage(self):

        list=["Serial Number", "Item Name", "Price", "Quantity", "Total Price"]
        self.mainList.insert(0,list)
        print(self.mainList)
        message=""

        '''
        BILL
        for i in range(1,len(self.mainList)):
            message=message+str(self.mainList[i])+"\n"
            print("LOOP MESSAGE:"+message)
        '''
        cur=con.cursor()
        query='select * from bill'
        cur.execute(query)
        self.data=cur.fetchall()
        for i in range(0,len(self.data)):
            self.billId=self.data[i][0]

        message=message+"Restaurant Mania:"+self.orderType+"    Bill ID:"+str(self.billId)+"    TOTAL AMOUNT:"+str(self.totalAmtVar)+"    GST:"+str(self.gstAmtVar)+"    NET AMOUNT:"+str(self.netAmtVar)+"    AMOUNT PAID:"+str(self.cash)+"    AMOUNT RETURNED:"+str(self.cashReturn)

        print("FULL MESSAGE:"+message)
        print("MOBILE NUMBER:"+str(self.mobileNumber))

        obj=sms(message,self.mobileNumber)

    def doubleClick(self, event):


        self.treeClick = self.treeview.item(self.treeview.focus())['values']
        menuItem = self.treeClick[1]
        message="Are you Sure To Delete Menu Item:"+menuItem+" ?"
        confirm = askyesno("Confirmation Window", message)
        if confirm:
            for i in range(0,len(self.mainList)):
                if self.mainList[i][1]==menuItem:

                    x=self.mainList[i]
                    print("***********MAINLIST ON REMOVAL DOUBLE CLICK ***********")
                    self.mainList.remove(x)
                    print(self.mainList)
                    showinfo("Message", "Item Removed")

                    self.serialConst()

                    self.treeData()
                    self.fieldReset()
                    self.priceFill()

                    break











    def billDetailQuery(self):
        '''GET BILL ID  FROM SERIAL NUMBER'''


        '''GET BILL ID,MENUID,PRICE,Quantity,Total FROM MAINLIST'''
        '''BILL ID FROM BILL TABLE AND MENUID FROM MENU TABLE'''
        for self.subList in self.mainList:
            cur = con.cursor()
            q="select * from bill"
            cur.execute(q)
            rs=cur.fetchall()
            billid=0
            for row in rs:
                billid=row[0]

            print(self.subList)

            query = 'select * from menu where name="' + self.subList[1] + '"'
            print(query)
            cur.execute(query)
            self.menuFetch = cur.fetchone()
            print(self.menuFetch)
            self.menuId = self.menuFetch[0]
            self.billSubPrice = self.subList[2]
            self.billQuantity = self.subList[3]
            self.billTotal = self.subList[4]

            query = 'insert into billdetail(billid,menuid,price,quantity,total) values('+ str(billid) + ',' + str(self.menuId) + ',' + str(self.billSubPrice) + ',' + str(self.billQuantity) + ',' + str(self.billTotal) + ')'
            print(query)
            cur.execute(query)
            con.commit()

            self.reset()





    def orderBar(self):
        self.gstAmtVar=self.gstAmtVar*100
        self.cashReturnedText['state'] = "normal"
        self.cashReturnedText.delete(0, END)
        self.orderType = self.orderCombo.get()
        print(self.orderType)
        self.address = self.addressText.get(0.0, END).strip()
        self.paymentMode = self.payModeCombo.get()
        self.cash = self.cashCollectedText.get()
        self.cashReturn = float(self.cash) - float(self.netAmtVar)
        self.cashReturnedText.insert(0, self.cashReturn)
        self.cashReturnedText['state'] = "readonly"
        self.mobileNumber=str(self.mobileText.get())
        self.status="PENDING"
        self.orderBillQuery()


    def generatePdf(self):
        obj=pdfGenerator()


    def generateBill(self):
        mixer.init()
        mixer.music.load('audio/buttonPushTrim.mp3')
        mixer.music.play()
        if self.netAmtVar>0:

            if self.orderCombo.get()=="":
                showinfo("","Select Order Type")
            else:
                if self.payModeCombo.get()=="":
                    showinfo("","Select Payment Mode")
                else:

                    if str(self.mobileText.get()).isnumeric() and len(self.mobileText.get())==10 :
                        if len(self.cashCollectedText.get())<1:
                            showinfo("","Cash Not Collected")
                        else:
                            if self.orderCombo.get()=="HOME DELIVERY":
                                if len(self.addressText.get(0.0, END).strip())<1:
                                    showinfo("","Address Not Filled!")
                                else:
                                    self.serial = 1
                                    self.orderBar()

                            else:
                                self.orderBar()
                    elif len(self.mobileText.get())==0:
                        showinfo("","Fill Mobile Number")

                    else:
                        showinfo("","Invalid Mobile Number!")

        else:
            showinfo("Message","Cart is Empty!")

    def getDate(self):

        self.d=datetime.now()
        s=str(self.d).split(" ")
        self.date=s[0]
        self.time=s[1].split('.')
        self.time=str(self.time[0])
        print(self.date)
        print("Time"+self.time)
        # self.label2["text"]=self.date
        # self.label3["text"]=self.time



    def __init__(self,parent):

        self.root=Toplevel()
        self.root.transient(parent)
        self.root.parent=parent
        #self.root.attributes("-fullscreen", True)
        self.flag = False
        self.mainList = []
        self.subList = ["Serial Number", "Item Name", "Price", "Quantity", "Total Price"]

        self.serial = 1
        self.row = 0
        self.root.iconbitmap("cart.ico")
        self.root.title("ADD TO CART")

        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value,height_value))

        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")
        self.root.resizable(0, 0)
        #self.root.attributes("-fullscreen", True)

        '''MAINBAR DETAILS'''
        self.mainBar = Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)

        self.mainBar.add_command(label='EXIT', command=lambda: self.root.destroy())

        #LABEL PHOTO
        '''
        image = Image.open("splashScreen/foodItem.png")
        photo = ImageTk.PhotoImage(image)
        photoLabel = Label(self.root, image=photo, bg="#89105f")
        photoLabel.grid(row=0, column=0, padx=10, pady=10)
        '''
        '''CANVAS'''
        '''CANVAS'''
        self.canvas = Canvas(self.root,width=300, height=200, bg='#89105f',relief="raised")
        gif1 = PhotoImage(file="splashScreen/foodItem.png")
        self.canvas.create_image(50, 10, image=gif1, anchor=NW)
        self.fetchDataCombo()
        self.quantity()
        '''TIME AND DATE'''
        self.frame0=PanedWindow(self.canvas)
        self.label1=Label(self.frame0,text="Date And Time",width=28,fg="#89105f",font=("Harlow Solid ",20,"bold"),height=1)
        clock = Label(self.frame0, font=('times', 20, 'bold'), bg='snow')
        date1 = Label(self.frame0, font=('times', 15, 'bold'), bg='snow')
        def tick():
            now = datetime.now()
            time2 = str(now.strftime("%I:%M:%S %p"))
            time3 = str(now.strftime("%A,%d-%b-%y"))
            clock.config(text=time2)
            date1.config(text=time3)
            clock.after(200, tick)

        tick()
        self.label1.grid(row=0,column=0)
        clock.grid(row=0,column=1)
        date1.grid(row=0, column=2)
        self.getDate()



        '''TIME AND DATE ENDS'''

        self.framea = PanedWindow(self.canvas)
        space=Label(self.canvas)
        space.pack()
        self.framea.pack()
        self.framea.config(bg="#89105f")

        self.frame1=PanedWindow(self.canvas)

        self.frame2=PanedWindow(self.canvas)

        self.frame3 = PanedWindow(self.canvas)


        '''FRAME 1'''
        selectMenuLabel=Label(self.frame1,text="Select Menu",width=35,bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"),pady=5)
        self.menuCombo = ttk.Combobox(self.frame1, values=self.menuItem, state="readonly",width=35)

        selectQuantity=Label(self.frame1,text="Select Quantity",width=35,bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"),pady=5)
        self.quantCombo=ttk.Combobox(self.frame1, values=self.menuQuantity, state="readonly",width=35)
        self.cartBtn=Button(self.frame1,text="ADD TO CART",command=self.insertCart,width=15, bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"),pady=5)
        selectMenuLabel.grid(row=0,column=0)
        self.menuCombo.grid(row=0,column=1)
        selectQuantity.grid(row=0,column=2)
        self.quantCombo.grid(row=0,column=3)
        self.cartBtn.grid(row=0,column=4)


        '''FRAME 2 '''
        self.treeview = ttk.Treeview(self.frame2, columns=("serialNo", "menuName","price","quantity","totalPrice"))
        self.treeview.heading("serialNo", text="Serial No.")

        self.treeview.heading("menuName", text="Menu Name")
        self.treeview.heading("price", text="Price")
        self.treeview.heading("quantity", text="Quantity")
        self.treeview.heading("totalPrice", text="Total Price")



        self.treeview["show"] = "headings"
        self.style = ttk.Style()
        self.style.configure("Treeview", bg="black",rowheight = 34,
                              fg="#9c004f", fieldbackground="red")
        self.treeview.pack()

        '''EVENT BIND HERE IN TREEVIEW'''
        self.treeview.bind("<Double-1>", self.doubleClick)

        '''Frame 3'''


        self.totalAmtLabel=Label(self.frame3,text="TOTAL AMOUNT:",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"),pady=5)
        self.gstLabel=Label(self.frame3,text="GST:",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"),pady=5)
        self.netAmtLabel=Label(self.frame3,text="NET AMOUNT:",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"),pady=5)



        self.totalAmtVar=""
        self.gstAmtVar=""
        self.netAmtVar=""





        '''PRICE INSERTION'''
        '''
        self.totalAmtVar=StringVar()
        self.totalAmt=Label(self.frame3,textvariable=self.totalAmtVar)


        '''

        self.totalAmt=Entry(self.frame3,state="readonly")
        self.gst=Entry(self.frame3,state="readonly")
        self.netAmt=Entry(self.frame3,state="readonly")
        self.totalAmt.insert(0,self.totalAmtVar)
        self.gst.insert(0, self.gstAmtVar)
        self.netAmt.insert(0, self.netAmtVar)




        self.totalAmtLabel.grid(row=0,column=0)
        self.gstLabel.grid(row=1,column=0)
        self.netAmtLabel.grid(row=2,column=0)
        self.totalAmt.grid(row=0,column=1)
        self.gst.grid(row=1,column=1)
        self.netAmt.grid(row=2,column=1)


        '''Frame 3 RIGHT SIDE BAR'''
        typeOrderLabel=Label(self.frame3,text="Type of Order",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        orderType=["TAKE AWAY","DINE IN","HOME DELIVERY"]
        self.orderCombo=ttk.Combobox(self.frame3,values=orderType,state="readonly",height=4,width=25)
        addressLabel=Label(self.frame3,text="Address",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        self.addressText=Text(self.frame3,height=4,width=25)
        payModeLabel=Label(self.frame3,text="Mode Of Payment",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        payMode=["CASH","CREDIT CARD","PAYTM"]
        self.payModeCombo=ttk.Combobox(self.frame3,values=payMode,state="readonly",height=4,width=25)
        cashCollectedLabel=Label(self.frame3,text="Cash Collected",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        self.cashCollectedText=Entry(self.frame3)
        cashReturned=Label(self.frame3,text="Cash Returned",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        self.cashReturnedText=Entry(self.frame3,state="readonly")
        self.cashReturnedBtn=Button(self.frame3,text="CASH RETURN",command=self.cashReturn,bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        mobileLabel=Label(self.frame3,text="Mobile No.",bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        self.mobileText=Entry(self.frame3)
        typeOrderLabel.grid(row=0,column=4,padx=180)
        self.orderCombo.grid(row=0,column=5,padx=10)
        addressLabel.grid(row=1,column=4,padx=10)
        self.addressText.grid(row=1,column=5,padx=10)
        payModeLabel.grid(row=2,column=4,padx=10)
        self.payModeCombo.grid(row=2,column=5,padx=10)
        cashCollectedLabel.grid(row=3,column=4,padx=10)
        self.cashCollectedText.grid(row=3,column=5,padx=10)
        cashReturned.grid(row=4,column=4,padx=10)
        self.cashReturnedText.grid(row=4,column=5,padx=10)
        self.cashReturnedBtn.grid(row=4, column=6, padx=10)
        mobileLabel.grid(row=5,column=4,padx=10)
        self.mobileText.grid(row=5,column=5,padx=10)


        '''FRAME 4'''
        self.frame4 = PanedWindow(self.canvas)
        self.frame4.config(width=1200)
        generatePdf=Button(self.frame4,text="GENERATE BILL EXCEL ",command=self.generateexcel,width=20,bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        generateBill=Button(self.frame4,text="GENERATE BILL",command=self.generateBill,width=20,bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        resetButton=Button(self.frame4,text="RESET",command=self.allClear,width=20,bg="#89105f", fg="white",
                                   font=("Harlow Solid ", 15, "bold"))
        generatePdf.grid(row=0,column=1,padx=120)
        generateBill.grid(row=0,column=2,padx=120)
        resetButton.grid(row=0,column=3,padx=120)

        self.frame0.config(width=1200, bg="#89105f")
        self.frame1.config(width=1200, bg="#89105f")
        self.frame2.config(width=1200, bg="#89105f")
        self.frame3.config(width=1200, bg="#89105f")
        self.frame4.config(width=1200, bg="#89105f")

        self.frame0.pack()
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

        self.canvas.pack()



        self.root.mainloop()


#obj=addToCart()