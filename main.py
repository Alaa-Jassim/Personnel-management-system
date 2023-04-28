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

import threading
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 


class Main(threading.Thread,Tk):
	""" The main class for im`plementing the application """

	def __init__(self):
		Tk.__init__(self)
		self.class_info = Widgets(self)
		self.class_employee_sections = Sections(self)
