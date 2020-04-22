from PyQt5 import QtCore, QtGui, QtWidgets
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
from MainWindow import Ui_Core
from Settings import Ui_Settings
import DBfunctions
import sqlite3
import random

class Settings_Menu(QtWidgets.QMainWindow, Ui_Settings):
    def __init__(self, parent = None):
        super(Settings_Menu, self).__init__(parent)
        self.setupUi(self)
        self.dark_theme.clicked.connect(self.buttonpressed_1)
        self.light_theme.clicked.connect(self.buttonpressed_2)

class Fifth_Window(QtWidgets.QMainWindow, Ui_Core):
    def show_first_last(self):
        self.FirstName.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.SecondName.setText(DBfunctions.read_db('Last', 'user', 'User_ID', User_ID))

    def __init__(self, parent = None):
        super(Fifth_Window, self).__init__(parent)
        self.setupUi(self)
        self.check_box.clicked.connect(self.check_box_checked)
        self.Settings_but.clicked.connect(self.settings_but_clicked)
        self.settings_but_open.clicked.connect(self.nextWindow)
        self.show_first_last()
        self.plus_button.clicked.connect(self.add_task_button_clicked)
        self.okey.clicked.connect(self.add_task_button_clicked)
        self.left_button.clicked.connect(self.left_button_popup_window_open)
    def nextWindow(self):
        self.next = Settings_Menu()
        self.next.show()

class Fourth_Window(QtWidgets.QMainWindow, Ui_Choose_Theme): ## Window of theme choosing
    def __init__(self, parent = None):
        super(Fourth_Window, self).__init__(parent)
        self.setupUi(self)
        self.toolButton_2.clicked.connect(self.buttonpressed_2)
        self.toolButton.clicked.connect(self.buttonpressed_1)
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
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
        #self.check(last_name,first_name)
        print(self.InputFirst.text())
        print(self.InputSecond.text())
        #if str(self.InputFirst.text()) or str(self.InputSecond.text()) == "":
        #    self.error()
        #    Second_Window.__init__(self)
        if self.check_signin() == 1:
            self.Letsgobutton.clicked.connect(self.nextWindow)
        else:
            global User_ID
            User_ID = random.randint(1000, 10000)
            data = [User_ID, first_name, last_name, None]
            DBfunctions.write_in_db_user(data)
            self.Letsgobutton.clicked.connect(self.nextWindow)

    def __init__(self, parent = None):
        super(Second_Window, self).__init__(parent)
        self.setupUi(self)
        self.Letsgobutton.clicked.connect(self.signin)
        #self.Letsgobutton.clicked.connect(self.nextWindow)
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
