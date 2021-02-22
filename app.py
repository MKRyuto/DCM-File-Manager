import pydicom as dicom
import os
import shutil
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(239, 80)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dcm-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.screen1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(120, 10, 111, 31))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.screen2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 211, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DCM File Manager"))
        self.button1.setText(_translate("MainWindow", "📄  Rename File"))
        self.button2.setText(_translate("MainWindow", "📖  Export to Excel"))
        self.label.setText(_translate("MainWindow", "Make by MKRyuto | github.com/MKRyuto"))

    def screen1(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_renameFile()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def screen2(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_exportData()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

class Ui_renameFile(object):

    inputDirectory = None;
    outputDirectory = None;

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 178)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dcm-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 361, 51))
        self.groupBox.setObjectName("groupBox")
        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.label1.setStyleSheet("background-color: rgb(222, 222, 222);\n" "padding-left: 5px;")
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
        self.label2.setStyleSheet("background-color: rgb(222, 222, 222);\n" "padding-left: 5px;")
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.button2 = QtWidgets.QPushButton(self.groupBox_2)
        self.button2.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.outputFolder)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.renameFile)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rename File"))
        self.groupBox.setTitle(_translate("MainWindow", ".dcm folder"))
        self.button1.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Output folder"))
        self.button2.setText(_translate("MainWindow", "..."))
        self.button3.setText(_translate("MainWindow", "Rename"))

    def show_popup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dcm-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setText(message)
        x = msg.exec_()

    def inputFolder(self):
        self.inputDirectory = QFileDialog.getExistingDirectory(None, "Select Directory")
        if self.inputDirectory:
            self.label1.setText(self.inputDirectory)
        else:
            self.label1.setText(None)
            self.show_popup('The .dmc file folder is not selected')
            pass

    def outputFolder(self):
        self.outputDirectory = QFileDialog.getExistingDirectory(None, "Select Directory")
        if self.outputDirectory:
            self.label2.setText(self.outputDirectory)
        else:
            self.label2.setText(None)
            self.show_popup('The output folder is not selected')
            pass

    def renameFile(self):
        if self.outputDirectory and self.inputDirectory:
            files = os.listdir(self.inputDirectory)
            for file in files:
                if file.endswith(".dcm"):
                    ds = dicom.read_file(self.inputDirectory + '/' + file, force=True)
                    index = (os.path.basename(os.path.normpath(self.outputDirectory)), ds.DetectorID, ds.AnodeTargetMaterial, ds.FilterMaterial, str(ds.KVP), str(ds.Exposure), ds.DateOfLastDetectorCalibration, ds.Grid)
                    newFileName = "_".join(index)
                    shutil.copy(self.inputDirectory + '/' + file,self.outputDirectory + '/' + newFileName + '.dcm')
            self.show_popup('Process complete')
        else:
            self.show_popup('No folder has not been selected')
            pass

