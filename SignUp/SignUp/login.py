######################################################################
# -------------------------------------------------------------------#
#|                       Programmer Info                            |#
#--------------------------------------------------------------------#
#|                  Author     :   Abhishek Patel                   |#
#|                  Programmer :   Abhishek Patel                   |#
#|                  Blog       :   codewithmobile.tech.blog         |#
#|                  Product    :   Login System                     |#
#|                 __Copyright__ By CodeWithMobile                  |#
#|                 __License__ By CodeWithMobile                    |#
#--------------------------------------------------------------------#
######################################################################
from tkinter import *
import tkinter.font as tfont
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
import sqlite3
t = Tk()
t.geometry("645x430+370+195")
t.resizable(0,0)
t.title("Login System")
fontstyle = tfont.Font(family="Impect", size="15")
# t.wm_iconbitmap('profile.ico')

#=================================================================================
#------------------------------Store Entry-----------------------------------------
#=================================================================================
Username=StringVar()
Password=StringVar()

#-----------------------------------------------------------------------------------



#=================================================================================
#------------------------------Add Images-----------------------------------------
#=================================================================================
Im=ImageTk.PhotoImage(file="image\\profile-user.png")
bg2=ImageTk.PhotoImage(file="image\\bg2.jpg")
bg1=ImageTk.PhotoImage(file="image\\bg3.jpg")
bg4=ImageTk.PhotoImage(file="image\\logout.png")


#-----------------------------------------------------------------------------------


#=================================================================================
#------------------------------Func Function--------------------------------------
#=================================================================================


