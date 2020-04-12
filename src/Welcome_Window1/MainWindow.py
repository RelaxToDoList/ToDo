from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("Line {\n"
"    background-color: #666666;\n"
"    }\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/icon_background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.left_button = QtGui.QToolButton(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(10,8,31,26))
        self.left_button.setIcon(QtGui.QIcon("icons/icon_list.png"))
        self.left_button.setIconSize(QtCore.QSize(31, 31))
        self.left_button.setGeometry(QtCore.QRect(10, 8, 31, 26))
        self.left_button.setStyleSheet("QToolButton {\n"
"    border: none;\n"
"    \n"
"}")
        self.left_button.setText("")
        self.left_button.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.left_button.setObjectName("left_button")
        self.Settings_but = QtGui.QToolButton(self.centralwidget)
        self.Settings_but.setGeometry(QtCore.QRect(900, 8, 28, 28))
        self.Settings_but.setIcon(QtGui.QIcon("icons/icon_gear_dark.png"))
        self.Settings_but.setIconSize(QtCore.QSize(70,70))
        self.Settings_but.setStyleSheet("border:none;\n")
        self.Settings_but.setText("")
        self.Settings_but.setObjectName("Settings_but")
        self.notification_but = QtGui.QToolButton(self.centralwidget)
        self.notification_but.setGeometry(QtCore.QRect(850, 8, 28, 28))
        self.notification_but.setObjectName("notification_but")
        self.notification_but.setIcon(QtGui.QIcon("icons/icon_notification_dark.png"))
        self.notification_but.setIconSize(QtCore.QSize(28,28))
        self.notification_but.setStyleSheet ("border: none; \n")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(399, 145, 531, 82))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setIcon(QtGui.QIcon("Checkbox_Dark.png"))
        self.checkBox.setIconSize(QtCore.QSize(24,24))
        self.checkBox.setStyleSheet("color: #FFFFFF;\n"
"font-size: 16px;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;\n"
"font-weight: bold;\n")
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.under_line = QtGui.QFrame(self.verticalLayoutWidget)
        self.under_line.setStyleSheet("")
        self.under_line.setFrameShape(QtGui.QFrame.HLine)
        self.under_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.under_line.setObjectName("under_line")
        self.verticalLayout.addWidget(self.under_line)
        self.toolButton_2 = QtGui.QToolButton(self.verticalLayoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.setIcon(QtGui.QIcon("icons/icon_plus.png"))
        self.toolButton_2.setIconSize(QtCore.QSize(28,28))
        self.toolButton_2.setStyleSheet("border:none;\n")
        self.verticalLayout.addWidget(self.toolButton_2)
        self.day = QtGui.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(400, 80, 71, 31))
        self.day.setStyleSheet("color: #FFFFFF;\n"
"font-size: 24px;\n"
"font-weight: 900;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
        self.day.setObjectName("day")
        self.Data = QtGui.QLabel(self.centralwidget)
        self.Data.setGeometry(QtCore.QRect(410, 50, 46, 13))
        self.Data.setObjectName("Data")
        self.FirstName = QtGui.QLabel(self.centralwidget)
        self.FirstName.setGeometry(QtCore.QRect(130, 70, 241, 21))
        self.FirstName.setStyleSheet("color: #FFFFFF;\n"
"font-size: 20px;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
        self.FirstName.setObjectName("FirstName")
        self.SecondName = QtGui.QLabel(self.centralwidget)
        self.SecondName.setGeometry(QtCore.QRect(130, 100, 241, 21))
        self.SecondName.setStyleSheet("color: #FFFFFF;\n"
"font-size: 20px;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style:normal;")
        self.SecondName.setObjectName("SecondName")
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(110, 410, 141, 64))
        self.dial.setObjectName("dial")
        self.dial_2 = QtGui.QDial(self.centralwidget)
        self.dial_2.setGeometry(QtCore.QRect(10, 270, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.Avatar = QtGui.QLabel(self.centralwidget)
        self.Avatar.setGeometry(QtCore.QRect(10, 60, 118, 120))
        self.Avatar.setText("")
        self.Avatar.setScaledContents(True)
        self.Avatar.setPixmap(QtGui.QPixmap("icons/Empty_avatar.png"))
        self.Avatar.setObjectName("Avatar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("ToDo", "ToDo", None, QtGui.QApplication.UnicodeUTF8))
        self.notification_but.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Let\'s start", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.day.setText(QtGui.QApplication.translate("MainWindow", "Today", None, QtGui.QApplication.UnicodeUTF8))
        self.Data.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.FirstName.setText(QtGui.QApplication.translate("MainWindow", "FirstName", None, QtGui.QApplication.UnicodeUTF8))
        self.SecondName.setText(QtGui.QApplication.translate("MainWindow", "SecondName", None, QtGui.QApplication.UnicodeUTF8))
        self.Avatar.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
