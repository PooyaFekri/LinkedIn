from PyQt5 import QtCore, QtGui, QtWidgets
from .newConnection_invitation import ui as ui_newConnection
from .SeeConnections import ui as ui_seeConnection
from .PeopleMayKnow import ui as ui_may_know


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data):
        self.data = data
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.newConnection = QtWidgets.QPushButton(self.centralwidget)
        self.newConnection.setGeometry(QtCore.QRect(10, 0, 582, 25))
        self.newConnection.setObjectName("newConnection")
        self.back_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 510, 582, 36))
        self.back_button.setObjectName("back_button")
        self.connections = QtWidgets.QPushButton(self.centralwidget)
        self.connections.setGeometry(QtCore.QRect(10, 29, 582, 25))
        self.connections.setObjectName("connections")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.MayKnow = QtWidgets.QPushButton(self.centralwidget)
        self.MayKnow.setGeometry(QtCore.QRect(10, 60, 582, 25))
        self.MayKnow.setObjectName("MayKnow")
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
        self.back_button.clicked.connect(lambda: ui_home.setupUi(MainWindow, self.data))
        self.newConnection.clicked.connect(lambda: ui_newConnection.setupUi(MainWindow, self.data))
        self.connections.clicked.connect(lambda: ui_seeConnection.setupUi(MainWindow, self.data))
        self.MayKnow.clicked.connect(lambda: self.you_may_know(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newConnection.setText(_translate("MainWindow", "New Connection"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.connections.setText(_translate("MainWindow", "Connections"))
        self.MayKnow.setText(_translate("MainWindow", "People You May Know"))

    def you_may_know(self, MainWindow):
        res = self.data.get('user').people_user_may_know().get('users')
        page = {
            'users': res
        }
        if len(res) > 0:
            ui_may_know.setupUi(MainWindow, self.data, page)



ui = Ui_MainWindow()
