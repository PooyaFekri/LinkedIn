# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ArchiveList = QtWidgets.QPushButton(self.centralwidget)
        self.ArchiveList.setObjectName("ArchiveList")
        self.verticalLayout.addWidget(self.ArchiveList)
        self.Chat_room = QtWidgets.QFrame(self.centralwidget)
        self.Chat_room.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chat_room.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Chat_room.setObjectName("Chat_room")
        self.SeeChat = QtWidgets.QPushButton(self.Chat_room)
        self.SeeChat.setGeometry(QtCore.QRect(14, 10, 231, 181))
        self.SeeChat.setObjectName("SeeChat")
        self.label = QtWidgets.QLabel(self.Chat_room)
        self.label.setGeometry(QtCore.QRect(280, 110, 81, 16))
        self.label.setObjectName("label")
        self.UserName = QtWidgets.QLabel(self.Chat_room)
        self.UserName.setGeometry(QtCore.QRect(290, 130, 121, 16))
        self.UserName.setObjectName("UserName")
        self.label_3 = QtWidgets.QLabel(self.Chat_room)
        self.label_3.setGeometry(QtCore.QRect(280, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.FirstName_lastName = QtWidgets.QLabel(self.Chat_room)
        self.FirstName_lastName.setGeometry(QtCore.QRect(290, 170, 201, 16))
        self.FirstName_lastName.setObjectName("FirstName_lastName")
        self.checkBoxRead = QtWidgets.QCheckBox(self.Chat_room)
        self.checkBoxRead.setGeometry(QtCore.QRect(420, 20, 70, 17))
        self.checkBoxRead.setObjectName("checkBoxRead")
        self.Delete_this_chat = QtWidgets.QPushButton(self.Chat_room)
        self.Delete_this_chat.setGeometry(QtCore.QRect(410, 70, 75, 23))
        self.Delete_this_chat.setObjectName("Delete_this_chat")
        self.Archive_this_chat = QtWidgets.QPushButton(self.Chat_room)
        self.Archive_this_chat.setGeometry(QtCore.QRect(410, 40, 75, 23))
        self.Archive_this_chat.setObjectName("Archive_this_chat")
        self.verticalLayout.addWidget(self.Chat_room)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout.addWidget(self.NextButton)
        self.BeforeRoomButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeRoomButton.setObjectName("BeforeRoomButton")
        self.verticalLayout.addWidget(self.BeforeRoomButton)
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

        from home import ui as ui_home
        self.retranslateUi(MainWindow)
        self.BackButton.clicked.connect(lambda : ui_home.setupUi(MainWindow,data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ArchiveList.setText(_translate("MainWindow", "Archive chat"))
        self.SeeChat.setText(_translate("MainWindow", "Chat"))
        self.label.setText(_translate("MainWindow", "User Name:"))
        self.UserName.setText(_translate("MainWindow", "User_"))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.FirstName_lastName.setText(_translate("MainWindow", "Name_last_name"))
        self.checkBoxRead.setText(_translate("MainWindow", "Read"))
        self.Delete_this_chat.setText(_translate("MainWindow", "Delete"))
        self.Archive_this_chat.setText(_translate("MainWindow", "Archive"))
        self.NextButton.setText(_translate("MainWindow", "Next Room"))
        self.BeforeRoomButton.setText(_translate("MainWindow", "Before Room"))
        self.BackButton.setText(_translate("MainWindow", "Back"))




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()
