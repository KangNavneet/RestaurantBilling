from tkinter.messagebox import showinfo

from reportlab.lib.pagesizes import *
from reportlab.pdfgen import canvas
import random
import subprocess
class pdfReport:
    def __init__(self,dataList,netAmt):


        name = str(random.randint(0, 100))
        name_pdf = str("pdfbills//a" + str(name) + ".pdf")
        my_canv = canvas.Canvas(name_pdf, pagesize=A5)
        my_canv.setFont('Helvetica', 20)
        my_canv.setLineWidth(.5)
        y = 580
        my_canv.drawString(160, y-1, 'Sales Report')
        my_canv.line(10, y - 3, 500, y - 3)


        my_canv.setFont('Helvetica', 10)
        my_canv.drawString(10, y - 12, "BILL ID")
        my_canv.drawString(70, y - 12, "TYPE OF ORDER")
        #my_canv.drawString(80, y - 12, "ADDRESS")
        my_canv.drawString(170, y - 12, "MODE OF PAYMENT")
        # my_canv.drawString(200, y - 12, "CASH COLLECTED")
        # my_canv.drawString(260, y - 12, "CASH RETURNED")
        # my_canv.drawString(320, y - 12, "MOBILE NUMBER")
        my_canv.drawString(270, y - 12, "NET AMOUNT")
        my_canv.drawString(370, y - 12, "GST")
      #  my_canv.drawString(490, y - 12, "DATE")
        y = y - 12
        my_canv.line(10, y - 3, 1000, y - 3)
        my_canv.setFont('Helvetica', 8)
        y = y - 3
        s = dataList
        print(s)
        gst = 5
        gst1=0.01*gst


        netAmt = netAmt

        totalAmt=netAmt/(1+gst1)

        print("TOTAL:"+str(totalAmt))
        print("GST:"+str(gst))
        print("NET AMOUNT:"+str(netAmt))




        for i in range(0, len(s)):
            my_canv.drawString(10, y - 12, str(s[i][0]))
            my_canv.drawString(70, y - 12, str(s[i][1]))
           # my_canv.drawString(210, y - 12, str(s[i][2]))
            my_canv.drawString(170, y - 12, str(s[i][3]))

            my_canv.drawString(270, y - 12, str(s[i][7]))
            my_canv.drawString(370, y - 12, str(s[i][8]))

            y = y - 12
        my_canv.line(10, y - 3, 1000, y - 3)
        y = y - 3
        my_canv.drawString(230, y - 12, "Total")
        my_canv.drawString(230, y - 24, "GST")
        my_canv.drawString(230, y - 36, "Payable")
        my_canv.drawString(330, y - 12, str(totalAmt))
        my_canv.drawString(330, y - 24, "5%")

        my_canv.drawString(330, y - 36, str(netAmt))
        my_canv.save()
        subprocess.Popen([name_pdf], shell=True)
        showinfo('', 'sales pdf generated stored at ' + str("pdfbills//a" + str(name) + ".pdf"))


