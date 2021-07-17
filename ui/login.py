from PyQt5 import QtCore, QtGui, QtWidgets
from .home import ui as ui_home
from .confirm_password import ui as ui_confirm_password
from .forget_password import ui as ui_forget_password

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.setWindowModality(QtCore.Qt.ApplicationModal)
        login.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.username_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_edit.setText("")
        self.username_edit.setObjectName("username_edit")
        self.verticalLayout.addWidget(self.username_edit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.password_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_edit.setText("")
        self.password_edit.setObjectName("password_edit")
        self.verticalLayout.addWidget(self.password_edit)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setObjectName("login_button")
        self.verticalLayout_2.addWidget(self.login_button)
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setObjectName("signup_button")
        self.verticalLayout_2.addWidget(self.signup_button)
        self.forget_password_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.forget_password_button.setObjectName("forget_password_button")
        self.verticalLayout_2.addWidget(self.forget_password_button)
        self.Error_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.Error_textBrowser.setObjectName("Error_textBrowser")
        self.verticalLayout_2.addWidget(self.Error_textBrowser)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)

        self.login_button.clicked.connect(lambda : (print('here'), ui_home.setupUi(login)))
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.label.setText(_translate("login", "UserName :"))
        self.label_2.setText(_translate("login", " Password :"))
        self.login_button.setText(_translate("login", "Login"))
        self.signup_button.setText(_translate("login", "sign up"))
        self.forget_password_button.setText(_translate("login", "forget password"))

def lunch_app():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui.setupUi(login)
    # ui_confirm_password.setupUi(login)
    login.show()
    sys.exit(app.exec_())

ui = Ui_login()
