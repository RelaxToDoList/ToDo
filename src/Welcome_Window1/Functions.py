import datetime
import DBfunctions

class Add_Task():

    def add_task(position, text_task, User_ID): #Add task to Data Base
        position += 1
        time = datetime.datetime.today()
        time_deadline = time + datetime.timedelta(days = 1)
        time_deadline_time = time_deadline - time
        time_deadline_time = (time_deadline_time.total_seconds())/3600
        task = [position, 0, str(datetime.date.today()), str(time_deadline_time), text_task, User_ID]
        DBfunctions.write_in_db_tasks(task)

    def add_complete(User_ID, position):
        status = 1
        comp = 0
        DBfunctions.update_status(User_ID, position, status)
        completed = DBfunctions.read_db('Completed','week_pb',User_ID)
        failed = DBfunctions.read_db('Failed', 'week_pb', User_ID)
        if failed != 0:
            f = failed - 1
            DBfunctions.write_in_db_pb('Failed', f, 'week_pb', User_ID)
        comp = completed + 1
        print(comp)
        DBfunctions.write_in_db_pb('Completed', comp, 'week_pb', User_ID)
        failed = 0
        f = 0
        failed = DBfunctions.read_db('Failed', 'daily_pb', User_ID)
        if failed != 0:
            f = failed - 1
            DBfunctions.write_in_db_pb('Failed', f, 'daily_pb', User_ID)
        completed = 0
        comp = 0
        completed = DBfunctions.read_db('Completed', 'daily_pb', User_ID)
        comp = completed + 1
        DBfunctions.write_in_db_pb('Completed', comp, 'daily_pb', User_ID)

    def add_fail(User_ID):
        f = 0
        failed = DBfunctions.read_db('Failed', 'week_pb', User_ID)
        f = failed + 1
        DBfunctions.write_in_db_pb('Failed', f, 'week_pb', User_ID)
        failed = 0
        f = 0
        failed = DBfunctions.read_db('Failed', 'daily_pb', User_ID)
        f = failed + 1
        DBfunctions.write_in_db_pb('Failed', f, 'daily_pb', User_ID)
