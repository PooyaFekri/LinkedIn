from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, page, counter=0):
        self.data = data
        self.page = page
        self.counter = counter
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.profile = QtWidgets.QPushButton(self.frame)
        self.profile.setGeometry(QtCore.QRect(30, 30, 151, 141))
        self.profile.setObjectName("profile")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 40, 91, 17))
        self.label.setObjectName("label")
        self.Username = QtWidgets.QLabel(self.frame)
        self.Username.setGeometry(QtCore.QRect(340, 70, 131, 17))
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(230, 120, 161, 17))
        self.label_2.setObjectName("label_2")
        self.mutualConnection = QtWidgets.QLabel(self.frame)
        self.mutualConnection.setGeometry(QtCore.QRect(380, 140, 67, 17))
        self.mutualConnection.setObjectName("mutualConnection")
        self.MessageButton = QtWidgets.QPushButton(self.frame)
        self.MessageButton.setGeometry(QtCore.QRect(40, 210, 89, 25))
        self.MessageButton.setObjectName("MessageButton")
        self.DisConnectButton = QtWidgets.QPushButton(self.frame)
        self.DisConnectButton.setGeometry(QtCore.QRect(40, 250, 89, 25))
        self.DisConnectButton.setObjectName("DisConnectButton")
        self.verticalLayout.addWidget(self.frame)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.verticalLayout.addWidget(self.next)
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setObjectName("Back")
        self.verticalLayout.addWidget(self.Back)
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setObjectName("home")
        self.verticalLayout.addWidget(self.home)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # TODO: find mutual connections
        self.retranslateUi(MainWindow)
        self.set_user()
        self.set_counter()
        from .home import ui as ui_home
        from .seeOtherPerson import ui as ui_other_person
        self.profile.clicked.connect(
            lambda: ui_other_person.setupUi(MainWindow, data, self.page.get("users")[self.counter]))
        # TODO: creat room and go to chatroom
        # self.MessageButton.clicked.connect()
        self.DisConnectButton.clicked.connect(lambda: self.dis_user(MainWindow))
        self.next.clicked.connect(lambda: ui.setupUi(MainWindow, data, page, self.counter_after))
        self.Back.clicked.connect(lambda: ui.setupUi(MainWindow, data, page, self.counter_before))
        self.home.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profile.setText(_translate("MainWindow", "Profile"))
        self.label.setText(_translate("MainWindow", "User name:"))
        self.label_2.setText(_translate("MainWindow", "mutual Connection :"))
        self.mutualConnection.setText(_translate("MainWindow", "number"))
        self.MessageButton.setText(_translate("MainWindow", "Message"))
        self.DisConnectButton.setText(_translate("MainWindow", "Disconnet"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.home.setText(_translate("MainWindow", "Home"))

    def set_user(self):
        self.Username.setText(self.page['users'][self.counter].username)
        # TODO: mutual connection

    def dis_user(self, MainWindow):
        from .home import ui as ui_home
        connection = self.page["connections"][self.counter].delete()
        ui_home.setupUi(MainWindow, self.data)


    def set_counter(self):
        self.counter_after = self.counter_before = self.counter
        if len(self.page['users']) > self.counter + 1:
            self.counter_after = self.counter + 1
        if self.counter != 0:
            self.counter_before = self.counter - 1

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
