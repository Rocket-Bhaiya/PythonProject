######################################################################
# -------------------------------------------------------------------#
#|                       Programmer Info                            |#
#--------------------------------------------------------------------#
#|                  Author     :   Abhishek Patel                   |#
#|                  Programmer :   Abhishek Patel                   |#
#|                  Blog       :   codewithmobile.tech.blog         |#
#|                  Product    :   Login SignUp System              |#
#|                 __Copyright__ By CodeWithMobile                  |#
#|                 __License__ By CodeWithMobile                    |#
#--------------------------------------------------------------------#
######################################################################
from tkinter import *
import tkinter.font as tfont

t = Tk()
t.geometry("720x900")
t.resizable(0,0)
fontstyle = tfont.Font(family="Impect", size="15")

f0 = Frame(bg="pink")
f0.place(x=0, y=0, width=720, height=900)
u0 = Label(f0, text="CodeWithMobile", fg="black", font="Script 60").place(width=720, height="100")

M_Name=Label(t,text="Password",bg="white",fg="#3A3B3C",font="Times 20 bold", background="pink")
M_Name.place(x=150, y=400)
E_Name=Entry(t,bg="lightgrey",font="Times 15 bold",bd=0)
E_Name.place(x=300, y=404)

b1 = Button(f0, text="SIGN IN", fg="black", bg="#3399FF", font="Times 27")
b1.place(x=250, y=600, width=140, height=50)
# b0 = Button(f0, text="SIGN UP", fg="black", bg="#3399FF", font="Times 27", command=signup)
# b0.place(x=200, y=600, width=140, height=50)

# ====Store entry Stop===========================================================


t.mainloop()