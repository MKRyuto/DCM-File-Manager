# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exportData.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 107)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/muham/OneDrive/Pictures/dcm-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 361, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label2 = QtWidgets.QLabel(self.groupBox_2)
        self.label2.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.label2.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"padding-left: 5px;")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.button2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button2.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(330, 70, 51, 23))
        self.button4.setObjectName("button4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Export to Excel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Folder file .dcm"))
        self.button2.setText(_translate("MainWindow", "..."))
        self.button3.setText(_translate("MainWindow", "Export"))
        self.button4.setText(_translate("MainWindow", "Back"))
