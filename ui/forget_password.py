from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ButtonSend = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSend.setGeometry(QtCore.QRect(280, 351, 75, 23))
        self.ButtonSend.setObjectName("ButtonSend")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(160, 261, 281, 21))
        self.Email.setObjectName("Email")
        self.NewPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.NewPassword.setGeometry(QtCore.QRect(160, 191, 281, 21))
        self.NewPassword.setObjectName("NewPassword")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 74, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 154, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 231, 47, 13))
        self.label_4.setObjectName("label_4")
        self.UserName_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.UserName_2.setGeometry(QtCore.QRect(160, 110, 281, 21))
        self.UserName_2.setObjectName("UserName_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonSend.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "User name :"))
        self.label_2.setText(_translate("MainWindow", "NewPassword:"))
        self.label_4.setText(_translate("MainWindow", "Email :"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
