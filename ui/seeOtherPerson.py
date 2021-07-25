from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection, Language, Skill, Endorse, Post
from tables.notification import Notification


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
        self.acc_button = QtWidgets.QPushButton(self.centralwidget)
        self.acc_button.setObjectName("acc_button")
        self.verticalLayout.addWidget(self.acc_button)
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
        from .SeeOtherAccom import ui as ui_other_accom
        self.acc_button.clicked.connect(lambda: ui_other_accom.setupUi(MainWindow, self.data, self.user))
        self.Back.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))
        self.nextPage_Button.clicked.connect(lambda : self.other_featured(MainWindow))
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
        self.acc_button.setText(_translate("MainWindow", "Accomplishments"))
        self.label_2.setText(_translate("MainWindow", "Intro :"))
        self.label_4.setText(_translate("MainWindow", "about:"))
        self.connect_checkBox.setText(_translate("MainWindow", "Connect"))
        self.nextPage_Button.setText(_translate("MainWindow", "next page"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.Name.setText(user.first_name + " " + user.last_name)
        self.Username.setText(user.username)
        language_support = Language.find_user_lang(user.id)
        self.textBrowser_intro.setText(user.intro)
        self.notif_seePerson()
        if self.skill != []:
             # endors = Endorse.find_user_endorses()
             who_enodors = ""
             self.lineEdit.setText(self.skill[self.skill_number].text+" ("+who_enodors+" )")
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
        user_id = self.data.get("user").id
        time = datetime.now()

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

                endors = Endorse.find(data)
                event = self.data.get("user").username + "endorse your "+self.skill[self.skill_number].text
                _data = {"user_id": self.user.id, "time": time, "event": event, "type": "Endorse",
                         'type_id': user_id}
                res = Notification.notify(**_data)


            else:
                find_endors.delete()

    def notif_seePerson(self):

        user_id = self.data.get("user").id
        time = datetime.now()
        event = self.data.get("user").username + "see your profile:"
        _data = {"user_id": self.user.id, "time": time, "event": event, "type": "User",
                 'type_id': user_id}
        res = Notification.notify(**_data)

    def other_featured(self, MainWindow):

        other_post = Post.get_post_by_user_id(self.user.id).get("posts")
        from .featured_of_other import ui as ui_featured

        ui_featured.setupUi(MainWindow,self.data,other_post)


ui = Ui_MainWindow()
