from PyQt5 import QtCore, QtGui, QtWidgets
from Welcome1 import Ui_MainWindow
from Introduction import Ui_Welcome
from Signin import Ui_Sign
from Choose_Theme import Ui_Choose_Theme
from MainWindow import Ui_Core

class Fifth_Window(QtWidgets.QMainWindow, Ui_Core):
    def __init__(self, parent = None):
        super(Fifth_Window, self).__init__(parent)
        self.setupUi(self)
        self.check_box.clicked.connect(self.check_box_checked)
class Fourth_Window(QtWidgets.QMainWindow, Ui_Choose_Theme): ## Window of theme choosing
    def __init__(self, parent = None):
        super(Fourth_Window, self).__init__(parent)
        self.setupUi(self)
        self.toolButton_2.clicked.connect(self.buttonpressed_2)
        self.toolButton.clicked.connect(self.buttonpressed_1)
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
    def nextWindow(self):
        self.close()
        self.next = Fifth_Window()
        self.next.show()

class Third_Window(QtWidgets.QMainWindow, Ui_Welcome): ## Window of Welcoming user
    def __init__(self, parent = None):
        super(Third_Window, self).__init__(parent)
        self.setupUi(self)
        self.Letsgobutton_2.clicked.connect(self.nextWindow)
    def nextWindow(self):
        self.close()
        self.next = Fourth_Window()
        self.next.show()

class Second_Window(QtWidgets.QMainWindow, Ui_Sign): ##Window of signing in
    def __init__(self, parent = None):
        super(Second_Window, self).__init__(parent)
        self.setupUi(self)
        self.Letsgobutton.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.next = Third_Window()
        self.next.show()


class First_Window(QtWidgets.QMainWindow,Ui_MainWindow): ## Window Start

    def __init__(self, parent= None):
        super(First_Window,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.first = First_Window()
        self.second = Second_Window()
        self.second.show()


if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = First_Window()
    window.show()

    sys.exit(app.exec_())
