from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import QTimer
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
import Choose_Theme
from MainWindow import Ui_Core
from Settings import Ui_Settings
from statistic import Ui_Statistic
import os.path
import DBfunctions
import sqlite3
import random
import datetime

class Statistic_Menu(QtWidgets.QMainWindow, Ui_Statistic):
    def __init__(self,parent = None):
        super(Statistic_Menu,self).__init__(parent)
        self.setupUi(self)
        self.check_theme()
        self.check_statistic()
        self.settings_but.clicked.connect(self.popup_window_open)
        self.mainwindow_button.clicked.connect(self.mainWindow)
        self.statistic_button.clicked.connect(self.statisticMenu)

    def check_statistic(self):
        completed_w = DBfunctions.read_db('Completed', 'week_pb')
        failed_w = DBfunctions.read_db('Failed', 'week_pb')

        statistic = completed_w + failed_w
        if statistic == 0:
            statistic = 1
        self.progress_bar.setValue((completed_w/statistic)*100)
    def mainWindow(self):
        self.previous = Fifth_Window()
        self.close()
        self.previous.show()
    def statisticMenu(self):
        self.statistic = Settings_Menu()
        self.close()
        self.statistic.show()

class Settings_Menu(QtWidgets.QMainWindow, Ui_Settings):
    def choose_picture_dialog_open(self):
        fname = QFileDialog.getOpenFileName(self,
                                            'Choose picture',
                                            './')
        if not fname[0]:
            return;
        pict_path = fname[0]
        pixmap = QtGui.QPixmap(fname[0])
        self.avatar.setPixmap(pixmap)
        DBfunctions.pict_import(User_ID, pict_path)

    def show_avatar(self):
        if DBfunctions.pict_export(User_ID) == 0:
            return;
        photo = QtGui.QPixmap(DBfunctions.pict_export(User_ID))
        self.avatar.setPixmap(photo)

    def __init__(self, parent = None):
        super(Settings_Menu, self).__init__(parent)
        self.setupUi(self)
        self.check_theme()
        self.name.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.secname.setText(DBfunctions.read_db('Last','user','User_ID',User_ID))
        self.show_avatar()
        self.dark_theme.clicked.connect(self.buttonpressed_1)
        self.light_theme.clicked.connect(self.buttonpressed_2)
        self.setting_menu.clicked.connect(self.settings_but_open)
        self.mainwindow_button.clicked.connect(self.back_main)
        self.statistic_button.clicked.connect(self.statistic_menu)
        #self.change_name.clicked.connect(self.change_name_func)
        #self.change_secname.clicked.connect(self.change_secname_func)
        self.change_avatar.clicked.connect(self.choose_picture_dialog_open)

    def change_name_func(self):
        self.change_name_pressed()
        self.save_change.clicked.connect(self.save_changes_button)
    def change_secname_func(self):
        self.change_secname_pressed()
        self.save_change.clicked.connect(self.save_changes_button)
    def save_changes_button(self):
        first_name = self.firstname_change.text()
        second_name = self.secondname_change.text()
        if first_name:
            DBfunctions.update_record('user','First',str(first_name),'User_ID',User_ID)
            self.name.setText(first_name)
        if second_name:
            DBfunctions.update_record('user','Last',second_name,'User_ID',User_ID)
            self.secname.setText(second_name)
        self.close_line_edit()

    def back_main(self):
        self.back = Fifth_Window()
        self.close()
        self.back.show()
    def statistic_menu(self):
        self.back = Statistic_Menu()
        self.close()
        self.back.show()
