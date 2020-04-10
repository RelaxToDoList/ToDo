from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 517)
        self.centralwidget = QtGui.QWidget(MainWindow)
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
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 951, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Documents/AProg/gitlab/ToDo/src/Welcome_Window1/icons/wall.png"))
        self.label.setObjectName("label")
        self.centralwidget.setObjectName("centralwidget")
        self.Firstnamelab = QtGui.QLabel(self.centralwidget)
        self.Firstnamelab.setGeometry(QtCore.QRect(220, 190, 151, 16))
        self.Firstnamelab.setStyleSheet("background: none;\n"
"font-size: 15px;\n"
"font-weight:bold;")
        self.Firstnamelab.setObjectName("Firstnamelab")
        self.Secondnamelab = QtGui.QLabel(self.centralwidget)
        self.Secondnamelab.setGeometry(QtCore.QRect(220, 270, 151, 16))
        self.Secondnamelab.setStyleSheet("background: none;\n"
"font-size: 15px;\n"
"font-weight:bold;")
        self.Secondnamelab.setObjectName("Secondnamelab")
        self.Signin = QtGui.QLabel(self.centralwidget)
        self.Signin.setGeometry(QtCore.QRect(360, 40, 231, 51))
        self.Signin.setStyleSheet("background: none;\n"
"font-size: 24px;\n"
"font-weight: bold;\n"
"color: #FFF;\n"
"mix-blend-mod:multiply;\n"
"display: inline-block;")
        self.Signin.setObjectName("Signin")
        self.Letsgobutton = QtGui.QPushButton(self.centralwidget)
        self.Letsgobutton.setGeometry(QtCore.QRect(370, 360, 191, 71))
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
        self.InputFirst = QtGui.QLineEdit(self.centralwidget)
        self.InputFirst.setGeometry(QtCore.QRect(220, 220, 497, 35))
        self.InputFirst.setStyleSheet("background: none;\n"
"border: 1px solid black;\n"
"border: 1px solid black;\n"
"font-size: 21px;\n"
"font-weight: 502;")
        self.InputFirst.setObjectName("InputFirst")
        self.InputFirst.setMaxLength(44)
        self.InputSecond = QtGui.QLineEdit(self.centralwidget)
        self.InputSecond.setGeometry(QtCore.QRect(220, 290, 497, 35))
        self.InputSecond.setStyleSheet("background: none;\n"
"border: 1px solid black;\n"
"border: 1px solid black;\n"
"font-size: 21px;\n"
"font-weight: 502;")
        self.InputSecond.setObjectName("InputSecond")
        self.InputSecond.setMaxLength(44)
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
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Firstnamelab.setText(QtGui.QApplication.translate("MainWindow", "First name", None, QtGui.QApplication.UnicodeUTF8))
        self.Secondnamelab.setText(QtGui.QApplication.translate("MainWindow", "Second Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Signin.setText(QtGui.QApplication.translate("MainWindow", "Sign in to ToDo list", None, QtGui.QApplication.UnicodeUTF8))
        self.Letsgobutton.setText(QtGui.QApplication.translate("MainWindow", "Let\'s Go", None, QtGui.QApplication.UnicodeUTF8))
