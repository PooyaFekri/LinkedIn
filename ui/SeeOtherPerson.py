# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeeOtherPerson.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Language, connection, Connection


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data,user):
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
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 613, 68))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setGeometry(QtCore.QRect(10, 19, 591, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.EnrolSkill = QtWidgets.QPushButton(self.frame)
        self.EnrolSkill.setGeometry(QtCore.QRect(10, 50, 571, 20))
        self.EnrolSkill.setObjectName("EnrolSkill")
        self.lineEdit_skill = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_skill.setGeometry(QtCore.QRect(10, 10, 571, 20))
        self.lineEdit_skill.setObjectName("lineEdit_skill")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
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
        self.languages_fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
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

        self.retranslateUi(MainWindow,data,user)
        from .home import ui as ui_home
        # self.Back.clicked.connect(lambda :ui_home.setupUi(MainWindow,data))
        self.Back.clicked.connect(lambda : self.back_home(MainWindow,data,user))
        # self.connect_checkBox.clicked.connect(lambda : self.connect_or_disconnect())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow,data,user):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "userName:"))
        self.Username.setText(user.username)
        self.Username.setText(_translate("MainWindow", "userName"))
        self.label_3.setText(_translate("MainWindow", "name:"))
        self.Name.setText(user.first_name+" "+user.last_name)
        self.Name.setText(_translate("MainWindow", "first name + last name"))
        self.label_5.setText(_translate("MainWindow", "skill:"))
        self.EnrolSkill.setText(_translate("MainWindow", "Enrol Skill"))
        self.label_2.setText(_translate("MainWindow", "Intro :"))
        self.textBrowser_intro.setText(user.intro)
        self.label_4.setText(_translate("MainWindow", "about:"))
        # self.textBrowser_about.setText(user.about)
        language_support = Language.find_user_lang(user.id)
        #todo check this after
        if Connection.is_connected(data['user_id'],user.id):
            self.connect_checkBox.mask()
        if language_support['status']:
            for k in language_support['languages']:
                self.languages_fontComboBox.addItem(k)
        else:
            print(language_support['error'])
        #todo check this after
        self.connect_checkBox.setText(_translate("MainWindow", "Connect"))

        self.nextPage_Button.setText(_translate("MainWindow", "next page"))
        self.Back.setText(_translate("MainWindow", "Back"))

    def connect_or_disconnect(self,data,usr):

        if self.connect_checkBox.isTristate():
            pass
        else:
            if Connection.is_connected(data.get('user').id,usr.id):
                pass
    def back_home(self,MainWindow,data, user):

        from .home import ui as ui_home

        self.connect_or_disconnect(data,user)
        ui_home.setupUi(MainWindow,data)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
