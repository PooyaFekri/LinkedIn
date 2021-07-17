from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Network(object):
    def setupUi(self, Network):
        Network.setObjectName("Network")
        Network.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Network)
        self.verticalLayout.setObjectName("verticalLayout")
        self.newConnection = QtWidgets.QPushButton(Network)
        self.newConnection.setObjectName("newConnection")
        self.verticalLayout.addWidget(self.newConnection)
        self.connections = QtWidgets.QPushButton(Network)
        self.connections.setObjectName("connections")
        self.verticalLayout.addWidget(self.connections)
        self.scrollArea = QtWidgets.QScrollArea(Network)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 475))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(10, 10, 561, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.username = QtWidgets.QLabel(self.frame)
        self.username.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.username.setObjectName("username")
        self.username_edit = QtWidgets.QLabel(self.frame)
        self.username_edit.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.username_edit.setObjectName("username_edit")
        self.Is_connect = QtWidgets.QCheckBox(self.frame)
        self.Is_connect.setGeometry(QtCore.QRect(460, 20, 70, 31))
        self.Is_connect.setObjectName("Is_connect")
        self.seeProfile = QtWidgets.QPushButton(self.frame)
        self.seeProfile.setGeometry(QtCore.QRect(350, 20, 91, 23))
        self.seeProfile.setObjectName("seeProfile")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.back_button = QtWidgets.QCommandLinkButton(Network)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)

        self.retranslateUi(Network)
        QtCore.QMetaObject.connectSlotsByName(Network)

    def retranslateUi(self, Network):
        _translate = QtCore.QCoreApplication.translate
        Network.setWindowTitle(_translate("Network", "Form"))
        self.newConnection.setText(_translate("Network", "New Connection"))
        self.connections.setText(_translate("Network", "Connections"))
        self.username.setText(_translate("Network", "Username:"))
        self.username_edit.setText(_translate("Network", "username"))
        self.Is_connect.setText(_translate("Network", "Connect"))
        self.seeProfile.setText(_translate("Network", "See Profile"))
        self.back_button.setText(_translate("Network", "Back"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Network = QtWidgets.QWidget()
#     ui = Ui_Network()
#     ui.setupUi(Network)
#     Network.show()
#     sys.exit(app.exec_())

ui = Ui_Network()
