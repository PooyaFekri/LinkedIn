# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enter_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EnterProfile(object):
    def setupUi(self, EnterProfile):
        EnterProfile.setObjectName("EnterProfile")
        EnterProfile.resize(600, 600)
        EnterProfile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtWidgets.QVBoxLayout(EnterProfile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(EnterProfile)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_firstName = QtWidgets.QLineEdit(EnterProfile)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.verticalLayout.addWidget(self.lineEdit_firstName)
        self.label_2 = QtWidgets.QLabel(EnterProfile)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_lastName = QtWidgets.QLineEdit(EnterProfile)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.verticalLayout.addWidget(self.lineEdit_lastName)
        self.label_3 = QtWidgets.QLabel(EnterProfile)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_telNum = QtWidgets.QLineEdit(EnterProfile)
        self.lineEdit_telNum.setObjectName("lineEdit_telNum")
        self.verticalLayout.addWidget(self.lineEdit_telNum)
        self.label_4 = QtWidgets.QLabel(EnterProfile)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_emailAdd = QtWidgets.QLineEdit(EnterProfile)
        self.lineEdit_emailAdd.setObjectName("lineEdit_emailAdd")
        self.verticalLayout.addWidget(self.lineEdit_emailAdd)
        self.label_6 = QtWidgets.QLabel(EnterProfile)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.dateEdit_birthday = QtWidgets.QDateEdit(EnterProfile)
        self.dateEdit_birthday.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateEdit_birthday.setKeyboardTracking(True)
        self.dateEdit_birthday.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_birthday.setObjectName("dateEdit_birthday")
        self.verticalLayout.addWidget(self.dateEdit_birthday)
        self.next_Button = QtWidgets.QPushButton(EnterProfile)
        self.next_Button.setObjectName("next_Button")
        self.verticalLayout.addWidget(self.next_Button)
        self.back_Button = QtWidgets.QCommandLinkButton(EnterProfile)
        self.back_Button.setObjectName("back_Button")
        self.verticalLayout.addWidget(self.back_Button)

        self.retranslateUi(EnterProfile)
        QtCore.QMetaObject.connectSlotsByName(EnterProfile)

    def retranslateUi(self, EnterProfile):
        _translate = QtCore.QCoreApplication.translate
        EnterProfile.setWindowTitle(_translate("EnterProfile", "Form"))
        self.label.setText(_translate("EnterProfile", "First name :"))
        self.label_2.setText(_translate("EnterProfile", "Last name :"))
        self.label_3.setText(_translate("EnterProfile", "Telephone number :"))
        self.label_4.setText(_translate("EnterProfile", "Email Address:"))
        self.label_6.setText(_translate("EnterProfile", "Birthday:"))
        self.next_Button.setText(_translate("EnterProfile", "Next"))
        self.back_Button.setText(_translate("EnterProfile", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterProfile = QtWidgets.QWidget()
    ui = Ui_EnterProfile()
    ui.setupUi(EnterProfile)
    EnterProfile.show()
    sys.exit(app.exec_())
