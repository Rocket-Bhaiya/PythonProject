######################################################################
# -------------------------------------------------------------------#
#|                       Programmer Info                            |#
#--------------------------------------------------------------------#
#|                  Author     :   Abhishek Patel                   |#
#|                  Programmer :   Abhishek Patel                   |#
#|                  Blog       :   codewithmobile.tech.blog         |#
#|                  Product    :   SignUp System                    |#
#|                  YouTube    :   CodeWithMobile                   |#
#--------------------------------------------------------------------#
######################################################################

from tkinter import *
from PIL import ImageTk,Image
import tkinter.font as tfont
from tkinter import messagebox
import sqlite3
import time


root = Tk()
root.geometry("644x461+370+195")
root.title('Registration Form')
root.resizable(0,0)
fontstyle = tfont.Font(family="Impect", size="15")
root.wm_iconbitmap('profile.ico')



#=================================================================================
#------------------------------Store Entry-----------------------------------------
#=================================================================================


Name=StringVar()
lname=StringVar()
Age=IntVar()
Number=IntVar()
Username=StringVar()
Password=StringVar()
Email=StringVar()
City=StringVar()


#-----------------------------------------------------------------------------------------




def SignUp_Data():
    if Name.get()=='' or lname.get()=='' or Age.get()=='' or Number.get()=='' or Username.get()=='' or Password.get()=='' or Email.get()=="" or City.get()=='':
        messagebox.showerror('Empty', "All Feilds Are Require ")
    else:

        #=================================================================================
		#------------------------------Connect With Database------------------------------
		#=================================================================================
        conn=sqlite3.connect("codewithmobile.db")
        conn.execute("create table IF NOT EXISTS data (fname text,lname text,age int,number int,username text,password text,city text,email text)")
        
        command=f"insert into data (fname,lname,age,number,username,password,city,email) Values('{Name.get()}','{lname.get()}','{Age.get()}','{Number.get()}','{Username.get()}','{Password.get()}','{City.get()}','{Email.get()}')"
        conn.execute(command)
        conn.commit()
        #=========backup txt file===================
        f=open("C:\\Users\\msi\\Desktop\\Record.txt", "a")
        f.write(f"{Name.get()},{lname.get()},{Age.get()},{Number.get()},{Username.get()},{Password.get()},{Email.get()},{City.get()}\n")
    e1.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    messagebox.showinfo("REGISTRATION","SUCCESS")
    time.sleep(1)
    def log():
        root.destroy()
        import login
    log()

#--------------------------------------------------------------------------------------------------------------------




#=================================================================================
#------------------------------SignUp Box Start-----------------------------------
#=================================================================================

Im12=ImageTk.PhotoImage(file="image\\bg4.jpg")
er=Label(root,image=Im12).place(x=0,y=0)
er=Label(root,bg="Grey",fg="white",text="SignUp System",font='Times 40',bd=0).place(x=70,y=20,height=100,width=500)
we=Label(root,bg="white",bd=0).place(x=170,y=130,height=300,width=300)


s5=Label(root,bg="white",fg='grey',text="First Name",font='Times 15',bd=0).place(x=183,y=140)
e1=Entry(root, textvariable=Name,bg="lightgrey",bd=0,font='Times 10')
e1.place(x=183,y=170)
s1=Label(root,bg="white",fg='grey',text="Age",font='Times 15',bd=0).place(x=183,y=190)
e2=Entry(root,bg="lightgrey",bd=0,textvariable=Age,font='Times 10')
e2.place(x=183,y=220)
e2.delete(0,END)
s2=Label(root,bg="white",fg='grey',text="Username",font='Times 15',bd=0).place(x=183,y=240)
e3=Entry(root,bg="lightgrey",bd=0,textvariable=Username,font='Times 10')
e3.place(x=183,y=270)
s3=Label(root,bg="white",fg='grey',text="City",font='Times 15',bd=0).place(x=183,y=290)
e4=Entry(root,bg="lightgrey",bd=0,textvariable=City,font='Times 10')
e4.place(x=183,y=320)


Label(root,bg='grey',bd=0).place(x=317,y=150,height=190,width=2)


e55=Label(root,bg="white",fg='grey',text="Last Name",font='Times 15',bd=0).place(x=329,y=140)
e5=Entry(root,bg="lightgrey",bd=0,font='Times 10',textvariable=lname)
e5.place(x=329,y=170)
s445=Label(root,bg="white",fg='grey',text="Number",font='Times 15',bd=0).place(x=329,y=190)
e6=Entry(root,bg="lightgrey",bd=0,textvariable=Number,font='Times 10')
e6.place(x=329,y=220)
e6.delete(0,END)

s544=Label(root,bg="white",fg='grey',text="Password",font='Times 15',bd=0)
s544.place(x=329,y=240)
e7=Entry(root,bg="lightgrey",bd=0,textvariable=Password,font='Times 10')
e7.place(x=329,y=270)
s45=Label(root,bg="white",fg='grey',text="Email",font='Times 15',bd=0).place(x=329,y=290)
e8=Entry(root,bg="lightgrey",bd=0,textvariable=Email,font='Times 10')
e8.place(x=329,y=320)
b345=Button(root,text="REGISTER NOW",command=SignUp_Data,bd=0,bg="#36af2e",font="Times 10 bold",fg="white",activebackground="#30ff5c", activeforeground="lightgrey").place(x=195,y=370,height=30,width=250)



#=================================================================================
#------------------------------SignUp Box Stop-----------------------------------
#=================================================================================

#----------------------------------------------------------------------------------------------------------

root.mainloop()


#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#--------------------------------------------------------The End-------------------------------------------------------------------
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
