from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
from MainWindow import Ui_Core
from Settings import Ui_Settings
from statistic import Ui_Statistic
import os.path
import DBfunctions
import sqlite3
import random
from Main_func import Second_Windo

class Statistic_Menu(QtWidgets.QMainWindow, Ui_Statistic):
    def __init__(self,parent = None):
        super(Statistic_Menu,self).__init__(parent)
        self.setupUi(self)
        self.check_theme()
        self.settings_but.clicked.connect(self.popup_window_open)
        self.mainwindow_button.clicked.connect(self.mainWindow)
        self.statistic_button.clicked.connect(self.statisticMenu)
    def mainWindow(self):
        self.previous = Fifth_Window()
        self.close()
        self.previous.show()
    def statisticMenu(self):
        self.statistic = Settings_Menu()
        self.close()
        self.statistic.show()

class Settings_Menu(QtWidgets.QMainWindow, Ui_Settings):
    def choose_picture_func(photo_data):
        photo_data = QFileDialog.getOpenFileName(self,
                                            'Choose picture',
                                            './')
        self.Main_func.choose_picture_dialog_open(photo_data)

    def __init__(self, parent = None):
        super(Settings_Menu, self).__init__(parent)
        self.setupUi(self)
        self.check_theme()
        self.name.setText(DBfunctions.read_db('First', 'user', 'User_ID', User_ID))
        self.secname.setText(DBfunctions.read_db('Last','user','User_ID',User_ID))
        if DBfunctions.show_avatar() != 0:
            photopath = QtGui.QPixmap(DBfunctions.show_avatar())
            self.avatar.setPixmap(photopath)
        self.dark_theme.clicked.connect(self.buttonpressed_1)
        self.light_theme.clicked.connect(self.buttonpressed_2)
        self.setting_menu.clicked.connect(self.settings_but_open)
        self.mainwindow_button.clicked.connect(self.back_main)
        self.statistic_button.clicked.connect(self.statistic_menu)
        # self.change_name.clicked.connect(self.Main_func.change_name_func)
        # self.change_secname.clicked.connect(self.Main_func.change_secname_func)
        self.change_avatar.clicked.connect(self.Main_func.choose_picture_func())
        if DBfunctions.show_avatar() != 0:
            photopath = QtGui.QPixmap(DBfunctions.show_avatar())
            self.avatar.setPixmap(photopath)
    def back_main(self):
        self.back = Fifth_Window()
        self.close()
        self.back.show()
    def statistic_menu(self):
        self.back = Statistic_Menu()
        self.close()
        self.back.show()
class Fifth_Window(QtWidgets.QMainWindow, Ui_Core):
    def __init__(self,parent = None):
        super(Fifth_Window, self).__init__(parent)
        self.setupUi(self)
        self.check_theme_person()
        self.check_box.clicked.connect(self.check_box_checked)
        self.Settings_but.clicked.connect(self.settings_but_clicked)
        self.settings_but_open.clicked.connect(self.nextWindow)
        if DBfunctions.show_avatar() != 0:
            photopath = QtGui.QPixmap(DBfunctions.show_avatar())
            self.Avatar.setPixmap(photopath)
        self.Main_func.show_first_last()
        self.plus_button.clicked.connect(self.add_task_button_clicked)
        self.okey.clicked.connect(self.add_task_button_clicked)
        self.left_button.clicked.connect(self.left_button_popup_window_open)
        self.statistic_button.clicked.connect(self.statisticMenu)
        self.okey.clicked.connect(self.Main_func.Add_Task())
    def statisticMenu(self):
        self.next = Statistic_Menu()
        self.next.show()
        self.close()
    def nextWindow(self):
        self.next = Settings_Menu()
        self.next.show()
        self.close()

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
        Main_func.show_username()
        self.Letsgobutton_2.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.next = Fourth_Window()
        self.next.show()

class Second_Window(QtWidgets.QMainWindow, Ui_Sign, Second_Windo): ##Window of signing in
    def __init__(self, parent = None):
        super(Second_Window, self).__init__(parent)
        self.setupUi(self)
        first_name = self.InputFirst.text()
        last_name = self.InputSecond.text()
        print(self.InputFirst.text())
        print(self.InputSecond.text())
        self.Letsgobutton.clicked.connect(self.signin(first_name, last_name))
    def nextWindow(self):
        self.close()
        self.next = Third_Window()
        self.next.show()
    def repeat_win(self):
        self.signin(first_name, last_name)
class First_Window(QtWidgets.QMainWindow,Ui_MainWindow): ## Window Start

    def __init__(self, parent= None):
        super(First_Window,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
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
