from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Skill, Language
from .edit_profile import ui as ui_edit_profile
from .accomplishment import ui as ui_accom


def find_skill(user):
    list_of_skill = Skill.find_user_id(user.id)
    str1 = ""
    if list_of_skill["status"]:
        for i in list_of_skill["skills"]:
            str1 += i.text + "\n"
    return str1


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Username_info = QtWidgets.QLabel(self.centralwidget)
        self.Username_info.setGeometry(QtCore.QRect(50, 60, 121, 31))
        self.Username_info.setObjectName("Username_info")
        # self.Username_info.setText()
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_4.setObjectName("label_4")
        self.FirstnameAndLastName = QtWidgets.QLabel(self.centralwidget)
        self.FirstnameAndLastName.setGeometry(QtCore.QRect(50, 123, 121, 31))
        self.FirstnameAndLastName.setObjectName("FirstnameAndLastName")
        self.Introduction = QtWidgets.QTextBrowser(self.centralwidget)
        self.Introduction.setGeometry(QtCore.QRect(350, 110, 211, 41))
        self.Introduction.setObjectName("Introduction")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.about = QtWidgets.QTextBrowser(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(350, 30, 211, 41))
        self.about.setObjectName("about")
        self.Skill = QtWidgets.QTextBrowser(self.centralwidget)
        self.Skill.setGeometry(QtCore.QRect(20, 210, 411, 351))
        self.Skill.setObjectName("Skill")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 90, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 180, 47, 13))
        self.label_7.setObjectName("label_7")
        self.EditProfile = QtWidgets.QPushButton(self.centralwidget)
        self.EditProfile.setGeometry(QtCore.QRect(440, 460, 75, 23))
        self.EditProfile.setObjectName("EditProfile")
        self.Back = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(440, 490, 185, 41))
        self.Back.setObjectName("Back")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 10, 47, 13))
        self.label_8.setObjectName("label_8")
        self.SupportLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.SupportLanguage.setGeometry(QtCore.QRect(500, 230, 69, 22))
        self.SupportLanguage.setObjectName("SupportLanguage")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 200, 121, 16))
        self.label_9.setObjectName("label_9")
        self.add_accom = QtWidgets.QPushButton(self.centralwidget)
        self.add_accom.setGeometry(QtCore.QRect(440, 420, 75, 23))
        self.add_accom.setObjectName("add_accom")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        from .home import ui as ui_home
        # print(data)
        self.retranslateUi(MainWindow, data.get("user"))
        # print(data)
        self.EditProfile.clicked.connect(lambda: ui_edit_profile.setupUi(MainWindow, data))
        self.Back.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))
        self.add_accom.clicked.connect(lambda: ui_accom.setupUi(MainWindow, data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, user):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Username_info.setText(_translate("MainWindow", user.username))
        self.label_4.setText(_translate("MainWindow", "Name :"))
        self.FirstnameAndLastName.setText(_translate("MainWindow", user.first_name + " " + user.last_name))
        self.label_6.setText(_translate("MainWindow", "Introduction:"))
        self.about.setText(user.intro)
        self.label.setText(_translate("MainWindow", "user name :"))
        self.label_7.setText(_translate("MainWindow", "skills:"))
        self.Skill.setText(find_skill(user))
        self.EditProfile.setText(_translate("MainWindow", "Edit profile"))
        self.Back.setText(_translate("MainWindow", "Back"))
        self.label_8.setText(_translate("MainWindow", "about :"))
        # self.about.setText(user.)
        self.label_9.setText(_translate("MainWindow", "support language:"))
        languages = Language.find_user_lang(user.id)
        if languages["status"]:
            for i in languages["languages"]:
                self.SupportLanguage.addItem(i.language)
        self.add_accom.setText(_translate("MainWindow", "Add Accom"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
