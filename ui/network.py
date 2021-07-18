from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newConnection = QtWidgets.QPushButton(self.centralwidget)
        self.newConnection.setGeometry(QtCore.QRect(10, -2, 582, 25))
        self.newConnection.setObjectName("newConnection")
        self.back_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 510, 582, 36))
        self.back_button.setObjectName("back_button")
        self.connections = QtWidgets.QPushButton(self.centralwidget)
        self.connections.setGeometry(QtCore.QRect(10, 29, 582, 25))
        self.connections.setObjectName("connections")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 581, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 579, 439))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 561, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.username_3 = QtWidgets.QLabel(self.frame_3)
        self.username_3.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.username_3.setObjectName("username_3")
        self.username_edit_3 = QtWidgets.QLabel(self.frame_3)
        self.username_edit_3.setGeometry(QtCore.QRect(10, 40, 141, 16))
        self.username_edit_3.setObjectName("username_edit_3")
        self.Is_connect_3 = QtWidgets.QCheckBox(self.frame_3)
        self.Is_connect_3.setGeometry(QtCore.QRect(460, 20, 70, 31))
        self.Is_connect_3.setObjectName("Is_connect_3")
        self.seeProfile_3 = QtWidgets.QPushButton(self.frame_3)
        self.seeProfile_3.setGeometry(QtCore.QRect(350, 20, 91, 23))
        self.seeProfile_3.setObjectName("seeProfile_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        from .home import ui as ui_home
        # TODO: check empty dictionary
        self.back_button.clicked.connect(lambda : ui_home.setupUi(MainWindow, {}))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newConnection.setText(_translate("MainWindow", "New Connection"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.connections.setText(_translate("MainWindow", "Connections"))
        self.username_3.setText(_translate("MainWindow", "Username:"))
        self.username_edit_3.setText(_translate("MainWindow", "username"))
        self.Is_connect_3.setText(_translate("MainWindow", "Connect"))
        self.seeProfile_3.setText(_translate("MainWindow", "See Profile"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
