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


#Run main loop
sys.exit(app.exec_())
