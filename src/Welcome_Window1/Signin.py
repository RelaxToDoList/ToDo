from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Sign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: #337AB7;\n"
"    }\n"
"QTextEdit {\n"
"    background: none;\n"
"    border: 1px solid black;\n"
"    font-size: 21px;\n"
"    font-weight: 502;\n"
"    }\n"
"QTLineEdit {\n"
"    background: none;\n"
"    border: 1px solid black;\n"
"    font-size: 21px;\n"
"    font-weight: 502;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.Firstnamelab = QtWidgets.QLabel(self.centralwidget)
        self.Firstnamelab.setGeometry(QtCore.QRect(220, 190, 151, 16))
        self.Firstnamelab.setStyleSheet("background: none;\n"
"font-size: 15px;\n"
"font-weight:bold;")
        self.Firstnamelab.setObjectName("Firstnamelab")
        self.Secondnamelab = QtWidgets.QLabel(self.centralwidget)
        self.Secondnamelab.setGeometry(QtCore.QRect(220, 270, 151, 16))
        self.Secondnamelab.setStyleSheet("background: none;\n"
"font-size: 15px;\n"
"font-weight:bold;")
        self.Secondnamelab.setObjectName("Secondnamelab")
        self.Signin = QtWidgets.QLabel(self.centralwidget)
        self.Signin.setGeometry(QtCore.QRect(360, 40, 231, 51))
        self.Signin.setStyleSheet("background: none;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"mix-blend-mod:multiply;\n"
"display: inline-block;")
        self.Signin.setObjectName("Signin")
        self.Letsgobutton = QtWidgets.QPushButton(self.centralwidget)
        self.Letsgobutton.setGeometry(QtCore.QRect(330, 360, 291, 71))
        self.Letsgobutton.setStyleSheet("QPushButton{\n"
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
        self.Letsgobutton.setObjectName("Letsgobutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/wall.png"))
        self.label.setObjectName("label")
        self.InputFirst = QtWidgets.QLineEdit(self.centralwidget)
        self.InputFirst.setGeometry(QtCore.QRect(220, 220, 497, 35))
        self.InputFirst.setStyleSheet("background: none;\n"
"border: 1px solid black;\n"
"border: 1px solid black;\n"
"font-size: 21px;\n"
"font-weight: 502;")
        self.InputFirst.setObjectName("InputFirst")
        self.InputSecond = QtWidgets.QLineEdit(self.centralwidget)
        self.InputSecond.setGeometry(QtCore.QRect(220, 290, 497, 35))
        self.InputSecond.setStyleSheet("background: none;\n"
"border: 1px solid black;\n"
"border: 1px solid black;\n"
"font-size: 21px;\n"
"font-weight: 502;")
        self.InputSecond.setMaxLength(25)
        self.InputFirst.setMaxLength(25)
        self.InputSecond.setObjectName("InputSecond")
        self.label.raise_()
        self.Firstnamelab.raise_()
        self.Secondnamelab.raise_()
        self.Signin.raise_()
        self.Letsgobutton.raise_()
        self.InputFirst.raise_()
        self.InputSecond.raise_()
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
        self.Firstnamelab.setText(_translate("MainWindow", "First name"))
        self.Secondnamelab.setText(_translate("MainWindow", "Second Name"))
        self.Signin.setText(_translate("MainWindow", "Sign in to ToDo list"))
        self.Letsgobutton.setText(_translate("MainWindow", "Let\'s Go"))

    def error(self):
        message = QMessageBox()
        message.setWindowTitle("ToDo")
        message.setText("Input first and second name")
        message.setStandardButtons(QMessageBox.Retry)
        message.setDefaultButton(QMessageBox.Retry)
        x = message.exec_()
