


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from PIL import Image , ImageTk
from datetime import datetime
import os , sys , shutil
import sqlite3
import time
from threading import Thread
from vacations.treeview_vacations import TreeviewVacations
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 

class DataBaseVacations:
	def __init__(self,root):
		self.root = root 
		
		self.main_database_employees = os.path.abspath(".")
		self.joins_path_main_database_employees = os.path.join(self.main_database_employees,"DataBaseEmployees.db")



		self.create_database_vacations()

		self.class_treeview_vacations = TreeviewVacations(self.root)
		self.class_treeview_vacations.ShowTreeview()

		self.run_function_select_data_vacations = Thread(target=self.class_treeview_vacations.select_data_vacations(),args=())
		self.run_function_select_data_vacations.start()

		self.class_treeview_vacations.table_vacations.bind('<ButtonRelease-1>',self.get_cursor)



		self.var_coincidence_day = StringVar()
		self.var_number_days_vacation = StringVar()
		self.var_section = StringVar()
		self.var_name = StringVar()
		self.var_date_coincidence = StringVar()
		self.var_type_coincidence = StringVar()
		self.var_id = StringVar()
		self.var_email = StringVar()
		self.variable_search_employee_vacations = StringVar()



	def create_database_vacations(self):
		self.connection = sqlite3.connect("vacations\\database_vacations.db")
		self.cursor = self.connection.cursor()

		self.cursor.execute(""" CREATE TABLE IF NOT EXISTS VacationsEmployee
		 (coincidence_day TEXT NOT NULL , number_days_vacation TEXT NOT NULL ,
		 Section TEXT NOT NULL , Name TEXT NOT NULL , date_coincidence TEXT NOT NULL ,
		 type_coincidence TEXT NOT NULL , ID TEXT NOT NULL , Email TEXT NOT NULL)""")


		self.connection.commit()


	def check_data(self):
		if self.var_email.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل البريد الإلكتروني فارغاً" , parent=self.root)
		elif self.var_id.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل الرقم الوظيفي فارغاً" , parent=self.root)

		elif self.var_type_coincidence.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل نوع الإجازة فارغاً" , parent=self.root)
		elif self.var_date_coincidence.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل تأريخ الإجازة فارغاً" , parent=self.root)


		elif self.var_name.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل إسم الموظف فارغاً" , parent=self.root)

		elif self.var_name.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل إسم الموظف فارغاً" , parent=self.root)

		elif self.var_section.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل القسم الوظيفي فارغاً" , parent=self.root)

		elif self.var_number_days_vacation.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل عدد أيام الإجازة فارغاً" , parent=self.root)

		elif self.var_coincidence_day.get() == "":
			messagebox.showerror("خطأ" , "لا يمكن ترك حقل اليوم المصادف للإجازة فارغاً" , parent=self.root)

		else :
			if self.confirm_data_vacation() == False:
				messagebox.showerror("خطأ" , "هذه المعلومات غير مسجلة في النظام الرجاء التحقق من صحة المعلومات" , parent=self.root)
			else :
				self.message_question = messagebox.askquestion("هل توافق عبى هذا الإجراء ؟" , "هل توافق على حفظ هذه البيانات في قاعدة البيانات؟" , parent=self.root)
				if self.message_question == 'yes':
					self.save_data() 
				else:
					pass





	def confirm_data_vacation(self):
		
		self.connection_date = sqlite3.connect(self.joins_path_main_database_employees)
		self.cursor_data = self.connection_date.cursor()

		self.cursor_data.execute('SELECT * FROM Employees WHERE Email=? AND ID=? AND Name=? '
			,(self.var_email.get(),self.var_id.get(),self.var_name.get()))

		if self.cursor_data.fetchall() :
			return True
		return False
	
		self.connection_date.commit()
		self.connection_date.close()





	def save_data(self):
		self.connection_insert = sqlite3.connect("vacations\\database_vacations.db")
		self.cursor_insert = self.connection_insert.cursor()

		self.cursor_insert.execute(""" INSERT INTO VacationsEmployee VALUES
		 (?,?,?,?,?,?,?,?)"""
		 ,(self.var_coincidence_day.get() ,self.var_number_days_vacation.get() , self.var_section.get(),
		 	self.var_name.get() , self.var_date_coincidence.get(),self.var_type_coincidence.get(),
		 	self.var_id.get(),self.var_email.get()))

		self.connection_insert.commit()
		self.run_function_select_data_vacations = Thread(target=self.class_treeview_vacations.select_data_vacations(),args=())
		self.clean_data_vacations()
		self.run_function_select_data_vacations.start()



	def clean_data_vacations(self):
		self.var_coincidence_day.set('') ; self.var_number_days_vacation.set('') ; self.var_section.set('');
		self.var_name.set('') ; self.var_date_coincidence.set('') ; self.var_type_coincidence.set('');
		self.var_id.set('') ; self.var_email.set('');



	def get_cursor(self,ev):

		try :
			self.cursor_row = self.class_treeview_vacations.table_vacations.focus()
			self.contents = self.class_treeview_vacations.table_vacations.item(self.cursor_row)
			self.row = self.contents['values']

			self.var_coincidence_day.set(self.row[0]) ; self.var_number_days_vacation.set(self.row[1]) ; self.var_section.set(self.row[2]);
			self.var_name.set(self.row[3]) ; self.var_date_coincidence.set(self.row[4]) ; self.var_type_coincidence.set(self.row[5]);
			self.var_id.set(self.row[6]) ; self.var_email.set(self.row[7]);

			
		except Exception as error :
			pass


	def update_data_vacations(self):
		if not os.path.exists("vacations\\database_vacations.db"):
			raise FileNotFoundError(f"The Path Not Found Error")

		
		
		self.connection_update_table = sqlite3.connect("vacations\\database_vacations.db")
		self.cursor_update_table = self.connection_update_table.cursor()
		self.sql_query = """UPDATE VacationsEmployee SET coincidence_day=? ,number_days_vacation=? , Section=?,
		 				 Name=? , date_coincidence=? ,type_coincidence=? WHERE ID=? AND Email=? """
		 				 
		 				 

		self.cursor_update_table.execute(self.sql_query,(self.var_coincidence_day.get() , self.var_number_days_vacation.get(),
														self.var_section.get() , self.var_name.get() , self.var_date_coincidence.get(),
														self.var_type_coincidence.get() , self.var_id.get() , self.var_email.get()))
		
		self.cursor_update_table.execute(""" SELECT * FROM VacationsEmployee""")
		self.class_treeview_vacations.table_vacations.delete(*self.class_treeview_vacations.table_vacations.get_children())
		
		for self.row in self.cursor_update_table.fetchall():
			self.class_treeview_vacations.table_vacations.insert('',END , value=self.row)
		
		
		self.connection_update_table.commit()
		self.clean_data_vacations()
		self.connection_update_table.close()
		
		
		






	def delete_data_vacations(self):
		""" Function Delete Al Data from Table AttendanceDeparture"""

		self.connection_delete = sqlite3.connect("vacations\\database_vacations.db")
		self.cursor_delete = self.connection_delete.cursor()

		self.messageDeleteAll = messagebox.askquestion('هل توافق على هذا الإجراء','عند موافقتك سيتم حذف قاعدة البيانات بالكامل' , parent=self.root)
		if self.messageDeleteAll == 'yes':
			self.cursor_delete.execute('DELETE FROM VacationsEmployee')
			self.class_treeview_vacations.table_vacations.delete(*self.class_treeview_vacations.table_vacations.get_children())

			for self.row in self.cursor_delete.fetchall() :
				self.class_treeview_vacations.table_vacations.insert('',END,value=self.row)

		self.connection_delete.commit()
		self.connection_delete.close()




	def show_data_vacations(self):
		self.connection_show = sqlite3.connect("vacations\\database_vacations.db")
		self.cursor_show = self.connection_show.cursor()

		self.cursor_show.execute('SELECT * FROM VacationsEmployee')
		if self.cursor_show.fetchall():
			self.run_function_select_data_vacations = Thread(target=self.class_treeview_vacations.select_data_vacations(),args=())
			self.run_function_select_data_vacations.start()


		self.connection_show.commit()
		self.connection_show.close() 



	def search_employee_vacations(self):
		""" The Function Search Data  from Table AttendanceDeparture """

		self.connection_search = sqlite3.connect("vacations\\database_vacations.db")
		self.cursor_search = self.connection_search.cursor()

		self.cursor_search.execute('SELECT * FROM VacationsEmployee WHERE ID =?',(self.variable_search_employee_vacations.get(),))
		self.result_search = self.cursor_search.fetchall()

		if not self.result_search:
			messagebox.showerror("خطا" , "ليست هناك نتائج بحث الرجاء إعادة المحاولة والتحقق من رقم الموظف" , parent=self.root)
		else :
			self.cursor_search.execute('SELECT * FROM VacationsEmployee WHERE ID =?',(self.variable_search_employee_vacations.get(),))
			self.class_treeview_vacations.table_vacations.delete(*self.class_treeview_vacations.table_vacations.get_children())

			for self.row in self.result_search :
				self.class_treeview_vacations.table_vacations.insert('',END,value=self.row)
		self.connection_search.commit()
		self.connection_search.close()



		




