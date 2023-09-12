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
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
t = Tk()
t.geometry("720x1240")
t.resizable(0,0)
fontstyle = tfont.Font(family="Impect", size="15")
#===================Import Image==============================
Im=ImageTk.PhotoImage(file="D:\\new project\\profile-user.png")
Im1=ImageTk.PhotoImage(file="D:\\new project\\images (5).jpg")


#=========================SignUp Function====================================
def SignUpData():
	f6 = Frame(bg="#3399FF")
	f6.place(x=0, y=0, width=720, height=1240)


#=================================This Is Lables===================================================
	u8 = Label(f6, text="CodeWithMobile	 SIGN IN", fg="black", font="Times 25")
	u8.place(x=200, y=1)
	u9 = Label(f6, text="Registration Submit Successfully", fg="black", font="Times 25")
	u9.place(x=30, y=200)

#=====================================This Is Button======================================================

	b12 = Button(f6, text="Back", fg="white", bg="#6C7084", command=home)
	b12.place(x=0, y=0, width=130, height=40)
#=================================This Is Lables===================================================
	Label(f6, text="Your Name Is    :  ", fg="white", bg="#3399FF",font="Times 25").place(x=20, y=300)
	Label(f6, text=name.get(),fg="white", bg="#3399FF", font="Times 25").place(x=350, y=300)

#==================================This Is Lables==============================================
	Label(f6, text="Your Age Is       : ", fg="white", bg="#3399FF", font="Times 25").place(x=20, y=400)
	Label(f6, text=Age.get(),fg="white", bg="#3399FF", font="Timesl 25").place(x=350, y=400)

#====================================This Is Lables=================================================
	Label(f6, text="Your UserName Is  : ", fg="white", bg="#3399FF",font="Times 25").place(x=20, y=500)
	Label(f6, text=UserName.get(), fg="white", bg="#3399FF", font="Times 25").place(x=350, y=500)


#======================================This Is Lables==============================================
	Label(f6, text="Your Password Is : ",fg="white", bg="#3399FF", font="Times 25").place(x=20, y=600)
	Label(f6, text=Password.get(), fg="white", bg="#3399FF", font="Times 25").place(x=350, y=600)
def log():
	if UserN.get()=="" or Pass.get()=="":
		messagebox.showerror("Sign In Faild","All Feilds Are Requir?")
	elif UserN.get()==UserName.get() and Pass.get()==Password.get():
		def LogInData():
			messagebox.showinfo("Hallo "+name.get(),"WELCOME")

#================This Is Frame For User Profile===========================================================
			fr=Frame(bg="#f2f2f2")
			fr.place(x=0,y=0,height=1240,width=720)


#====================================Lables start=========================================================
			Label(fr,image=Im).place(x=300,y=0,height=130,width=130)

			lbl1=Label(fr,text=(f"Hallo, {name.get()}"), font="bold 40")
			lbl1.place(x=120,y=135,)


			lbl2=Label(fr,bg="#404040")
			lbl2.place(x=0,y=220,height=16,width=720)


			lbl3=Label(fr,bg="#1ab2ff")
			lbl3.place(x=0,y=236,height=700,width=720)


			lbl4=Label(fr, text="Account Info",bg="#1ab2ff", fg="White", font="Times 20")
			lbl4.place(x=280,y=280)


			lbl5=Label(fr,bg="#333333")
			lbl5.place(x=100,y=380,height=300,width=530)


			lbl6=Label(fr,text="Name",bg="#333333",fg="White",font="Times 20")
			lbl6.place(x=140,y=420)


			lbl7=Label(fr,text=name.get(),bg="#333333",fg="White",font="Times 20")
			lbl7.place(x=400,y=420)


			lbl8=Label(fr,text="Age",bg="#333333",fg="White",font="Times 20")
			lbl8.place(x=140,y=460)


			lbl8=Label(fr,text=Age.get(),bg="#333333",fg="White",font="Times 20")
			lbl8.place(x=400,y=460)


			lbl9=Label(fr,text="Username",bg="#333333",fg="White",font="Times 20")
			lbl9.place(x=140,y=500)


			lbl9=Label(fr,text=UserName.get(),bg="#333333",fg="White",font="Times 20")
			lbl9.place(x=400,y=500)


			lbl10=Label(fr,text="Password",bg="#333333",fg="White",font="Times 20")
			lbl10.place(x=140,y=540)


			lbl10=Label(fr,text=Password.get(),bg="#333333",fg="White",font="Times 20")
			lbl10.place(x=400,y=540)

#====================================Lables Stop=========================================================



			#This  Is Button 
			btn=Button(fr, text="Logout",bg="White", font="Times 20",command=home)
			btn.place(x=260,y=610,height=40,width=190)
		LogInData()
	else:
		messagebox.showerror("Password Wrong","Please Try Again?")





