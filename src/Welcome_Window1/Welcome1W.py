from PySide import QtCore, QtGui
import sys
from Welcome1 import Ui_MainWindow
# Run Application
app = QtGui.QApplication(sys.argv)
#Create UI and form of application
MainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#Logic here!


#Run main loop
sys.exit(app.exec_())