class Fifth_Window(QtWidgets.QMainWindow, Ui_Core):
    def show_first_last(self):
        self.FirstName.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.SecondName.setText(DBfunctions.read_db('Last', 'user', 'User_ID', User_ID))

    def show_Avatar(self):
        if DBfunctions.pict_export(User_ID) == 0:
            return;
        photo = QtGui.QPixmap(DBfunctions.pict_export(User_ID))
        self.Avatar.setPixmap(photo)

    def __init__(self,parent = None):
        super(Fifth_Window, self).__init__(parent)
        self.setupUi(self)
        time = datetime.datetime.today()
        self.setupUi(self)
        self.Data.setText(time.strftime("%A, %d %B"))
        if DBfunctions.read_db('count(Num_Task)', 'tasks') == 0:
            self.position = 0
        else:
            self.position = DBfunctions.read_position_task(User_ID)
            self.position = int(self.position)
        self.check_statistic()
        self.check_theme_person()
        self.check_box1.clicked.connect(self.check_box_checked1)
        self.check_box2.clicked.connect(self.check_box_checked2)
        self.check_box3.clicked.connect(self.check_box_checked3)
        self.check_box4.clicked.connect(self.check_box_checked4)
        self.check_box5.clicked.connect(self.check_box_checked5)
        self.check_box6.clicked.connect(self.check_box_checked6)
        self.check_box7.clicked.connect(self.check_box_checked7)
        self.check_box8.clicked.connect(self.check_box_checked8)
        self.check_box9.clicked.connect(self.check_box_checked9)
        self.check_box10.clicked.connect(self.check_box_checked10)
        self.Settings_but.clicked.connect(self.settings_but_clicked)
        self.settings_but_open.clicked.connect(self.nextWindow)
        self.show_first_last()
        self.show_Avatar()
        self.tableWidget.setCellWidget(0,0,self.plus_button)
        self.plus_button.clicked.connect(self.add_task_button_clicked)
        self.okey.clicked.connect(self.add_task_button_clicked)
        self.left_button.clicked.connect(self.left_button_popup_window_open)
        self.statistic_button.clicked.connect(self.statisticMenu)
        self.okey.clicked.connect(self.Add_Task)
        self.okey.clicked.connect(self.check_statistic)
        self.logout_button.clicked.connect(self.logout_to_signin)
        self.addtaskfromfile()
        self.Output_Task()

    def logout_to_signin(self):
        self.next = Second_Window()
        self.next.show()
        if os.path.exists('./Data_base/pict_user.png'):
            os.remove('./Data_base/pict_user.png')
        else:
            pass
        self.close()
    def check_statistic(self):
        completed_d = DBfunctions.read_db('Completed', 'daily_pb')
        failed_d = DBfunctions.read_db('Failed', 'daily_pb')
        self.label_have_to_do.setText(str(failed_d))
        self.label_did.setText(str(completed_d))
        statistic = completed_d + failed_d
        if statistic == 0:
            statistic = 1
        self.progress.setValue((completed_d/statistic)*100)
    def statisticMenu(self):
        self.next = Statistic_Menu()
        self.next.show()
        self.close()
    def nextWindow(self):
        self.next = Settings_Menu()
        self.next.show()
        self.close()

    def adding_complete(self,position):
        DBfunctions.update_record('tasks','Status_task',1,'Num_Task',position)
        completed = DBfunctions.read_db('Completed','week_pb')
        failed = DBfunctions.read_db('Failed','week_pb')
        if failed != 0:
            f = failed - 1
            DBfunctions.write_in_db_pb('Failed', f,'week_pb',User_ID)
        comp = completed + 1
        self.label_did.setText(str(comp))
        DBfunctions.write_in_db_pb('Completed', comp,'week_pb',User_ID)
        failed = 0
        f = 0
        failed = DBfunctions.read_db('Failed','daily_pb')
        if failed != 0:
            f = failed - 1
            DBfunctions.write_in_db_pb('Failed',f,'daily_pb',User_ID)
            self.label_have_to_do.setText(str(f))
        completed = 0
        comp = 0
        completed = DBfunctions.read_db('Completed','daily_pb')
        comp = completed + 1
        self.label_did.setText(str(comp))
        DBfunctions.write_in_db_pb('Completed', comp,'daily_pb', User_ID)
        self.check_statistic()

    def adding_fail(self):
        failed = DBfunctions.read_db('Failed', 'week_pb')
        f = failed + 1
        DBfunctions.write_in_db_pb('Failed', f, 'week_pb', User_ID)
        failed = 0
        f = 0
        failed = DBfunctions.read_db('Failed', 'daily_pb')
        f = failed + 1
        DBfunctions.write_in_db_pb('Failed', f, 'daily_pb', User_ID)
        self.check_statistic()

    def Add_Task(self):
        self.position = self.position + 1
        if self.line_enter.text() == '':
            return
        time = datetime.datetime.today()
        time_deadline = time + datetime.timedelta(days = 1)
        time_deadline_time = time_deadline-time
        time_deadline_time = (time_deadline_time.total_seconds())/3600
        text_task = self.line_enter.text()
        task = [self.position, 0, str(datetime.date.today()), str(time_deadline_time), text_task, User_ID]
        DBfunctions.write_in_db_tasks(task)
        self.adding_fail()
        self.line_enter.clear()
        self.addWidgetss(text_task,time_deadline_time)

    def Output_Task(self):
        time = datetime.datetime.today()
        time_deadline = time + datetime.timedelta(days = 1)
        time_deadline_time = time_deadline-time
        time_deadline_time = (time_deadline_time.total_seconds())/3600
        User = DBfunctions.read_db('User_ID', 'user', 'First', first_name)
        conn = sqlite3.connect("Data_base/DataBase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT Task_text FROM tasks WHERE User_ID = :User", {"User": User})
        TaskDB = cursor.fetchall()
        self.line_enter.clear()
        #self.check_status_task()
        for i in range(0,len(TaskDB),1):
            Task = TaskDB[i]
            TaskNT = Task[0]
            self.Reading_Tasks(TaskNT,time_deadline_time)
        conn.close()
    # def check_status_task(self):
    #     User = DBfunctions.read_db('User_ID','user','First',first_name)
    #     conn = sqlite3.connect("Data_base/DataBase.db")
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT Status_task FROM tasks WHERE User_ID = :User',{'User':User})
    #     status = cursor.fetchall()
    #     cursor.execute('SELECT Num_Task FROM tasks WHERE User_ID = :User',{'User':User})
    #     position = cursor.fetchall()
    #     for stat in status:
    #         if stat == (1,):
    #             for pos in position:
    #                     if pos == (1,):
    #                         print(f"first{stat}")
    #                         print(f"first{pos}")
    #                         self.check_box1.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box1.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box1.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (2,):
    #                         print(f"second{stat}")
    #                         print(f"second{pos}")
    #                         self.check_box2.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box2.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box2.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (3,):
    #                         self.check_box3.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box3.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box3.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (4,):
    #                         self.check_box4.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box4.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box4.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (5,):
    #                         self.check_box5.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box5.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box5.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (6,):
    #                         self.check_box6.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box6.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box6.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (7,):
    #                         self.check_box7.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box7.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box7.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (8,):
    #                         self.check_box8.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box8.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box8.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (9,):
    #                         self.check_box9.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box9.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box9.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #                     if pos == (10,):
    #                         self.check_box10.disconnect()
    #                         if Choose_Theme.theme == 0:
    #                             self.check_box10.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    #                         else:
    #                             self.check_box10.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
    #             else:
    #                 pass

    def add_task_random(self,text_task): #adding task from left_button_popup_window
        self.position = self.position + 1
        self.daily_add_button.disconnect()
        time = datetime.datetime.today()
        time_deadline = time + datetime.timedelta(days = 1)
        time_deadline_time = time_deadline-time
        time_deadline_time = (time_deadline_time.total_seconds())/3600
        task = [None, 0, str(datetime.date.today()), str(time_deadline_time), text_task, User_ID]
        DBfunctions.write_in_db_tasks(task)
        self.adding_fail()
        self.addWidgetss(text_task,time_deadline_time)

