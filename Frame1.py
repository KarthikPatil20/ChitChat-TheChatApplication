# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame1.ui'
#
# Created: Sat Apr  2 23:01:25 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from PySide.QtCore import *
from PySide.QtGui import *

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

class Ui_frame1(object):
    def register(self):
        from Frame2 import Ui_frame2
        print "Entered .. "
        self.w2=Ui_frame2()
        frame2=QtGui.QMainWindow()
        self.w2.setupUi(frame2)  
 
    def login2(self):
        from Frame3 import Ui_LoginWindow
        print "Entered"
        self.w2=Ui_LoginWindow()
        LoginWindow=QtGui.QMainWindow()
        self.w2.setupUi(LoginWindow)  
  
 
   
    def setupUi(self, frame1):
        frame1.setObjectName(_fromUtf8("frame1"))
        frame1.setEnabled(True)
        frame1.resize(800, 600)
        self.centralwidget = QtGui.QWidget(frame1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 130, 491, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.register_2 = QtGui.QPushButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(130, 280, 131, 41))
        self.register_2.setObjectName(_fromUtf8("register_2"))
        self.register_2.clicked.connect(self.register)     

        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(470, 280, 121, 41))
        self.login.setObjectName(_fromUtf8("login"))
        self.login.clicked.connect(self.login2) 

        frame1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(frame1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        frame1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(frame1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        frame1.setStatusBar(self.statusbar)

        self.retranslateUi(frame1)
        QtCore.QMetaObject.connectSlotsByName(frame1)

    def retranslateUi(self, frame1):
        frame1.setWindowTitle(_translate("frame1", "WelCome !!", None))
        self.label.setText(_translate("frame1", "Welcome to ChitChat!", None))
        self.register_2.setText(_translate("frame1", "Register", None))
        self.login.setText(_translate("frame1", "Login", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frame1 = QtGui.QMainWindow()
    ui = Ui_frame1()
    ui.setupUi(frame1)
    frame1.show()
    sys.exit(app.exec_()) 
    
