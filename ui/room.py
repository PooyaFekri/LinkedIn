# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Room(object):
    def setupUi(self, Room):
        Room.setObjectName("Room")
        Room.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Room)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ArchiveList = QtWidgets.QPushButton(Room)
        self.ArchiveList.setObjectName("ArchiveList")
        self.verticalLayout.addWidget(self.ArchiveList)
        self.scrollArea = QtWidgets.QScrollArea(Room)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 504))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Chat_room = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.Chat_room.setGeometry(QtCore.QRect(19, 10, 541, 101))
        self.Chat_room.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Chat_room.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Chat_room.setObjectName("Chat_room")
        self.SeeChat = QtWidgets.QPushButton(self.Chat_room)
        self.SeeChat.setGeometry(QtCore.QRect(14, 10, 101, 81))
        self.SeeChat.setObjectName("SeeChat")
        self.label = QtWidgets.QLabel(self.Chat_room)
        self.label.setGeometry(QtCore.QRect(140, 20, 81, 16))
        self.label.setObjectName("label")
        self.UserName = QtWidgets.QLabel(self.Chat_room)
        self.UserName.setGeometry(QtCore.QRect(150, 40, 47, 13))
        self.UserName.setObjectName("UserName")
        self.label_3 = QtWidgets.QLabel(self.Chat_room)
        self.label_3.setGeometry(QtCore.QRect(140, 60, 47, 13))
        self.label_3.setObjectName("label_3")
        self.FirstName_lastName = QtWidgets.QLabel(self.Chat_room)
        self.FirstName_lastName.setGeometry(QtCore.QRect(150, 80, 81, 16))
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.Back = QtWidgets.QCommandLinkButton(Room)
        self.Back.setObjectName("Back")
        self.verticalLayout.addWidget(self.Back)

        self.retranslateUi(Room)
        QtCore.QMetaObject.connectSlotsByName(Room)

    def retranslateUi(self, Room):
        _translate = QtCore.QCoreApplication.translate
        Room.setWindowTitle(_translate("Room", "Form"))
        self.ArchiveList.setText(_translate("Room", "Archive chat"))
        self.SeeChat.setText(_translate("Room", "Chat"))
        self.label.setText(_translate("Room", "User Name:"))
        self.UserName.setText(_translate("Room", "User_"))
        self.label_3.setText(_translate("Room", "Name :"))
        self.FirstName_lastName.setText(_translate("Room", "Name_last_name"))
        self.checkBoxRead.setText(_translate("Room", "Read"))
        self.Delete_this_chat.setText(_translate("Room", "Delete"))
        self.Archive_this_chat.setText(_translate("Room", "Archive"))
        self.Back.setText(_translate("Room", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Room = QtWidgets.QWidget()
    ui = Ui_Room()
    ui.setupUi(Room)
    Room.show()
    sys.exit(app.exec_())
