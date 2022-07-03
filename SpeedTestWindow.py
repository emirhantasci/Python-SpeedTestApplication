# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpeedTestWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SpeedTestWindow(object):
    def setupUi(self, SpeedTestWindow):
        SpeedTestWindow.setObjectName("SpeedTestWindow")
        SpeedTestWindow.resize(758, 218)
        self.centralwidget = QtWidgets.QWidget(SpeedTestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pbTesteBasla = QtWidgets.QPushButton(self.centralwidget)
        self.pbTesteBasla.setGeometry(QtCore.QRect(10, 12, 731, 31))
        self.pbTesteBasla.setStyleSheet("QPushButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 85, 255);\n"
"    font: 11pt \"Impact\";\n"
"}")
        self.pbTesteBasla.setObjectName("pbTesteBasla")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 90, 731, 91))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prbDownload = QtWidgets.QProgressBar(self.widget)
        self.prbDownload.setStyleSheet("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 15px;\n"
"color: black;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: #05B8CC;\n"
"border-radius :15px;\n"
"}    ")
        self.prbDownload.setProperty("value", 0)
        self.prbDownload.setTextVisible(False)
        self.prbDownload.setObjectName("prbDownload")
        self.horizontalLayout.addWidget(self.prbDownload)
        self.prbUpload = QtWidgets.QProgressBar(self.widget)
        self.prbUpload.setStyleSheet("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 15px;\n"
"color: black;\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: #05B8CC;\n"
"border-radius :15px;\n"
"}    ")
        self.prbUpload.setProperty("value", 0)
        self.prbUpload.setTextVisible(False)
        self.prbUpload.setObjectName("prbUpload")
        self.horizontalLayout.addWidget(self.prbUpload)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lneDownload = QtWidgets.QLineEdit(self.widget)
        self.lneDownload.setReadOnly(True)
        self.lneDownload.setObjectName("lneDownload")
        self.horizontalLayout_2.addWidget(self.lneDownload)
        self.lneUpload = QtWidgets.QLineEdit(self.widget)
        self.lneUpload.setReadOnly(True)
        self.lneUpload.setObjectName("lneUpload")
        self.horizontalLayout_2.addWidget(self.lneUpload)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        SpeedTestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SpeedTestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName("menubar")
        SpeedTestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SpeedTestWindow)
        self.statusbar.setObjectName("statusbar")
        SpeedTestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SpeedTestWindow)
        QtCore.QMetaObject.connectSlotsByName(SpeedTestWindow)

    def retranslateUi(self, SpeedTestWindow):
        _translate = QtCore.QCoreApplication.translate
        SpeedTestWindow.setWindowTitle(_translate("SpeedTestWindow", "Speed Test TeknoBol"))
        self.pbTesteBasla.setText(_translate("SpeedTestWindow", "Teste Başla"))
        self.label.setText(_translate("SpeedTestWindow", "Download Hızı"))
        self.label_2.setText(_translate("SpeedTestWindow", "Upload Hızı"))

