import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from QT.basswindow import Ui_MainWindow

import QT.basswindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
