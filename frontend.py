from tkinter import Listbox
from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("600x400")

l1=Label(window, text = "Contact List")
l1.grid(row=0,column=0)


l2=Label(window, text = "New Contact")
l2.grid(row=0,column=5)

l2=Label(window, text = "First Name:")
l2.grid(row=1,column=4)

l2=Label(window, text = "Last Name:")
l2.grid(row=2,column=4,columnspan=1)

l2=Label(window, text = "Phone #:")
l2.grid(row=3,column=4)

C1 = Checkbutton(window, text = "Friend")
C1.grid(row=4, column=5)

l2=Label(window, text = "Email:")
l2.grid(row=5,column=4)

l2=Label(window, text = "Birthday:")
l2.grid(row=6,column=4)

l2=Label(window, text = "Last Name:")
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


list1 = Listbox(window, height=12, width=22)
list1.grid(row=1,column=0,columnspan=1)

btn1 = ttk.Button(window, text="Add Contact")
btn1.grid(row=7, column=5)
btn2 = ttk.Button(window, text="Display Contact")
btn2.grid(row=2, column=0)
btn3 = ttk.Button(window, text="Search")
btn3.grid(row=9, column=1)

window.mainloop()