from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

from .next_page_of_edite_person import ui as ui_next_page


def make_date(birthday):
    print(birthday)
    time = birthday.split()[0].split('-')
    return QDate(int(time[0]),int(time[1]),int(time[2]))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 645)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit_birthday = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_birthday.setGeometry(QtCore.QRect(0, 216, 584, 26))
        self.dateEdit_birthday.setObjectName("dateEdit_birthday")
        self.lineEdit_firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_firstName.setGeometry(QtCore.QRect(0, 41, 584, 25))
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.lineEdit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(0, 334, 584, 25))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_address.setGeometry(QtCore.QRect(0, 451, 584, 25))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.intro = QtWidgets.QLabel(self.centralwidget)
        self.intro.setGeometry(QtCore.QRect(0, 131, 584, 21))
        self.intro.setObjectName("intro")
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(0, 540, 584, 25))
        self.back_button.setObjectName("back_button")
        self.lineEdit_telNum = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_telNum.setGeometry(QtCore.QRect(0, 509, 584, 25))
        self.lineEdit_telNum.setObjectName("lineEdit_telNum")
        self.lastName = QtWidgets.QLabel(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(0, 72, 584, 22))
        self.lastName.setObjectName("lastName")
        self.address = QtWidgets.QLabel(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(0, 423, 584, 22))
        self.address.setObjectName("address")
        self.birthday = QtWidgets.QLabel(self.centralwidget)
        self.birthday.setGeometry(QtCore.QRect(0, 189, 584, 21))
        self.birthday.setObjectName("birthday")
        self.firstName = QtWidgets.QLabel(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(0, 14, 584, 21))
        self.firstName.setObjectName("firstName")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(0, 307, 584, 21))
        self.password.setObjectName("password")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(0, 392, 584, 25))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(0, 365, 584, 21))
        self.email.setObjectName("email")
        self.telNum = QtWidgets.QLabel(self.centralwidget)
        self.telNum.setGeometry(QtCore.QRect(0, 482, 584, 21))
        self.telNum.setObjectName("telNum")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(0, 276, 584, 25))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_intro = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_intro.setGeometry(QtCore.QRect(0, 158, 584, 25))
        self.lineEdit_intro.setObjectName("lineEdit_intro")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(0, 571, 584, 25))
        self.submit_button.setObjectName("submit_button")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(0, 248, 584, 22))
        self.username.setObjectName("username")
        self.lineEdit_lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_lastName.setGeometry(QtCore.QRect(0, 100, 584, 25))
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        from .profile_me import ui as ui_profile_me
        # print(data)
        self.retranslateUi(MainWindow,data["user"])
        self.back_button.clicked.connect(lambda: ui_profile_me.setupUi(MainWindow, data))
        self.submit_button.clicked.connect(lambda: self.submit(MainWindow, data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def submit(self, MainWindow, data):
        user = data.get("user")
        dict = {}
        if self.lineEdit_intro.text() != "":
            user.intro = self.lineEdit_intro.text()
            dict["intro"] = user.intro
        if self.lineEdit_email.text() != "":
            user.email = self.lineEdit_email.text()
            dict["email"] = user.email
        if self.lineEdit_address.text() != "":
            user.address = self.lineEdit_address.text()
        if self.lineEdit_password.text() != "":
            dict["password"] = self.lineEdit_password.text()
        if self.lineEdit_address.text() != "":
            user.nationality = self.lineEdit_address.text()
            dict["nationality"] = user.nationality
        if self.lineEdit_firstName.text() != "":
            user.first_name = self.lineEdit_firstName.text()
            dict["first_name"] = user.first_name
        if self.lineEdit_lastName.text() != "":
            user.last_name = self.lineEdit_lastName.text()
            dict["last_name"] = user.last_name

        if self.lineEdit_telNum.text() != "":
            user.tel_num = self.lineEdit_telNum.text()
            dict["tel num"] = user.tel_num

        if self.dateEdit_birthday.dateTime().currentDateTime().toPyDateTime() != user.birthday:
            # print(self.dateEdit_birthday.dateTime().toPyDateTime())
            dict["birthday"] = self.dateEdit_birthday.dateTime().toPyDateTime()
            user.birthday = str(self.dateEdit_birthday.dateTime().toPyDateTime())
            # print(user.birthday)
            # print(user.birthday)
        user.update(**dict)
        ui_next_page.setupUi(MainWindow, data)
        # self.setupUi(MainWindow,data)

    def retranslateUi(self, MainWindow,user):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.intro.setText(_translate("MainWindow", "intro"))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.lastName.setText(_translate("MainWindow", "last name"))
        self.address.setText(_translate("MainWindow", "address"))
        self.birthday.setText(_translate("MainWindow", "birthday"))
        self.firstName.setText(_translate("MainWindow", "first name"))
        self.password.setText(_translate("MainWindow", "password"))
        self.email.setText(_translate("MainWindow", "email"))
        self.telNum.setText(_translate("MainWindow", "tel num"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.username.setText(_translate("MainWindow", "username"))
        # print(user.birthday)
        self.dateEdit_birthday.setDate(make_date(user.birthday))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
