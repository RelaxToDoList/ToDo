import sqlite3

def create_db():
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()

	cur.execute('PRAGMA foreign_keys = ON')

	cur.execute('CREATE TABLE IF NOT EXISTS user(User_ID INTEGER UNIQUE PRIMARY KEY NOT NULL, '
												'First TEXT NOT NULL, '
												'Last TEXT NOT NULL, '
												'Image BLOB)')
	con.commit()

	cur.execute('CREATE TABLE IF NOT EXISTS tasks(Num_Task INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT, '
												 'Status_task INTEGER, '
												 'Date TEXT, '
												 'Time TEXT, '
												 'Task_text TEXT NOT NULL, '
												 'User_ID INTEGER NOT NULL, '
												 'FOREIGN KEY(User_ID) REFERENCES user(User_ID) ON DELETE CASCADE)')
	con.commit()

	cur.execute('CREATE TABLE IF NOT EXISTS remind(Rem_active INTEGER NOT NULL, '
												  'Rem_time TEXT, '
												  'Num_Task INTEGER UNUQUE PRIMARY KEY NOT NULL, '
												  'FOREIGN KEY(Num_Task) REFERENCES tasks(Num_Task) ON DELETE CASCADE)')
	con.commit()

	cur.close()
	con.close()

create_db()
