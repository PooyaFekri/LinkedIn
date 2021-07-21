import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QScrollArea

from .simple import ui as ui_simple
from tables import User, Connection
from tables.notification import Notification


class Ui_NewConnection(object):
    def setupUi(self, NewConnection, data):
        self.data = data
        NewConnection.setObjectName("NewConnection")
        NewConnection.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(NewConnection)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setObjectName("SearchButton")
        self.verticalLayout.addWidget(self.SearchButton)
        # self.scrollArea_users = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea_users.setWidgetResizable(True)
        # self.scrollArea_users.setObjectName("scrollArea_users")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 189))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.frame_3.setGeometry(QtCore.QRect(10, 10, 561, 71))
        # self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_3.setObjectName("frame_3")
        # self.username_3 = QtWidgets.QLabel(self.frame_3)
        # self.username_3.setGeometry(QtCore.QRect(10, 10, 141, 16))
        # self.username_3.setObjectName("username_3")
        # self.username_edit_3 = QtWidgets.QLabel(self.frame_3)
        # self.username_edit_3.setGeometry(QtCore.QRect(10, 40, 141, 16))
        # self.username_edit_3.setObjectName("username_edit_3")
        # self.seeProfile_search = QtWidgets.QPushButton(self.frame_3)
        # self.seeProfile_search.setGeometry(QtCore.QRect(350, 20, 91, 23))
        # self.seeProfile_search.setObjectName("seeProfile_search")
        # self.ConnectButton = QtWidgets.QPushButton(self.frame_3)
        # self.ConnectButton.setGeometry(QtCore.QRect(450, 20, 89, 25))
        # self.ConnectButton.setObjectName("ConnectButton")
        # self.scrollArea_users.setWidget(self.scrollAreaWidgetContents)
        # self.verticalLayout.addWidget(self.scrollArea_users)
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setObjectName("label_2")
        # self.verticalLayout.addWidget(self.label_2)
        # self.scrollArea_invitation = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea_invitation.setWidgetResizable(True)
        # self.scrollArea_invitation.setObjectName("scrollArea_invitation")
        # self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 580, 189))
        # self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        # self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        # self.frame_4.setGeometry(QtCore.QRect(10, 10, 561, 71))
        # self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_4.setObjectName("frame_4")
        # self.username_4 = QtWidgets.QLabel(self.frame_4)
        # self.username_4.setGeometry(QtCore.QRect(10, 10, 141, 16))
        # self.username_4.setObjectName("username_4")
        # self.username_edit_4 = QtWidgets.QLabel(self.frame_4)
        # self.username_edit_4.setGeometry(QtCore.QRect(10, 40, 141, 16))
        # self.username_edit_4.setObjectName("username_edit_4")
        # self.seeProfile_invitations = QtWidgets.QPushButton(self.frame_4)
        # self.seeProfile_invitations.setGeometry(QtCore.QRect(230, 20, 91, 23))
        # self.seeProfile_invitations.setObjectName("seeProfile_invitations")
        # self.ConnectButton_NO = QtWidgets.QPushButton(self.frame_4)
        # self.ConnectButton_NO.setGeometry(QtCore.QRect(450, 20, 89, 25))
        # self.ConnectButton_NO.setObjectName("ConnectButton_NO")
        # self.ConnnectButton_Yes = QtWidgets.QPushButton(self.frame_4)
        # self.ConnnectButton_Yes.setGeometry(QtCore.QRect(340, 20, 101, 25))
        # self.ConnnectButton_Yes.setObjectName("ConnnectButton_Yes")
        # self.scrollArea_invitation.setWidget(self.scrollAreaWidgetContents_2)
        # self.verticalLayout.addWidget(self.scrollArea_invitation)
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout.addWidget(self.BackButton)
        NewConnection.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewConnection)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        NewConnection.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewConnection)
        self.statusbar.setObjectName("statusbar")
        self.find_invitations()
        NewConnection.setStatusBar(self.statusbar)

        self.retranslateUi(NewConnection)
        from .network import ui as ui_network
        self.BackButton.clicked.connect(lambda: ui_network.setupUi(NewConnection,self.data))
        self.SearchButton.clicked.connect(lambda: self.search())
        QtCore.QMetaObject.connectSlotsByName(NewConnection)

    def retranslateUi(self, NewConnection):
        _translate = QtCore.QCoreApplication.translate
        NewConnection.setWindowTitle(_translate("NewConnection", "MainWindow"))
        self.label.setText(_translate("NewConnection", "Username"))
        self.SearchButton.setText(_translate("NewConnection", "Search"))
        # self.username_3.setText(_translate("NewConnection", "Username:"))
        # self.username_edit_3.setText(_translate("NewConnection", "username"))
        # self.seeProfile_search.setText(_translate("NewConnection", "See Profile"))
        # self.ConnectButton.setText(_translate("NewConnection", "Connect"))
        # self.label_2.setText(_translate("NewConnection", "Invitations"))
        # self.username_4.setText(_translate("NewConnection", "Username:"))
        # self.username_edit_4.setText(_translate("NewConnection", "username"))
        # self.seeProfile_invitations.setText(_translate("NewConnection", "See Profile"))
        # self.ConnectButton_NO.setText(_translate("NewConnection", "No"))
        # self.ConnnectButton_Yes.setText(_translate("NewConnection", "Yes, Connect"))
        self.BackButton.setText(_translate("NewConnection", "Back"))

    def search(self):
        username = self.lineEdit_username.text()
        users = self.data.get("user").search(username).get("users")

        for user in users:
            username = QtWidgets.QLabel()
            username.setGeometry(QtCore.QRect(10, 10, 141, 16))
            username.setObjectName("username")
            username_text = QtWidgets.QLabel()
            username_text.setGeometry(QtCore.QRect(10, 40, 141, 16))
            username_text.setObjectName("username_edit")
            seeProfile_search = QtWidgets.QPushButton()
            seeProfile_search.setGeometry(QtCore.QRect(350, 20, 91, 23))
            seeProfile_search.setObjectName("seeProfile_search")
            ConnectButton = QtWidgets.QPushButton()
            ConnectButton.setGeometry(QtCore.QRect(450, 20, 89, 25))
            self.verticalLayout.addWidget(username)
            self.verticalLayout.addWidget(username_text)
            self.verticalLayout.addWidget(seeProfile_search)
            self.verticalLayout.addWidget(ConnectButton)
            ConnectButton.setObjectName("ConnectButton")
            username_text.setText(f'New Connection : {user.username}')
            seeProfile_search.setText("See Profile")
            ConnectButton.setText("Connect")
            # TODO: complete this part
            # seeProfile_search.clicked.connect(lambda )
            ConnectButton.clicked.connect(lambda: self.connect(user.id))
            # self.scrollArea_users.setWidget(frame)
            # self.scrollArea_users.setWidget(self.scrollAreaWidgetContents)

    def find_invitations(self):
        _filter = {
            'user_invited_id': self.data.get("user").id,
            'connected': False
        }
        connections = Connection.find(**_filter).get('connections')

        for connection in connections:
            user = User.find_via_pk(connection.user_caller_id).get('user')
            username = QtWidgets.QLabel()
            username.setGeometry(QtCore.QRect(10, 10, 141, 16))
            username.setObjectName("username_inv")
            username_text = QtWidgets.QLabel()
            username_text.setGeometry(QtCore.QRect(10, 40, 141, 16))
            username_text.setObjectName("username_edit_inv")
            seeProfile_inv = QtWidgets.QPushButton()
            seeProfile_inv.setGeometry(QtCore.QRect(350, 20, 91, 23))
            seeProfile_inv.setObjectName("seeProfile_inv")
            NoConnectButton = QtWidgets.QPushButton()
            YesConnectButton = QtWidgets.QPushButton()
            NoConnectButton.setGeometry(QtCore.QRect(450, 20, 89, 25))
            YesConnectButton.setGeometry(QtCore.QRect(450, 20, 89, 25))
            self.verticalLayout.addWidget(username)
            self.verticalLayout.addWidget(username_text)
            self.verticalLayout.addWidget(seeProfile_inv)
            self.verticalLayout.addWidget(YesConnectButton)
            self.verticalLayout.addWidget(NoConnectButton)
            YesConnectButton.setObjectName("YesConnectButton")
            NoConnectButton.setObjectName("NoConnectButton")
            username_text.setText(f'New Invitation : {user.username}')
            seeProfile_inv.setText("See Profile")
            YesConnectButton.setText("Yes, Connect")
            NoConnectButton.setText("No")
            # TODO: complete this part
            # seeProfile_inv.clicked.connect(lambda: self.connect(user.id))
            YesConnectButton.clicked.connect(lambda: self.accept_or_reject_inv(connection, True))
            NoConnectButton.clicked.connect(lambda: self.accept_or_reject_inv(connection, False))
            # self.scrollArea_users.setWidget(frame)
            # self.scrollArea_users.setWidget(self.scrollAreaWidgetContents)

    def accept_or_reject_inv(self, connection: 'Connection', action):
        if action:
            res = connection.accept_request()
            if res['status']:
                Notification.notify(
                    user_id=connection.user_caller_id,
                    type_id=connection.id,
                    type='Connection',
                    time=datetime.datetime.now(),
                    event='Connect accepted'
                )
        else:
            res = connection.delete()

    def connect(self, user):
        # TODO: check if user send connect request before
        kwargs = {
            'user_caller_id': self.data.get('user').id,
            'user_invited_id': user
        }
        res = Connection.connect_request(**kwargs)
        if res.get('status'):
            res = Connection.find(**kwargs)
            if res.get('status'):
                Notification.notify(user_id=user,
                                    type_id=res.get('connections')[-1].id,
                                    type='Connection',
                                    time=datetime.datetime.now(),
                                    )


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     NewConnection = QtWidgets.QMainWindow()
#     ui = Ui_NewConnection()
#     ui.setupUi(NewConnection)
#     NewConnection.show()
#     sys.exit(app.exec_())

ui = Ui_NewConnection()
