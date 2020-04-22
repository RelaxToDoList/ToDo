import sqlite3

def create_db():
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()

	cur.execute('PRAGMA foreign_keys = ON')

	cur.execute('CREATE TABLE IF NOT EXISTS user(User_ID INTEGER UNIQUE PRIMARY KEY, '
												'First TEXT, '
												'Last TEXT, '
												'Image BLOB)')
	con.commit()

	cur.execute('CREATE TABLE IF NOT EXISTS tasks(Num_Task INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, '
												'Pos_Task TEXT, '
												'Date_time TEXT, '
												'Task_name TEXT, '
												'Task_text TEXT, '
												'Deadline TEXT, '
												'Rem_time TEXT, '
												'Status TEXT, '
												'User_ID INTEGER, '
												'FOREIGN KEY(User_ID) REFERENCES user(User_ID))')
	con.commit()

	cur.close()
	con.close()

create_db()