class Fourth_Window(QtWidgets.QMainWindow, Ui_Choose_Theme): ## Window of theme choosing
    def __init__(self, parent = None):
        super(Fourth_Window, self).__init__(parent)
        self.setupUi(self)
        self.toolButton_2.clicked.connect(self.buttonpressed_2)
        self.toolButton.clicked.connect(self.buttonpressed_1)
    def nextWindow(self):
        self.close()
        self.next = Fifth_Window()
        self.next.show()

class Third_Window(QtWidgets.QMainWindow, Ui_Welcome): ## Window of Welcoming user
    def check_tasks(self):
        today = datetime.date.today()
        if DBfunctions.read_db('count(Num_Task)', 'tasks', 'User_ID', User_ID) == 0:
            return
        elif str(today) == str(DBfunctions.read_db('Date', 'tasks', 'User_ID', User_ID)):
            return
        else:
            date = DBfunctions.read_db('Date', 'tasks', 'User_ID', User_ID)
            DBfunctions.delete_record('tasks', 'Date', str(date))

    def check_daily_progressbar(self):
        today = datetime.date.today()
        if DBfunctions.read_db('count(Num_Task)', 'tasks', 'User_ID', User_ID) == 0:
            return
        elif str(today) == str(DBfunctions.read_db('Date', 'tasks', 'User_ID', User_ID)):
            return
        else:
            DBfunctions.write_in_db_pb('Completed', 0,'daily_pb', User_ID)
            DBfunctions.write_in_db_pb('Failed', 0,'daily_pb', User_ID)

    def __init__(self, parent = None):
        super(Third_Window, self).__init__(parent)
        self.setupUi(self)
        self.check_daily_progressbar()
        self.check_tasks()
        self.usersname.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
    def nextWindow(self):
        self.close()
        self.next = Fourth_Window()
        self.next.show()