class Ui_exportData(object):

    inputDirectory = None;
    outputDirectory = None;

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 107)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dcm-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_1.setGeometry(QtCore.QRect(20, 10, 361, 51))
        self.groupBox_1.setObjectName("groupBox_1")
        self.label1 = QtWidgets.QLabel(self.groupBox_1)
        self.label1.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.label1.setStyleSheet("background-color: rgb(222, 222, 222);\n" "padding-left: 5px;")
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.button1 = QtWidgets.QPushButton(self.groupBox_1)
        self.button1.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.inputFolder)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.exportData)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Export to Excel"))
        self.groupBox_1.setTitle(_translate("MainWindow", "Folder file .dcm"))
        self.button1.setText(_translate("MainWindow", "..."))
        self.button2.setText(_translate("MainWindow", "Export"))

    def show_popup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Alert")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dcm-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        msg.setText(message)
        x = msg.exec_()

    def inputFolder(self):
        self.inputDirectory = QFileDialog.getExistingDirectory(None, "Select Directory")
        if self.inputDirectory:
            self.label1.setText(self.inputDirectory)
        else:
            self.label1.setText(None)
            self.show_popup('The .dmc file folder is not selected')
            pass

    def exportData(self):
        if self.inputDirectory:
            self.outputDirectory = QFileDialog.getSaveFileName(None, "Save file", "", "Excel (*.xlsx)")
            files = os.listdir(self.inputDirectory)
            dfAll = pd.DataFrame(columns=['Implementation Version Name', 'Image Type', 'Acquisition Date', 'Acquisition Time', 'Modality', 'Presentation Intent Type', 'Manufacturer', 'Institution Name', 'Manufacturer Model Name', 'Patient Name', 'kVp', 'Device Serial Number', 'Software Versions(s)', 'Distance Source to Detector', 'Distance Source to Patient', 'Field of View Shape', 'Field of View Dimensions(s)', 'Exposure Time', 'X-ray Tube Current', 'Exposure', 'Exposure in uAs', 'Rectification Type', 'Imager Pixel Spacing', 'Grid', 'Focal Spot(s)', 'Anode Target Material', 'Body Part Thickness', 'Compression Force', 'Detector Type', 'Detector Configuration', 'Detector Description', 'Detector Mode', 'Detector ID', 'Date of Last Detector Calibration', 'Time of Last Detector Calibration', 'Exposures on Detector Since Last Calibration', 'Exposures on Detector Since Manufactured', 'Detector Time Since Last Exposure', 'Detector Active Time', 'Detector Activation Offset From Exposure', 'Detector Binning', 'Detector Element Physical Size', 'Detector Element Spacing', 'Detector Active Shape', 'Detector Active Dimension(s)', 'Filter Material LT', 'Filter Thickness Minimum', 'Filter Thickness Maximum', 'Exposure Control Mode', 'Exposure Control Mode Description', 'Photometric Interpretation', 'Rows', 'Columns', 'Bits Allocated', 'Bits Stored', 'High Bit', 'Pixel Intensity Relationship', 'Distance Source to Entrance', 'Organ Dose', 'Entrance Dose in mGy'])
            for file in files:
                if file.endswith(".dcm"):
                    ds = dicom.read_file(self.inputDirectory + '/' + file, force=True)
                    ImageType = ' | '.join(filter(None, ds.ImageType))
                    SoftwareVersions = ' | '.join(filter(None, ds.SoftwareVersions))
                    try : 
                        ds.RectificationType
                        ds.DetectorMode
                        ds.TimeOfLastDetectorCalibration
                        ds.ExposuresOnDetectorSinceLastCalibration
                        ds.ExposuresOnDetectorSinceManufactured
                        ds.DetectorTimeSinceLastExposure
                        ds.DetectorActiveTime
                        ds.DetectorActivationOffsetFromExposure
                        ds.FilterThicknessMinimum
                        ds.FilterThicknessMaximum
                    except:
                        ds.RectificationType = 'Null'
                        ds.DetectorMode = 'Null'
                        ds.TimeOfLastDetectorCalibration = 'Null'
                        ds.ExposuresOnDetectorSinceLastCalibration = 0
                        ds.ExposuresOnDetectorSinceManufactured = 0
                        ds.DetectorTimeSinceLastExposure = 0
                        ds.DetectorActiveTime = 0
                        ds.DetectorActivationOffsetFromExposure = 0
                        ds.FilterThicknessMinimum = 0
                        ds.FilterThicknessMaximum = 0
                    dataDicom = {
                                'Implementation Version Name' : [ds.file_meta.ImplementationVersionName], 
                                'Image Type' : [ImageType], 
                                'Acquisition Date' : [ds.AcquisitionDate], 
                                'Acquisition Time' : [ds.AcquisitionTime], 
                                'Modality' : [ds.Modality], 
                                'Presentation Intent Type' : [ds.PresentationIntentType], 
                                'Manufacturer' : [ds.Manufacturer], 
                                'Institution Name' : [ds.InstitutionName], 
                                'Manufacturer Model Name' : [ds.ManufacturerModelName], 
                                'Patient Name' : [ds.PatientName], 
                                'kVp' : [ds.KVP], 
                                'Device Serial Number' : [ds.DeviceSerialNumber], 
                                'Software Versions(s)' : [SoftwareVersions], 
                                'Distance Source to Detector' : [ds.DistanceSourceToDetector], 
                                'Distance Source to Patient' : [ds.DistanceSourceToPatient], 
                                'Field of View Shape' : [ds.FieldOfViewShape], 
                                'Field of View Dimensions(s)' : [str(ds.FieldOfViewDimensions)], 
                                'Exposure Time' : [ds.ExposureTime], 
                                'X-ray Tube Current' : [ds.XRayTubeCurrent], 
                                'Exposure' : [ds.Exposure], 
                                'Exposure in uAs' : [ds.ExposureInuAs], 
                                'Rectification Type' : [ds.RectificationType], 
                                'Imager Pixel Spacing' : [str(ds.ImagerPixelSpacing)], 
                                'Grid' : [ds.Grid], 
                                'Focal Spot(s)' : [ds.FocalSpots], 
                                'Anode Target Material' : [ds.AnodeTargetMaterial], 
                                'Body Part Thickness' : [ds.BodyPartThickness], 
                                'Compression Force' : [ds.CompressionForce], 
                                'Detector Type' : [ds.DetectorType], 
                                'Detector Configuration' : [ds.DetectorConfiguration], 
                                'Detector Description' : [ds.DetectorDescription], 
                                'Detector Mode' : [ds.DetectorMode], 
                                'Detector ID' : [ds.DetectorID], 
                                'Date of Last Detector Calibration' : [ds.DateOfLastDetectorCalibration], 
                                'Time of Last Detector Calibration' : [ds.TimeOfLastDetectorCalibration], 
                                'Exposures on Detector Since Last Calibration' : [ds.ExposuresOnDetectorSinceLastCalibration], 
                                'Exposures on Detector Since Manufactured' : [ds.ExposuresOnDetectorSinceManufactured], 
                                'Detector Time Since Last Exposure' : [ds.DetectorTimeSinceLastExposure], 
                                'Detector Active Time' : [ds.DetectorActiveTime], 
                                'Detector Activation Offset From Exposure' : [ds.DetectorActivationOffsetFromExposure], 
                                'Detector Binning' : [str(ds.DetectorBinning)], 
                                'Detector Element Physical Size' : [str(ds.DetectorElementPhysicalSize)], 
                                'Detector Element Spacing' : [str(ds.DetectorElementSpacing)], 
                                'Detector Active Shape' : [ds.DetectorActiveShape], 
                                'Detector Active Dimension(s)' : [str(ds.DetectorActiveDimensions)], 
                                'Filter Material LT' : [ds.FilterMaterial], 
                                'Filter Thickness Minimum' : [ds.FilterThicknessMinimum], 
                                'Filter Thickness Maximum' : [ds.FilterThicknessMaximum], 
                                'Exposure Control Mode' : [ds.ExposureControlMode], 
                                'Exposure Control Mode Description' : [ds.ExposureControlModeDescription], 
                                'Photometric Interpretation' : [ds.PhotometricInterpretation], 
                                'Rows' : [ds.Rows], 
                                'Columns' : [ds.Columns], 
                                'Bits Allocated' : [ds.BitsAllocated], 
                                'Bits Stored' : [ds.BitsStored], 
                                'High Bit' : [ds.HighBit], 
                                'Pixel Intensity Relationship' : [ds.PixelIntensityRelationship], 
                                'Distance Source to Entrance' : [ds.DistanceSourceToEntrance], 
                                'Organ Dose' : [ds.OrganDose], 
                                'Entrance Dose in mGy' : [ds.EntranceDoseInmGy]
                                }
                    df = pd.DataFrame(dataDicom)
                    dfAll = dfAll.append(df, ignore_index=True)

            dfAll.to_excel (str(self.outputDirectory[0]), index = False, header=True)
            self.show_popup('Process complete')
        else:
            self.show_popup('No folder has not been selected')
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
