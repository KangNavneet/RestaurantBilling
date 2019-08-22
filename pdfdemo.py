from tkinter.messagebox import showinfo
from saleReport import *
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas
import random
import subprocess
class pdfGenerator:
    def __init__(self,dataList,netAmt):

        name = str(random.randint(0, 100))
        name_pdf = str("pdfbills//a" + str(name) + ".pdf")
        my_canv = canvas.Canvas(name_pdf, pagesize=A1)
        my_canv.setFont('Helvetica', 14)
        my_canv.setLineWidth(.2)
        y = 400
        my_canv.drawString(160, y, 'Sales Report')
        my_canv.line(10, y - 3, 400, y - 3)

        my_canv.setFont('Helvetica', 10)
        my_canv.drawString(30, y - 12, "BILL ID")
        my_canv.drawString(130, y - 12, "TYPE OF ORDER")
        my_canv.drawString(230, y - 12, "ADDRESS")
        my_canv.drawString(330, y - 12, "MODE OF PAYMENT")
        my_canv.drawString(430, y - 12, "CASH COLLECTED")
        my_canv.drawString(530, y - 12, "CASH RETURNED")
        my_canv.drawString(630, y - 12, "MOBILE NUMBER")
        my_canv.drawString(730, y - 12, "NET AMOUNT")
        my_canv.drawString(830, y - 12, "GST")
        my_canv.drawString(930, y - 12, "DATE")
        y = y - 12
        my_canv.line(10, y - 3, 400, y - 3)
        my_canv.setFont('Helvetica', 8)
        y = y - 3
        s = dataList
        print(s)
        netTotal = netAmt
        gst=5
        total=netAmt/(0.01*gst)

        for i in range(0, len(s)):
            my_canv.drawString(30, y - 12, str(s[i][0]))
            my_canv.drawString(50, y - 12, str(s[i][1]))
            my_canv.drawString(70, y - 12, str(s[i][2]))
            my_canv.drawString(100, y - 12, str(s[i][3]))
            my_canv.drawString(120, y - 12, str(s[i][4]))
            my_canv.drawString(130, y - 12, str(s[i][5]))
            my_canv.drawString(140, y - 12, str(s[i][6]))
            my_canv.drawString(150, y - 12, str(s[i][7]))
            my_canv.drawString(160, y - 12, str(s[i][8]))
            my_canv.drawString(170, y - 12, str(s[i][9]))
            y = y - 12
        my_canv.line(10, y - 3, 1000, y - 3)
        y = y - 3
        my_canv.drawString(230, y - 12, "Total")
        my_canv.drawString(230, y - 24, "GST")
        my_canv.drawString(230, y - 36, "Payable")
        my_canv.drawString(330, y - 12, str(total))
        my_canv.drawString(330, y - 24, "5%")
        na = total - ((5 * total) / 100)
        my_canv.drawString(330, y - 36, str(na))
        my_canv.save()
        subprocess.Popen([name_pdf], shell=True)
        showinfo('', 'sales pdf generated stored at ' + str("pdfbills//a" + str(name) + ".pdf"))


