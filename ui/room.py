# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ArchiveList = QtWidgets.QPushButton(self.centralwidget)
        self.ArchiveList.setObjectName("ArchiveList")
        self.verticalLayout.addWidget(self.ArchiveList)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(170, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.Delete_this_chat = QtWidgets.QPushButton(self.frame)
        self.Delete_this_chat.setGeometry(QtCore.QRect(440, 80, 75, 23))
        self.Delete_this_chat.setObjectName("Delete_this_chat")
        self.FirstName_lastName = QtWidgets.QLabel(self.frame)
        self.FirstName_lastName.setGeometry(QtCore.QRect(180, 90, 81, 16))
        self.FirstName_lastName.setObjectName("FirstName_lastName")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 30, 81, 16))
        self.label.setObjectName("label")
        self.checkBoxRead = QtWidgets.QCheckBox(self.frame)
        self.checkBoxRead.setGeometry(QtCore.QRect(450, 30, 70, 17))
        self.checkBoxRead.setObjectName("checkBoxRead")
        self.UserName = QtWidgets.QLabel(self.frame)
        self.UserName.setGeometry(QtCore.QRect(180, 50, 47, 13))
        self.UserName.setObjectName("UserName")
        self.SeeChat = QtWidgets.QPushButton(self.frame)
        self.SeeChat.setGeometry(QtCore.QRect(44, 20, 101, 81))
        self.SeeChat.setObjectName("SeeChat")
        self.Archive_this_chat = QtWidgets.QPushButton(self.frame)
        self.Archive_this_chat.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.Archive_this_chat.setObjectName("Archive_this_chat")
        self.verticalLayout.addWidget(self.frame)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout.addWidget(self.NextButton)
        self.BeforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeButton.setObjectName("BeforeButton")
        self.verticalLayout.addWidget(self.BeforeButton)
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout.addWidget(self.BackButton)
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
        self.ArchiveList.setText(_translate("MainWindow", "Archive chat"))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.Delete_this_chat.setText(_translate("MainWindow", "Delete"))
        self.FirstName_lastName.setText(_translate("MainWindow", "Name_last_name"))
        self.label.setText(_translate("MainWindow", "User Name:"))
        self.checkBoxRead.setText(_translate("MainWindow", "Read"))
        self.UserName.setText(_translate("MainWindow", "User_"))
        self.SeeChat.setText(_translate("MainWindow", "Chat"))
        self.Archive_this_chat.setText(_translate("MainWindow", "Archive"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.BeforeButton.setText(_translate("MainWindow", "Before"))
        self.BackButton.setText(_translate("MainWindow", "Back"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
