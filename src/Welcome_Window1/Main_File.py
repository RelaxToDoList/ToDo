from PyQt5 import QtCore, QtGui, QtWidgets
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
from MainWindow import Ui_Core
from Settings import Ui_Settings
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
        con = sqlite3.connect('./Data_base/DataBase.db')
        cur = con.cursor()
        query = 'SELECT First FROM user'
        cur.execute(query)
        data = cur.fetchone()
        self.FirstName.setText(data[0])
        query = 'SELECT Last FROM user'
        cur.execute(query)
        data = cur.fetchone()
        self.SecondName.setText(data[0])
        cur.close()
        con.close()

    def __init__(self, parent = None):
        super(Fifth_Window, self).__init__(parent)
        self.setupUi(self)
        self.check_box.clicked.connect(self.check_box_checked)
        self.Settings_but.clicked.connect(self.settings_but_clicked)
        self.settings_but_open.clicked.connect(self.nextWindow)
        # self.show_first_last()
        self.plus_button.clicked.connect(self.add_task_button_clicked)
        self.okey.clicked.connect(self.add_task_button_clicked)
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
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
    def nextWindow(self):
        self.close()
        self.next = Fourth_Window()
        self.next.show()

class Second_Window(QtWidgets.QMainWindow, Ui_Sign): ##Window of signing in
    def signin(self):
        first_name = self.InputFirst.text()
        last_name = self.InputSecond.text()
        user_id = random.randint(1000, 10000)
        con = sqlite3.connect('./Data_base/DataBase.db')
        cur = con.cursor()
        query = 'INSERT INTO user VALUES (?, ?, ?, ?)'
        cur.execute(query, (user_id, first_name, last_name, None))
        con.commit()
        cur.close()
        con.close()

    def __init__(self, parent = None):
        super(Second_Window, self).__init__(parent)
        self.setupUi(self)
        # self.Letsgobutton.clicked.connect(self.signin)
        self.Letsgobutton.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.next = Third_Window()
        self.next.show()


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
