from tkinter import *
from tkinter.ttk import *
from connection import *



class addtocart:

    def priceClear(self):

        self.amountbox=Entry(self.frame3)
        self.gstbox=Entry(self.frame3)
        self.netamntbox=Entry(self.frame3)
        self.amountbox.grid(row=0,column=1)
        self.gstbox.grid(row=1,column=1)
        self.netamntbox.grid(row=2,column=1)


    # ''''''''''' FRAME 1'''''''

    def addMenuItem(self):
        cur = con.cursor()
        query = "select * from menu "

        cur.execute(query)
        self.data = cur.fetchall()
        print(self.data)


        self.combobox1 = []

        for i in self.data:
            print(i[1])
            print(self.combobox1)
            self.combobox1.append(i[1])


        print(self.combobox1)



    def quantity(self):
        self.menuQuantity=[]
        for i in range(1,11):
            self.menuQuantity.append(i)
            print(self.menuQuantity)



    def combobox1(self):

        self.serial = self.serial + 1
        self.addMenuItem()
        self.Qantity = self.combobox2.get()
        self.MenuNam = self.combobox1.get()
        print("Quantity:" + self.Qantity)
        print("Price:" + str(self.Price))
        self.totalPrice = (int(self.price) * int(self.Qantity))
        print("Total Price:" + str(self.totalPrice))
        self.treeData = [self.SerialNum, self.MenuName, self.Price, self.Qantity, self.TotalPrice]
        self.row = self.row + 1
        self.treeview.insert("", self.row, values=self.treeData)

    def priceCalculationBox(self):
        self.priceClear()

        self.amountbox['state'] = "normal"
        self.gstbox['state'] = "normal"
        self.netamntbox['state'] = "normal"


        self.amountbox.insert(0, self.totalAmtVar)
        self.gstbox.insert(0, self.gstAmtVar)
        self.netamntbox.insert(0, self.netAmtVar)
        self.amountbox['state'] = "readonly"
        self.gstbox['state'] = "readonly"
        self.netamntbox['state'] = "readonly"




    def fillTreeview(self):

        self.resetTreeview()

        for i in range(0, len(self.mainList)):
            self.treeview.insert("", i, values=self.mainList[i])
        self.pricecalculation()
        self.priceCalculationBox()


    def pricecalculation(self):

        print("MAINLIST")
        print(self.mainList)

        self.totalAmtVar=0
        for i in range(0,len(self.mainList)):

            self.totalAmtVar=self.mainList[i][4]+self.totalAmtVar

            print("Total Amount="+str(self.totalAmtVar))

        self.gstAmtVar=5*(0.01)
        self.netAmtVar=self.totalAmtVar+(self.totalAmtVar*self.gstAmtVar)
        print("Total Net:"+str(self.netAmtVar))

        print(str(self.totalAmtVar))
        print(str(self.gstAmtVar))
        print(str(self.netAmtVar))
        print('Total Amount: ' + str(self.totalAmtVar) + " " + str(self.gstAmtVar) + " " + str(self.netAmtVar))








    def addCart(self):
        self.serial = self.serial + 1
        self.menuName=self.combobox1.get()
        cur=con.cursor()
        query='select * from menu where name="'+self.menuName +'"'
        print(query)
        cur.execute(query)
        self.data=cur.fetchone()
        self.price=self.data[3]
        self.quantity=self.combobox2.get()
        self.totalPrice=(int(self.price)*int(self.quantity))

        print("SERIAL NUMBER:"+str(self.serial)+" Menu Name:"+self.menuName+"--Price:"+str(self.price)+"--Quantity:"+str(self.quantity)+"--Self.totalPrice"+str(self.totalPrice))
        self.sublist=[self.serial,self.menuName,self.price,self.quantity,self.totalPrice]
        print(self.sublist)

        self.mainList.append(self.sublist)

        print("MAIN LIST:")
        print(self.mainList)
        self.fillTreeview()






    def resetTreeview(self):

        for i in self.treeview.get_children():
            self.treeview.delete(i)


            # '''''''INSERT IN FRAME 3 PRICE CALCULATION''''



    def __init__(self):

        self.mainList=[]


        self.serial = 0
        self.row = 0
        self.window=Tk()
        self.frame1=PanedWindow()
        self.addMenuItem()
        self.quantity()
        self.slctname=Label(self.frame1,text="SELECT NAME")
        self.combobox1=Combobox(self.frame1,value=self.combobox1,state="readonly")





        self.slctquantity=Label(self.frame1,text="SELECT QUANTITY")
        self.combobox2=Combobox(self.frame1,value=self.menuQuantity)



        self.addbttn=Button(self.frame1,text="ADD TO CART",command=self.addCart)


        self.slctname.grid(row=0,column=0)
        self.combobox1.grid(row=0,column=1)


        self.slctquantity.grid(row=0,column=2)
        self.combobox2.grid(row=0,column=3)


        self.addbttn.grid(row=0,column=4)






        # '''''''''''''FRAME 2'''''

        self.frame2=PanedWindow()



        self.treeview=Treeview(self.frame2,column=("SerialNum","MenuName","Price","Qantity","TotalPrice"))
        self.treeview.heading("SerialNum",text="SERIAL NUMBER")
        self.treeview.heading("MenuName",text="MENU NAME")
        self.treeview.heading("Price",text="PRICE")
        self.treeview.heading("Qantity",text="QUANTITY")
        self.treeview.heading("TotalPrice",text="TOTAL PRICE")

        self.treeview["show"]="headings"




        self.treeview.pack()






        # '''''''''''''FRAME 3'''''''''''''''''


        self.frame3=Tk()

        self.frame3=PanedWindow()

        self.totalAmnt=Label(self.frame3,text="TOTAL AMOUNT")
        self.gst=Label(self.frame3,text="GST")
        self.netAmnt=Label(self.frame3,text="NET AMOUNT")






        self.totalAmnt.grid(row=0,column=0)
        self.gst.grid(row=1,column=0)
        self.netAmnt.grid(row=2,column=0)













        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.window.mainloop()

obj=addtocart()



# self.t=StringVar()
#
#         self.total=Label(self.frame3,textvariable=self.t)
#         self.t.set("hi")
#
#
#
#         self.g=StringVar()
#         self.gst=Label(self.frame3,textvariable=self.g)
#         self.g.set("hey")
#
#
#
#
#         self.n=StringVar()
#         self.netamount=Label(self.frame3,textvariable=self.n)
#         self.n.set("hello")
#
#
#
#
#
#
#
#         self.gst=Label(self.frame3,text="GST")
#
#
#         self.netamount=Label(self.frame3,text="NET AMOUNT")
