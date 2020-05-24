import unittest
import os.path
import Functions
import DBfunctions
import Create_db
import datetime
class TestFucn(unittest.TestCase):

	def setUp(self):
		User_ID = 1
		first_name = "Danil"
		last_name = "Waterfall"
		data = [User_ID,first_name,last_name, None]
		DBfunctions.write_in_db_user(data)
		position = 1
		status = 0
		time = datetime.date.today()
		text_task = "Hello World"
		data = [position,status,str(time),str(24.0),text_task,User_ID]
		DBfunctions.write_in_db_tasks(data)
		DBfunctions.create_in_db_pb(User_ID)
		column = 'Completed'
		record = 20
		DBfunctions.write_in_db_pb(column, record, 'week_pb', User_ID)
		column = 'Failed'
		record = 40
		DBfunctions.write_in_db_pb(column, record, 'week_pb', User_ID)
		column = 'Completed'
		record = 3
		DBfunctions.write_in_db_pb(column, record, 'daily_pb', User_ID)
		column = 'Failed'
		record = 7
		DBfunctions.write_in_db_pb(column, record, 'daily_pb', User_ID)

	def tearDown(self):
		User_ID = 1
		DBfunctions.delete_record('user','User_ID',User_ID)
		DBfunctions.delete_record('week_pb','User_ID',User_ID)
		DBfunctions.delete_record('daily_pb','User_ID',User_ID)
		DBfunctions.delete_record('tasks','User_ID',User_ID)

	# def test_main_signin_empty(self):
	# 	name = 'random'
	# 	result = Main_File.Second_Window.check_signin(self,name)
	# 	self.assertFalse(result)
	#
	# def test_main_signin_name(self):
	# 	first_name = 'Danil'
	# 	result = Main_File.Second_Window.check_signin(self,first_name)
	# 	self.assertTrue(result)
	#
	# def test_main_check_daily_progressbar_today(self):
	# 	User_ID = 1
	# 	result = Main_File.Third_Window.check_daily_progressbar(self, User_ID)
	# 	self.assertIsNone(result)
	#
	# def test_main_check_daily_progressbar_not_today(self):
	# 	User_ID = 1
	# 	DBfunctions.write_in_db_pb('Date','2021-05-22','tasks',User_ID)
	# 	Main_File.Third_Window.check_daily_progressbar(self, User_ID)
	# 	c = DBfunctions.read_db('Completed','daily_pb','User_ID',User_ID)
	# 	f = DBfunctions.read_db('Failed','daily_pb','User_ID',User_ID)
	# 	result = c + f
	# 	self.assertFalse(result)
	#
	# def test_main_check_task_today(self):
	# 	User_ID = 1
	# 	result = Main_File.Third_Window.check_tasks(self, User_ID)
	# 	self.assertIsNone(result)
	#
	# def test_main_check_task_not_today(self):
	# 	User_ID = 1
	# 	DBfunctions.update_record('tasks','Date','2021-05-22','User_ID', User_ID )
	# 	Main_File.Third_Window.check_tasks(self, User_ID)
	# 	result = DBfunctions.read_db('count(Num_Task)', 'tasks', 'User_ID', User_ID)
	# 	self.assertFalse(result)
	#
	def test_main_adding_fail_daily(self):
		User_ID = 1
		Functions.Add_Task.add_fail(User_ID)
		result = DBfunctions.read_db('Failed','daily_pb','User_ID',User_ID)
		self.assertEqual(result, 8)

	def test_main_adding_fail_week(self):
		User_ID = 1
		Functions.Add_Task.add_fail(User_ID)
		result = DBfunctions.read_db('Failed','week_pb','User_ID',User_ID)
		self.assertEqual(result, 41)

	def test_main_adding_complete_daily(self):
		User_ID = 1
		position = 1
		Functions.Add_Task.add_complete(User_ID, position)
		result = DBfunctions.read_db('Failed','daily_pb','User_ID',User_ID)
		self.assertEqual(result, 6)
		result = DBfunctions.read_db('Completed','daily_pb','User_ID',User_ID)
		self.assertEqual(result, 4)

	def test_main_adding_complete_week(self):
		User_ID = 1
		position = 1
		Functions.Add_Task.add_complete(User_ID, position)
		result = DBfunctions.read_db('Failed','week_pb','User_ID',User_ID)
		self.assertEqual(result, 39)
		result = DBfunctions.read_db('Completed','week_pb','User_ID',User_ID)
		self.assertEqual(result, 21)

	def test_db_read_position_task_not_null(self):
		User_ID = 1
		result = DBfunctions.read_position_task(User_ID)
		self.assertEqual(result, '1')

	def test_db_read_position_task_null(self):
		User_ID = 1
		DBfunctions.delete_record('tasks','User_ID',User_ID)
		result = DBfunctions.read_position_task(User_ID)
		self.assertFalse(result)

	def test_db_str_compare_str_not_equal(self):
		first_name = "Vlad"
		result = DBfunctions.str_compare_str(first_name)
		self.assertFalse(result)

	def test_db_str_compare_str_equal(self):
		first_name = "Danil"
		result = DBfunctions.str_compare_str(first_name)
		self.assertTrue(result)

	def test_db_str_compare_int_not_equal(self):
		User_ID = 0
		result = DBfunctions.str_compare_int(str(User_ID))
		self.assertFalse(result)

	def test_db_str_compare_int_equal(self):
		User_ID = 1
		result = DBfunctions.str_compare_int(str(User_ID))
		self.assertTrue(result)

	def test_pict_import_true(self):
		User_ID = 1
		pict_path = 'icons/Empty_avatar.png'
		DBfunctions.pict_import(User_ID,pict_path)
		result = DBfunctions.read_db('Image', 'user', 'User_ID', User_ID)
		self.assertIsNotNone(result)

	def test_pict_export_none(self):
		User_ID = 1
		result = DBfunctions.pict_export(User_ID)
		self.assertFalse(result)

	def test_pict_export_not_none(self):
		User_ID = 1
		pict_path = 'icons/Empty_avatar.png'
		DBfunctions.pict_import(User_ID, pict_path)
		result = DBfunctions.pict_export(User_ID)
		self.assertTrue(result)
		if os.path.exists('./Data_base/pict_user.png'):
			os.remove('./Data_base/pict_user.png')
		else:
			pass
