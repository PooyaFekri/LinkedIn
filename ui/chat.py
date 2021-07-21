# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 5, 581, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_chat = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_chat.setObjectName("textBrowser_chat")
        self.verticalLayout.addWidget(self.textBrowser_chat)
        self.lineEdit_message = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_message.setObjectName("lineEdit_message")
        self.verticalLayout.addWidget(self.lineEdit_message)
        self.Send_button = QtWidgets.QPushButton(self.layoutWidget)
        self.Send_button.setObjectName("Send_button")
        self.verticalLayout.addWidget(self.Send_button)
        self.Back = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.Back.setObjectName("Back")
        self.verticalLayout.addWidget(self.Back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Send_button.setText(_translate("MainWindow", "Send"))
        self.Back.setText(_translate("MainWindow", "Back"))




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()
