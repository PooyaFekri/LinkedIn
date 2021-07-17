from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConfirmPassword(object):
    def setupUi(self, ConfirmPassword):
        ConfirmPassword.setObjectName("ConfirmPassword")
        ConfirmPassword.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfirmPassword)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(ConfirmPassword)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_username = QtWidgets.QLineEdit(ConfirmPassword)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.verticalLayout.addWidget(self.lineEdit_username)
        self.label_4 = QtWidgets.QLabel(ConfirmPassword)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_password = QtWidgets.QLineEdit(ConfirmPassword)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout.addWidget(self.lineEdit_password)
        self.label_5 = QtWidgets.QLabel(ConfirmPassword)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_confirm_password = QtWidgets.QLineEdit(ConfirmPassword)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")
        self.verticalLayout.addWidget(self.lineEdit_confirm_password)
        self.sign_up_button = QtWidgets.QPushButton(ConfirmPassword)
        self.sign_up_button.setObjectName("sign_up_button")
        self.verticalLayout.addWidget(self.sign_up_button)
        self.back_button = QtWidgets.QCommandLinkButton(ConfirmPassword)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button)

        self.retranslateUi(ConfirmPassword)
        QtCore.QMetaObject.connectSlotsByName(ConfirmPassword)

    def retranslateUi(self, ConfirmPassword):
        _translate = QtCore.QCoreApplication.translate
        ConfirmPassword.setWindowTitle(_translate("ConfirmPassword", "Form"))
        self.label_3.setText(_translate("ConfirmPassword", "Username :"))
        self.label_4.setText(_translate("ConfirmPassword", "Password :"))
        self.label_5.setText(_translate("ConfirmPassword", "Confirm password :"))
        self.sign_up_button.setText(_translate("ConfirmPassword", "Sign Up "))
        self.back_button.setText(_translate("ConfirmPassword", "Back"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Network = QtWidgets.QWidget()
#     ui = Ui_ConfirmPassword()
#     ui.setupUi(Network)
#     Network.show()
#     sys.exit(app.exec_())


ui = Ui_ConfirmPassword()
