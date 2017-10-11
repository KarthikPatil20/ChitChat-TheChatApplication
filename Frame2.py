# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame2.ui'
#
# Created: Sat Apr  2 23:52:55 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from email.utils import parseaddr

def msg_box(title, message):
    w=QtGui.QWidget()
    QtGui.QMessageBox.information(w, title, message)

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

class Ui_frame2(object):
   
    def okAction(self):
        count=0
        nameA=self.name_line.text()
        unameA=self.username_line.text()
        emailA=self.email_line.text()
        

        while (self.password_line.text())!=(self.cpassword_line.text()) and count<=3:
            count=count+1
            if count>2:
                w1=QtGui.QWidget()
                QtGui.QMessageBox.information(w1, "Info", "Passwords entered twice incorrect\nCome back later !!")
                frame2.Destroy()
            else:
                w2=QtGui.QWidget()
                #text.setEchoMode(QtGui.QLineEdit.Password)
                text, ok = QtGui.QInputDialog.getText(w2, 'Text Input Dialog', 'Enter correct confirmation password')
                
                if ok:
                    self.cpassword_line.setText(str(text))

        
        passwordA=self.password_line.text()
        cpassA=self.cpassword_line.text()
        
        
        with open(unameA+'.txt','a') as f:
            f.write(passwordA)
            f.write("\n")
            f.write(nameA)
            f.write("\n")
            f.write(unameA)
            f.write("\n")
            f.write(emailA)
            f.write("\n")
            f.write(cpassA)
            f.close()
        w1=QtGui.QWidget()
        QtGui.QMessageBox.information(w1, "Info", "User successfully registered. ThankYou !!")
        frame2.Destroy()
        
    def setupUi(self, frame2):
        frame2.setObjectName(_fromUtf8("frame2"))
        frame2.resize(800, 600)
        self.centralwidget = QtGui.QWidget(frame2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame2_register = QtGui.QLabel(self.centralwidget)
        self.frame2_register.setGeometry(QtCore.QRect(250, 30, 251, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.frame2_register.setFont(font)
        self.frame2_register.setObjectName(_fromUtf8("frame2_register"))
        self.name = QtGui.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(100, 130, 66, 17))
        self.name.setObjectName(_fromUtf8("name"))
        self.username = QtGui.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(80, 180, 81, 20))
        self.username.setObjectName(_fromUtf8("username"))
        self.email = QtGui.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(90, 230, 66, 17))
        self.email.setObjectName(_fromUtf8("email"))
        self.password = QtGui.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(80, 280, 81, 16))
        self.password.setObjectName(_fromUtf8("password"))
        self.c_password = QtGui.QLabel(self.centralwidget)
        self.c_password.setGeometry(QtCore.QRect(30, 330, 141, 20))
        self.c_password.setObjectName(_fromUtf8("c_password"))
        self.name_line = QtGui.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(190, 130, 381, 27))
        self.name_line.setObjectName(_fromUtf8("name_line"))
        self.username_line = QtGui.QLineEdit(self.centralwidget)
        self.username_line.setGeometry(QtCore.QRect(190, 180, 381, 27))
        self.username_line.setObjectName(_fromUtf8("username_line"))
        self.email_line = QtGui.QLineEdit(self.centralwidget)
        self.email_line.setGeometry(QtCore.QRect(190, 220, 381, 27))
        self.email_line.setObjectName(_fromUtf8("email_line"))
        

        self.password_line = QtGui.QLineEdit(self.centralwidget)
        self.password_line.setGeometry(QtCore.QRect(190, 270, 381, 27))
        self.password_line.setObjectName(_fromUtf8("password_line"))
        self.password_line.setEchoMode(QtGui.QLineEdit.Password)	

        self.cpassword_line = QtGui.QLineEdit(self.centralwidget)
        self.cpassword_line.setGeometry(QtCore.QRect(190, 320, 381, 27))
        self.cpassword_line.setObjectName(_fromUtf8("cpassword_line"))
        self.cpassword_line.setEchoMode(QtGui.QLineEdit.Password)

        self.okButton = QtGui.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(280, 410, 141, 41))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        #self.okButton.clicked.connect(self.ok)

        self.okButton.clicked.connect(self.okAction)

        frame2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(frame2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        frame2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(frame2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        frame2.setStatusBar(self.statusbar)

        self.retranslateUi(frame2)
        QtCore.QMetaObject.connectSlotsByName(frame2)

        print "Showing.."
        frame2.show()
        sys.exit(app.exec_())
        print "Shown.."

    #def ok(self):
     #   print self.email_line.text()
      #  c=self.email_line.text()
        #print parseaddr(self.email_line.text())
        #print tupleEmail
       # print parseaddr(str(c))


    def retranslateUi(self, frame2):
        frame2.setWindowTitle(_translate("frame2", "Register", None))
        self.frame2_register.setText(_translate("frame2", "Register", None))
        self.name.setText(_translate("frame2", "Name:", None))
        self.username.setText(_translate("frame2", "Username:   ", None))
        self.email.setText(_translate("frame2", "Email id:", None))
        self.password.setText(_translate("frame2", "Password:", None))
        self.c_password.setText(_translate("frame2", "Confirm Password:   ", None))
        self.okButton.setText(_translate("frame2", "OK", None))

    
        

    

