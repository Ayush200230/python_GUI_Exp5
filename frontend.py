from ctypes import alignment
from msilib.schema import ListBox
from tkinter import *

window = Tk()

l1=Label(window, text = "Contact List")
l1.grid(row=0,column=1)

l2=Label(window, text = "New Contact")
l2.grid(row=0,column=5)

l2=Label(window, text = "First Name:")
l2.grid(row=1,column=4)

l2=Label(window, text = "Last Name:")
l2.grid(row=2,column=4)

l2=Label(window, text = "Phone #:")
l2.grid(row=3,column=4)

l3=Label(window, text = "Friend")
l3.grid(row=4,column=5)

l2=Label(window, text = "Email:")
l2.grid(row=5,column=4)

l2=Label(window, text = "Birthday:")
l2.grid(row=6,column=4)

l2=Label(window, text = "Last Name")
l2.grid(row=8,column=0)

First_text = StringVar()
e1=Entry(window,textvariable=First_text)
e1.grid(row=1, column=5)

Last1_text = StringVar()
e2=Entry(window,textvariable=Last1_text)
e2.grid(row=2, column=5)

Phone_text = StringVar()
e3=Entry(window,textvariable=Phone_text)
e3.grid(row=3, column=5)

Email_text = StringVar()
e4=Entry(window,textvariable=Email_text)
e4.grid(row=5, column=5)

Birthday_text = StringVar()
e5=Entry(window,textvariable=Birthday_text)
e5.grid(row=6, column=5)

Last2_text = StringVar()
e6=Entry(window,textvariable=Last2_text)
e6.grid(row=8, column=1)


list1 = Listbox(window, height=10, width=20)
list1.grid(row=1,column=1,columnspan=1)

window.mainloop()