def func():
	if Username.get()=='' or Password.get()=='':
		messagebox.showerror('Empty', "All Feilds Are Require ",icon="warning")
	#======Connect With Sqlite3 Database======================
	else:


		#=================================================================================
		#------------------------------Connect With Database------------------------------
		#=================================================================================



		def sql_func(self):
			self.conn=sqlite3.connect("codewithmobile.db")
			self.cur=self.conn.cursor()
			self.query = f"select * from data where username ='{Username.get()}' AND password='{Password.get()}';"
			self.data=self.cur.execute(self.query)
			if not self.cur.fetchone():
				messagebox.showerror("Login Fail","Wrong Password,\nPlease Enter Correct Password",icon="warning")
				e1.delete(0,END)
				e2.delete(0,END)
			else:



				#=================================================================================
				#------------------------------Fetch All Data From Database-----------------------
				#=================================================================================


				self.d=self.cur.fetchone()
				self.d[0]#fname
				self.d[1]#lname			
				self.d[2]#age
				self.d[3]#number
				self.d[4]#username
				self.d[5]#Password
				self.d[6]#city
				self.d[7]#Email




				#=================================================================================
				#------------------------------Profile Start--------------------------------------
				#=================================================================================


				messagebox.showinfo(f'Welcome',f"Hi, {self.d[0]} {self.d[1]}",icon="info")
				t.geometry("645x800+370+2")
				t.title("Profile")
				t.resizable(0,0)
				fontstyle = tfont.Font(family="Impect", size="15")
				
				#---------------Image Label---------------#


				labl1=Label(t,image=bg2)
				labl1.place(x=0,y=0)
				#---------------Label---------------#


				labl2=Label(t,bg="#d0f0f8",text="Welcome",font="Times 25 bold",fg="#3A3B3C")
				labl2.place(x=0,y=20,height=54,width=645)




				#---------------Label---------------#
				labl2=Label(t,bg="#d0d6d4",text=f"Hi, {self.d[0]} {self.d[1]}",font="Times 25 bold",fg="#3A3B3C")
				labl2.place(x=0,y=80,height=54,width=645)




				#---------------Label---------------#
				labl2=Label(t,bg="#3A3B3C")
				labl2.place(x=72,y=170,height=554,width=500)



				#---------------Label---------------#
				labl2=Label(t,bg="#3A3B3C",text="Account Info",font="Times 25 bold",fg="#d0d6d4")
				labl2.place(x=230,y=180)



				#---------------Label---------------#
				labl2=Label(t,bg="#d0d6d4")
				labl2.place(x=72,y=170,height=5,width=500)



				#---------------Label---------------#
				labl2=Label(t,bg="#d0d6d4")
				labl2.place(x=72,y=170,height=554,width=5)



				#---------------Label---------------#
				labl2=Label(t,bg="#d0d6d4")
				labl2.place(x=72,y=720,height=5,width=500)



				#---------------Label---------------#
				labl2=Label(t,bg="#d0d6d4")
				labl2.place(x=570,y=170,height=554,width=5)



				#---------------Label---------------#
				labl2=Label(t,bg="#d0d6d4")
				labl2.place(x=72,y=234,height=5,width=500)



				#---------------Label---------------#
				labl45=Label(t,bg="#d0d6d4")
				labl45.place(x=72,y=260,height=2,width=500)


				#---------------Label---------------#
				lbl6=Label(t,text="Name",bg="#3A3B3C",fg="White",font="Times 20")
				lbl6.place(x=120,y=280)


				#---------------Label---------------#
				lbl7=Label(t,text=f"{self.d[0]} {self.d[1]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl7.place(x=340,y=280)


				#---------------Label---------------#
				lbl8=Label(t,text="Age",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=120,y=320)


				#---------------Label---------------#
				lbl8=Label(t,text=f"{self.d[2]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=340,y=320)


				#---------------Label---------------#
				lbl19=Label(t,text="Number",bg="#3A3B3C",fg="White",font="Times 20")
				lbl19.place(x=120,y=360)


				#---------------Label---------------#
				lbl8=Label(t,text=f"{self.d[3]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=340,y=360)


				#---------------Label---------------#
				lbl19=Label(t,text="Username",bg="#3A3B3C",fg="White",font="Times 20")
				lbl19.place(x=120,y=400)


				#---------------Label---------------#
				lbl8=Label(t,text=f"{self.d[4]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=340,y=400)


				#---------------Label---------------#
				lbl19=Label(t,text="Password",bg="#3A3B3C",fg="White",font="Times 20")
				lbl19.place(x=120,y=440)


				#---------------Label---------------#
				lbl8=Label(t,text=f"{self.d[5]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=340,y=440)


				#---------------Label---------------#
				lbl19=Label(t,text="City",bg="#3A3B3C",fg="White",font="Times 20")
				lbl19.place(x=120,y=480)


				#---------------Label---------------#
				lbl8=Label(t,text=f"{self.d[6]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=340,y=480)


				#---------------Label---------------#
				lbl19=Label(t,text="Email",bg="#3A3B3C",fg="White",font="Times 20")
				lbl19.place(x=120,y=520)


				#---------------Label---------------#
				lbl8=Label(t,text=f"{self.d[7]}",bg="#3A3B3C",fg="White",font="Times 20")
				lbl8.place(x=340,y=520)


				#---------------Label---------------#
				labl45=Label(t,bg="#d0d6d4")
				labl45.place(x=72,y=580,height=2,width=500)
				labl45=Label(t,bg="#d0d6d4")


				#---------------Label---------------#
				labl45.place(x=72,y=600,height=5,width=500)
				#---------------Label---------------#


				#---------------Logout Func---------------#
				def logout():
					messagebox.showinfo("Logout",f"Success {self.d[0]} {self.d[1]}")
					t.destroy()
					import login
				bt1=Button(t,image=bg4,bd=0,command=logout)
				bt1.place(x=80,y=640,height=30,width=489)
				#=================================================================================
				#------------------------------Profile Stop---------------------------------------
				#=================================================================================
		sql_func(self=sql_func)
#=================================================================================
#------------------------------Function Stop--------------------------------------
#=================================================================================

#-----------------------------------------------------------------------------------

#=================================================================================
#------------------------------Login Box Start------------------------------------
#=================================================================================
labl1=Label(t,image=bg1)
labl1.place(x=0,y=0)
#---------------Label---------------#
labl2=Label(t,bg="#3A3B3C",text="Sign In System",font="Times 25 bold",fg="lightgrey")
labl2.place(x=0,y=20,height=54,width=645)
#---------------Frame---------------#
F1=Frame(t,bg="#3A3B3C")
F1.place(x=90,y=97,height=300,width=457)
#---------------Label---------------#
labl3=Label(F1,text="Username",bg="#3A3B3C",fg="lightgrey",font='Times 20 bold')
labl3.place(x=30,y=23)
#---------------Entry---------------#
e1=Entry(F1,font="Times 12 bold",textvariable=Username,bd=0,fg="#3A3B3C",bg="lightgrey")
e1.place(x=230,y=30,height=24,width=180)
#---------------Label---------------#
labl3=Label(F1,text="Password",bg="#3A3B3C",fg="lightgrey",font='Times 20 bold')
labl3.place(x=32,y=86)
#---------------Entry---------------#
e2=Entry(F1,show="*",font="Times 12 bold",textvariable=Password,bd=0,fg="#3A3B3C",bg="lightgrey")
e2.place(x=230,y=90,height=24,width=180)
#---------------Button---------------#
b345=Button(F1,text="Login",bd=0,bg="#36af2e",command=func,font="Times 12 bold",fg="white",activebackground="#30ff5c", activeforeground="lightgrey").place(x=45,y=190,height=30,width=360)

#-----------------------------------------------------------------------------------

#=================================================================================
#------------------------------Forget Password Start------------------------------
#=================================================================================


def forget_password():
	messagebox.showinfo("Forget Password","Comming Soon")

#=================================================================================
#------------------------------Forget Password Stop-------------------------------
#=================================================================================

#-----------------------------------------------------------------------------------

#=================================================================================
#------------------------------SignUp Func Start----------------------------------
#=================================================================================
def signup():
	t.destroy()
	import SignUp

#=================================================================================
#------------------------------SignUp Func Start----------------------------------
#=================================================================================






#-----------------------------------------------------------------------------------









#=================================================================================
#------------------------------Forget Password And SignUp  Button Start-----------
#=================================================================================

Button(F1,text="Forget Password?",bg="#3A3B3C",fg="Lightgrey",bd=0,activebackground="#3A3B3C",command=forget_password).place(x=150,y=250)
Button(F1,text="SignUp",bg="#3A3B3C",fg="Lightgrey",bd=0,activebackground="#3A3B3C",command=signup).place(x=245,y=250)
#=================================================================================
#------------------------------Forget Password And SignUp  Button Stop------------
#=================================================================================





#-----------------------------------------------------------------------------------








#=================================================================================
#------------------------------Login Box Stop-------------------------------------
#=================================================================================

t.mainloop()


#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#--------------------------------------------------------The End-------------------------------------------------------------------
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================
#==================================================================================================================================