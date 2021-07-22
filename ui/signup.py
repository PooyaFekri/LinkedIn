from PyQt5 import QtCore, QtGui, QtWidgets
from utils.validate_input import ValidateInput
from tables import User

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 10, 571, 531))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.verticalLayout.addWidget(self.lineEdit_firstName)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.verticalLayout.addWidget(self.lineEdit_lastName)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.lineEdit_email = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.verticalLayout.addWidget(self.lineEdit_email)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.verticalLayout.addWidget(self.lineEdit_confirm_password)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout.addWidget(self.dateEdit)
        self.sign_up_button = QtWidgets.QPushButton(self.layoutWidget)
        self.sign_up_button.setObjectName("sign_up_button")
        self.verticalLayout.addWidget(self.sign_up_button)
        self.back_button = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.sign_up_button.clicked.connect(lambda: self.signup(MainWindow))
        from .login import ui as ui_login
        self.back_button.clicked.connect(lambda: ui_login.setupUi(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "First Name:"))
        self.label_7.setText(_translate("MainWindow", "Last Name:"))
        self.label_8.setText(_translate("MainWindow", "Email:"))
        self.label_3.setText(_translate("MainWindow", "Username :"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.label_5.setText(_translate("MainWindow", "Confirm password :"))
        self.label_9.setText(_translate("MainWindow", "Date:"))
        self.sign_up_button.setText(_translate("MainWindow", "Sign Up "))
        self.back_button.setText(_translate("MainWindow", "Back"))

    def signup(self, MainWindow):
        variables = {
            "first_name": self.lineEdit_firstName.text(),
            "last_name": self.lineEdit_lastName.text(),
            "email": self.lineEdit_email.text(),
            "username": self.lineEdit_username.text(),
            "password": self.lineEdit_password.text(),
            "birthday": self.dateEdit.dateTime().toPyDateTime()
        }
        from .login import ui as ui_login
        conf_password= self.lineEdit_confirm_password.text()
        # TODO : validate inputs
        if ValidateInput.is_empty(*list(variables.values())):
            # TODO : send response if the boxs are empty
            pass
        elif variables["password"] != conf_password:
            # TODO
            pass
        else:
            res = User.signup(**variables)
            print("dsd")
            print(res)
            if res["status"]:
                from .home import ui as ui_home
                print("dsd")
                ui_login.setupUi(MainWindow)
                print("dsd")



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
