# -*- coding: utf-8 -*-
"""
Created on Fri Jan 01 22:25:13 2016

@author: AkishinoShiame
"""

import sys
from PyQt4 import *
from my_pred_GUI import Ui_MainWindow




class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.FileSlt_btn.clicked.connect(self.Browse_File)
        
        #openFile = QtGui.QAction("&Open File",self)
        #openFile.setShortcut("Ctrl+O")
        #openFile.setStatusTip('Open File')
        #openFile.triggered.connect(self.Browse_File)
    
    def Browse_File(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', self.ui.FileName_lab.text(), filter = ("Images (*.jpeg *.jpg *.jpe)"))
        if name:
            self.ui.FileName_lab.setText(QDir.toNativeSperators(name))
        #file = open(name,'r')
        #self.textEdit = QtGui.QTextEdit()
        #self.setCentralWidget(self.textEdit)
        
               

if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())