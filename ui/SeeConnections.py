from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection


class Ui_SeeConnections(object):
    def setupUi(self, SeeConnections, data):
        SeeConnections.setObjectName("SeeConnections")
        SeeConnections.resize(600, 600)
        self.data = data
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 224))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 561, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.numberMututalConnection = QtWidgets.QLabel(self.frame_2)
        self.numberMututalConnection.setGeometry(QtCore.QRect(300, 50, 251, 21))
        self.numberMututalConnection.setObjectName("numberMututalConnection")
        self.MessageButton = QtWidgets.QPushButton(self.frame_2)
        self.MessageButton.setGeometry(QtCore.QRect(20, 80, 91, 23))
        self.MessageButton.setObjectName("MessageButton")
        self.SeeProfile = QtWidgets.QPushButton(self.frame_2)
        self.SeeProfile.setGeometry(QtCore.QRect(10, 10, 281, 61))
        self.SeeProfile.setObjectName("SeeProfile")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(290, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.UserName = QtWidgets.QLabel(self.frame_2)
        self.UserName.setGeometry(QtCore.QRect(370, 20, 181, 20))
        self.UserName.setObjectName("UserName")
        self.ShareFrom = QtWidgets.QLabel(self.frame_2)
        self.ShareFrom.setGeometry(QtCore.QRect(106, 160, 301, 20))
        self.ShareFrom.setText("")
        self.ShareFrom.setObjectName("ShareFrom")
        self.DisconnectButton = QtWidgets.QPushButton(self.frame_2)
        self.DisconnectButton.setGeometry(QtCore.QRect(140, 80, 89, 25))
        self.DisconnectButton.setObjectName("DisconnectButton")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
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
        self.BackButton.clicked.connect(lambda : ui_network.setupUi(SeeConnections,data))
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
        self.numberMututalConnection.setText(_translate("SeeConnections", "numberMututalConnection"))
        self.MessageButton.setText(_translate("SeeConnections", "Message"))
        self.SeeProfile.setText(_translate("SeeConnections", "see profile"))
        self.label_3.setText(_translate("SeeConnections", "Username:"))
        self.UserName.setText(_translate("SeeConnections", "User name "))
        self.DisconnectButton.setText(_translate("SeeConnections", "Disconnect"))
        self.BackButton.setText(_translate("SeeConnections", "Back"))

    def search(self):
        __filter1 = {
            'user_caller_id': self.data.get('user').id,

        }
        __filter2 = {
            'user_invited_id': self.data.get('user').id,

        }
        Connection.find()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     SeeConnections = QtWidgets.QMainWindow()
#     ui = Ui_SeeConnections()
#     ui.setupUi(SeeConnections)
#     SeeConnections.show()
#     sys.exit(app.exec_())

ui = Ui_SeeConnections()
