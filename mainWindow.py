
from addMenu import *
from addMenuTree import *
from updateMenu import *
from addStaff import *
from addToCart import *
from staffTree import *
from searchMenu import *
from kitchenScreen1 import *
from changePassword import *
from changeEmail import *
from pygame import mixer

from PIL import ImageTk,Image

import time
from threading import Thread

wn=""
p=FALSE
class mainWindow:

    '''Menu'''
    def addMenu(self):
        obj=addMenu(self.root)

    def reOpen(self):
        print("LOGOUT")
        global p
        p=False
        from restaurantLogin import restaurantLogin

        obj =restaurantLogin()
        self.root.destroy()


    def exit(self):
        self.root.destroy()



    def updateMenu(self):
        obj=updateMenu(self.root)
    def addMenuTree(self):
        obj = addMenuTree(self.root)
    def searchMenu(self):
        obj=searchMenu(self.root)


    '''STAFF'''
    def addStaff(self):
        obj=addStaff(self.root)
    def staffTree(self):
        obj=staffTree(self.root)



    '''CART '''
    def addToCart(self):
        obj=addToCart(self.root)

    def kitchenScreen(self):
        obj=kitchenScreen1(self.root)


    '''SALE REPORT'''
    def saleReport(self):
        obj = saleReport(self.root)

    '''CHANGE PASSWORD'''
    def changePassword(self):
        obj=changePassword(self.root,self.username,self.password)

    '''CHANGE EMAIL'''
    def changeEmail(self):
        obj=changeEmail(self.root,self.username,self.password)

    '''EXIT SCREEN'''
    def exitScreen(self):
        worker().stop()
        sys.exit()


    def __init__(self,parent,username,password):
        global wn,p
        p=True
        self.username=username
        self.password=password
        self.root = Toplevel()
        wn=self.root

        self.root.transient(parent)
        self.root.parent = parent

        # self.root.attributes("-fullscreen",True)
        self.root.iconbitmap("i.ico")
        self.root.title("Main Page")

        width_value = self.root.winfo_screenwidth()
        height_value = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (width_value, height_value))
        self.root.resizable(0, 0)
        worker().start()
        self.root.config(bg="#89105f", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")

        '''ADD RESTAURANT CANVAS'''



        #self.root.geometry("1200x1200")
        #
        #self.root.attributes("-fullscreen",True)
        self.mainBar=Menu(self.root)
        self.root.config(menu=self.mainBar)
        self.mainmenu = Menu(self.mainBar, tearoff=0)
        '''MENU'''
        menuDetail = Menu(self.mainmenu, tearoff=0)
        menuDetail.add_command(label="ADD MENU", command=lambda: self.addMenu())
        menuDetail.add_command(label="FULL MENU DATABASE", command=lambda: self.addMenuTree())
        menuDetail.add_command(label="SEARCH MENU", command=lambda: self.searchMenu())
        menuDetail.add_command(label="UPDATE MENU", command=lambda: self.updateMenu())
        self.mainBar.add_cascade(label="MENU", menu=menuDetail)


        '''STAFF'''
        staffDetail = Menu(self.mainmenu, tearoff=0)
        staffDetail.add_command(label="ADD STAFF", command=lambda: self.addStaff())
        staffDetail.add_command(label="STAFF DETAILS", command=lambda: self.staffTree())
        self.mainBar.add_cascade(label="STAFF", menu=staffDetail)


        '''ADD TO CART'''

        self.mainBar.add_command(label="CART", command=lambda: self.addToCart())

        '''KITCHEN SCREEN'''

        self.mainBar.add_command(label="KITCHEN SCREEN", command=lambda: self.kitchenScreen())

        '''SALE REPORT'''

        self.mainBar.add_command(label="SALE REPORT", command=lambda: self.saleReport())

        '''CHANGE PASSWORD'''
        self.mainBar.add_command(label='CHANGE PASSWORD', command=lambda:self.changePassword())

        '''CHANGE EMAIL'''
        self.mainBar.add_command(label='CHANGE EMAIL', command=lambda:self.changeEmail())

        self.mainBar.add_command(label="LOGOUT",command=self.reOpen)
        self.mainBar.add_command(label='EXIT', command=lambda: self.exitScreen())



        self.root.mainloop()



class worker(Thread):
    def run(self):
        global  wn
        lst = [ "splashScreen/1.png", "splashScreen/5.png"]
        i = 0

        self.canvas = Canvas(wn, bg='black', relief="raised")
        self.canvas.configure(bg='black')
        self.canvas.pack( expand="yes",fill=BOTH)
        self.canvas.config(bg="black", highlightthickness=6, highlightbackground="#89105f", highlightcolor="#fff2f2")

        '''CANVAS'''
        while(p==True):

            gif1 = PhotoImage(file=str(lst[i]))
            self.canvas.create_image(50, 10, image=gif1, anchor=NW)
            i=i+1
            time.sleep(2)

            if i==2:
                i=0



    def stop(self):
        exit=True


