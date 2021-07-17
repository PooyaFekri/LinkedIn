from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgetPassword(object):
    def setupUi(self, ForgetPassword):
        ForgetPassword.setObjectName("ForgetPassword")
        ForgetPassword.resize(600, 600)
        self.label = QtWidgets.QLabel(ForgetPassword)
        self.label.setGeometry(QtCore.QRect(90, 93, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ForgetPassword)
        self.label_2.setGeometry(QtCore.QRect(90, 173, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ForgetPassword)
        self.label_3.setGeometry(QtCore.QRect(100, 250, 47, 13))
        self.label_3.setObjectName("label_3")
        self.UserName = QtWidgets.QLineEdit(ForgetPassword)
        self.UserName.setGeometry(QtCore.QRect(140, 129, 281, 21))
        self.UserName.setObjectName("UserName")
        self.NewPassword = QtWidgets.QLineEdit(ForgetPassword)
        self.NewPassword.setGeometry(QtCore.QRect(140, 210, 281, 21))
        self.NewPassword.setObjectName("NewPassword")
        self.Email = QtWidgets.QLineEdit(ForgetPassword)
        self.Email.setGeometry(QtCore.QRect(140, 280, 281, 21))
        self.Email.setObjectName("Email")
        self.ButtonSend = QtWidgets.QPushButton(ForgetPassword)
        self.ButtonSend.setGeometry(QtCore.QRect(260, 370, 75, 23))
        self.ButtonSend.setObjectName("ButtonSend")

        self.retranslateUi(ForgetPassword)
        QtCore.QMetaObject.connectSlotsByName(ForgetPassword)

    def retranslateUi(self, ForgetPassword):
        _translate = QtCore.QCoreApplication.translate
        ForgetPassword.setWindowTitle(_translate("ForgetPassword", "Form"))
        self.label.setText(_translate("ForgetPassword", "User name :"))
        self.label_2.setText(_translate("ForgetPassword", "NewPassword:"))
        self.label_3.setText(_translate("ForgetPassword", "Email :"))
        self.ButtonSend.setText(_translate("ForgetPassword", "Send"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ForgetPassword = QtWidgets.QWidget()
#     ui = Ui_ForgetPassword()
#     ui.setupUi(ForgetPassword)
#     ForgetPassword.show()
#     sys.exit(app.exec_())

ui = Ui_ForgetPassword()
