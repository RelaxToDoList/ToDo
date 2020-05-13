from PyQt5 import QtCore, QtGui, QtWidgets
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
from MainWindow import Ui_Core
from Settings import Ui_Settings
from statistic import Ui_Statistic
import DBfunctions
import sqlite3
import random
class Statistic_Menu(QtWidgets.QMainWindow, Ui_Statistic):
    def __init__(self,parent = None):
        super(Statistic_Menu,self).__init__(parent)
        self.setupUi(self)
        self.check_theme()
        self.completed = 20
        self.failed = 5
        self.check_statistic()
        self.settings_but.clicked.connect(self.popup_window_open)
        self.mainwindow_button.clicked.connect(self.mainWindow)
        self.statistic_button.clicked.connect(self.statisticMenu)

    def check_statistic(self):
        statistic = self.completed + self.failed

        self.progress_bar.setValue((self.completed/statistic)*100)
    def mainWindow(self):
        self.previous = Fifth_Window()
        self.close()
        self.previous.show()
    def statisticMenu(self):
        self.statistic = Settings_Menu()
        self.close()
        self.statistic.show()

class Settings_Menu(QtWidgets.QMainWindow, Ui_Settings):
    def __init__(self, parent = None):
        super(Settings_Menu, self).__init__(parent)
        self.setupUi(self)
        self.check_theme()
        self.name.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.secname.setText(DBfunctions.read_db('Last','user','User_ID',User_ID))
        self.dark_theme.clicked.connect(self.buttonpressed_1)
        self.light_theme.clicked.connect(self.buttonpressed_2)
        self.setting_menu.clicked.connect(self.settings_but_open)
        self.mainwindow_button.clicked.connect(self.back_main)
        self.statistic_button.clicked.connect(self.statistic_menu)
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

    def __init__(self,parent = None):
        super(Fifth_Window, self).__init__(parent)
        self.setupUi(self)
        self.completed = 20
        self.failed = 5
        self.check_statistic()
        self.check_theme_person()
        self.check_box.clicked.connect(self.check_box_checked)
        self.Settings_but.clicked.connect(self.settings_but_clicked)
        self.settings_but_open.clicked.connect(self.nextWindow)
        self.show_first_last()
        self.plus_button.clicked.connect(self.add_task_button_clicked)
        self.okey.clicked.connect(self.add_task_button_clicked)
        self.left_button.clicked.connect(self.left_button_popup_window_open)
        self.statistic_button.clicked.connect(self.statisticMenu)
        self.okey.clicked.connect(self.Add_Task)
    def check_statistic(self):
        statistic = self.completed + self.failed
        self.progress.setValue((self.completed/statistic)*100)
    def statisticMenu(self):
        self.next = Statistic_Menu()
        self.next.show()
        self.close()
    def nextWindow(self):
        self.next = Settings_Menu()
        self.next.show()
        self.close()
    def show_task(self,text_task):
        self.deal_text.setText(DBfunctions.read_db('Task_text', 'tasks', 'User_ID', User_ID))
    def Add_Task(self):
        text_task = self.line_enter.text()
        task = [None, None, None, text_task, User_ID]
        DBfunctions.write_in_db_tasks(task)
        self.line_enter.clear()
        self.show_task(text_task)

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
    def __init__(self, parent = None):
        super(Third_Window, self).__init__(parent)
        self.setupUi(self)
        self.usersname.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.Letsgobutton_2.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.next = Fourth_Window()
        self.next.show()

class Second_Window(QtWidgets.QMainWindow, Ui_Sign): ##Window of signing in
    def check_signin(self):
        if DBfunctions.read_db('count(User_ID)', 'user') == 0:
            return 0
        elif DBfunctions.str_compare(first_name, 'user') == 0:
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
        print(self.InputFirst.text())
        print(self.InputSecond.text())
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
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = First_Window()
    window.show()

    sys.exit(app.exec_())
