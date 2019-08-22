from http.client import*
from tkinter.messagebox import showinfo


class sms:
    def __init__(self,message,mobileNo):
        msg =message
        mobile = str(mobileNo)

        msg = msg.replace(" ", "%20")
        msg = msg.replace(":", "%3A")

        conn = HTTPConnection("server1.vmm.education")
        conn.request('GET',
                     "/VMMCloudMessaging/AWS_SMS_Sender?""username=monika&password=L78E7CIB&message=" + msg + "&phone_numbers=" + mobile)
        response = conn.getresponse()
        print(response.read())
        showinfo("Message","SMS SENT")
        
