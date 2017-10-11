# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame5.ui'
#
# Created: Sun Apr  3 19:43:28 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(641, 425)
        self.centralwidget = QtGui.QWidget(MainWindow)
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
        self.clientButton = QtGui.QPushButton(self.centralwidget)
        self.clientButton.setGeometry(QtCore.QRect(410, 290, 131, 51))
        self.clientButton.setObjectName(_fromUtf8("clientButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.questionLabel.setText(_translate("MainWindow", "Wanna be a \"Server\" or a \"Client\" ?? ", None))
        self.choiceLabel.setText(_translate("MainWindow", "Click your choice", None))
        self.serverButton.setText(_translate("MainWindow", "Server", None))
        self.clientButton.setText(_translate("MainWindow", "Client", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

