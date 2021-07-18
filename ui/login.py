from PyQt5 import QtCore, QtGui, QtWidgets

from tables import User
from .forget_password import ui as ui_forgot_password
from .home import ui as ui_home
from .signup import ui as ui_signup
from utils.validate_input import ValidateInput


class Ui_MainWindow(object):
    user = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UserName_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserName_lineEdit.setGeometry(QtCore.QRect(10, 35, 582, 25))
        self.UserName_lineEdit.setObjectName("UserName_lineEdit")
        self.Password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Password_lineEdit.setGeometry(QtCore.QRect(10, 89, 582, 25))
        self.Password_lineEdit.setObjectName("Password_lineEdit")
        self.forget_password_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.forget_password_button.setGeometry(QtCore.QRect(10, 182, 582, 36))
        self.forget_password_button.setObjectName("forget_password_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 577, 582, 17))
        self.label.setText("")
        self.label.setObjectName("label")
        self.SignUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(10, 151, 582, 25))
        self.SignUpButton.setObjectName("SignUpButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 66, 582, 17))
        self.label_3.setObjectName("label_3")
        self.UserName_libale = QtWidgets.QLabel(self.centralwidget)
        self.UserName_libale.setGeometry(QtCore.QRect(10, 12, 582, 17))
        self.UserName_libale.setObjectName("UserName_libale")
        self.Error_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.Error_textBrowser.setGeometry(QtCore.QRect(10, 224, 582, 347))
        self.Error_textBrowser.setObjectName("Error_textBrowser")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(10, 120, 582, 25))
        self.LoginButton.setObjectName("LoginButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.LoginButton.clicked.connect(lambda: self.login(MainWindow))
        self.forget_password_button.clicked.connect(lambda: ui_forgot_password.setupUi(MainWindow))
        self.SignUpButton.clicked.connect(lambda: ui_signup.setupUi(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.forget_password_button.setText(_translate("MainWindow", "Forget password"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign up"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.UserName_libale.setText(_translate("MainWindow", "UserName"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))

    def login(self, MainWindow):
        global user
        variables = {
            "username": self.UserName_lineEdit.text(),
            "password": self.Password_lineEdit.text()
        }

        if ValidateInput.is_empty(*list(variables.values())):
            self.Error_textBrowser.setText('Your password or username is empty')
        else:
            self.Error_textBrowser.setText('')
            res = User.login(**variables)
            if res["status"]:
                data = {"user":res["user"]}
                ui_home.setupUi(MainWindow, **data)
            else:
                self.Error_textBrowser.setText(res["error"])


def lunch_app():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

ui = Ui_MainWindow()
