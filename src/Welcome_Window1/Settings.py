from PyQt5 import QtCore, QtGui, QtWidgets
import Choose_Theme

class Ui_Settings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("icons/background_Settings.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("label")
        self.save_change = QtWidgets.QPushButton(self.centralwidget)
        self.save_change.setGeometry(QtCore.QRect(270,420,101,41))
        self.save_change.setStyleSheet("QPushButton{"
        "background-color:#3BA851;"
        "border-radius: 15px;"
        "color:white;"
        "border:none;"
        "font-size:16px;"
        "}"
        "QPushButton:hover{"
        "border-radius: 15px;"
        "background-color:#159B30;"
        "color:white;"
        "border:none;"
        "font-size:16px;"
        "}"
        "QPushButton:pressed{"
        "background-color:#159B30;"
        "border-radius: 15px;"
        "border:none;"
        "color:white;"
        "font-size:16px;"
        "}")
        self.save_change.setObjectName("save_change")
        self.settings_popup = QtWidgets.QGraphicsView(self.centralwidget)
        self.settings_popup.setGeometry(QtCore.QRect(650, 41 , 308, 517))
        self.settings_popup.setObjectName("settings_popup")
        self.settings_popup.setStyleSheet("background-color: #666666;"
        "border:5px black")
        self.setting_menu = QtWidgets.QToolButton(self.centralwidget)
        self.setting_menu.setGeometry(QtCore.QRect(900, 10, 31, 26))
        self.setting_menu.setStyleSheet("border:none;\n"
"")
        self.setting_menu.setIconSize(QtCore.QSize(70,70))
        self.setting_menu.setIcon(QtGui.QIcon("icons/icon_gear_dark.png"))
        self.setting_menu.setObjectName("setting_menu")
        self.personalInf = QtWidgets.QLabel(self.centralwidget)
        self.personalInf.setGeometry(QtCore.QRect(360, 60, 221, 51))
        self.personalInf.setStyleSheet("font-size: 20px;\n"
"color: #FFFFFF;\n"
"font-weight: bold;\n"
"")
        self.personalInf.setObjectName("personalInf")
        self.mainwindow_button = QtWidgets.QToolButton(self.centralwidget)
        self.mainwindow_button.setGeometry(QtCore.QRect(660,55,25, 25))
        self.mainwindow_button.setIcon(QtGui.QIcon("icons/icon_list.png"))
        self.mainwindow_button.setStyleSheet("border: none;")
        self.mainwindow_button.setIconSize(QtCore.QSize(25,25))
        self.account_label = QtWidgets.QLabel(self.centralwidget)
        self.account_label.setGeometry(QtCore.QRect(710,50,50,30))
        self.account_label.setStyleSheet("font-weight: bold;"
        "font-size:14px;"
        "color: #000000;")
        self.account_label.setObjectName("account_label")
        self.statistic_button = QtWidgets.QToolButton(self.centralwidget)
        self.statistic_button.setIcon(QtGui.QIcon("icons/icon_statistic.png"))
        self.statistic_button.setGeometry(QtCore.QRect(660,100,30,30))
        self.statistic_button.setStyleSheet("border: none;")
        self.statistic_button.setIconSize(QtCore.QSize(30,30))
        self.statistic_button.setObjectName("statistic_button")
        self.statistic_label = QtWidgets.QLabel(self.centralwidget)
        self.statistic_label.setGeometry(QtCore.QRect(710,90,100,50))
        self.statistic_label.setStyleSheet("font-weight: bold;"
        "font-size:15px;"
        "color: #000000;")
        self.statistic_label.setObjectName("statistic_label")
        self.avatar = QtWidgets.QLabel(self.centralwidget)
        self.avatar.setGeometry(QtCore.QRect(380, 110, 149, 123))
        self.avatar.setText("")
        self.avatar.setPixmap(QtGui.QPixmap("icons/Empty_avatar.png"))
        self.avatar.setScaledContents(True)
        self.avatar.setObjectName("avatar")
        self.change_avatar = QtWidgets.QPushButton(self.centralwidget)
        self.change_avatar.setGeometry(QtCore.QRect(410, 250, 91, 23))
        self.change_avatar.setStyleSheet("border:none;\n"
"color: #663366;\n"
"font-weight: bold;")
        self.change_avatar.setObjectName("change_avatar")
        self.first_line = QtWidgets.QFrame(self.centralwidget)
        self.first_line.setGeometry(QtCore.QRect(50, 300, 817, 3))
        self.first_line.setStyleSheet("background-color:#666666;\n"
"\n"
"")
        self.first_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.first_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.first_line.setObjectName("first_line")
        self.second_line = QtWidgets.QFrame(self.centralwidget)
        self.second_line.setGeometry(QtCore.QRect(50, 350, 314, 3))
        self.second_line.setStyleSheet("background-color: #666666;\n"
"")
        self.second_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.second_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.second_line.setObjectName("second_line")
        self.thrid_line = QtWidgets.QFrame(self.centralwidget)
        self.thrid_line.setGeometry(QtCore.QRect(50, 410, 314, 3))
        self.thrid_line.setStyleSheet("background-color: #666666;\n"
"")
        self.thrid_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.thrid_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.thrid_line.setObjectName("thrid_line")
        self.first_name = QtWidgets.QLabel(self.centralwidget)
        self.first_name.setGeometry(QtCore.QRect(60, 320, 101, 16))
        self.first_name.setStyleSheet("font-size: 20px;\n"
"color: #949494;\n"
"")
        self.first_name.setObjectName("first_name")
        self.second_name = QtWidgets.QLabel(self.centralwidget)
        self.second_name.setGeometry(QtCore.QRect(60, 380, 131, 20))
        self.second_name.setStyleSheet("font-size: 20px;\n"
"color: #949494;\n"
"")
        self.second_name.setObjectName("second_name")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(180, 303, 51, 50))
        self.name.setStyleSheet("color: #FFFFFF;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"\n"
"")
        self.name.setObjectName("name")
        self.secname = QtWidgets.QLabel(self.centralwidget)
        self.secname.setGeometry(QtCore.QRect(200, 365, 91, 50))
        self.secname.setStyleSheet("font-size: 16px;\n"
"font-weight: bold;\n"
"color: #FFFFFF;\n"
"")
        self.secname.setObjectName("secname")
        self.change_name = QtWidgets.QToolButton(self.centralwidget)
        self.change_name.setGeometry(QtCore.QRect(240, 320, 51, 19))
        self.change_name.setStyleSheet("border:none;\n"
"color:#663366;\n"
"font-weight: bold;\n"
"")
        self.change_name.setObjectName("change_name")
        self.change_secname = QtWidgets.QToolButton(self.centralwidget)
        self.change_secname.setGeometry(QtCore.QRect(290, 380, 51, 19))
        self.change_secname.setStyleSheet("border:none;\n"
"color:#663366;\n"
"font-weight: bold;\n"
"")
        self.change_secname.setObjectName("change_secname")
        self.theme = QtWidgets.QLabel(self.centralwidget)
        self.theme.setGeometry(QtCore.QRect(570, 310, 81, 31))
        self.theme.setStyleSheet("font-size:20px;\n"
"font-weight: bold;\n"
"color:#FFFFFF;\n"
"")
        self.theme.setObjectName("theme")
        self.Light_border_up_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.Light_border_up_2.setGeometry(QtCore.QRect(400, 340, 167, 40))
        self.Light_border_up_2.setStyleSheet("background-color: #FFFFFF;\n"
"")
        self.Light_border_up_2.setObjectName("Light_border_up_2")
        self.light_theme = QtWidgets.QToolButton(self.centralwidget)
        self.light_theme.setGeometry(QtCore.QRect(400, 380, 167, 60))
        self.light_theme.setStyleSheet("QToolButton:clicked {\n"
"    background-color:#959595;\n"
"    border-style: hidden;\n"
"    }\n"
"QToolButton:hover {\n"
"    background-color: #959595;\n"
"    border-style: hidden;\n"
"    }\n"
"QToolButton {\n"
"    background-color: #959595;\n"
"    border-style: hidden;\n"
"    }\n"
"")
        self.light_theme.setText("")
        self.light_theme.setObjectName("light_theme")
        self.Checkbox_Light = QtWidgets.QLabel(self.centralwidget)
        self.Checkbox_Light.setGeometry(QtCore.QRect(410, 400, 21, 21))
        self.Checkbox_Light.setText("")
        self.Checkbox_Light.setPixmap(QtGui.QPixmap("icons/Checkbox_Light.png"))
        self.Checkbox_Light.setScaledContents(True)
        self.Checkbox_Light.setObjectName("Checkbox_Light")
        self.LightDeal = QtWidgets.QLabel(self.centralwidget)
        self.LightDeal.setGeometry(QtCore.QRect(450, 400, 81, 20))
        self.LightDeal.setStyleSheet("color: #363636;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.LightDeal.setObjectName("LightDeal")
        self.Light = QtWidgets.QLabel(self.centralwidget)
        self.Light.setGeometry(QtCore.QRect(460, 340, 61, 31))
        self.Light.setStyleSheet("color: #363636;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.Light.setObjectName("Light")
        self.Dark_border_up_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.Dark_border_up_2.setGeometry(QtCore.QRect(640, 340, 167, 40))
        self.Dark_border_up_2.setStyleSheet("background-color: #1B1B1B;\n"
"border-color: black;\n"
"\n"
"\n"
"")
        self.Dark_border_up_2.setObjectName("Dark_border_up_2")
        self.Dark = QtWidgets.QLabel(self.centralwidget)
        self.Dark.setGeometry(QtCore.QRect(700, 340, 51, 31))
        self.Dark.setStyleSheet("color: #D7D7D7;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.Dark.setObjectName("Dark")
        self.dark_theme = QtWidgets.QToolButton(self.centralwidget)
        self.dark_theme.setGeometry(QtCore.QRect(640, 380, 167, 60))
        self.dark_theme.setStyleSheet("background-color: #0D0D0D;\n"
"")
        self.dark_theme.setText("")
        self.dark_theme.setObjectName("dark_theme")
        self.Checkbox_Dark_2 = QtWidgets.QLabel(self.centralwidget)
        self.Checkbox_Dark_2.setGeometry(QtCore.QRect(650, 400, 21, 21))
        self.Checkbox_Dark_2.setStyleSheet("")
        self.Checkbox_Dark_2.setText("")
        self.Checkbox_Dark_2.setPixmap(QtGui.QPixmap("icons/Checkbox_Dark.png"))
        self.Checkbox_Dark_2.setScaledContents(True)
        self.Checkbox_Dark_2.setObjectName("Checkbox_Dark_2")
        self.DarkDEal = QtWidgets.QLabel(self.centralwidget)
        self.DarkDEal.setGeometry(QtCore.QRect(690, 400, 91, 21))
        self.DarkDEal.setStyleSheet("color: #949494;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.DarkDEal.setObjectName("DarkDEal")
        self.firstname_change = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname_change.setGeometry(QtCore.QRect(165,317,200,27))
        self.firstname_change.setMaxLength(25)
        self.firstname_change.setObjectName("firstname_change")
        self.secondname_change = QtWidgets.QLineEdit(self.centralwidget)
        self.secondname_change.setGeometry(QtCore.QRect(190,376,172,27))
        self.secondname_change.setMaxLength(25)
        self.secondname_change.setObjectName("secondname_change")
        self.background.raise_()
        self.setting_menu.raise_()
        self.personalInf.raise_()
        self.save_change.raise_()
        self.save_change.hide()
        self.account_label.raise_()
        self.account_label.hide()
        self.avatar.raise_()
        self.change_avatar.raise_()
        self.first_line.raise_()
        self.second_line.raise_()
        self.thrid_line.raise_()
        self.first_name.raise_()
        self.second_name.raise_()
        self.name.raise_()
        self.secname.raise_()
        #self.change_name.raise_()
        #self.change_secname.raise_()
        self.secondname_change.raise_()
        self.secondname_change.hide()
        self.firstname_change.raise_()
        self.firstname_change.hide()
        self.theme.raise_()
        self.light_theme.raise_()
        self.Light_border_up_2.raise_()
        self.Checkbox_Light.raise_()
        self.LightDeal.raise_()
        self.Light.raise_()
        self.Dark_border_up_2.raise_()
        self.Dark.raise_()
        self.dark_theme.raise_()
        self.Checkbox_Dark_2.raise_()
        self.DarkDEal.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo"))
        self.save_change.setText(_translate("MainWindow","Save"))
        self.setting_menu.setText(_translate("MainWindow", "..."))
        self.personalInf.setText(_translate("MainWindow", "Personal Information"))
        self.change_avatar.setText(_translate("MainWindow", "Add or Change"))
        self.first_name.setText(_translate("MainWindow", "First Name:"))
        self.second_name.setText(_translate("MainWindow", "Second Name:"))
        self.name.setText(_translate("MainWindow", "Name"))
        self.secname.setText(_translate("MainWindow", "Secname"))
        self.change_name.setText(_translate("MainWindow", "Change"))
        self.change_secname.setText(_translate("MainWindow", "Change"))
        self.theme.setText(_translate("MainWindow", "Theme"))
        self.LightDeal.setText(_translate("MainWindow", "Your Deal"))
        self.Light.setText(_translate("MainWindow", "Light"))
        self.Dark.setText(_translate("MainWindow", "Dark"))
        self.DarkDEal.setText(_translate("MainWindow", "Your Deal"))
        self.statistic_label.setText(_translate("MainWindow","Statistic"))
        self.account_label.setText(_translate("MainWindow","Tasks"))

    def close_line_edit(self):
        self.save_change.close()
        self.firstname_change.close()
        self.secondname_change.close()
        self.secondname_change.clear()
        self.firstname_change.clear()
    def change_name_pressed(self):
        self.save_change.show()
        self.firstname_change.show()
    def change_secname_pressed(self):
        self.save_change.show()
        self.secondname_change.show()
    def check_theme(self):
        if Choose_Theme.theme == 0:
            self.background.setPixmap(QtGui.QPixmap("icons/background_settings_light.png"))
            self.background.setScaledContents(True)
            self.setting_menu.setIcon(QtGui.QIcon("icons/icon_gear.png"))
            self.personalInf.setStyleSheet("font-size: 20px;\n"
            "color: black;\n"
            "font-weight: bold;\n"
            "")
            self.first_name.setStyleSheet("font-size: 20px;\n"
            "color: black;\n"
            "")
            self.second_name.setStyleSheet("font-size: 20px;\n"
            "color: black;\n"
            "")
            self.name.setStyleSheet("color: #474747;\n"
            "font-size:16px;\n"
            "font-weight:bold;\n"
            "\n"
            "")
            self.secname.setStyleSheet("font-size: 16px;\n"
        "font-weight: bold;\n"
        "color: #474747;\n"
        "")
            self.theme.setStyleSheet("font-size:20px;\n"
            "font-weight: bold;\n"
            "color:black;\n"
            "")
            self.secondname_change.setStyleSheet("background-color:#C4C1C1;"
            "font-size: 14px;"
            "border: none;"
            "color:black;"
            "font-weight: bold;"
            "border-radius:10px;"
            "border-color:white;")
            self.firstname_change.setStyleSheet("background-color:#C4C1C1;"
            "font-size: 14px;"
            "border: none;"
            "color:black;"
            "font-weight: bold;"
            "border-radius:10px;"
            "border-color:white;")
            self.settings_popup.setStyleSheet("color: #E2E2E2;")
            self.mainwindow_button.setIcon(QtGui.QIcon("icons/icon_list_light.png"))
        else:
            self.background.setPixmap(QtGui.QPixmap("icons/background_Settings.png"))
            self.background.setScaledContents(True)
            self.setting_menu.setIcon(QtGui.QIcon("icons/icon_gear_dark.png"))
            self.personalInf.setStyleSheet("font-size: 20px;\n"
            "color: white;\n"
            "font-weight: bold;\n"
            "")
            self.first_name.setStyleSheet("font-size: 20px;\n"
            "color: white;\n"
            "")
            self.second_name.setStyleSheet("font-size: 20px;\n"
            "color: white;\n"
            "")
            self.name.setStyleSheet("color: #FFFFFF;\n"
            "font-size:16px;\n"
            "font-weight:bold;\n"
            "\n"
            "")
            self.secname.setStyleSheet("font-size: 16px;\n"
        "font-weight: bold;\n"
        "color: #FFFFFF;\n"
        "")
            self.theme.setStyleSheet("font-size:20px;\n"
            "font-weight: bold;\n"
            "color:white;\n"
            "")
            self.secondname_change.setStyleSheet("background-color:#262927;"
            "font-size: 14px;"
            "border: none;"
            "color:white;"
            "font-weight: bold;"
            "border-radius:10px;"
            "border-color:white;")
            self.firstname_change.setStyleSheet("background-color:#262927;"
            "font-size: 14px;"
            "border: none;"
            "color:white;"
            "font-weight: bold;"
            "border-radius:10px;"
            "border-color:white;")
            self.settings_popup.setStyleSheet("background-color: #666666;")

    def settings_but_open(self):
        self.statistic_label.raise_()
        self.account_label.show()
        self.settings_popup.raise_()
        self.settings_popup.show()
        self.mainwindow_button.raise_()
        self.mainwindow_button.show()
        self.statistic_button.raise_()
        self.statistic_button.show()
        self.setting_menu.clicked.connect(self.settings_but_close)
        self.setting_menu.clicked.connect(self.close_line_edit)
    def settings_but_close(self):
        self.statistic_label.hide()
        self.settings_popup.hide()
        self.mainwindow_button.hide()
        self.account_label.hide()
        self.statistic_button.hide()
        self.setting_menu.clicked.connect(self.settings_but_open)
        self.setting_menu.clicked.connect(self.close_line_edit)
    def buttonpressed_1(self):
        self.settings_but_close()
        Choose_Theme.theme = 1
        self.check_theme()
        self.dark_theme.setStyleSheet("QToolButton{\n"
    "    border-style: hidden;\n"
    " background-color: #4E1580;  }\n"
    "")
        self.light_theme.setStyleSheet("QToolButton:clicked {\n"
    "    background-color:#959595;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "QToolButton:hover {\n"
    "    background-color: #959595;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "QToolButton {\n"
    "    background-color: #959595;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "")
    def buttonpressed_2(self):
        self.settings_but_close()
        Choose_Theme.theme = 0
        self.check_theme()
        self.light_theme.setStyleSheet("QToolButton{\n"
    "    border-style: hidden;\n"
    " background-color: #B782E5;  }\n"
    "")
        self.dark_theme.setStyleSheet("QToolButton {\n"
    "    background-color: #0D0D0D;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "")
