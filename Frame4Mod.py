# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame4.ui'
#
# Created: Wed Apr 13 00:10:55 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Frame4(object):

    def serverAction(self):
        print "f5.."
        from Frame5M import Ui_mainWindow
        print "Entered f5.. "
        self.w2=Ui_mainWindow()
        mainWindow=QtGui.QMainWindow()
        self.w2.setupUi(mainWindow)  

    def clientAction(self):
        print "f6.."
        from Frame6ClientM import Ui_mainWindow
        print "Entered f6.. "
        self.w2=Ui_mainWindow()
        mainWindow=QtGui.QMainWindow()
        self.w2.setupUi(mainWindow)  

    def setupUi(self, Frame4):
        Frame4.setObjectName(_fromUtf8("Frame4"))
        Frame4.resize(641, 425)
        self.centralwidget = QtGui.QWidget(Frame4)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.questionLabel = QtGui.QLabel(self.centralwidget)
        self.questionLabel.setGeometry(QtCore.QRect(30, 10, 581, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.questionLabel.setFont(font)
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setObjectName(_fromUtf8("questionLabel"))
        self.choiceLabel = QtGui.QLabel(self.centralwidget)
        self.choiceLabel.setGeometry(QtCore.QRect(40, 160, 561, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Bitstream Charter"))
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.choiceLabel.setFont(font)
        self.choiceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.choiceLabel.setObjectName(_fromUtf8("choiceLabel"))
        self.serverButton = QtGui.QPushButton(self.centralwidget)
        self.serverButton.setGeometry(QtCore.QRect(110, 286, 141, 51))
        self.serverButton.setObjectName(_fromUtf8("serverButton"))
        self.serverButton.clicked.connect(self.serverAction)

        self.clientButton = QtGui.QPushButton(self.centralwidget)
        self.clientButton.setGeometry(QtCore.QRect(410, 290, 131, 51))
        self.clientButton.setObjectName(_fromUtf8("clientButton"))
        self.clientButton.clicked.connect(self.clientAction)
        Frame4.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Frame4)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Frame4.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Frame4)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Frame4.setStatusBar(self.statusbar)

        self.retranslateUi(Frame4)
        QtCore.QMetaObject.connectSlotsByName(Frame4)

        print "Showing f4.."
        Frame4.show()
        sys.exit(app.exec_())
        print "Shown f4.."


    def retranslateUi(self, Frame4):
        Frame4.setWindowTitle(_translate("Frame4", "MainWindow", None))
        self.questionLabel.setText(_translate("Frame4", "Wanna be a \"Server\" or a \"Client\" ?? ", None))
        self.choiceLabel.setText(_translate("Frame4", "Click your choice", None))
        self.serverButton.setText(_translate("Frame4", "Server", None))
        self.clientButton.setText(_translate("Frame4", "Client", None))




