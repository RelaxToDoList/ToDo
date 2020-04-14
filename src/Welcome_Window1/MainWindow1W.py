from PySide import QtCore, QtGui
import sys
from MainWindow import Ui_MainWindow

#Run Application
app = QtGui.QApplication(sys.argv)
#Create UI and form of Application
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#LOGIC HERE!
def check_box_unchecked():
    ui.check_box.setIcon(QtGui.QIcon("icons/Empty_Box_Light.png"))
    ui.check_box.clicked.connect(check_box_checked)
def check_box_checked():
    ui.check_box.setIcon(QtGui.QIcon("icons/Checkbox_Light.png"))
    ui.check_box.clicked.connect(check_box_unchecked)

def main():
    ui.check_box.clicked.connect(check_box_checked)
main()
#Run main loop
sys.exit(app.exec_())
