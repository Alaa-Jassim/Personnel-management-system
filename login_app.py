
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from datetime import datetime
from PIL import Image
from widegts_app import Widgets
import sqlite3
from PIL import Image , ImageTk
from tkinter import filedialog
from threading import Thread
from sections.sections import Sections

from main import Main
import threading
from babel.dates import format_date, parse_date, get_day_names 
from babel.numbers import * 
import os 

class CreateNewAccount(Tk):
	""" The class responsible for creating a new account or registering a new account in the database"""
	def __init__(self):
		Tk.__init__(self)
		self.geometry('925x500+500+200')
		self.resizable(width=False , height=False)
		self.configure(background='#fff')
		self.title('إنشاء حساب')
		self.iconbitmap("images_login\\title_new_account.ico")

		self.database_sign_in = os.path.abspath(".")
		self.joins_database_sign_in = os.path.join(self.database_sign_in,"DataBaseSign-In.db")

		self.create_username = StringVar()
		self.create_password = StringVar()
		self.password_confirm = StringVar()


		self.add_logo_sing_up()
		self.add_labels_info_sign_up()
		self.add_button_create_account()


		

	def add_logo_sing_up(self):
		self.cut_image_sing_up = Image.open("images_login\\sing_up.png")
		self.cut_image_sing_up = self.cut_image_sing_up.resize((350,350))
		self.image_logo_sing_up = ImageTk.PhotoImage(self.cut_image_sing_up)

		self.label_logo_new = Label(
			self.master , image=self.image_logo_sing_up , border=0 ,bg='white')
		self.label_logo_new.place(x=50,y=90)


	def click_username_entry(self,value):
		self.input_username_sign_up.delete(0,END)

	def click_username_leave(self,valeu):
		self.value_username = self.input_username_sign_up.get()
		if self.value_username == '':
			self.input_username_sign_up.insert(0,"المستخدم إسم")



	def click_password_entry(self,value):
		self.input_password_sign_up.delete(0,END)

	def click_password_leave(self,valeu):
		self.value_password = self.input_password_sign_up.get()
		if self.value_password == '':
			self.input_password_sign_up.insert(0,"المرور كلمة")




	def click_password_confirm_entry(self,value):
		self.input_confirm_password.delete(0,END)

	def click_password_confirm_leave(self,valeu):
		self.value_password_confirm = self.input_confirm_password.get()
		if self.value_password_confirm == '':
			self.input_confirm_password.insert(0,"المرور كلمة تأكيد")



	def add_labels_info_sign_up(self):

		
		self.main_frame_sign_up = Frame(
			self , borderwidth=0 , background='black' , width=350,height=350,bg='#fff'

			).place(x=480,y=50)


		self.heading_label_sign_up = Label(self.main_frame_sign_up,
			text="حساب إنشاء",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23 ,"bold"))
		self.heading_label_sign_up.place(x=580,y=70)

		#======================================================================================

		self.input_username_sign_up = Entry(self.main_frame_sign_up ,font=("Microsoft YaHei UI Light",11 ,"bold"),bg='white',
			fg='black',border=0 ,width=25,textvariable=self.create_username)
		self.input_username_sign_up.place(x=496,y=140)
		self.input_username_sign_up.insert(0, "المستخدم إسم")
		self.input_username_sign_up.bind('<FocusIn>',self.click_username_entry)
		self.input_username_sign_up.bind('<FocusOut>',self.click_username_leave)

		self.farme_user_desgin_sign_up = Frame(self.main_frame_sign_up,
			width=295,height=2,bg="black")
		self.farme_user_desgin_sign_up.place(x=496,y=165)





		#===================================================================================
		self.input_password_sign_up = Entry(self.main_frame_sign_up ,font=("Microsoft YaHei UI Light",11 ,"bold"),bg='white',
			fg='black',border=0 ,width=25,textvariable=self.create_password)
		self.input_password_sign_up.place(x=496,y=240)
		self.input_password_sign_up.insert(0, "المرور كلمة")
		self.input_password_sign_up.bind('<FocusIn>',self.click_password_entry)
		self.input_password_sign_up.bind('<FocusOut>',self.click_password_leave)

		self.farme_pass_desgin_sign_up = Frame(self.main_frame_sign_up,
			width=295,height=2,bg="black")
		self.farme_pass_desgin_sign_up.place(x=496,y=265)

		#=====================================================================================


		self.farme_pass_confirm_desgin_sign_up = Frame(self.main_frame_sign_up,
			width=295,height=2,bg="black")
		self.farme_pass_confirm_desgin_sign_up.place(x=496,y=380)



		self.input_confirm_password = Entry(self.main_frame_sign_up ,font=("Microsoft YaHei UI Light",11 ,"bold"),bg='white',
			fg='black',border=0 ,width=25,textvariable=self.password_confirm)
		self.input_confirm_password.place(x=496,y=353)
		self.input_confirm_password.insert(0,"المرور كلمة تأكيد")

		self.input_confirm_password.bind('<FocusIn>',self.click_password_confirm_entry)
		self.input_confirm_password.bind('<FocusOut>',self.click_password_confirm_leave)



	def add_button_create_account(self):
		""" Open Window Login Account """

		self.button_create_account = Button(self.main_frame_sign_up,
			font=('bold',13) , bg="#57a1f8" , fg='white' ,pady=7 ,border=0,
			width=32,text="إنشاء الحساب" ,command=self.check_data_create_account)
		self.button_create_account.place(x=498,y=397)



	def check_data_create_account(self):
		if self.create_username.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل إسم المستخدم فارغاً!")
		elif self.create_password.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل كلمة المرور فارغاً!")
		elif self.password_confirm.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل تأكيد كلمة المرور فارغاً")

		elif self.password_confirm.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل تأكيد كلمة المرور فارغاً!")

		elif self.create_password.get() != self.password_confirm.get():
			messagebox.showerror("خطأ" ,"كلمة المرور غير متطابقة!")
		else :
			self.question = messagebox.askquestion("هل توافق على هذا هذا الإجراء ؟" , "هل توافق على إنشاء الحساب بهذه المعلومات؟")
			if self.question == "yes":
				self.insert_dataToSQlite3()
				self.destory_main_createaccount()



	def insert_dataToSQlite3(self):
		
		self.connection_insert = sqlite3.connect(self.joins_database_sign_in)
		self.cursor_insert = self.connection_insert.cursor()

		self.cursor_insert.execute("""INSERT INTO SignIn VALUES (?,?,?) """,
			(self.create_username.get() , self.create_password.get() , self.create_password.get()))

		self.connection_insert.commit()




	def destory_main_createaccount(self):
		self.destroy()
		self.class_login = LoginApplication()
		self.class_login.mainloop()



