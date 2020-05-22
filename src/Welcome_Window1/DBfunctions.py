import sqlite3

def str_compare_str(str1):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'SELECT First FROM user'
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
	cur.close()
	con.close()
	return 0

def str_compare_int(str1):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'SELECT User_ID FROM week_pb'
	cur.execute(query)
	data = cur.fetchall()
	str1.lower()
	str2 = ''
	for i in range(int(read_db('count(User_ID)', 'week_pb'))):
		for line in list(map(str,data[i])):
			str2 = line + str2
		str2.lower()
		if str1 == str2:
			return 1
		str2 = ''
	cur.close()
	con.close()
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

def read_db_all(show_column_name, table, param_column_name = None, record = None):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	if record is None:
		query = 'SELECT '+show_column_name+' FROM '+table
		cur.execute(query)
		data = cur.fetchall()
		cur.close()
		con.close()
		return data
	else:
		query = 'SELECT '+show_column_name+' FROM '+table+' WHERE '+param_column_name+" = '"+str(record)+"'"
		cur.execute(query)
		data = cur.fetchall()
		cur.close()
		con.close()
		return data

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
	query = 'DELETE FROM '+table+' WHERE '+id_column+" = '"+str(record_id)+"'"
	cur.execute(query)
	con.commit()
	cur.close()
	con.close()

def update_record(table, param_column, param_val, id_column, record_id):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = f'UPDATE {table} SET {param_column} = ? WHERE {id_column} = ?'
	cur.execute(query, (param_val, record_id))
	con.commit()
	cur.close()
	con.close()

def write_in_db_tasks(records):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)'
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

def write_in_db_pb(column, record, table, User_ID):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	if record == 0:
		if column == 'Completed':
			query = 'UPDATE ' +table+' SET '+column+'='+str(record)+' WHERE '+'User_ID'+" = '"+str(User_ID)+"'"
			cur.execute(query)
		else:
			query = 'UPDATE ' +table+' SET '+column+'='+str(record)+' WHERE '+'User_ID'+" = '"+str(User_ID)+"'"
			cur.execute(query)
	else:
		if column == 'Completed':
			query = 'UPDATE '+table+' SET '+column+'='+str(record)+' WHERE '+'User_ID'+" = '"+str(User_ID)+"'"
			cur.execute(query)
		else:
			cw = read_db('Completed', 'week_pb')
			query = 'UPDATE '+table+' SET '+column+'='+str(record)+' WHERE '+'User_ID'+" = '"+str(User_ID)+"'"
			cur.execute(query)
	con.commit()
	cur.close()
	con.close()

def create_in_db_pb(User_ID):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	query = 'INSERT INTO week_pb VALUES (?, ?, ?)'
	records = [0, 0, User_ID]
	cur.execute(query, records)
	con.commit()
	query = 'INSERT INTO daily_pb VALUES (?, ?, ?)'
	records = [0, 0, User_ID]
	cur.execute(query, records)
	con.commit()
	cur.close()
	con.close()

def pict_export(User_ID):
    pict_binary = read_db('Image', 'user', 'User_ID', User_ID)
    if pict_binary == None:
        return 0;
    photoPath =  "./Data_base/pict_user.png"
    write_pict_from_binary(photoPath,pict_binary)
    return photoPath

def pict_import(User_ID, pict_path):
    binary_pict = import_pict_binary(pict_path)
    update_record('user', 'Image', binary_pict, 'User_ID', User_ID)

def write_pict_from_binary(file_path, pict_binary):
    f = open(file_path, 'wb')
    f.write(pict_binary)

def import_pict_binary(pict_path):
    f = open(pict_path, 'rb')
    pict_binary = f.read()
    return pict_binary

def read_position_task(User_ID):
	con = sqlite3.connect('./Data_base/DataBase.db')
	cur = con.cursor()
	id_column = 'User_ID'
	query = 'SELECT Num_Task FROM tasks WHERE '+id_column+" = '"+str(User_ID)+"'"
	cur.execute(query)
	data = cur.fetchall()
	i = int(read_db('count(User_ID)', 'tasks', 'User_ID',User_ID))
	if i == 0:
		return 0
	str1 = ''
	for line in list(map(str,data[i-1])):
		str1 = line + str1
	return str1
