# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 14:31:56 2022

@author: emirh
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from speedtest import Speedtest

from SpeedTestWindow import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_SpeedTestWindow()
ui.setupUi(MainWindow)

MainWindow.show()

st = Speedtest()

def testebasla():
    ui.statusbar.showMessage("Teste başlandı...", 10000)
    downloadSpeed = st.download()/1000000
    uploadSpeed = st.upload()/1000000
    ui.prbDownload.setValue(downloadSpeed)
    ui.prbUpload.setValue(uploadSpeed)
    ui.lneDownload.setText(str(downloadSpeed))
    ui.lneUpload.setText(str(uploadSpeed))
    ui.statusbar.showMessage("Test tamamlandı...", 10000)
    
ui.pbTesteBasla.clicked.connect(testebasla)

sys.exit(app.exec_())
