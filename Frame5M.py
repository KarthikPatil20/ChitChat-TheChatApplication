# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame4.ui'
#
# Created: Sun Apr  3 19:25:34 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import socket

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

port_textbox=''
ip_textbox=''
s=''

def searchIP():
    global s
    portStr =port_textbox.text() # Reserve a port for your service.
    port=int(portStr)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
    ip=ip_textbox.text()
    print "ip:"+ ip
    host = ip     # Get local machine name
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.
   
    print 'Server listening...'



class Ui_mainWindow(object):

    
    def chooseFile(self):
        text=self.fChoosenLine
        text.setText(QtGui.QFileDialog.getOpenFileName())


    def sendFile(self):
        global s
        print "Ready to send..."
        conn, addr = s.accept()
        print "Got connection from : ",addr
        flag=0
        while True:
             print "Entered while"
             if flag==0:
                 '''sendText=str(self.textEdit.toPlainText())
             
                 print 'Ready to send text msg' 
                 print ("Plain Text:", str(sendText))         
                 if(sendText!=''):
                     conn.send("text")
                     print "Entered!!!!"
                     conn.send("Server:")
                     conn.send(sendText)
                     print ("Sent text:",sendText)
                     flag=1
                     self.textEdit.setText("")
              
                 else:'''   
      
                  # Establish connection with client.
                 print 'Got connection from', addr
                 print "Entered!!"
                 #data = conn.recv(1024)
                 #print('Server received', repr(data))

                 filename=self.fChoosenLine.text()

                 if(filename!=''):
                     conn.send("file")
                     f = open(filename,'rb')
                     print f
                     l = f.read(1024)
                     while (l):
                         conn.send(l)
                         print('Sent 1024')
                         l = f.read(1024)
                     f.close()

                     print('Done sending')
                     w=QtGui.QWidget()
                     QtGui.QMessageBox.information(w, "title", "You've successfully sent a file!")
                     conn.send('Thank you for connecting')
                     flag=1
                 self.fChoosenLine.setText("")
             
             
             '''data=conn.recv(8)
             print("data received",str(data))
             if(data=="file"):
                 with open('received_fileServer.txt', 'wb') as f:
                     print 'file opened'
                     while True:
                         print('receiving data...')
                         data = conn.recv(1024)
                         print('data=%s', (data))
                         if not data:
                             break
                                 # write data to a file
                         f.write(data)

                     f.close()
                     w=QtGui.QWidget()
                     QtGui.QMessageBox.information(w, "title", "You've successfully received a file!")
                     print('Successfully got the file')
             #a.close()	'''
             break
    
        conn.close()
        print "Conn 1 closed!!"
        #s.close()
        #print "Conn 2 closed!!"

    def SendMessageServer(self):
        global s
        print "Ready to send..."
        conn, addr = s.accept()
        print "Got connection from : ",addr
        flag=0
        while True:
             print "Entered while"
             if flag==0:
                 sendText=str(self.textEdit.toPlainText())
             
                 print 'Ready to send text msg' 
                 print ("Plain Text:", str(sendText))         
                 if(sendText!=''):
                     conn.send("text")
                     print "Entered!!!!"
                     #conn.send("Server:")
                     conn.send(sendText)
                     print ("Sent text:",sendText)
                     flag=1
                     #self.textEdit.setText("")
             break
        conn.close()
        print "Conn 1 closed!!"


    def receive1(self):
        global s
        print "Ready to receive.."
        conn, addr = s.accept()
        print "Got connection from : ",addr," under receive1"
        #flag=0
        while True:
            data=conn.recv(4)
            print("data received",str(data))

            if(data=="text"):
                while True:
                    print("Entered:",str(data))
                    self.textEdit.setPlainText(str(data))
                    print("after text setting...")
                    data=conn.recv(1024)
                    if not data:
                        break

            else:
                with open('received_fileServer', 'wb') as f:
                    print 'file opened'
                    while True:
                        print('receiving data...')
                        data = conn.recv(1024)
                        print('data=%s', (data))
                        if not data:
                            break
                                # write data to a file
                        f.write(data)
                    f.close()
                    w=QtGui.QWidget()
                    QtGui.QMessageBox.information(w, "title", "You've successfully received a file!")
                    print('Successfully got the file') 
            break
    
        conn.close()
        print "Conn 1 closed!!" 

    def QuitServer(self):
        global s
        s.close()
        print "Connection closed"
        w=QtGui.QWidget()
        QtGui.QMessageBox.information(w, "title", "ThankYou for using the Application")
        mainWindow.Destroy() 
        

    def setupUi(self, mainWindow):
        global port_textbox
        global ip_textbox
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(800, 600)
        mainWindow.setStatusTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ip_label = QtGui.QLabel(self.centralwidget)
        self.ip_label.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.ip_label.setObjectName(_fromUtf8("ip_label"))
        ip_textbox = QtGui.QLineEdit(self.centralwidget)
        ip_textbox.setGeometry(QtCore.QRect(110, 60, 581, 31))
        ip_textbox.setObjectName(_fromUtf8("ip_textbox"))
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(480, 110, 150, 31))
        self.search.setObjectName(_fromUtf8("search"))
        self.search.clicked.connect(searchIP)
 
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 210, 581, 121))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 681, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tfButton = QtGui.QPushButton(self.centralwidget)
        self.tfButton.setGeometry(QtCore.QRect(90, 400, 98, 41))
        self.tfButton.setObjectName(_fromUtf8("tfButton"))
        self.tfButton.clicked.connect(self.chooseFile)

        self.imageButton = QtGui.QPushButton(self.centralwidget)
        self.imageButton.setGeometry(QtCore.QRect(250, 400, 98, 41))
        self.imageButton.setObjectName(_fromUtf8("imageButton"))
        self.imageButton.clicked.connect(self.chooseFile)

        self.audioButton = QtGui.QPushButton(self.centralwidget)
        self.audioButton.setGeometry(QtCore.QRect(400, 400, 98, 41))
        self.audioButton.setObjectName(_fromUtf8("audioButton"))
        self.audioButton.clicked.connect(self.chooseFile)

        self.videoButton = QtGui.QPushButton(self.centralwidget)
        self.videoButton.setGeometry(QtCore.QRect(560, 400, 98, 41))
        self.videoButton.setObjectName(_fromUtf8("videoButton"))
        self.videoButton.clicked.connect(self.chooseFile)

        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(130, 480, 98, 41))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.sendButton.clicked.connect(self.sendFile)

        self.fileChoosen = QtGui.QLabel(self.centralwidget)
        self.fileChoosen.setGeometry(QtCore.QRect(60, 350, 101, 21))
        self.fileChoosen.setObjectName(_fromUtf8("fileChoosen"))
        self.fChoosenLine = QtGui.QLineEdit(self.centralwidget)
        self.fChoosenLine.setGeometry(QtCore.QRect(170, 350, 521, 27))
        self.fChoosenLine.setObjectName(_fromUtf8("fChoosenLine"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 180, 241, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.portLabel = QtGui.QLabel(self.centralwidget)
        self.portLabel.setGeometry(QtCore.QRect(20, 120, 101, 17))
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        port_textbox = QtGui.QLineEdit(self.centralwidget)
        port_textbox.setGeometry(QtCore.QRect(120, 110, 241, 31))
        port_textbox.setObjectName(_fromUtf8("port_textbox"))

        self.receiveBtnServer = QtGui.QPushButton(self.centralwidget)
        self.receiveBtnServer.setGeometry(QtCore.QRect(310, 480, 111, 41))
        self.receiveBtnServer.setObjectName(_fromUtf8("receiveBtnServer"))
        self.receiveBtnServer.clicked.connect(self.receive1)

        self.quitServer = QtGui.QPushButton(self.centralwidget)
        self.quitServer.setGeometry(QtCore.QRect(510, 480, 121, 41))
        self.quitServer.setObjectName(_fromUtf8("quitServer"))
        self.quitServer.clicked.connect(self.QuitServer)

        self.sendMessageServer = QtGui.QPushButton(self.centralwidget)
        self.sendMessageServer.setGeometry(QtCore.QRect(650, 250, 121, 41))
        self.sendMessageServer.setObjectName(_fromUtf8("sendMessageServer"))
        self.sendMessageServer.clicked.connect(self.SendMessageServer)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)


        print "Showing f5.."
        mainWindow.show()
        sys.exit(app.exec_())
        print "Shown f5.."

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "frame5", None))
        self.ip_label.setText(_translate("mainWindow", "Ip Address:", None))
        self.search.setText(_translate("mainWindow", "Connect to Client", None))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("mainWindow", "Enter the destination ip address", None))
        self.tfButton.setText(_translate("mainWindow", "Text File", None))
        self.imageButton.setText(_translate("mainWindow", "Image", None))
        self.audioButton.setText(_translate("mainWindow", "Audio", None))
        self.videoButton.setText(_translate("mainWindow", "Video", None))
        self.sendButton.setText(_translate("mainWindow", "Send", None))
        self.fileChoosen.setText(_translate("mainWindow", "File Choosen:", None))
        self.label.setText(_translate("mainWindow", "Wanna chat?   Enter the message:", None))
        self.portLabel.setText(_translate("mainWindow", "Port Number :", None))
        self.receiveBtnServer.setText(_translate("mainWindow", "Receive", None))
        self.quitServer.setText(_translate("mainWindow", "Quit App", None))
        self.sendMessageServer.setText(_translate("mainWindow", "Send Message", None))




