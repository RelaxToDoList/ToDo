from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QPalette
import Choose_Theme
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from qroundprogressbar import QRoundProgressBar
import random
class Ui_Core(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("Line {\n"
"    background-color: #666666;\n"
"    }\n"
"QLabel{\n"
"        color:FFFFFF;\n"
"       font-weight:bold;\n"
"        font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;\n"
"        }\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(380,141,700,335)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.horizontalHeader().hide()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,200)
        self.progress = QRoundProgressBar(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(125,410,141,100))
        self.progress.setBarStyle(QRoundProgressBar.BarStyle.DONUT)
        self.palette = QPalette()
        self.brush = QBrush(QColor(138,43,226))
        self.brush.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active,QPalette.Highlight, self.brush)
        self.progress.setPalette(self.palette)
        self.progress.show()
        self.progress.setValue(0)
        self.progress.setStyleSheet("background-color:#333333;"
        "color: #414040;")
        self.radio_monday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_monday.setGeometry(QtCore.QRect(90, 167, 150, 50))
        self.radio_monday.setObjectName("radio_monday")
        self.radio_tuesday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_tuesday.setGeometry(QtCore.QRect(90,207,150,50))
        self.radio_tuesday.setObjectName("radio_tuesday")
        self.radio_wednesday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_wednesday.setGeometry(QtCore.QRect(115,247,150,50))
        self.radio_wednesday.setObjectName("radio_wednesday")
        self.radio_thursday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_thursday.setGeometry(QtCore.QRect(100,287,150,50))
        self.radio_thursday.setObjectName("radio_thursday")
        self.radio_friday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_friday.setGeometry(QtCore.QRect(70,327,150,50))
        self.radio_friday.setObjectName("radio_friday")
        self.radio_saturday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_saturday.setGeometry(QtCore.QRect(90,367,150,50))
        self.radio_saturday.setObjectName("radio_saturday")
        self.radio_sunday = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_sunday.setGeometry(QtCore.QRect(85,407,150,50))
        self.radio_sunday.setObjectName("radio_sunday")
        self.label_task_prog = QtWidgets.QLabel(self.centralwidget)
        self.label_task_prog.setGeometry(QtCore.QRect(10,94,300,50))
        self.label_task_prog.setObjectName("label_task_prog")
        self.label_task_prog.setStyleSheet("color: white;"
        "font-size:20px;")
        self.label_monday = QtWidgets.QLabel(self.centralwidget)
        self.label_monday.setGeometry(QtCore.QRect(10,164,150,50))
        self.label_monday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_monday.setObjectName("label_monday")
        self.label_tuesday = QtWidgets.QLabel(self.centralwidget)
        self.label_tuesday.setGeometry(QtCore.QRect(10,204,150,50))
        self.label_tuesday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_tuesday.setObjectName("label_tuesday")
        self.label_wednesday = QtWidgets.QLabel(self.centralwidget)
        self.label_wednesday.setGeometry(QtCore.QRect(10,244,150,50))
        self.label_wednesday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_wednesday.setObjectName("label_wednesday")
        self.label_thursday = QtWidgets.QLabel(self.centralwidget)
        self.label_thursday.setGeometry(QtCore.QRect(10,284,150,50))
        self.label_thursday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_thursday.setObjectName("label_thursday")
        self.label_friday = QtWidgets.QLabel(self.centralwidget)
        self.label_friday.setGeometry(QtCore.QRect(10,324,150,50))
        self.label_friday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_friday.setObjectName("label_friday")
        self.label_saturday = QtWidgets.QLabel(self.centralwidget)
        self.label_saturday.setGeometry(QtCore.QRect(10,364,150,50))
        self.label_saturday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_saturday.setObjectName("label_saturday")
        self.label_sunday = QtWidgets.QLabel(self.centralwidget)
        self.label_sunday.setGeometry(QtCore.QRect(10,404,150,50))
        self.label_sunday.setStyleSheet("color:white;"
        "font-size:20px;")
        self.label_sunday.setObjectName("label_sunday")
        self.todo_list_week = QtWidgets.QLabel(self.centralwidget)
        self.todo_list_week.setGeometry(QtCore.QRect(10,124,350,50))
        self.todo_list_week.setObjectName("todo_list_week")
        self.todo_list_week.setStyleSheet("color:black;"
        "font-size:21px;"
        "font-weight:bold;")
        self.label_daily_task = QtWidgets.QLabel(self.centralwidget)
        self.label_daily_task.setGeometry(QtCore.QRect(10,44,145,50))
        self.label_daily_task.setObjectName("label_daily_task")
        self.label_daily_task.setStyleSheet("color: black;"
        "font-size:21px; "
        "font-weight:bold;")
        self.left_button_popup_window = QtWidgets.QGraphicsView(self.centralwidget)
        self.left_button_popup_window.setGeometry(QtCore.QRect(0,42,380,517))
        self.left_button_popup_window.setObjectName("left_button_popup_window")
        self.left_button_popup_window.setStyleSheet("background-color: #666666;"
        "border: 1px;")
        self.okey = QtWidgets.QToolButton(self.centralwidget)
        self.okey.setGeometry(QtCore.QRect(895,385,25,25))
        self.okey.setIcon(QtGui.QIcon("icons/icon_plus.png"))
        self.okey.setIconSize(QtCore.QSize(25,25))
        self.okey.setStyleSheet("border:none;")
        self.okey.setObjectName("okey")
        self.settings_but_open = QtWidgets.QToolButton(self.centralwidget)
        self.settings_but_open.setGeometry(QtCore.QRect(660,50,30, 30))
        self.settings_but_open.setIcon(QtGui.QIcon("icons/icon_account.png"))
        self.settings_but_open.setStyleSheet("border: none;")
        self.settings_but_open.setIconSize(QtCore.QSize(30,30))
        self.line_enter = QtWidgets.QLineEdit(self.centralwidget)
        self.line_enter.setGeometry(QtCore.QRect(400,350,531,31))
        self.line_enter.setObjectName("line_enter")
        self.line_enter.setStyleSheet("font-weight: bold;"
        "font-size:16px;")
        self.statistic_label = QtWidgets.QLabel(self.centralwidget)
        self.statistic_label.setGeometry(QtCore.QRect(710,100,50,30))
        self.statistic_label.setStyleSheet("font-weight: bold;"
        "font-size:15px;"
        "color: #000000;")
        self.account_label = QtWidgets.QLabel(self.centralwidget)
        self.account_label.setGeometry(QtCore.QRect(710,50,50,30))
        self.account_label.setStyleSheet("font-weight: bold;"
        "font-size:14px;"
        "color: #000000;")
        self.settings_popup = QtWidgets.QGraphicsView(self.centralwidget)
        self.settings_popup.setGeometry(QtCore.QRect(650, 41 , 308, 517))
        self.settings_popup.setObjectName("settings_popup")
        self.did = QtWidgets.QLabel(self.centralwidget)
        self.did.setGeometry(QtCore.QRect(10,290, 371, 21))
        self.did.setObjectName("did")
        self.do = QtWidgets.QLabel(self.centralwidget)
        self.do.setGeometry(QtCore.QRect(10, 250, 371, 21 ))
        self.do.setObjectName("do")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.left_button = QtWidgets.QToolButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.left_button.setIconSize(QtCore.QSize(31, 31))
        self.left_button.setGeometry(QtCore.QRect(10, 8, 31, 26))
        self.left_button.setStyleSheet("QToolButton {\n"
"    border: none;\n"
"    \n"
"}")
        self.left_button.setText("")
        self.left_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.left_button.setObjectName("left_button")
        self.Settings_but = QtWidgets.QToolButton(self.centralwidget)
        self.Settings_but.setGeometry(QtCore.QRect(900, 10, 31, 26))
        self.Settings_but.setIconSize(QtCore.QSize(70,70))
        self.Settings_but.setStyleSheet("border:none;")
        self.Settings_but.setText("")
        self.Settings_but.setObjectName("Settings_but")
        self.daily_add_button = QtWidgets.QToolButton(self.centralwidget)
        self.daily_add_button.setGeometry(QtCore.QRect(110,45,100,50))
        self.daily_add_button.setObjectName("daily_add_button")
        self.statistic_button = QtWidgets.QToolButton(self.centralwidget)
        self.statistic_button.setGeometry(QtCore.QRect(660,100,35,35))
        self.statistic_button.setObjectName("statistic_button")
        self.statistic_button.setIcon(QtGui.QIcon("icons/icon_statistic.png"))
        self.statistic_button.setIconSize(QtCore.QSize(35,35))
        self.statistic_button.setStyleSheet("border:none;")
        self.notification_but = QtWidgets.QToolButton(self.centralwidget)
        self.notification_but.setGeometry(QtCore.QRect(850, 10, 31, 26))
        self.notification_but.setIconSize(QtCore.QSize(28,28))
        self.notification_but.setObjectName("notification_but")
        self.notification_but.setStyleSheet("border:none;")
        self.day = QtWidgets.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(400, 80, 77, 31))
        self.day.setStyleSheet("color: #FFFFFF;\n"
"font-size: 24px;\n"#
"font-weight: 900;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
        self.day.setObjectName("day")
        self.Data = QtWidgets.QLabel(self.centralwidget)
        self.Data.setGeometry(QtCore.QRect(400, 50, 150, 31))
        self.Data.setStyleSheet("color:#949494;"
        "font-size:16px;")
        self.Data.setObjectName("Data")
        self.FirstName = QtWidgets.QLabel(self.centralwidget)
        self.FirstName.setGeometry(QtCore.QRect(130, 70, 241, 21))
        self.FirstName.setObjectName("FirstName")
        self.SecondName = QtWidgets.QLabel(self.centralwidget)
        self.SecondName.setGeometry(QtCore.QRect(130, 100, 241, 21))
        self.SecondName.setObjectName("SecondName")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(110, 410, 141, 64))
        self.dial.setObjectName("dial")
        self.dial_2 = QtWidgets.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(10, 270, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.Avatar = QtWidgets.QLabel(self.centralwidget)
        self.Avatar.setGeometry(QtCore.QRect(10, 60, 118, 120))
        self.Avatar.setText("")
        self.Avatar.setPixmap(QtGui.QPixmap("icons/Empty_avatar.png"))
        self.Avatar.setScaledContents(True)
        self.Avatar.setObjectName("Avatar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 270, 529, 21))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(390, 130, 551, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.check_box = QtWidgets.QToolButton(self.centralwidget)
        self.check_box.setIconSize(QtCore.QSize(27,27))
        self.check_box.setStyleSheet("border:none")
        self.check_box.setObjectName("check_box")
        self.deal_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.deal_text.setText("Your Task")
        self.deal_text.setObjectName("deal_text")
        self.accept = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.accept.setGeometry(QtCore.QRect(880,370,50,50))
        self.accept.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.accept.setObjectName("accept")
        self.label_hint = QtWidgets.QLabel(self.centralwidget)
        self.label_hint.setGeometry(QtCore.QRect(600,300,152,70))
        self.label_hint.setObjectName("label_hint")
        self.label_hint.setStyleSheet("color: black;"
        "font-size:14px;"
        "font-weight:bold;")
        self.gridLayout_2.addWidget(self.deal_text, 0, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(380, 317, 585, 200))
        self.graphicsView.setObjectName("graphicsView")
        self.remaining_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.remaining_time.setObjectName("remaining_time")
        self.gridLayout_2.addWidget(self.remaining_time, 0, 2, 1, 1)
        self.notification_single_but = QtWidgets.QToolButton(self.centralwidget)
        self.notification_single_but.setGeometry(400,390,25,25)
        self.notification_single_but.setIcon(QtGui.QIcon("icons/icon_notification.png"))
        self.notification_single_but.setStyleSheet("border:none;\n")
        self.notification_single_but.setIconSize(QtCore.QSize(25,25))
        self.notification_single_but.setObjectName("notification_single_but")
        self.plus_button = QtWidgets.QToolButton(self.centralwidget)
        self.plus_button.setStyleSheet("border:none;\n")
        self.plus_button.setIconSize(QtCore.QSize(24,24))
        self.plus_button.setIcon(QtGui.QIcon("icons/icon_plus.png"))
        self.plus_button.setObjectName("plus_button")
        self.add_task = QtWidgets.QLabel(self.centralwidget)
        self.add_task.setText("Add task")
        self.add_task.setText("Add")
        self.add_task.setObjectName("add_task")
        self.label.raise_()
        self.left_button.raise_()
        self.Settings_but.raise_()
        self.notification_but.raise_()
        self.Data.raise_()
        self.FirstName.raise_()
        self.progress.raise_()
        self.day.raise_()
        self.SecondName.raise_()
        self.Avatar.raise_()
        self.gridLayoutWidget.raise_()
        self.do.raise_()
        self.did.raise_()
        self.tableWidget.raise_()
        self.graphicsView.raise_()
        self.settings_popup.raise_()
        self.settings_but_open.raise_()
        self.line_enter.raise_()
        self.account_label.raise_()
        self.settings_popup.hide()
        self.settings_but_open.hide()
        self.account_label.hide()
        self.graphicsView.hide()
        self.line_enter.hide()
        self.left_button_popup_window.raise_()
        self.left_button_popup_window.hide()
        self.radio_monday.raise_()
        self.radio_monday.hide()
        self.radio_tuesday.raise_()
        self.radio_tuesday.hide()
        self.radio_wednesday.raise_()
        self.radio_wednesday.hide()
        self.radio_thursday.raise_()
        self.radio_thursday.hide()
        self.radio_friday.raise_()
        self.radio_friday.hide()
        self.radio_saturday.raise_()
        self.radio_saturday.hide()
        self.radio_sunday.raise_()
        self.radio_sunday.hide()
        self.label_monday.raise_()
        self.label_monday.hide()
        self.label_tuesday.raise_()
        self.label_tuesday.hide()
        self.label_thursday.raise_()
        self.label_thursday.hide()
        self.label_wednesday.raise_()
        self.label_wednesday.hide()
        self.label_friday.raise_()
        self.label_friday.hide()
        self.label_saturday.raise_()
        self.label_saturday.hide()
        self.label_sunday.raise_()
        self.label_sunday.hide()
        self.todo_list_week.raise_()
        self.todo_list_week.hide()
        self.daily_add_button.raise_()
        self.daily_add_button.hide()
        self.label_task_prog.raise_()
        self.label_task_prog.hide()
        self.label_daily_task.raise_()
        self.label_daily_task.hide()
        self.label_hint.raise_()
        self.label_hint.hide()
        self.radio_monday.raise_()
        self.radio_monday.hide()
        self.statistic_button.raise_()
        self.statistic_button.hide()
        self.statistic_label.raise_()
        self.statistic_label.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.theme = 1
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ToDo", "ToDo"))
        self.do.setText(_translate("MainWindow","Today you have to do"))
        self.did.setText(_translate("MainWindow","Today you completed"))
        self.account_label.setText(_translate("MainWindow","Account"))
        self.notification_but.setText(_translate("MainWindow", "..."))
        self.day.setText(_translate("MainWindow", "Today"))
        self.Data.setText(_translate("MainWindow", "Date"))
        self.FirstName.setText(_translate("MainWindow", "FirstName"))
        self.SecondName.setText(_translate("MainWindow", "SecondName"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.check_box.setText(_translate("MainWindow", "..."))
        self.deal_text.setText(_translate("MainWindow", "Your task"))
        self.remaining_time.setText(_translate("MainWindow", "Remaining_Time"))
        self.notification_single_but.setText(_translate("MainWindow", "..."))
        self.plus_button.setText(_translate("MainWindow", "..."))
        self.add_task.setText(_translate("MainWindow", "Add"))
        self.label_hint.setText(_translate("MainWindow","Put your task here!"))
        self.label_daily_task.setText(_translate("MainWindow","Your Daily task:"))
        self.label_task_prog.setText(_translate("MainWindow","task"))
        self.daily_add_button.setText(_translate("MainWindow","Add"))
        self.todo_list_week.setText(_translate("MainWindow","Choose day of the week:"))
        self.label_monday.setText(_translate("MainWindow","Monday"))
        self.label_tuesday.setText(_translate("MainWindow","Tuesday"))
        self.label_wednesday.setText(_translate("MainWindow","Wednesday"))
        self.label_thursday.setText(_translate("MainWindow","Thursday"))
        self.label_friday.setText(_translate("MainWindow","Friday"))
        self.label_saturday.setText(_translate("MainWindow","Saturday"))
        self.label_sunday.setText(_translate("MainWindow","Sunday"))
        self.statistic_label.setText(_translate("MainWindow","Statistic"))

    def check_theme_person(self):
        if Choose_Theme.theme == 0:
            self.label.setPixmap(QtGui.QPixmap("icons/background_light.png"))
            self.label.setScaledContents(True)
            self.left_button.setIcon(QtGui.QIcon("icons/icon_list_light.png"))
            self.Settings_but.setIcon(QtGui.QIcon("icons/icon_gear.png"))
            self.notification_but.setIcon(QtGui.QIcon("icons/icon_notification.png"))
            self.FirstName.setStyleSheet("color:#666666;"
            "font-size: 20px;\n"
            "font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
            "font-style:normal;")
            self.SecondName.setStyleSheet("color:#666666;"
            "font-size: 20px;\n"
            "font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
            "font-style:normal;")
            self.do.setStyleSheet("color:#666666;"
            "font-size: 20px;")
            self.did.setStyleSheet("color:#666666;"
            "font-size: 20px;")
            self.daily_add_button.setStyleSheet("color: #663366;"
            "font-size:12px;"
            "border:none;"
            "font-weight: bold;")
            self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Dark.png"))
            self.deal_text.setStyleSheet("color:#161616;\n"
            "font-weight:bold;\n"
            "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;"
            "font-size:10px;")
            self.Data.setStyleSheet("color:#605E5E;"
            "font-size:16px;")
            self.day.setStyleSheet("color: black;\n"
            "font-size: 24px;\n"
            "font-weight: 900;\n"
            "font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
            "font-style:normal;")
            self.remaining_time.setStyleSheet("color: black;"
            "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;")
            self.add_task.setStyleSheet("color: black;"
            "font-size:14px;")
            self.settings_popup.setStyleSheet("background-color: #E2E2E2;"
            "border:5px black")
            self.left_button_popup_window.setStyleSheet("background-color: #E2E2E2;"
            "border: 1px;")
            self.graphicsView.setStyleSheet("background-color:#E2E2E2;"
            "border-radius:15px;")
            self.label_monday.setStyleSheet("color:#474747;"
            "font-size:20px;")
            self.label_tuesday.setStyleSheet("color:#474747;"
            "font-size:20px;")
            self.label_wednesday.setStyleSheet("color:#474747;"
            "font-size:20px;")
            self.label_thursday.setStyleSheet("color:#474747;"
            "font-size:20px;")
            self.label_friday.setStyleSheet("color: #474747;"
            "font-size:20px;")
            self.label_saturday.setStyleSheet("color: #474747;"
            "font-size:20px;")
            self.label_sunday.setStyleSheet("color: #474747;"
            "font-size:20px;")
            self.label_task_prog.setStyleSheet("color: #474747;"
            "font-size:20px;")
            self.tableWidget.setStyleSheet("QTableWidget{"
            "background-color:#D7D7D7;"
            "color:white;\n"
            "font-weight:bold;\n"
            "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;"
            "font-size:16px;"
            "selection-background-color:#D7D7D7;"
            "border: none;}"
            "QTableWidget:item {"
            "border-style:2px solid;"
            "gridline-color: #fffff8;"
            "border-color:#D7D7D7; }"
            #"QTableView:item {"
        #    "border-bottom: 2px solid white;}"
            )
        else:
            self.add_task.setStyleSheet("color: #949494;"
            "font-size:14px;")
            self.remaining_time.setStyleSheet("color: #666666;"
            "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;")
            self.graphicsView.setStyleSheet("background-color:#666666;"
            "border-radius:15px;")
            self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Light.png"))
            self.deal_text.setStyleSheet("color:white;\n"
    "font-weight:bold;\n"
    "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;"
    "font-size:16px;")
            self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Dark.png"))
            self.SecondName.setStyleSheet("color: #FFFFFF;\n"
    "font-size: 20px;\n"
    "font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
    "font-style:normal;")
            self.FirstName.setStyleSheet("color: #FFFFFF;\n"
    "font-size: 20px;\n"
    "font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
    "font-style:normal;")
            self.notification_but.setIcon(QtGui.QIcon("icons/icon_notification_dark.png"))
            self.daily_add_button.setStyleSheet("color: #663366;"
            "font-size:12px;"
            "border:none;"
            "font-weight: bold;")
            self.daily_add_button.setStyleSheet("color: #663366;"
            "font-size:12px;"
            "border:none;"
            "font-weight: bold;")
            self.Settings_but.setIcon(QtGui.QIcon("icons/icon_gear_dark.png"))
            self.left_button.setIcon(QtGui.QIcon("icons/icon_list.png"))
            self.label.setPixmap(QtGui.QPixmap("icons/icon_background.png"))
            self.do.setStyleSheet("color: white;"
            "font-size: 20px;")
            self.did.setStyleSheet("color:white;"
            "font-size: 20px;")
            self.settings_popup.setStyleSheet("background-color: #666666;"
            "border:5px black")
            self.tableWidget.setStyleSheet("QTableWidget{"
            "background-color:#0D0D0D;"
            "color:white;\n"
            "font-weight:bold;\n"
            "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;"
            "font-size:16px;"
            "selection-background-color:#0D0D0D;"
            "border: none;}"
            "QTableWidget:item {"
            "border-style:2px solid;"
            "gridline-color: #fffff8;"
            "border-color:#0D0D0D; }"
            #"QTableView:item {"
        #    "border-bottom: 2px solid white;}"
            )
    def left_button_popup_window_open(self):
        self.radio_tuesday.show()
        self.radio_wednesday.show()
        self.radio_thursday.show()
        self.radio_friday.show()
        self.radio_saturday.show()
        self.radio_sunday.show()
        self.radio_monday.show()
        self.daily_add_button.show()
        self.label_monday.show()
        self.label_tuesday.show()
        self.label_wednesday.show()
        self.label_thursday.show()
        self.label_friday.show()
        self.label_saturday.show()
        self.label_sunday.show()
        self.todo_list_week.show()
        self.label_task_prog.show()
        self.left_button_popup_window.show()
        self.label_daily_task.show()
        self.left_button.clicked.connect(self.left_button_popup_window_close)
        self.left_button.clicked.connect(self.add_task_button_unclicked)
        self.left_button.clicked.connect(self.close_window)
        self.addtaskfromfile()
        self.daily_add_button.show()
    def left_button_popup_window_close(self):
        self.radio_tuesday.hide()
        self.radio_wednesday.hide()
        self.radio_thursday.hide()
        self.radio_friday.hide()
        self.radio_saturday.hide()
        self.radio_sunday.hide()
        self.radio_monday.hide()
        self.label_monday.hide()
        self.label_tuesday.hide()
        self.label_wednesday.hide()
        self.label_thursday.hide()
        self.label_friday.hide()
        self.label_saturday.hide()
        self.label_sunday.hide()
        self.todo_list_week.hide()
        self.label_task_prog.hide()
        self.label_daily_task.hide()
        self.daily_add_button.hide()
        self.left_button_popup_window.hide()
        self.left_button.clicked.connect(self.left_button_popup_window_open)
    def add_task_button_unclicked(self):
        self.label_hint.hide()
        self.okey.hide()
        self.notification_single_but.hide()
        self.line_enter.hide()
        self.graphicsView.hide()
        self.plus_button.clicked.connect(self.add_task_button_clicked)
        self.okey.clicked.connect(self.add_task_button_clicked)
    def add_task_button_clicked(self):
        self.okey.raise_()
        self.okey.show()
        self.label_hint.show()
        self.notification_single_but.raise_()
        self.notification_single_but.show()
        self.line_enter.show()
        self.graphicsView.show()
        self.close_window()
        self.left_button_popup_window_close()
        self.plus_button.clicked.connect(self.close_window)
        self.plus_button.clicked.connect(self.left_button_popup_window_close)
        self.plus_button.clicked.connect(self.add_task_button_unclicked)
        self.okey.clicked.connect(self.add_task_button_unclicked)
    def settings_but_clicked(self):
        self.statistic_label.show()
        self.statistic_button.show()
        self.settings_popup.show()
        self.settings_but_open.show()
        self.account_label.show()
        self.add_task_button_unclicked()
        self.left_button_popup_window_close()
        self.Settings_but.clicked.connect(self.close_window)
        self.Settings_but.clicked.connect(self.left_button_popup_window_close)
        self.Settings_but.clicked.connect(self.add_task_button_unclicked)
    def close_window(self):
        self.statistic_label.hide()
        self.statistic_button.hide()
        self.settings_popup.hide()
        self.settings_but_open.hide()
        self.account_label.hide()
        self.Settings_but.clicked.connect(self.settings_but_clicked)
    def check_box_unchecked(self):
        if Choose_Theme.theme == 0:
            self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Dark.png"))
            self.check_box.clicked.connect(self.check_box_checked)
        else:
            self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Light.png"))
            self.check_box.clicked.connect(self.check_box_checked)
    def check_box_checked(self):
        if Choose_Theme.theme == 0:
            self.check_box.setIcon(QtGui.QIcon("icons/Checkbox_Dark.png"))
        else:
            self.check_box.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))

    def addtaskfromfile(self):
        taskfile = open("tasks/tasks.txt","r", encoding ='utf-8')
        row = random.randint(0,21)
        lines = taskfile.readlines()[row]
        lines = str(lines)
        self.label_task_prog.setText(lines)
        self.daily_add_button.clicked.connect(lambda: self.add_task_random(lines))


    # def addWidgetssDB(self,task_db):  # Not real. Just for seeing
    #     row = self.tableWidget.rowCount()
    #     self.tableWidget.insertRow(row)
    #     row = row - 9
    #     time2 = 0
    #     item = QTableWidgetItem(deal_text)
    #     time = QTableWidgetItem(f"Remaining Time: {time2}")
    #     self.tableWidget.setCellWidget(row,0,self.check_box)
    #     self.tableWidget.setItem(row,1,item)
    #     self.tableWidget.setItem(row,2,time)
    #     row = row + 1
    #     self.tableWidget.setCellWidget(row,0,self.plus_button)

    def addWidgetss(self,text_task, str1, str2,time_deadline_time):  # Not real. Just for seeing
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        row = row - str1
        time = QTableWidgetItem(time_deadline_time)
        object = self.check_box
        item = QTableWidgetItem(text_task)
        self.tableWidget.setCellWidget(row,0,object)
        self.tableWidget.setItem(row,1,item)
        self.tableWidget.setItem(row,2,QTableWidgetItem(f"Remaining time: {time_deadline_time} hours"))
        row = row + str2
        self.tableWidget.setCellWidget(row,0,self.plus_button)
global daily_task
daily_task = 0
