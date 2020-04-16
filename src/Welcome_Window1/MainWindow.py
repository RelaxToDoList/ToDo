from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(130,410,141,64)
        self.progress.setStyleSheet("border: 15px;"
        "color: ;")
        self.progress.setValue(50)
        self.did = QtWidgets.QLabel(self.centralwidget)
        self.did.setGeometry(QtCore.QRect(10,290, 371, 21))
        self.did.setObjectName("did")
        self.did.setStyleSheet("color:white;"
        "font-size: 20px;")
        self.do = QtWidgets.QLabel(self.centralwidget)
        self.do.setGeometry(QtCore.QRect(10, 250, 371, 21 ))
        self.do.setObjectName("do")
        self.do.setStyleSheet("color: white;"
        "font-size: 20px;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/icon_background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.left_button = QtWidgets.QToolButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.left_button.setIcon(QtGui.QIcon("icons/icon_list.png"))
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
        self.Settings_but.setIcon(QtGui.QIcon("icons/icon_gear_dark.png"))
        self.Settings_but.setIconSize(QtCore.QSize(70,70))
        self.Settings_but.setStyleSheet("border:none;")
        self.Settings_but.setText("")
        self.Settings_but.setObjectName("Settings_but")
        self.notification_but = QtWidgets.QToolButton(self.centralwidget)
        self.notification_but.setGeometry(QtCore.QRect(850, 10, 31, 26))
        self.notification_but.setIcon(QtGui.QIcon("icons/icon_notification_dark.png"))
        self.notification_but.setIconSize(QtCore.QSize(28,28))
        self.notification_but.setObjectName("notification_but")
        self.notification_but.setStyleSheet("border:none;")
        self.day = QtWidgets.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(400, 80, 71, 31))
        self.day.setStyleSheet("color: #FFFFFF;\n"
"font-size: 24px;\n"
"font-weight: 900;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
        self.day.setObjectName("day")
        self.Data = QtWidgets.QLabel(self.centralwidget)
        self.Data.setGeometry(QtCore.QRect(400, 50, 70, 31))
        self.Data.setStyleSheet("color:#949494;"
        "font-size:16px;")
        self.Data.setObjectName("Data")
        self.FirstName = QtWidgets.QLabel(self.centralwidget)
        self.FirstName.setGeometry(QtCore.QRect(130, 70, 241, 21))
        self.FirstName.setStyleSheet("color: #FFFFFF;\n"
"font-size: 20px;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
        self.FirstName.setObjectName("FirstName")
        self.SecondName = QtWidgets.QLabel(self.centralwidget)
        self.SecondName.setGeometry(QtCore.QRect(130, 100, 241, 21))
        self.SecondName.setStyleSheet("color: #FFFFFF;\n"
"font-size: 20px;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
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
        self.check_box = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Light.png"))
        self.check_box.setIconSize(QtCore.QSize(24,24))
        self.check_box.setStyleSheet("border:none")
        self.check_box.setObjectName("check_box")
        self.gridLayout_2.addWidget(self.check_box, 0, 0, 1, 1)
        self.deal_text = QtWidgets.QLabel(self.gridLayoutWidget)
        self.deal_text.setStyleSheet("color:white;\n"
"font-weight:bold;\n"
"font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;"
"font-size:16px;")
        self.deal_text.setText("Your Task")
        self.deal_text.setObjectName("deal_text")
        self.gridLayout_2.addWidget(self.deal_text, 0, 1, 1, 1)
        self.remaining_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.remaining_time.setStyleSheet("color: #666666;"
        "font-family: Calibri, Candara, Segoe, \\Segoe UI\\, Optima, Arial, sans-serif;")
        self.remaining_time.setObjectName("remaining_time")
        self.gridLayout_2.addWidget(self.remaining_time, 0, 2, 1, 1)
        self.notification_single_but = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.notification_single_but.setIcon(QtGui.QIcon("icons/icon_timer_dark.png"))
        self.notification_single_but.setStyleSheet("border:none;\n")
        self.notification_single_but.setIconSize(QtCore.QSize(50,34))
        self.notification_single_but.setObjectName("notification_single_but")
        self.gridLayout_2.addWidget(self.notification_single_but, 0, 3, 1, 1)
        self.plus_button = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.plus_button.setIcon(QtGui.QIcon("icons/icon_plus.png"))
        self.plus_button.setIconSize(QtCore.QSize(24,24))
        self.plus_button.setStyleSheet("border:none;\n")
        self.plus_button.setObjectName("plus_button")
        self.gridLayout_2.addWidget(self.plus_button, 2, 0, 1, 1)
        self.add_task = QtWidgets.QLabel(self.gridLayoutWidget)
        self.add_task.setText("Add task")
        self.add_task.setStyleSheet("color: #949494;"
        "font-size:14px;")
        self.add_task.setText("Add")
        self.add_task.setObjectName("add_task")
        self.gridLayout_2.addWidget(self.add_task, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 4)
        self.label.raise_()
        self.left_button.raise_()
        self.Settings_but.raise_()
        self.notification_but.raise_()
        self.Data.raise_()
        self.FirstName.raise_()
        self.day.raise_()
        self.SecondName.raise_()
        self.Avatar.raise_()
        self.gridLayoutWidget.raise_()
        self.do.raise_()
        self.did.raise_()
        self.progress.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ToDo", "ToDo"))
        self.do.setText(_translate("MainWindow","Today you have to do"))
        self.did.setText(_translate("MainWindow","Today you completed"))
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

    def check_box_unchecked(self):
        self.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Light.png"))
        self.check_box.clicked.connect(self.check_box_checked)
    def check_box_checked(self):
        self.check_box.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
        self.check_box.clicked.connect(self.check_box_unchecked)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Core()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
