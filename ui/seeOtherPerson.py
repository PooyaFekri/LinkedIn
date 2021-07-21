# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeeOtherPerson2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection, Language, Skill, Endorse


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, user):
        self.data = data
        self.skill = Skill.find_user_id(user.id)['skills']
        self.skill_number = 0
        self.user = user

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Username = QtWidgets.QLabel(self.centralwidget)
        self.Username.setObjectName("Username")
        self.verticalLayout.addWidget(self.Username)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setObjectName("Name")
        self.verticalLayout.addWidget(self.Name)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout.addWidget(self.NextButton)
        self.BeforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeButton.setObjectName("BeforeButton")
        self.verticalLayout.addWidget(self.BeforeButton)
        self.enrolButton = QtWidgets.QPushButton(self.centralwidget)
        self.enrolButton.setObjectName("enrolButton")
        self.verticalLayout.addWidget(self.enrolButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textBrowser_intro = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_intro.setObjectName("textBrowser_intro")
        self.verticalLayout.addWidget(self.textBrowser_intro)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.textBrowser_about = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_about.setObjectName("textBrowser_about")
        self.verticalLayout.addWidget(self.textBrowser_about)
        self.languages_fontComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.languages_fontComboBox.setObjectName("languages_fontComboBox")
        self.verticalLayout.addWidget(self.languages_fontComboBox)
        self.connect_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.connect_checkBox.setObjectName("connect_checkBox")
        self.verticalLayout.addWidget(self.connect_checkBox)
        self.nextPage_Button = QtWidgets.QPushButton(self.centralwidget)
        self.nextPage_Button.setObjectName("nextPage_Button")
        self.verticalLayout.addWidget(self.nextPage_Button)
        self.Back = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back.setObjectName("Back")
        self.verticalLayout.addWidget(self.Back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow, user)
        from .home import ui as ui_home
        self.NextButton.clicked.connect(lambda: self.next_skill())
        self.BeforeButton.clicked.connect(lambda: self.before_skill())
        self.enrolButton.clicked.connect(lambda: self.enrol_skill())

        self.Back.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, user):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "userName:"))
        self.Username.setText(_translate("MainWindow", "userName"))
        self.label_3.setText(_translate("MainWindow", "name:"))
        self.Name.setText(_translate("MainWindow", "first name + last name"))
        self.label_5.setText(_translate("MainWindow", "skill:"))
        self.NextButton.setText(_translate("MainWindow", "Next skill"))
        self.BeforeButton.setText(_translate("MainWindow", "Before skill"))
        self.enrolButton.setText(_translate("MainWindow", "endorse or dendorse this skill"))
        self.label_2.setText(_translate("MainWindow", "Intro :"))
        self.label_4.setText(_translate("MainWindow", "about:"))
        self.connect_checkBox.setText(_translate("MainWindow", "Connect"))
        self.nextPage_Button.setText(_translate("MainWindow", "next page"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.Name.setText(user.first_name + " " + user.last_name)
        self.Username.setText(user.username)
        language_support = Language.find_user_lang(user.id)
        self.textBrowser_intro.setText(user.intro)
        if self.skill != []:
             self.lineEdit.setText(self.skill[self.skill_number].text)
        if Connection.is_connected(self.data['user'].id, user.id):
            self.connect_checkBox.mask()
        if language_support['status']:
            for k in language_support['languages']:
                self.languages_fontComboBox.addItem(k.language)
        else:
            print(language_support['error'])
        # todo check this after

    def connect_or_disconnect(self, data, usr):

        if self.connect_checkBox.isTristate():
            if not Connection.is_connected(data.get('user').id, usr.id)["status"]:
                data = {"user_caller_id": data["user"].id, "user_invited_id": usr.id}
                Connection.connect_request(**data)

        else:
            if Connection.is_connected(data.get('user').id, usr.id)["status"]:
                connection = Connection.get_connect_with_users_id(data.get('user').id, usr.id)
                connection.delete()
            elif Connection.get_connect_with_users_id(data.get("user").id, usr.id)["status"]:
                connection = Connection.get_connect_with_users_id(data.get('user').id, usr.id)
                connection.delete()

    def back_home(self, MainWindow, data, user):

        from .home import ui as ui_home

        self.connect_or_disconnect(data, user)
        ui_home.setupUi(MainWindow, data)

    def next_skill(self):

        if self.skill != [] and len(self.skill) > self.skill_number + 1:
            self.skill_number += 1
            self.lineEdit.setText(self.skill[self.skill_number].text)

    def before_skill(self):

        if self.skill != [] and self.skill_number > 0:
            self.skill_number -= 1
            self.lineEdit.setText(self.skill[self.skill_number].text)

    def enrol_skill(self):
        if self.lineEdit.text()!= None:
            this_endors = False
            endors_user = Endorse.find_user_endorses(self.user.id)
            find_endors = None
            if endors_user['status']:
                for i in endors_user['endorse']:
                    if i.user_id == self.data['user'].id and i.skill_id == self.skill[self.skill_number].id:
                        find_endors = i
                        this_endors = True

            if not this_endors:
                data = {'skill_id': self.skill[self.skill_number].id, 'user_id': self.data['user'].id}
                Endorse.create(**data)
            else:
                find_endors.delete()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()
