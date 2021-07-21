from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection, User


class Ui_SeeConnections(object):
    def setupUi(self, SeeConnections, data):
        self.data = data
        SeeConnections.setObjectName("SeeConnections")
        SeeConnections.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(SeeConnections)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_location = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.verticalLayout.addWidget(self.lineEdit_location)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_profileLanguage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_profileLanguage.setObjectName("lineEdit_profileLanguage")
        self.verticalLayout.addWidget(self.lineEdit_profileLanguage)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_currentCompany = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_currentCompany.setObjectName("lineEdit_currentCompany")
        self.verticalLayout.addWidget(self.lineEdit_currentCompany)
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setObjectName("SearchButton")
        self.verticalLayout.addWidget(self.SearchButton)
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout.addWidget(self.BackButton)
        SeeConnections.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SeeConnections)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        SeeConnections.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SeeConnections)
        self.statusbar.setObjectName("statusbar")
        SeeConnections.setStatusBar(self.statusbar)

        self.retranslateUi(SeeConnections)
        from .network import ui as ui_network
        self.BackButton.clicked.connect(lambda: ui_network.setupUi(SeeConnections, self.data))
        self.SearchButton.clicked.connect(lambda: self.search())

        QtCore.QMetaObject.connectSlotsByName(SeeConnections)

    def retranslateUi(self, SeeConnections):
        _translate = QtCore.QCoreApplication.translate
        SeeConnections.setWindowTitle(_translate("SeeConnections", "MainWindow"))
        self.label.setText(_translate("SeeConnections", "Connections"))
        self.label_2.setText(_translate("SeeConnections", "Search By Username"))
        self.label_4.setText(_translate("SeeConnections", "Search By Location"))
        self.label_5.setText(_translate("SeeConnections", "Search By Profile Language"))
        self.label_6.setText(_translate("SeeConnections", "Search By Current Company"))
        self.SearchButton.setText(_translate("SeeConnections", "Search"))
        self.BackButton.setText(_translate("SeeConnections", "Back"))

    def search(self):
        user_id = self.data.get('user').id
        variables = {
            'user_id': user_id,
            'username': self.lineEdit_username.text(),
            'location': self.lineEdit_location.text(),
            'language': self.lineEdit_profileLanguage.text(),
            'experience': self.lineEdit_currentCompany.text()
        }
        connections = Connection.search_connection(**variables).get('connections')
        users = []
        for connection in connections:
            connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
            user = User.find_via_pk(connect_user_id)
            users.append(user)


ui = Ui_SeeConnections()
