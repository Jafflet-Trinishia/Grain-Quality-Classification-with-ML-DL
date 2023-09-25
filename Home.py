import tkinter as tk
from tkinter import Message ,Text
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import tkinter.messagebox as tm
import psycopg2
from tkinter import filedialog
import tkinter.messagebox as tm
from tkinter import ttk
import CNN as cnn
import KNN as knn

def Main():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Postgresql")

	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)
	
	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

	message1 = tk.Label(window, text="Postgresql" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)

	lbl = tk.Label(window, text="Select Dataset Folder",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=10, y=200)

	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=300, y=215)
	
	def browse():
		path=filedialog.askdirectory()
		print(path)
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Dataset Folder")	


	def knnprocess():
		sym=txt.get()
		if sym != "":
			knn.process(sym)
			tm.showinfo("Input", "KNN finished Successfully")

		else:
			tm.showinfo("Input error", "Select Dataset Folder")

	def cnnprocess():
		sym=txt.get()
		if sym != "":
			cnn.process(sym)
			tm.showinfo("Input", "CNN Finished Successfully")

		else:
			tm.showinfo("Input error", "Select Dataset Folder")
		
	def logout():
		window.destroy()
		Home()
		

	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=530, y=205)

	texta = tk.Button(window, text="KNN", command=knnprocess  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	texta.place(x=520, y=600)

	pred = tk.Button(window, text="CNN", command=cnnprocess  ,fg=fgcolor,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	pred.place(x=760, y=600)

	quitWindow = tk.Button(window, text="Logout", command=logout  ,fg=fgcolor ,bg=bgcolor  ,width=18  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=1020, y=600)

	window.mainloop()



def Home():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Postgresql")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

	def login():
		print("Login")
		window.destroy()
		Login()
		
	def home():
		print("Home")
		window.destroy()
		Home()

	def signup():
		print("Signup")
		window.destroy()
		Signup()
	
	message1 = tk.Label(window, text="Postgresql" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	home = tk.Button(window, text="Home", command=home  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	home.place(x=140, y=120)

	signup = tk.Button(window, text="Signup", command=signup  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	signup.place(x=340, y=120)

 
	login = tk.Button(window, text="Login", command=login  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	login.place(x=540, y=120)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=740, y=120)



	

	window.mainloop()


def Login():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Postgresql")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

		
	message1 = tk.Label(window, text="Postgresql" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	#message2 = tk.Label(window, text="Content Here dddddddddddddddd" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	#message2.place(x=50, y=250)		
    
	def login():
		print("Login")
		window.destroy()
		Login()	
	def home():
		print("Home")
		window.destroy()
		Home()

	def signup():
		print("Signup")
		window.destroy()
		Signup()

	def submit():
		print("submit")
		sym=txt.get()
		sym1=txt1.get()
		if sym != "" and sym1 != "":
			conn = psycopg2.connect(user = "postgres",password = "ammaappa123.",host = "127.0.0.1",port = "5432",database = "login")
			cursor = conn.cursor()
			cmd="SELECT username,password FROM login WHERE username='"+sym+"' and password='"+sym1+"'"
			print(cmd)
			cursor.execute(cmd)
			
			isRecordExist=0
			for row in cursor:
				isRecordExist=1
			if(isRecordExist==1):
			        tm.showinfo("Input", "Lgoin Succesfully")
			        window.destroy()
			        Main()
			else:
				tm.showinfo("Input", "Check Username and Password")
		else:
			tm.showinfo("Input error", "Enter UserName And Password")
	
	home = tk.Button(window, text="Home", command=home  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	home.place(x=140, y=150)

	signup = tk.Button(window, text="Signup", command=signup  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	signup.place(x=340, y=150)

 
	login = tk.Button(window, text="Login", command=login  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	login.place(x=540, y=150)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=740, y=150)
	
	lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=300, y=300)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=600, y=315)

	lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=300, y=400)
	
	txt1 = tk.Entry(window,show="*",width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=600, y=415)

	submit = tk.Button(window, text="Submit", command=submit  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	submit.place(x=600, y=550)
	
	window.mainloop()
def Signup():
	global window
	bgcolor="#ECFDB0"
	fgcolor="black"
	window = tk.Tk()
	window.title("Postgresql")
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)

		
	message1 = tk.Label(window, text="Postgresql" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	message1.place(x=100, y=10)		
    
	#message2 = tk.Label(window, text="Content Here dddddddddddddddd" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
	#message2.place(x=50, y=250)		
    
	def login():
		print("Login")
		window.destroy()
		Login()	
	def home():
		print("Home")
		window.destroy()
		Home()

	def signup():
		print("Signup")
		window.destroy()
		Signup()

	def submit():
		print("submit")
		sym=txt.get()
		sym1=txt1.get()
		sym2=txt2.get()
		sym3=txt3.get()
		if sym != "" and sym1 != "" and sym2 != "" and sym3 != "":
			conn = psycopg2.connect(user = "postgres",password = "ammaappa123.",host = "127.0.0.1",port = "5432",database = "login")
			cursor = conn.cursor()
			cmd="SELECT * FROM login WHERE username='"+sym+"'"
			print(cmd)
			cursor.execute(cmd)
			print(cursor)
			isRecordExist=0
			for row in cursor:
				isRecordExist=1
			if(isRecordExist==1):
			        tm.showinfo("Input", "Username Already Exists")
			else:
				print("insert")
				cmd="INSERT INTO login Values('"+sym+"','"+sym1+"','"+sym2+"','"+sym3+"')"
				print(cmd)
				tm.showinfo("Input","Inserted Successfully")
				cursor.execute(cmd)
				conn.commit()
				conn.close() 

			
		else:
			tm.showinfo("Input error", "Enter UserName And Password")
	
	home = tk.Button(window, text="Home", command=home  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	home.place(x=140, y=150)

	signup = tk.Button(window, text="Signup", command=signup  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	signup.place(x=340, y=150)

 
	login = tk.Button(window, text="Login", command=login  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	login.place(x=540, y=150)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor  ,bg=bgcolor ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=740, y=150)
	
	lbl = tk.Label(window, text="User Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=300, y=250)
	
	txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=600, y=265)

	lbl1 = tk.Label(window, text="Password",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=300, y=300)
	
	txt1 = tk.Entry(window,show="*",width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=600, y=315)

	lbl2 = tk.Label(window, text="Name",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=300, y=350)
	
	txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=600, y=365)

	lbl3 = tk.Label(window, text="Email",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=300, y=400)
	
	txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=600, y=415)

	submit = tk.Button(window, text="Submit", command=submit  ,fg=fgcolor  ,bg=bgcolor  ,width=16  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	submit.place(x=600, y=550)
	
	window.mainloop()
	
Home()
#Main()