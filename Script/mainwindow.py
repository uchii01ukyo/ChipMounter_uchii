# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PickerCalib\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 691)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelView = QtWidgets.QLabel(self.centralwidget)
        self.labelView.setGeometry(QtCore.QRect(0, 10, 640, 480))
        self.labelView.setMouseTracking(True)
        self.labelView.setFrameShape(QtWidgets.QFrame.Box)
        self.labelView.setText("")
        self.labelView.setObjectName("labelView")
        self.horizontalSliderHU1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderHU1.setGeometry(QtCore.QRect(60, 520, 160, 22))
        self.horizontalSliderHU1.setMaximum(360)
        self.horizontalSliderHU1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderHU1.setObjectName("horizontalSliderHU1")
        self.horizontalSliderHL1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderHL1.setGeometry(QtCore.QRect(60, 550, 160, 22))
        self.horizontalSliderHL1.setMaximum(360)
        self.horizontalSliderHL1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderHL1.setObjectName("horizontalSliderHL1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 520, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 550, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 500, 60, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalSliderSL1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderSL1.setGeometry(QtCore.QRect(230, 550, 160, 22))
        self.horizontalSliderSL1.setMaximum(100)
        self.horizontalSliderSL1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSL1.setObjectName("horizontalSliderSL1")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 500, 60, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalSliderSU1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderSU1.setGeometry(QtCore.QRect(230, 520, 160, 22))
        self.horizontalSliderSU1.setMaximum(100)
        self.horizontalSliderSU1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSU1.setObjectName("horizontalSliderSU1")
        self.horizontalSliderVL1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderVL1.setGeometry(QtCore.QRect(390, 550, 160, 22))
        self.horizontalSliderVL1.setMaximum(100)
        self.horizontalSliderVL1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVL1.setObjectName("horizontalSliderVL1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 500, 60, 16))
        self.label_6.setObjectName("label_6")
        self.horizontalSliderVU1 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderVU1.setGeometry(QtCore.QRect(390, 520, 160, 22))
        self.horizontalSliderVU1.setMaximum(100)
        self.horizontalSliderVU1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVU1.setObjectName("horizontalSliderVU1")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 500, 60, 16))
        self.label_7.setObjectName("label_7")
        self.horizontalSliderHL2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderHL2.setGeometry(QtCore.QRect(60, 630, 160, 22))
        self.horizontalSliderHL2.setMaximum(360)
        self.horizontalSliderHL2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderHL2.setObjectName("horizontalSliderHL2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 630, 60, 16))
        self.label_8.setObjectName("label_8")
        self.horizontalSliderVL2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderVL2.setGeometry(QtCore.QRect(390, 630, 160, 22))
        self.horizontalSliderVL2.setMaximum(100)
        self.horizontalSliderVL2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVL2.setObjectName("horizontalSliderVL2")
        self.horizontalSliderHU2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderHU2.setGeometry(QtCore.QRect(60, 600, 160, 22))
        self.horizontalSliderHU2.setMaximum(360)
        self.horizontalSliderHU2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderHU2.setObjectName("horizontalSliderHU2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 600, 60, 16))
        self.label_9.setObjectName("label_9")
        self.horizontalSliderSL2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderSL2.setGeometry(QtCore.QRect(230, 630, 160, 22))
        self.horizontalSliderSL2.setMaximum(100)
        self.horizontalSliderSL2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSL2.setObjectName("horizontalSliderSL2")
        self.horizontalSliderVU2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderVU2.setGeometry(QtCore.QRect(390, 600, 160, 22))
        self.horizontalSliderVU2.setMaximum(100)
        self.horizontalSliderVU2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderVU2.setObjectName("horizontalSliderVU2")
        self.horizontalSliderSU2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSliderSU2.setGeometry(QtCore.QRect(230, 600, 160, 22))
        self.horizontalSliderSU2.setMaximum(100)
        self.horizontalSliderSU2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderSU2.setObjectName("horizontalSliderSU2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 580, 60, 16))
        self.label_10.setObjectName("label_10")
        self.radioButtonRaw = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonRaw.setGeometry(QtCore.QRect(570, 520, 99, 20))
        self.radioButtonRaw.setChecked(True)
        self.radioButtonRaw.setObjectName("radioButtonRaw")
        self.radioButtonBack = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBack.setGeometry(QtCore.QRect(570, 540, 99, 20))
        self.radioButtonBack.setObjectName("radioButtonBack")
        self.radioButtonBlack = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBlack.setGeometry(QtCore.QRect(570, 560, 99, 20))
        self.radioButtonBlack.setObjectName("radioButtonBlack")
        self.radioButtonComponent = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonComponent.setGeometry(QtCore.QRect(570, 580, 99, 20))
        self.radioButtonComponent.setObjectName("radioButtonComponent")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(560, 500, 60, 16))
        self.label_11.setObjectName("label_11")
        self.pushButtonCapture = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCapture.setGeometry(QtCore.QRect(650, 620, 211, 32))
        self.pushButtonCapture.setObjectName("pushButtonCapture")
        self.pushButtonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonQuit.setGeometry(QtCore.QRect(750, 650, 113, 32))
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(650, 650, 113, 32))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonMoveTrayCamera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveTrayCamera.setGeometry(QtCore.QRect(740, 160, 121, 32))
        self.pushButtonMoveTrayCamera.setObjectName("pushButtonMoveTrayCamera")
        self.pushButtonMoveNextBaseCorner = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveNextBaseCorner.setGeometry(QtCore.QRect(640, 0, 131, 32))
        self.pushButtonMoveNextBaseCorner.setObjectName("pushButtonMoveNextBaseCorner")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(660, 50, 31, 16))
        self.label_12.setObjectName("label_12")
        self.plainTextEditAreaCompL = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditAreaCompL.setGeometry(QtCore.QRect(700, 495, 51, 26))
        self.plainTextEditAreaCompL.setPlaceholderText("")
        self.plainTextEditAreaCompL.setObjectName("plainTextEditAreaCompL")
        self.plainTextEditAreaCompU = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditAreaCompU.setGeometry(QtCore.QRect(780, 495, 51, 26))
        self.plainTextEditAreaCompU.setPlaceholderText("")
        self.plainTextEditAreaCompU.setObjectName("plainTextEditAreaCompU")
        self.plainTextEditAreaBlackU = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditAreaBlackU.setGeometry(QtCore.QRect(780, 535, 51, 26))
        self.plainTextEditAreaBlackU.setPlaceholderText("")
        self.plainTextEditAreaBlackU.setObjectName("plainTextEditAreaBlackU")
        self.plainTextEditAreaBlackL = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditAreaBlackL.setGeometry(QtCore.QRect(700, 535, 51, 26))
        self.plainTextEditAreaBlackL.setPlaceholderText("")
        self.plainTextEditAreaBlackL.setObjectName("plainTextEditAreaBlackL")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(660, 505, 41, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(700, 480, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(700, 520, 60, 16))
        self.label_15.setObjectName("label_15")
        self.plainTextEditPosCamera1X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera1X.setGeometry(QtCore.QRect(680, 210, 61, 26))
        self.plainTextEditPosCamera1X.setPlaceholderText("")
        self.plainTextEditPosCamera1X.setObjectName("plainTextEditPosCamera1X")
        self.plainTextEditPosCamera1Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera1Y.setGeometry(QtCore.QRect(750, 210, 61, 26))
        self.plainTextEditPosCamera1Y.setPlaceholderText("")
        self.plainTextEditPosCamera1Y.setObjectName("plainTextEditPosCamera1Y")
        self.plainTextEditPosCamera2X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera2X.setGeometry(QtCore.QRect(680, 240, 61, 26))
        self.plainTextEditPosCamera2X.setPlaceholderText("")
        self.plainTextEditPosCamera2X.setObjectName("plainTextEditPosCamera2X")
        self.plainTextEditPosCamera2Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera2Y.setGeometry(QtCore.QRect(750, 240, 61, 26))
        self.plainTextEditPosCamera2Y.setPlaceholderText("")
        self.plainTextEditPosCamera2Y.setObjectName("plainTextEditPosCamera2Y")
        self.plainTextEditPosCamera3X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera3X.setGeometry(QtCore.QRect(680, 270, 61, 26))
        self.plainTextEditPosCamera3X.setPlaceholderText("")
        self.plainTextEditPosCamera3X.setObjectName("plainTextEditPosCamera3X")
        self.plainTextEditPosCamera3Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera3Y.setGeometry(QtCore.QRect(750, 270, 61, 26))
        self.plainTextEditPosCamera3Y.setPlaceholderText("")
        self.plainTextEditPosCamera3Y.setObjectName("plainTextEditPosCamera3Y")
        self.plainTextEditPosCamera4X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera4X.setGeometry(QtCore.QRect(680, 300, 61, 26))
        self.plainTextEditPosCamera4X.setPlaceholderText("")
        self.plainTextEditPosCamera4X.setObjectName("plainTextEditPosCamera4X")
        self.plainTextEditPosCamera4Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCamera4Y.setGeometry(QtCore.QRect(750, 300, 61, 26))
        self.plainTextEditPosCamera4Y.setPlaceholderText("")
        self.plainTextEditPosCamera4Y.setObjectName("plainTextEditPosCamera4Y")
        self.plainTextEditPosReal3Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal3Y.setGeometry(QtCore.QRect(750, 420, 61, 26))
        self.plainTextEditPosReal3Y.setPlaceholderText("")
        self.plainTextEditPosReal3Y.setObjectName("plainTextEditPosReal3Y")
        self.plainTextEditPosReal4Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal4Y.setGeometry(QtCore.QRect(750, 450, 61, 26))
        self.plainTextEditPosReal4Y.setPlaceholderText("")
        self.plainTextEditPosReal4Y.setObjectName("plainTextEditPosReal4Y")
        self.plainTextEditPosReal1X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal1X.setGeometry(QtCore.QRect(680, 360, 61, 26))
        self.plainTextEditPosReal1X.setPlaceholderText("")
        self.plainTextEditPosReal1X.setObjectName("plainTextEditPosReal1X")
        self.plainTextEditPosReal4X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal4X.setGeometry(QtCore.QRect(680, 450, 61, 26))
        self.plainTextEditPosReal4X.setPlaceholderText("")
        self.plainTextEditPosReal4X.setObjectName("plainTextEditPosReal4X")
        self.plainTextEditPosReal2X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal2X.setGeometry(QtCore.QRect(680, 390, 61, 26))
        self.plainTextEditPosReal2X.setPlaceholderText("")
        self.plainTextEditPosReal2X.setObjectName("plainTextEditPosReal2X")
        self.plainTextEditPosReal3X = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal3X.setGeometry(QtCore.QRect(680, 420, 61, 26))
        self.plainTextEditPosReal3X.setPlaceholderText("")
        self.plainTextEditPosReal3X.setObjectName("plainTextEditPosReal3X")
        self.plainTextEditPosReal2Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal2Y.setGeometry(QtCore.QRect(750, 390, 61, 26))
        self.plainTextEditPosReal2Y.setPlaceholderText("")
        self.plainTextEditPosReal2Y.setObjectName("plainTextEditPosReal2Y")
        self.plainTextEditPosReal1Y = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosReal1Y.setGeometry(QtCore.QRect(750, 360, 61, 26))
        self.plainTextEditPosReal1Y.setPlaceholderText("")
        self.plainTextEditPosReal1Y.setObjectName("plainTextEditPosReal1Y")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(660, 190, 111, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(660, 340, 81, 16))
        self.label_17.setObjectName("label_17")
        self.pushButtonMoveTrayCorner1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveTrayCorner1.setGeometry(QtCore.QRect(810, 360, 61, 32))
        self.pushButtonMoveTrayCorner1.setObjectName("pushButtonMoveTrayCorner1")
        self.pushButtonMoveTrayCorner2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveTrayCorner2.setGeometry(QtCore.QRect(810, 390, 61, 32))
        self.pushButtonMoveTrayCorner2.setObjectName("pushButtonMoveTrayCorner2")
        self.pushButtonMoveTrayCorner3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveTrayCorner3.setGeometry(QtCore.QRect(810, 420, 61, 32))
        self.pushButtonMoveTrayCorner3.setObjectName("pushButtonMoveTrayCorner3")
        self.pushButtonMoveTrayCorner4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveTrayCorner4.setGeometry(QtCore.QRect(810, 450, 61, 32))
        self.pushButtonMoveTrayCorner4.setObjectName("pushButtonMoveTrayCorner4")
        self.plainTextEditPosCameraX = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCameraX.setGeometry(QtCore.QRect(720, 100, 61, 26))
        self.plainTextEditPosCameraX.setPlaceholderText("")
        self.plainTextEditPosCameraX.setObjectName("plainTextEditPosCameraX")
        self.plainTextEditPosCameraY = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCameraY.setGeometry(QtCore.QRect(790, 100, 61, 26))
        self.plainTextEditPosCameraY.setPlaceholderText("")
        self.plainTextEditPosCameraY.setObjectName("plainTextEditPosCameraY")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(660, 100, 51, 16))
        self.label_19.setObjectName("label_19")
        self.plainTextEditManualMove = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditManualMove.setGeometry(QtCore.QRect(680, 580, 61, 26))
        self.plainTextEditManualMove.setPlaceholderText("")
        self.plainTextEditManualMove.setObjectName("plainTextEditManualMove")
        self.pushButtonMoveX = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveX.setGeometry(QtCore.QRect(750, 580, 41, 32))
        self.pushButtonMoveX.setObjectName("pushButtonMoveX")
        self.pushButtonMoveY = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveY.setGeometry(QtCore.QRect(790, 580, 41, 32))
        self.pushButtonMoveY.setObjectName("pushButtonMoveY")
        self.pushButtonMoveZ = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveZ.setGeometry(QtCore.QRect(820, 580, 41, 32))
        self.pushButtonMoveZ.setObjectName("pushButtonMoveZ")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(670, 560, 101, 16))
        self.label_20.setObjectName("label_20")
        self.comboBoxTrayNumber = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxTrayNumber.setGeometry(QtCore.QRect(690, 40, 61, 32))
        self.comboBoxTrayNumber.setObjectName("comboBoxTrayNumber")
        self.plainTextEditTrayNumber = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditTrayNumber.setGeometry(QtCore.QRect(770, 45, 41, 26))
        self.plainTextEditTrayNumber.setPlainText("")
        self.plainTextEditTrayNumber.setObjectName("plainTextEditTrayNumber")
        self.pushButtonAddTray = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddTray.setGeometry(QtCore.QRect(810, 40, 61, 32))
        self.pushButtonAddTray.setObjectName("pushButtonAddTray")
        self.pushButtonDeleteTray = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDeleteTray.setGeometry(QtCore.QRect(810, 70, 61, 32))
        self.pushButtonDeleteTray.setObjectName("pushButtonDeleteTray")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(660, 220, 21, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(660, 250, 21, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(660, 280, 21, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(660, 310, 21, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(660, 390, 21, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(660, 420, 21, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(660, 450, 21, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(660, 360, 21, 16))
        self.label_28.setObjectName("label_28")
        self.pushButtonGetTrayCamera1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetTrayCamera1.setGeometry(QtCore.QRect(810, 210, 61, 32))
        self.pushButtonGetTrayCamera1.setObjectName("pushButtonGetTrayCamera1")
        self.pushButtonGetTrayCamera2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetTrayCamera2.setGeometry(QtCore.QRect(810, 240, 61, 32))
        self.pushButtonGetTrayCamera2.setObjectName("pushButtonGetTrayCamera2")
        self.pushButtonGetTrayCamera3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetTrayCamera3.setGeometry(QtCore.QRect(810, 270, 61, 32))
        self.pushButtonGetTrayCamera3.setObjectName("pushButtonGetTrayCamera3")
        self.pushButtonGetTrayCamera4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGetTrayCamera4.setGeometry(QtCore.QRect(810, 300, 61, 32))
        self.pushButtonGetTrayCamera4.setObjectName("pushButtonGetTrayCamera4")
        self.labelMousePos = QtWidgets.QLabel(self.centralwidget)
        self.labelMousePos.setGeometry(QtCore.QRect(570, 620, 51, 16))
        self.labelMousePos.setObjectName("labelMousePos")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(760, 500, 21, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(760, 540, 21, 16))
        self.label_30.setObjectName("label_30")
        self.plainTextEditPosCameraZ = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditPosCameraZ.setGeometry(QtCore.QRect(790, 130, 61, 26))
        self.plainTextEditPosCameraZ.setPlaceholderText("")
        self.plainTextEditPosCameraZ.setObjectName("plainTextEditPosCameraZ")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(770, 130, 21, 16))
        self.label_31.setObjectName("label_31")
        self.radioButtonComponentChk = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonComponentChk.setGeometry(QtCore.QRect(570, 600, 99, 20))
        self.radioButtonComponentChk.setObjectName("radioButtonComponentChk")
        self.pushButtonMoveUp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMoveUp.setGeometry(QtCore.QRect(780, 0, 91, 32))
        self.pushButtonMoveUp.setObjectName("pushButtonMoveUp")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Upper"))
        self.label_3.setText(_translate("MainWindow", "Lower"))
        self.label_4.setText(_translate("MainWindow", "Hue"))
        self.label_5.setText(_translate("MainWindow", "Sat"))
        self.label_6.setText(_translate("MainWindow", "Val"))
        self.label_7.setText(_translate("MainWindow", "for Back"))
        self.label_8.setText(_translate("MainWindow", "Lower"))
        self.label_9.setText(_translate("MainWindow", "Upper"))
        self.label_10.setText(_translate("MainWindow", "for Black"))
        self.radioButtonRaw.setText(_translate("MainWindow", "Raw"))
        self.radioButtonBack.setText(_translate("MainWindow", "Back"))
        self.radioButtonBlack.setText(_translate("MainWindow", "Black"))
        self.radioButtonComponent.setText(_translate("MainWindow", "Component"))
        self.label_11.setText(_translate("MainWindow", "Mode"))
        self.pushButtonCapture.setText(_translate("MainWindow", "Capture"))
        self.pushButtonQuit.setText(_translate("MainWindow", "Quit"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonMoveTrayCamera.setText(_translate("MainWindow", "Move to Camera"))
        self.pushButtonMoveNextBaseCorner.setText(_translate("MainWindow", "Next Base Mark"))
        self.label_12.setText(_translate("MainWindow", "Tray"))
        self.plainTextEditAreaCompL.setPlainText(_translate("MainWindow", "300"))
        self.plainTextEditAreaCompU.setPlainText(_translate("MainWindow", "700"))
        self.plainTextEditAreaBlackU.setPlainText(_translate("MainWindow", "1000"))
        self.plainTextEditAreaBlackL.setPlainText(_translate("MainWindow", "200"))
        self.label_13.setText(_translate("MainWindow", "Area"))
        self.label_14.setText(_translate("MainWindow", "Component"))
        self.label_15.setText(_translate("MainWindow", "Black"))
        self.plainTextEditPosCamera1X.setPlainText(_translate("MainWindow", "10"))
        self.plainTextEditPosCamera1Y.setPlainText(_translate("MainWindow", "10"))
        self.plainTextEditPosCamera2X.setPlainText(_translate("MainWindow", "600"))
        self.plainTextEditPosCamera2Y.setPlainText(_translate("MainWindow", "10"))
        self.plainTextEditPosCamera3X.setPlainText(_translate("MainWindow", "600"))
        self.plainTextEditPosCamera3Y.setPlainText(_translate("MainWindow", "400"))
        self.plainTextEditPosCamera4X.setPlainText(_translate("MainWindow", "10"))
        self.plainTextEditPosCamera4Y.setPlainText(_translate("MainWindow", "400"))
        self.plainTextEditPosReal3Y.setPlainText(_translate("MainWindow", "208"))
        self.plainTextEditPosReal4Y.setPlainText(_translate("MainWindow", "208"))
        self.plainTextEditPosReal1X.setPlainText(_translate("MainWindow", "3"))
        self.plainTextEditPosReal4X.setPlainText(_translate("MainWindow", "3"))
        self.plainTextEditPosReal2X.setPlainText(_translate("MainWindow", "30"))
        self.plainTextEditPosReal3X.setPlainText(_translate("MainWindow", "30"))
        self.plainTextEditPosReal2Y.setPlainText(_translate("MainWindow", "222"))
        self.plainTextEditPosReal1Y.setPlainText(_translate("MainWindow", "222"))
        self.label_16.setText(_translate("MainWindow", "Camera Corners"))
        self.label_17.setText(_translate("MainWindow", "Real Corners"))
        self.pushButtonMoveTrayCorner1.setText(_translate("MainWindow", "Move"))
        self.pushButtonMoveTrayCorner2.setText(_translate("MainWindow", "Move"))
        self.pushButtonMoveTrayCorner3.setText(_translate("MainWindow", "Move"))
        self.pushButtonMoveTrayCorner4.setText(_translate("MainWindow", "Move"))
        self.plainTextEditPosCameraX.setPlainText(_translate("MainWindow", "10"))
        self.plainTextEditPosCameraY.setPlainText(_translate("MainWindow", "10"))
        self.label_19.setText(_translate("MainWindow", "Camera"))
        self.plainTextEditManualMove.setPlainText(_translate("MainWindow", "0"))
        self.pushButtonMoveX.setText(_translate("MainWindow", "X"))
        self.pushButtonMoveY.setText(_translate("MainWindow", "Y"))
        self.pushButtonMoveZ.setText(_translate("MainWindow", "Z"))
        self.label_20.setText(_translate("MainWindow", "Manual Move"))
        self.pushButtonAddTray.setText(_translate("MainWindow", "Add"))
        self.pushButtonDeleteTray.setText(_translate("MainWindow", "Del"))
        self.label_21.setText(_translate("MainWindow", "UL"))
        self.label_22.setText(_translate("MainWindow", "UR"))
        self.label_23.setText(_translate("MainWindow", "LR"))
        self.label_24.setText(_translate("MainWindow", "LL"))
        self.label_25.setText(_translate("MainWindow", "UR"))
        self.label_26.setText(_translate("MainWindow", "LR"))
        self.label_27.setText(_translate("MainWindow", "LL"))
        self.label_28.setText(_translate("MainWindow", "UL"))
        self.pushButtonGetTrayCamera1.setText(_translate("MainWindow", "Get"))
        self.pushButtonGetTrayCamera2.setText(_translate("MainWindow", "Get"))
        self.pushButtonGetTrayCamera3.setText(_translate("MainWindow", "Get"))
        self.pushButtonGetTrayCamera4.setText(_translate("MainWindow", "Get"))
        self.labelMousePos.setText(_translate("MainWindow", "-"))
        self.label_29.setText(_translate("MainWindow", "-"))
        self.label_30.setText(_translate("MainWindow", "-"))
        self.plainTextEditPosCameraZ.setPlainText(_translate("MainWindow", "10"))
        self.label_31.setText(_translate("MainWindow", "Z"))
        self.radioButtonComponentChk.setText(_translate("MainWindow", "Cmp&Check"))
        self.pushButtonMoveUp.setText(_translate("MainWindow", "Move Up"))
