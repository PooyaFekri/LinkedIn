from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chat(object):
    def setupUi(self, Chat):
        Chat.setObjectName("Chat")
        Chat.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Chat)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Chat)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 478))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.chat_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.chat_frame.setGeometry(QtCore.QRect(10, 9, 551, 141))
        self.chat_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat_frame.setObjectName("chat_frame")
        self.textBrowser_message = QtWidgets.QTextBrowser(self.chat_frame)
        self.textBrowser_message.setGeometry(QtCore.QRect(10, 0, 371, 131))
        self.textBrowser_message.setObjectName("textBrowser_message")
        self.label = QtWidgets.QLabel(self.chat_frame)
        self.label.setGeometry(QtCore.QRect(420, 10, 81, 16))
        self.label.setObjectName("label")
        self.username_label = QtWidgets.QLabel(self.chat_frame)
        self.username_label.setGeometry(QtCore.QRect(430, 40, 71, 16))
        self.username_label.setObjectName("username_label")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.lineEdit_message = QtWidgets.QLineEdit(Chat)
        self.lineEdit_message.setObjectName("lineEdit_message")
        self.verticalLayout.addWidget(self.lineEdit_message)
        self.Send_button = QtWidgets.QPushButton(Chat)
        self.Send_button.setObjectName("Send_button")
        self.verticalLayout.addWidget(self.Send_button)
        self.Back = QtWidgets.QCommandLinkButton(Chat)
        self.Back.setObjectName("Back")
        self.verticalLayout.addWidget(self.Back)

        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        _translate = QtCore.QCoreApplication.translate
        Chat.setWindowTitle(_translate("Chat", "Form"))
        self.label.setText(_translate("Chat", "User_Name:"))
        self.username_label.setText(_translate("Chat", "user_name"))
        self.Send_button.setText(_translate("Chat", "Send"))
        self.Back.setText(_translate("Chat", "Back"))

ui = Ui_Chat()