def home():
	#================This Is Frame For Home===========================================================
	f0 = Frame(bg="pink")
	f0.place(x=0, y=0, width=720, height=1240)
	u0 = Label(f0, text="CodeWithMobile", fg="black", font="Script 70").place(width=720, height="100")
	lb=Label(f0, image=Im1)
	lb.place(x=220,y=300)
	b1 = Button(f0, text="SIGN IN", fg="black", bg="#3399FF", font="Times 27", command=signin)
	b1.place(x=400, y=600, width=140, height=50)
	b0 = Button(f0, text="SIGN UP", fg="black", bg="#3399FF", font="Times 27", command=signup)
	b0.place(x=200, y=600, width=140, height=50)



#================This Is Frame For SignUp===========================================================
def signup():
	f1 = Frame(bg="#3399FF")
	f1.place(x=0, y=0, width=720, height=1240)
	u1 = Label(f1, text="CodeWithMobile	 SIGN UP", fg="black", font="Times 27")
	u1.place(x=200, y=1)
	b2 = Button(f1, text="Back", fg="white", bg="grey",font="Times 20", command=home)
	b2.place(x=0, y=0, width=130, height=40)



#========================1st fill box for Name start
	u2 = Label(f1, text="Enter Your Name: ", fg="white", bg="#3399FF",font="Times 20")
	u2.place(x=30, y=200)
	e0 = Entry(f1, textvariable=name,bg="lightgrey",font="Times 20")
	e0.place(x=383, y=200, width=250, height=40)
#========================1st fill box for Name stop


#=====================2nd fill box for Age start
	u3 = Label(f1, text="Enter Your Age: ", fg="white", bg="#3399FF",font="Times 20")
	u3.place(x=30, y=253)
	e1 = Entry(f1, textvariable=Age,bg="lightgrey",font="Times 20")
	e1.place(x=383, y=253, width=250, height=40)

#======================2nd fill box for Age start




#==================3rd fill box for UserName start
	u3 = Label(f1, text="Enter Your UserName: ", fg="white", bg="#3399FF",font="Times 20")
	u3.place(x=30, y=306)
	e1 = Entry(f1, textvariable=UserName,bg="lightgrey",font="Times 20")
	e1.place(x=383, y=306, width=250, height=40)
#3rd fill box for UserName start



#4th fill box start
	u4 = Label(f1, text="Create Your Password: ", fg="white", bg="#3399FF",font="Times 20")
	u4.place(x=30, y=359)
	e2 = Entry(f1, show="•", textvariable=Password,bg="lightgrey",font="Times 20")
	e2.place(x=383, y=359, width=250, height=40)
	b4 = Button(f1, text="SIGN UP", fg="white", bg="#3399FF",font="Times 27", command=SignUpData)
	b4.place(x=230, y=470, width=200, height=70)
#4th fill box start

#================Store entry start===========================================================
name = StringVar()
Age = IntVar()
UserName = StringVar()
Password = StringVar()
#================Store entry Stop===========================================================

def signin():
	#====================================User SignIn start=========================================================
	f2 = Frame(bg="#3399FF")
	f2.place(x=0, y=0, width=720, height=1240)
	u2 = Label(f2, text="CodeWithMobile	 SIGN IN",fg="Black", bg="White",font="Times 20")
	u2.place(x=200, y=1)
	b4 = Button(f2, text="Back", fg="white", bg="gray",font="Times 20", command=home)
	b4.place(x=0, y=0, width=130, height=40)
	lb=Label(f2, image=Im1)
	lb.place(x=220,y=220)


	u33 = Label(f2, text="Enter Your UserName: ",fg="white", bg="#3399FF",font="Times 20")
	u33.place(x=30, y=500)
	e30 = Entry(f2, textvariable=UserN,bg="lightgrey",font="Times 20")
	e30.place(x=370, y=500, width=250, height=40)





#2nd fill box
	u33 = Label(f2, text="Enter Your Password: ", fg="white", bg="#3399FF",font="Times 20")
	u33.place(x=30, y=553)
	e31 = Entry(f2, show="•", textvariable=Pass,bg="lightgrey",font="Times 20")
	e31.place(x=370, y=553, width=250, height=40)
	b35 = Button(f2, text="SIGN IN", fg="white", bg="#3399FF",font="Times 27", command=log)
	b35.place(x=230, y=670, width=200, height=70)



#====================================User SignIn stop=========================================================

#================Store entry start===========================================================
UserN = StringVar()
Pass = StringVar()
#================Store entry Stop===========================================================
signin()
signup()
home()
t.mainloop()