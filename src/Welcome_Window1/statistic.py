from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Statistic(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("icons/background_Settings.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(350, 50, 241, 191))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 270, 852, 3))
        self.line.setStyleSheet("background-color:#666666;\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.all_task = QtWidgets.QLabel(self.centralwidget)
        self.all_task.setGeometry(QtCore.QRect(50, 280, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.all_task.setFont(font)
        self.all_task.setStyleSheet("color: #F2F2F2;\n"
"")
        self.all_task.setObjectName("all_task")
        self.completted = QtWidgets.QLabel(self.centralwidget)
        self.completted.setGeometry(QtCore.QRect(50, 330, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.completted.setFont(font)
        self.completted.setStyleSheet("color: #F2F2F2;\n"
"")
        self.completted.setObjectName("completted")
        self.failed = QtWidgets.QLabel(self.centralwidget)
        self.failed.setGeometry(QtCore.QRect(50, 380, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.failed.setFont(font)
        self.failed.setStyleSheet("color: #F2F2F2;\n"
"")
        self.failed.setObjectName("failed")
        self.unfinished = QtWidgets.QLabel(self.centralwidget)
        self.unfinished.setGeometry(QtCore.QRect(50, 420, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.unfinished.setFont(font)
        self.unfinished.setStyleSheet("color: #F2F2F2;\n"
"")
        self.unfinished.setObjectName("unfinished")
        self.number_all = QtWidgets.QLabel(self.centralwidget)
        self.number_all.setGeometry(QtCore.QRect(310, 286, 121, 31))
        self.number_all.setStyleSheet("font-size: 24px;\n"
"color:#663366;\n"
"font-weight: bold;\n"
"")
        self.number_all.setObjectName("number_all")
        self.completted_number = QtWidgets.QLabel(self.centralwidget)
        self.completted_number.setGeometry(QtCore.QRect(460, 332, 121, 31))
        self.completted_number.setStyleSheet("color: #339900;\n"
"font-size: 24px;\n"
"font-weight: bold;")
        self.completted_number.setObjectName("completted_number")
        self.failed_number = QtWidgets.QLabel(self.centralwidget)
        self.failed_number.setGeometry(QtCore.QRect(400, 387, 101, 21))
        self.failed_number.setStyleSheet("color: #990000;\n"
"font-weight: bold;\n"
"font-size:24px;\n"
"")
        self.failed_number.setObjectName("failed_number")
        self.unfinished_number = QtWidgets.QLabel(self.centralwidget)
        self.unfinished_number.setGeometry(QtCore.QRect(460, 427, 111, 21))
        self.unfinished_number.setStyleSheet("color:#FFFF00;\n"
"font-weight: bold;\n"
"font-size:24px;\n"
"")
        self.unfinished_number.setObjectName("unfinished_number")
        self.settings_but = QtWidgets.QToolButton(self.centralwidget)
        self.settings_but.setGeometry(QtCore.QRect(900, 10, 31, 26))
        self.settings_but.setStyleSheet("border:none;\n"
"")
        self.settings_but.setIcon(QtGui.QIcon("icons/icon_gear_dark.png"))
        self.settings_but.setIconSize(QtCore.QSize(70,70))
        self.settings_but.setObjectName("settings_but")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "ToDo"))
        self.all_task.setText(_translate("MainWindow", "Number of all task:"))
        self.completted.setText(_translate("MainWindow", "Number of all completted task:"))
        self.failed.setText(_translate("MainWindow", "Number of all failed task:"))
        self.unfinished.setText(_translate("MainWindow", "Number of all unfinished  task:"))
        self.number_all.setText(_translate("MainWindow", "Number"))
        self.completted_number.setText(_translate("MainWindow", "Number"))
        self.failed_number.setText(_translate("MainWindow", "Number"))
        self.unfinished_number.setText(_translate("MainWindow", "Number"))
        self.settings_but.setText(_translate("MainWindow", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Statistic()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
