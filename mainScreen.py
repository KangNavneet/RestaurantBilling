from tkinter import *

class mainScreen:



    def __init__(self):



        root = Toplevel()
        self.root.geometry("1000x1000")
        mainBar = Menu(root)
        self.mainmenu = Menu(mainBar, tearoff=0)

        '''MENU'''
        menuDetail = Menu(mainBar, tearoff=0)
        menuDetail.add_command(label="ADD MENU")
        menuDetail.add_command(label="MENU TREE")
        menuDetail.add_command(label="SEARCH MENU")
        menuDetail.add_command(label="UPDATE MENU")
        #filemenu.add_separator()

        mainBar.add_cascade(label="MENU", menu=menuDetail)




        '''STAFF'''
        staffDetail = Menu(self.mainBar, tearoff=0)
        staffDetail.add_command(label="ADD STAFF")
        staffDetail.add_command(label="STAFF TREE")
        mainBar.add_cascade(label="STAFF", menu=staffDetail)


        '''ADD TO CART'''

        self.mainmenu.add_command(label="ADD TO CART")



        '''KITCHEN SCREEN'''

        self.mainmenu.add_command(label="KITCHEN SCREEN")



        root.config(menu=mainBar)
        root.mainloop()


obj=mainScreen()