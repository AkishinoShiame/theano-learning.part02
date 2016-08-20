# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\winpython\Documents\python_GUI\my_pred_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(664, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.imagewidget = ImageWidget(self.centralwidget)
        self.imagewidget.setGeometry(QtCore.QRect(10, 250, 400, 300))
        self.imagewidget.setOrientation(QtCore.Qt.Vertical)
        self.imagewidget.setObjectName(_fromUtf8("imagewidget"))
        self.Step1_Grp = QtGui.QGroupBox(self.centralwidget)
        self.Step1_Grp.setGeometry(QtCore.QRect(50, 30, 281, 131))
        self.Step1_Grp.setObjectName(_fromUtf8("Step1_Grp"))
        self.FL_lab = QtGui.QLabel(self.Step1_Grp)
        self.FL_lab.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.FL_lab.setObjectName(_fromUtf8("FL_lab"))
        self.FileName_lab = QtGui.QLabel(self.Step1_Grp)
        self.FileName_lab.setGeometry(QtCore.QRect(40, 30, 221, 16))
        self.FileName_lab.setText(_fromUtf8(""))
        self.FileName_lab.setObjectName(_fromUtf8("FileName_lab"))
        self.FileSlt_btn = QtGui.QPushButton(self.Step1_Grp)
        self.FileSlt_btn.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.FileSlt_btn.setObjectName(_fromUtf8("FileSlt_btn"))
        self.Step2_grp = QtGui.QGroupBox(self.centralwidget)
        self.Step2_grp.setGeometry(QtCore.QRect(350, 30, 291, 131))
        self.Step2_grp.setObjectName(_fromUtf8("Step2_grp"))
        self.Start_btn = QtGui.QPushButton(self.Step2_grp)
        self.Start_btn.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.Start_btn.setObjectName(_fromUtf8("Start_btn"))
        self.Resault_grp = QtGui.QGroupBox(self.centralwidget)
        self.Resault_grp.setGeometry(QtCore.QRect(460, 250, 161, 271))
        self.Resault_grp.setObjectName(_fromUtf8("Resault_grp"))
        self.Res_lab = QtGui.QLabel(self.Resault_grp)
        self.Res_lab.setGeometry(QtCore.QRect(16, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.Res_lab.setFont(font)
        self.Res_lab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Res_lab.setTextFormat(QtCore.Qt.PlainText)
        self.Res_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Res_lab.setObjectName(_fromUtf8("Res_lab"))
        self.pic_lab = QtGui.QLabel(self.centralwidget)
        self.pic_lab.setGeometry(QtCore.QRect(50, 220, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.pic_lab.setFont(font)
        self.pic_lab.setObjectName(_fromUtf8("pic_lab"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Step1_Grp.setTitle(_translate("MainWindow", "Step1 : Choose a Picture", None))
        self.FL_lab.setText(_translate("MainWindow", "File:", None))
        self.FileSlt_btn.setText(_translate("MainWindow", "Select File", None))
        self.Step2_grp.setTitle(_translate("MainWindow", "Step2 : Ready to Star Recognize", None))
        self.Start_btn.setText(_translate("MainWindow", "Start !", None))
        self.Resault_grp.setTitle(_translate("MainWindow", "Resault", None))
        self.Res_lab.setText(_translate("MainWindow", "NaN", None))
        self.pic_lab.setText(_translate("MainWindow", "Loaded picture :", None))

from guiqwt.plot import ImageWidget
