import pydicom as dicom
import xlsxwriter
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QStatusBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 178)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./dcm-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 361, 51))
        self.groupBox.setObjectName("groupBox")
        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.label1.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"padding-left: 5px;")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.button1 = QtWidgets.QPushButton(self.groupBox)
        self.button1.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.inputFolder)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 361, 51))
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
        self.button2.clicked.connect(self.outputFolder)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.button3.setObjectName("button3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DCM File Manager"))
        self.groupBox.setTitle(_translate("MainWindow", ".dcm folder"))
        self.button1.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output folder"))
        self.button2.setText(_translate("MainWindow", "..."))
        self.button3.setText(_translate("MainWindow", "Rename"))

    def inputFolder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.label1.setText(folder)

    def outputFolder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Directory")
        self.label2.setText(folder)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
