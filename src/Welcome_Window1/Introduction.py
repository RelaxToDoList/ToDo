from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Welcome(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: #337AB7;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("icons/wall.png"))
        self.background.setObjectName("background")
        self.listIcon = QtWidgets.QLabel(self.centralwidget)
        self.listIcon.setGeometry(QtCore.QRect(380, 20, 161, 141))
        self.listIcon.setStyleSheet("color: white;\n"
"")
        self.listIcon.setText("")
        self.listIcon.setPixmap(QtGui.QPixmap("icons/icon_list.png"))
        self.listIcon.setScaledContents(True)
        self.listIcon.setObjectName("listIcon")
        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(330, 180, 121, 51))
        self.Welcome.setStyleSheet("font-size: 24px;\n"
"font-weight: bold;\n"
"color: #241D1D;\n"
"")
        self.Welcome.setObjectName("Welcome")
        self.usersname = QtWidgets.QLabel(self.centralwidget)
        self.usersname.setGeometry(QtCore.QRect(460, 180, 151, 51))
        self.usersname.setStyleSheet("font-size: 24px;\n"
"font-weight: bold;\n"
"color: #241D1D;")
        self.usersname.setObjectName("usersname")
        self.Things = QtWidgets.QLabel(self.centralwidget)
        self.Things.setGeometry(QtCore.QRect(260, 240, 411, 71))
        self.Things.setStyleSheet("font-size: 20px;\n"
"color: #1E1B1B;\n"
"font-family: Сomic Sans MS, cursive;\n"
"font-weight: ligther;\n"
"font-style:oblique;")
        self.Things.setObjectName("Things")
        self.Letsgobutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Letsgobutton_2.setGeometry(QtCore.QRect(310, 370, 291, 71))
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
        self.Welcome.setText(_translate("MainWindow", "Welcome,"))
        self.usersname.setText(_translate("MainWindow", "Firstname"))
        self.Things.setText(_translate("MainWindow", "We hope you\'re ready to organize your things"))
        self.Letsgobutton_2.setText(_translate("MainWindow", "Continue"))
