# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame3.ui'
#
# Created: Sat Apr  2 23:58:53 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os.path

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

class Ui_LoginWindow(object):
    def okLoginAction(self):
        unameA=self.logintf_username.text()
        passwordA=self.logintf_password.text()

        if not os.path.isfile(unameA+'.txt'):
            w1=QtGui.QWidget()
            QtGui.QMessageBox.information(w1, "Info", "User has not registered yet\nUser must register first to login")
            LoginWindow.Destroy()
                 
        
        for line in open(unameA+'.txt'):
            print len(line)
            verifyLine=line[0:len(line)-1]
            print verifyLine
            
            if verifyLine!=passwordA:
                w1=QtGui.QWidget()
                QtGui.QMessageBox.information(w1, "Info", "Password doesn't match\nCome back later")
                LoginWindow.Destroy()
            break

        from Frame4Mod import Ui_Frame4
        print "Entered frame4.. "
        self.w2=Ui_Frame4()
        Frame4=QtGui.QMainWindow()
        self.w2.setupUi(Frame4)  
        
    
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName(_fromUtf8("LoginWindow"))
        LoginWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(LoginWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.login = QtGui.QLabel(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(320, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setObjectName(_fromUtf8("login"))
        self.login_username = QtGui.QLabel(self.centralwidget)
        self.login_username.setGeometry(QtCore.QRect(155, 180, 91, 20))
        self.login_username.setObjectName(_fromUtf8("login_username"))
        self.login_password = QtGui.QLabel(self.centralwidget)
        self.login_password.setGeometry(QtCore.QRect(160, 240, 91, 20))
        self.login_password.setObjectName(_fromUtf8("login_password"))
        self.logintf_username = QtGui.QLineEdit(self.centralwidget)
        self.logintf_username.setGeometry(QtCore.QRect(250, 180, 321, 27))
        self.logintf_username.setObjectName(_fromUtf8("logintf_username"))

        self.logintf_password = QtGui.QLineEdit(self.centralwidget)
        self.logintf_password.setGeometry(QtCore.QRect(250, 240, 321, 27))
        self.logintf_password.setObjectName(_fromUtf8("logintf_password"))
        self.logintf_password.setEchoMode(QtGui.QLineEdit.Password)

        self.okLoginButton = QtGui.QPushButton(self.centralwidget)
        self.okLoginButton.setGeometry(QtCore.QRect(350, 340, 141, 51))
        self.okLoginButton.setObjectName(_fromUtf8("okLoginButton"))

        self.okLoginButton.clicked.connect(self.okLoginAction)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(LoginWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        print "Showing.."
        LoginWindow.show()
        sys.exit(app.exec_())
        print "Shown.."

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login", None))
        self.login.setText(_translate("LoginWindow", "  Login", None))
        self.login_username.setText(_translate("LoginWindow", "Username:", None))
        self.login_password.setText(_translate("LoginWindow", "Password:", None))
        self.okLoginButton.setText(_translate("LoginWindow", "OK", None))

