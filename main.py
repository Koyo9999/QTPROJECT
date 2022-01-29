from PySide2 import QtCore, QtGui, QtWidgets
import sys
from QT.basswindow import Ui_MainWindow
from App.AppMain import MainWindow

# class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.setupUi(self)

    # @pyqtSlot()
    # def setTextHelloWorld(self):
    #     self.label.setText("Hello World")

if __name__ == '__main__':
    argvs = sys.argv
    app = QtWidgets.QApplication(argvs)
    a = MainWindow()
    a.show()
    sys.exit(app.exec_())
