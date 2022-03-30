from email import message
from tkinter import *
from smtpd import SMTPServer
import smtplib

a = Tk()
a.geometry('400x300')
a.resizable(0, 0)

a1 = Label(a, text='Kiruvchi e-mail')
a1.pack()

etr_sign = StringVar()
a2 = Entry(a, textvariable=etr_sign)
a2.pack(ipadx=40)

b = Label(a, text='Jonatish e-mail')
b.pack()
etr_rec = StringVar()
b1 = Entry(a, textvariable=etr_rec)
b1.pack(ipadx=40)

b2 = Label(a, text='Matn')
b2.pack()

etr_ms = StringVar()
b3 = Entry(a, textvariable=etr_ms)
b3.pack(ipadx=40)

b4 = Label(a, text='Jonatish soni')
b4.pack()
etr_cou = StringVar()
b5 = Entry(a, textvariable=etr_cou)
b5.pack()


def function():
    for i in range(1,int(etr_cou.get())+1):    
        sender = etr_sign.get()
        receiver = etr_rec.get()
        password = 'reigyrgzslhognrl'
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(sender, password)
        msg = etr_ms.get()
        smtpserver.sendmail(sender, receiver, msg)
        print(i)
        smtpserver.close()


b6 = Button(a, text='Jonatish', command=function)
b6.pack(ipadx=12)

a.mainloop()


