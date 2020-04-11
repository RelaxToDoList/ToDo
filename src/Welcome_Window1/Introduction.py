from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: #337AB7;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtGui.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("icons/wall.png"))
        self.background.setObjectName("background")
        self.listIcon = QtGui.QLabel(self.centralwidget)
        self.listIcon.setGeometry(QtCore.QRect(380, 20, 161, 141))
        self.listIcon.setStyleSheet("color: white;\n"
"")
        self.listIcon.setText("")
        self.listIcon.setPixmap(QtGui.QPixmap("icons/icon_list"))
        self.listIcon.setScaledContents(True)
        self.listIcon.setObjectName("listIcon")
        self.Welcome = QtGui.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(330, 180, 121, 51))
        self.Welcome.setStyleSheet("font-size: 24px;\n"
"font-weight: bold;\n"
"color: #241D1D;\n"
"")
        self.Welcome.setObjectName("Welcome")
        self.usersname = QtGui.QLabel(self.centralwidget)
        self.usersname.setGeometry(QtCore.QRect(460, 180, 151, 51))
        self.usersname.setStyleSheet("font-size: 24px;\n"
"font-weight: bold;\n"
"color: #241D1D;")
        self.usersname.setObjectName("usersname")
        self.Things = QtGui.QLabel(self.centralwidget)
        self.Things.setGeometry(QtCore.QRect(260, 240, 411, 71))
        self.Things.setStyleSheet("font-size: 20px;\n"
"color: #1E1B1B;\n"
"font-family: Сomic Sans MS, cursive;\n"
"font-weight: ligther;\n"
"font-style:oblique;")
        self.Things.setObjectName("Things")
        self.Letsgobutton_2 = QtGui.QPushButton(self.centralwidget)
        self.Letsgobutton_2.setGeometry(QtCore.QRect(370, 370, 191, 71))
        self.Letsgobutton_2.setStyleSheet("QPushButton{\n"
"    background-color:#663366;\n"
"    color: white;\n"
"    font-size: 24px;\n"
"    font-weight:bold;\n"
"    font-family:Copperplate Gothic Bold, sans-serif;\n"
"    }\n"
"QPushButton:hover{\n"
"    background-color: #663385;\n"
"    color: #aaa;\n"
"    font-size: 24px;\n"
"    font-weight:bold;\n"
"    font-family:Copperplate Gothic Bold, sans-serif;\n"
"    }\n"
"QPushButton:pressed {\n"
"    background-color: #663350;\n"
"    color: white;\n"
"    font-size: 24px;\n"
"    font-weight:bold;\n"
"    font-family:Copperplate Gothic Bold, sans-serif;\n"
"    }")
        self.Letsgobutton_2.setObjectName("Letsgobutton_2")
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("ToDoList", "ToDoList", None, QtGui.QApplication.UnicodeUTF8))
        self.Welcome.setText(QtGui.QApplication.translate("MainWindow", "Welcome,", None, QtGui.QApplication.UnicodeUTF8))
        self.usersname.setText(QtGui.QApplication.translate("MainWindow", "Firstname", None, QtGui.QApplication.UnicodeUTF8))
        self.Things.setText(QtGui.QApplication.translate("MainWindow", "We hope you\'re ready to organize your things", None, QtGui.QApplication.UnicodeUTF8))
        self.Letsgobutton_2.setText(QtGui.QApplication.translate("MainWindow", "Continue", None, QtGui.QApplication.UnicodeUTF8))
