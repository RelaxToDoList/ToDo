from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Choose_Theme(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 517)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: #337AB7;\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.Choose = QtWidgets.QLabel(self.centralwidget)
        self.Choose.setGeometry(QtCore.QRect(310, 60, 291, 51))
        self.Choose.setStyleSheet("font-size: 28px;\n"
"font-weight: bold;\n"
"color:#FFFFFF;\n"
"")
        self.Choose.setObjectName("Choose")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 950, 517))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("icons/wall.png"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.Checkbox_Dark = QtWidgets.QLabel(self.centralwidget)
        self.Checkbox_Dark.setGeometry(QtCore.QRect(550, 280, 21, 21))
        self.Checkbox_Dark.setStyleSheet("")
        self.Checkbox_Dark.setText("")
        self.Checkbox_Dark.setPixmap(QtGui.QPixmap("icons/Сheckbox_Dark.png"))
        self.Checkbox_Dark.setScaledContents(True)
        self.Checkbox_Dark.setObjectName("Checkbox_Dark")
        self.DarkDEal = QtWidgets.QLabel(self.centralwidget)
        self.DarkDEal.setGeometry(QtCore.QRect(580, 280, 91, 21))
        self.DarkDEal.setStyleSheet("color: #949494;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.DarkDEal.setObjectName("DarkDEal")
        self.Checkbox_Light = QtWidgets.QLabel(self.centralwidget)
        self.Checkbox_Light.setGeometry(QtCore.QRect(150, 280, 21, 21))
        self.Checkbox_Light.setText("")
        self.Checkbox_Light.setPixmap(QtGui.QPixmap("icons/Checkbox_Light.png"))
        self.Checkbox_Light.setScaledContents(True)
        self.Checkbox_Light.setObjectName("Checkbox_Light")
        self.LightDeal = QtWidgets.QLabel(self.centralwidget)
        self.LightDeal.setGeometry(QtCore.QRect(180, 280, 81, 20))
        self.LightDeal.setStyleSheet("color: #363636;\n"
"font-size: 16px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.LightDeal.setObjectName("LightDeal")
        self.Light_border_up = QtWidgets.QGraphicsView(self.centralwidget)
        self.Light_border_up.setGeometry(QtCore.QRect(130, 210, 261, 48))
        self.Light_border_up.setStyleSheet("background-color: #FFFFFF;\n"
"")
        self.Light_border_up.setObjectName("Light_border_up")
        self.Light = QtWidgets.QLabel(self.centralwidget)
        self.Light.setGeometry(QtCore.QRect(230, 220, 61, 31))
        self.Light.setStyleSheet("color: #363636;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.Light.setObjectName("Light")
        self.Dark_border_up = QtWidgets.QGraphicsView(self.centralwidget)
        self.Dark_border_up.setGeometry(QtCore.QRect(530, 210, 261, 48))
        self.Dark_border_up.setStyleSheet("background-color: #1B1B1B;\n"
"border-style: hidden;\n"
"")
        self.Dark_border_up.setObjectName("Dark_border_up")
        self.Dark = QtWidgets.QLabel(self.centralwidget)
        self.Dark.setGeometry(QtCore.QRect(640, 220, 60, 31))
        self.Dark.setStyleSheet("color: #D7D7D7;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"font-family: Calibri, Candara, Segoe, \"Segoe UI\", Optima, Arial, sans-serif;\n"
"font-style: normal;")
        self.Dark.setObjectName("Dark")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(130, 258, 261, 71))
        self.toolButton.setStyleSheet("QToolButton:clicked {\n"
"    background-color:#D7D7D7;\n"
"    border-style: hidden;\n"
"    }\n"
"QToolButton:hover {\n"
"    background-color: #D7D7D7;\n"
"    border-style: hidden;\n"
"    }\n"
"QToolButton {\n"
"    background-color: #D7D7D7;\n"
"    border-style: hidden;\n"
"    }\n"
"")
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(529, 258, 261, 71))
        self.toolButton_2.setStyleSheet("background-color: #0D0D0D;")
        self.toolButton_2.setText("")
        self.toolButton_2.setObjectName("toolButton_2")
        self.Letsgobutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Letsgobutton_2.setGeometry(QtCore.QRect(310, 380, 291, 71))
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
        self.Background.raise_()
        self.toolButton.raise_()
        self.toolButton_2.raise_()
        self.Light_border_up.raise_()
        self.Light.raise_()
        self.Letsgobutton_2.raise_()
        self.Dark_border_up.raise_()
        self.Dark.raise_()
        self.Choose.raise_()
        self.LightDeal.raise_()
        self.Checkbox_Light.raise_()
        self.DarkDEal.raise_()
        self.Checkbox_Dark.raise_()
        self.theme = 1
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
        self.Choose.setText(_translate("MainWindow", "Choose your theme:"))
        self.DarkDEal.setText(_translate("MainWindow", "Your Deal"))
        self.LightDeal.setText(_translate("MainWindow", "Your Deal"))
        self.Light.setText(_translate("MainWindow", "Light"))
        self.Dark.setText(_translate("MainWindow", "Dark"))
        self.Letsgobutton_2.setText(_translate("MainWindow", "Create my list"))
    def buttonpressed_2(self):
        global theme
        theme = 1                                  # Функция смены цвета при нажатии на кнопку
        self.toolButton_2.setStyleSheet("QToolButton{\n"
    "    border-style: hidden;\n"
    " background-color: #4E1580;  }\n"
    "")
        self.toolButton.setStyleSheet("QToolButton:clicked {\n"
    "    background-color:#D7D7D7;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "QToolButton:hover {\n"
    "    background-color: #D7D7D7;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "QToolButton {\n"
    "    background-color: #D7D7D7;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "")
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
    def buttonpressed_1(self):
        self.click = 1
        global theme
        theme = 0                                       # Функция смены цвета при нажатии на кнопку
        self.toolButton.clicked.connect(int)
        self.toolButton.setStyleSheet("QToolButton{\n"
    "    border-style: hidden;\n"
    " background-color: #B782E5;  }\n"
    "")
        self.toolButton_2.setStyleSheet("QToolButton {\n"
    "    background-color: #0D0D0D;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "")
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