class LoginApplication(Tk):
	""" The class responsible for logging into the application """
	def __init__(self):
		Tk.__init__(self)
		self.geometry('925x500+500+200')
		self.resizable(width=False , height=False)
		self.configure(background='#fff')
		self.title('تسجيل الدخول')
		self.iconbitmap("images_login\\title_icon.ico")
		self.database_sign_in = os.path.abspath(".")
		self.joins_database_sign_in = os.path.join(self.database_sign_in,"DataBaseSign-In.db")

		self.var_username = StringVar()
		self.var_password = StringVar()


		self.create_database_signIN()



	def create_database_signIN(self):
	
		self.connection_sign = sqlite3.connect(self.joins_database_sign_in)
		self.cursor_sign = self.connection_sign.cursor()

		self.cursor_sign.execute(""" CREATE TABLE IF NOT EXISTS SignIn 
			(username TEXT NOT NULL ,
			password TEXT NOT NULL ,
			confirm_password TEXT NOT NULL)""")

		self.connection_sign.commit()
		self.connection_sign.close()


		
	
		self.add_logo()
		self.add_labels_info()
		self.add_button()
		self.add_button_sign_up()


	def add_logo(self):
		self.cut_image = Image.open("images_login\\login.png")
		self.cut_image = self.cut_image.resize((450,450))
		self.image_logo = ImageTk.PhotoImage(self.cut_image)
		self.label_logo = Label(
			self , image=self.image_logo , borderwidth=0 ,bg='white'

			).place(x=50,y=20)

	def on_entry_user(self,e):
		self.entry_user.delete(0,'end')

	def on_leave_user(self,e):
		self.name = self.entry_user.get()
		if self.name == '':
			self.entry_user.insert(0,"مستخدم إسم")


	def on_entry_pass(self,e):
		self.entry_password.delete(0,'end')

	def on_leave_pass(self,e):
		self.name_pass = self.entry_password.get()
		if self.name_pass == '':
			self.entry_password.insert(0,"مرور كلمة")



	def add_labels_info(self):

		
		self.main_frame = Frame(
			self , borderwidth=0 , background='black' , width=350,height=350,bg='white'

			).place(x=550,y=90)

		self.heading_label = Label(self,
			text="الدخول تسجيل",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23 ,"bold"))
		self.heading_label.place(x=670,y=105)


		#======================================================================================================
		self.entry_user = Entry(
			self.main_frame , width=25 ,fg="black" , border=0 , bg="white" ,
			 font=("Microsoft YaHei UI Light",11),textvariable=self.var_username)

		self.entry_user.place(x=590,y=180)
		self.entry_user.insert(0, "المستخدم إسم")
		self.entry_user.bind('<FocusIn>',self.on_entry_user)
		self.entry_user.bind('<FocusOut>',self.on_leave_user)


		self.farme_user_desgin = Frame(self.main_frame,
			width=295,height=2,bg="black")
		self.farme_user_desgin.place(x=590,y=205)

		#======================================================================================================

		self.entry_password = Entry(
			self.main_frame , width=25 ,fg="black" , border=0 , bg="white" , 
			font=("Microsoft YaHei UI Light",11),textvariable=self.var_password)
		self.entry_password.bind('<FocusIn>',self.on_entry_pass)
		self.entry_password.bind('<FocusOut>',self.on_leave_pass)



		self.entry_password.place(x=590,y=290)
		self.entry_password.insert(0, "المرور كلمة")


		self.farme_password_desgin = Frame(self.main_frame,
			width=295,height=2,bg="black")
		self.farme_password_desgin.place(x=590,y=315)

		#======================================================================================================



	def add_button(self):
		""" Open Window Login Account """
		
		self.button_login = Button(self.main_frame,
			font=('bold',13) , bg="#57a1f8" , fg='white' ,pady=7 ,border=0,
			width=32,text="تسجيل الدخول" ,command=self.check_data_login,)
		self.button_login.place(x=590,y=335)



	def add_button_sign_up(self):
		self.label_not_account = Label(self.main_frame,
			text="؟ حساب لديك ليس",fg="black",bg="white",font=("Microsoft YaHei UI Light",11))
		self.label_not_account.place(x=796,y=400)


		self.button_sign_up = Button(self.main_frame,
			bg='white' ,cursor="hand2" ,fg="#57a1f8",border=0,width=6,
			text="تسجيل" ,font=("Microsoft YaHei UI Light",12),command=self.open_application_sign_up)
		self.button_sign_up.place(x=740,y=398)




	def check_data_login(self):

		if self.var_username.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل إسم المستخدم فارغا")
		elif self.var_password.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل كلمة المرور  فارغا")

		else :
			self.select_data_login()

				

	def select_data_login(self):
		
		self.connection_view = sqlite3.connect(self.joins_database_sign_in)
		self.cursor_select_view = self.connection_view.cursor()

		self.cursor_select_view.execute("""SELECT username , password  FROM SignIn WHERE username=? AND password=? """,
			(self.var_username.get(),self.var_password.get()))

		self.result = self.cursor_select_view.fetchall()
		if not self.result :
			messagebox.showerror("خطأ" ,"هذه المعلومات غير صحيحية الرجاء التحقق من صحة المعلومات")
		else:
			self.question = messagebox.askquestion("هل توفقنا على هذا الإجراء ؟" , "هل توافق على تسجيل الدخول ؟")
			if self.question == 'yes':
				self.open_application_main()
			

		self.connection_view.commit()


	def open_application_main(self):
		self.destroy()
		main_application = Main()
		main_application.mainloop()

	def open_application_sign_up(self):
		self.destroy()
		application_sign_up = CreateNewAccount()
		application_sign_up.mainloop()



if __name__=='__main__':
	main_class = LoginApplication()
	main_class.mainloop()
