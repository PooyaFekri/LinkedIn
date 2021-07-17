from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Post(object):
    def setupUi(self, Post):
        Post.setObjectName("Post")
        Post.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Post)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Post)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.sendButton = QtWidgets.QPushButton(Post)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        self.Back_button = QtWidgets.QCommandLinkButton(Post)
        self.Back_button.setObjectName("Back_button")
        self.verticalLayout.addWidget(self.Back_button)

        self.retranslateUi(Post)
        QtCore.QMetaObject.connectSlotsByName(Post)

    def retranslateUi(self, Post):
        _translate = QtCore.QCoreApplication.translate
        Post.setWindowTitle(_translate("Post", "Form"))
        self.sendButton.setText(_translate("Post", "Send"))
        self.Back_button.setText(_translate("Post", "Back"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Post = QtWidgets.QWidget()
#     ui = Ui_Post()
#     ui.setupUi(Post)
#     Post.show()
#     sys.exit(app.exec_())

ui = Ui_Post()
