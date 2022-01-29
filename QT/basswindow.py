# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'basswindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(425, 199)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 425, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

