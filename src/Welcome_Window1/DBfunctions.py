import sqlite3

def str_compare(str1, table):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'SELECT First FROM '+table
	cur.execute(query)
	data = cur.fetchall()
	str1.lower()
	str2 = ''
	for i in range(int(read_db('count(User_ID)', 'user'))):
		for line in data[i]:
			str2 = line + str2
		str2.lower()
		if str1 == str2:
			return 1
		str2 = ''
	return 0

def read_db(show_column_name, table, param_column_name = None, record = None):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	if record is None:
		query = 'SELECT '+show_column_name+' FROM '+table
		cur.execute(query)
		data = cur.fetchone()
		cur.close()
		con.close()
		return data[0]
	else:
		query = 'SELECT '+show_column_name+' FROM '+table+' WHERE '+param_column_name+" = '"+str(record)+"'"
		cur.execute(query)
		data = cur.fetchone()
		cur.close()
		con.close()
		return data[0]

def delete_table(table):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'DROP TABLE IF EXISTS '+table
	c.execute(query)
	con.commit()
	cur.close()
	con.close()

def delete_record(table, id_column, record_id):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'DELETE FROM '+table+' WHERE '+id_column+" = '"+record_id+"'"
	cur.execute(query)
	con.commit()
	cur.close()
	con.close()

def update_record(table, param_column, param_val, id_column, record_id):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'UPDATE '+table+' SET '+param_column+'='+str(param_val)+' WHERE '+id_column+" = '"+str(record_id)+"'"
	cur.execute(query)
	con.commit()
	cur.close()
	con.close()

def write_in_db_tasks(records):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ? ,?)'
	cur.execute(query, records)
	con.commit()
	cur.close()
	con.close()

def write_in_db_user(records):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'INSERT INTO user VALUES (?, ?, ?, ?)'
	cur.execute(query, records)
	con.commit()
	cur.close()
	con.close()
