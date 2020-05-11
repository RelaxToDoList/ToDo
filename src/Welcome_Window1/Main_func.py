import os.path
import DBfunctions
import sqlite3
import random
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
from MainWindow import Ui_Core
from Settings import Ui_Settings
from statistic import Ui_Statistic

class Second_Windo(object): ##Window of signing in
	def signin(self, first_name, second_name): ##Window of signing in
		if not first_name:
			self.error()
			return
		elif not last_name:
			self.error()
			return
		else:
			if check_signin(first_name) == 1:
				self.nextWindow()
			else:
				global User_ID
				User_ID = random.randint(1000, 10000)
				data = [User_ID, first_name, last_name, None]
				DBfunctions.write_in_db_user(data)
				self.nextWindow()

	def check_signin(first_name):
		if DBfunctions.read_db('count(User_ID)', 'user') == 0:
			return 0
		elif DBfunctions.str_compare(first_name, 'user') == 0:
			return 0
		else:
			global User_ID
			User_ID = DBfunctions.read_db('User_ID', 'user', 'First', first_name)
			return 1



class Third_Window(Ui_Welcome): ## Window of Welcoming user
	def show_username(self):
		self.usersname.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))




class Fifth_Window(Ui_Core): ## Main Window
	def show_task(self, text_task):
		self.deal_text.setText(DBfunctions.read_db('Task_text', 'tasks', 'User_ID', User_ID))

	def Add_Task(self):
		text_task = self.line_enter.text()
		task = [None, None, None, text_task, User_ID]
		DBfunctions.write_in_db_tasks(task)
		self.line_enter.clear()
		show_task(text_task)

	def show_first_last(self):
		self.FirstName.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
		self.SecondName.setText(DBfunctions.read_db('Last', 'user', 'User_ID', User_ID))




class Settings_Menu(Ui_Settings):
	def change_name_func(self): ##Settings menu
		self.change_name_pressed()
		self.save_change.clicked.connect(self.save_changes_button)
	def change_secname_func(self):
		self.change_secname_pressed()
		self.save_change.clicked.connect(self.save_changes_button)

	def save_changes_button(self):
		first_name = self.firstname_change.text()
		second_name = self.secondname_change.text()
		if first_name:
			DBfunctions.update_record('user', 'First', str(first_name), 'User_ID', User_ID)
			self.name.setText(first_name)
		if second_name:
			DBfunctions.update_record('user', 'Last', str(second_name), 'User_ID', User_ID)
			self.secname.setText(second_name)
		self.close_line_edit()

	def choose_picture_dialog_open(self, pict_path):
		fname = pict_path
		if not fname[0]:
			return;
		pict_path = fname[0]
		DBfunctions.pict_import(User_ID, pict_path)