class Second_Window(QtWidgets.QMainWindow, Ui_Sign): ##Window of signing in
    def create_pb(self):
        if DBfunctions.read_db('count(User_ID)', 'week_pb') == 0:
            DBfunctions.create_in_db_pb(User_ID)
        elif DBfunctions.str_compare_int(str(User_ID)) == 0:
            DBfunctions.create_in_db_pb(User_ID)
        else:
            return

    def check_signin(self):
        if DBfunctions.read_db('count(User_ID)', 'user') == 0:
            return 0
        elif DBfunctions.str_compare_str(first_name) == 0:
            return 0
        else:
            global User_ID
            User_ID = DBfunctions.read_db('User_ID', 'user', 'First', first_name)
            return 1

    def signin(self):
        global first_name
        first_name = self.InputFirst.text()
        global last_name
        last_name = self.InputSecond.text()
        if not first_name:
            self.error()
            return
        elif not last_name:
            self.error()
            return
        else:
            if self.check_signin() == 1:
                self.nextWindow()
            else:
                global User_ID
                User_ID = random.randint(1000, 10000)
                data = [User_ID, first_name, last_name, None]
                DBfunctions.write_in_db_user(data)
                self.nextWindow()

    def __init__(self, parent = None):
        super(Second_Window, self).__init__(parent)
        self.setupUi(self)
        self.Letsgobutton.clicked.connect(self.signin)
        self.Letsgobutton.clicked.connect(self.create_pb)
    def nextWindow(self):
        self.close()
        self.next = Third_Window()
        self.next.show()
    def repeat_win(self):
        self.signin()
class First_Window(QtWidgets.QMainWindow,Ui_MainWindow): ## Window Start

    def __init__(self, parent= None):
        super(First_Window,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.nextWindow)
    def nextWindow(self):
        self.close()
        self.first = First_Window()
        self.second = Second_Window()
        self.second.show()


if __name__ =="__main__":
    import sys, os
    app = QtWidgets.QApplication(sys.argv)

    window = First_Window()
    window.show()

    status = app.exec_()
    if os.path.exists('./Data_base/pict_user.png'):
        os.remove('./Data_base/pict_user.png')
    else:
        pass

    sys.exit(status)
