from tkinter import *
import tkinter 
root = Tk()

fw = 220
fh = 150
x  = ( root.winfo_screenwidth() - fw ) / 2
y  = ( root.winfo_screenheight() - fh ) / 2

from tkinter import messagebox

def submit():
   if txt_name.get()=="Orange" and txt_password.get() =="CodingAcademy" :
       print("Name: "+ txt_name.get() + "\n"+"Password: "+txt_password.get())
   else:
        print("Wrong UserName Or Password")

name = Label(root,text="Name").place( x = 30 , y=40)
email = Label(root,text="Emial").place( x = 30 , y=80)

e1 = Entry(root,text="Name").place( x = 70 , y=40)
e2 = Entry(root,text="Emial").place( x = 70 , y=80)

submit = Button(root,text="Submit").place( x = 30 , y=110)

root.geometry( '%dx%d+%d+%d' %(fw,fh,x,y) )



































"""
from tkinter import Tk
from tkinter import *
from tkinter import messagebox



def Pressed():
    dialog_title= "Please Answer"
    dialog_text = "Do You Like To Travel ? "

    answer = messagebox.askquestion(dialog_title,dialog_text)


    if answer == "Yes" :
        print(" I Like This !")
    else:
        print("You must have clicked the wrong button by accident.")



root = Tk()


button = Button(root,text="press Me" ,command = Pressed )
button.pack(pady=40,padx=40)

root.mainloop()
"""


