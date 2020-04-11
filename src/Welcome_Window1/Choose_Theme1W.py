from PySide import QtCore, QtGui
import sys
from Choose_Theme import Ui_MainWindow

#Run Application
app = QtGui.QApplication(sys.argv)
#Create UI and form of Application
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#LOGIC HERE!
def buttonpressed_2():
    ui.toolButton_2.clicked.connect(int)
    ui.toolButton_2.setStyleSheet("QToolButton{\n"
    "    border-style: hidden;\n"
    " background-color: #4E1580;  }\n"
    "")
    ui.toolButton.setStyleSheet("QToolButton:clicked {\n"
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
def buttonpressed_1():
    ui.toolButton.clicked.connect(int)
    ui.toolButton.setStyleSheet("QToolButton{\n"
    "    border-style: hidden;\n"
    " background-color: #B782E5;  }\n"
    "")
    ui.toolButton_2.setStyleSheet("QToolButton {\n"
    "    background-color: #0D0D0D;\n"
    "    border-style: hidden;\n"
    "    }\n"
    "")
def main():
    ui.toolButton.clicked.connect(buttonpressed_1)
    ui.toolButton_2.clicked.connect(buttonpressed_2)
main()

#Run main loop
sys.exit(app.exec_())
