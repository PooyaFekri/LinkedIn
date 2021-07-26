import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection
from tables.notification import Notification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, page, counter=0):
        self.data = data
        self.page = page
        self.counter = counter
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(10, 499, 582, 23))
        self.Back.setObjectName("Back")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(10, 470, 582, 23))
        self.next.setObjectName("next")
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(10, 528, 582, 23))
        self.home.setObjectName("home")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 582, 454))
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
        self.ConnectButton = QtWidgets.QPushButton(self.frame)
        self.ConnectButton.setGeometry(QtCore.QRect(40, 250, 89, 25))
        self.ConnectButton.setObjectName("ConnectButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.set_user()
        self.set_counter()
        from .home import ui as ui_home
        from .seeOtherPerson import ui as ui_other_person
        self.profile.clicked.connect(
            lambda: ui_other_person.setupUi(MainWindow, data, self.page.get("users")[self.counter]))
        self.ConnectButton.clicked.connect(lambda: self.connect())
        self.next.clicked.connect(lambda: ui.setupUi(MainWindow, self.data, self.page, self.counter_after))
        self.Back.clicked.connect(lambda: ui.setupUi(MainWindow, self.data, self.page, self.counter_before))
        self.home.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.next.setText(_translate("MainWindow", "Next"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.profile.setText(_translate("MainWindow", "Profile"))
        self.label.setText(_translate("MainWindow", "User name:"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect"))

    def set_user(self):
        self.label.setText(f'Username: {self.page.get("users")[self.counter].username}')

    def set_counter(self):
        self.counter_after = self.counter_before = self.counter
        if len(self.page['users']) > self.counter + 1:
            self.counter_after = self.counter + 1
        if self.counter != 0:
            self.counter_before = self.counter - 1

    def connect(self):
        another_user_id = self.page.get('users')[self.counter].id
        data = {
            "user_caller_id": self.data["user"].id,
            "user_invited_id": another_user_id
        }
        res = Connection.connect_request(**data)
        if res.get('status'):
            res = Connection.find(**data)
            if res.get('status'):
                Notification.notify(user_id=another_user_id,
                                    type_id=res.get('connections')[-1].id,
                                    type='Connection',
                                    time=datetime.datetime.now(),
                                    )


ui = Ui_MainWindow()
