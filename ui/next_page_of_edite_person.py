from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Skill, Language, Experience


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.data = data
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_skill = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_skill.setObjectName("lineEdit_skill")
        self.verticalLayout.addWidget(self.lineEdit_skill)
        self.add_skill_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_skill_Button.setObjectName("add_skill_Button")
        self.verticalLayout.addWidget(self.add_skill_Button)
        self.lineEdit_delete_skill = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_delete_skill.setObjectName("lineEdit_delete_skill")
        self.verticalLayout.addWidget(self.lineEdit_delete_skill)
        self.delete_skill_Button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_skill_Button.setObjectName("delete_skill_Button")
        self.verticalLayout.addWidget(self.delete_skill_Button)
        self.lineEdit_language = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_language.setObjectName("lineEdit_language")
        self.verticalLayout.addWidget(self.lineEdit_language)
        self.add_language_Button = QtWidgets.QPushButton(self.centralwidget)
        self.add_language_Button.setObjectName("add_language_Button")
        self.verticalLayout.addWidget(self.add_language_Button)
        self.lineEdit_remove_language = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_remove_language.setObjectName("lineEdit_remove_language")
        self.verticalLayout.addWidget(self.lineEdit_remove_language)
        self.remove_language_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.remove_language_pushButton.setObjectName("remove_language_pushButton")
        self.verticalLayout.addWidget(self.remove_language_pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dateEdit_start_date = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_start_date.setObjectName("dateEdit_start_date")
        self.verticalLayout.addWidget(self.dateEdit_start_date)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dateEdit_end_date = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_end_date.setObjectName("dateEdit_end_date")
        self.verticalLayout.addWidget(self.dateEdit_end_date)
        self.lineEdit_exprince_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_exprince_name.setObjectName("lineEdit_exprince_name")
        self.verticalLayout.addWidget(self.lineEdit_exprince_name)
        self.add_exprince = QtWidgets.QPushButton(self.centralwidget)
        self.add_exprince.setObjectName("add_exprince")
        self.verticalLayout.addWidget(self.add_exprince)
        self.lineEdit_remove_exprince = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_remove_exprince.setObjectName("lineEdit_remove_exprince")
        self.verticalLayout.addWidget(self.lineEdit_remove_exprince)
        self.remove_exprince_Button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_exprince_Button.setObjectName("remove_exprince_Button")
        self.verticalLayout.addWidget(self.remove_exprince_Button)
        self.sumbit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.sumbit_pushButton.setObjectName("sumbit_pushButton")
        self.verticalLayout.addWidget(self.sumbit_pushButton)
        self.Back_LinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_LinkButton.setObjectName("Back_LinkButton")
        self.verticalLayout.addWidget(self.Back_LinkButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        from .profile_me import ui as ui_profile_me
        from .edit_profile import ui as ui_edit_profile
        self.add_skill_Button.clicked.connect(lambda : self.add_skill(self.lineEdit_skill.text()))
        self.delete_skill_Button.clicked.connect(lambda : self.delete_skill(self.lineEdit_delete_skill.text()))
        self.add_language_Button.clicked.connect(lambda : self.add_language(self.lineEdit_language.text()))
        self.remove_language_pushButton.clicked.connect(lambda : self.remove_language1(self.lineEdit_remove_language.text()))
        self.add_exprince.clicked.connect(lambda : self.add_exprince_to(self.dateEdit_start_date,self.dateEdit_end_date,self.lineEdit_exprince_name.text()))
        self.remove_language_pushButton.clicked.connect(lambda : self.remove_exprince(self.lineEdit_remove_exprince.text()))
        self.sumbit_pushButton.clicked.connect(lambda :ui_profile_me.setupUi(MainWindow,data))
        self.Back_LinkButton.clicked.connect(lambda : ui_edit_profile.setupUi(MainWindow,data))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_skill_Button.setText(_translate("MainWindow", "add skill"))
        self.delete_skill_Button.setText(_translate("MainWindow", "Delete skill"))
        self.add_language_Button.setText(_translate("MainWindow", "add language"))
        self.remove_language_pushButton.setText(_translate("MainWindow", "remove language"))
        self.label.setText(_translate("MainWindow", "Start :"))
        self.label_2.setText(_translate("MainWindow", "End :"))
        self.add_exprince.setText(_translate("MainWindow", "add exprince"))
        self.remove_exprince_Button.setText(_translate("MainWindow", "remove exprince"))
        self.sumbit_pushButton.setText(_translate("MainWindow", "Submit"))
        self.Back_LinkButton.setText(_translate("MainWindow", "back"))

    def add_skill(self, text):
        info = {"user_id":self.data["user"].id,"text":text}
        Skill.insert(**info)

    def delete_skill(self, text):

        get_core = Skill.find_user_id(self.data["user"].id)
        if get_core["status"]:
            for i in get_core["skills"]:
                if i.text == text:
                    i.delete()

    def add_language(self, text):
        info = {"user_id":self.data["user"].id,"language":text}
        Language.add(**info)

    def remove_language1(self, text):
        get_core = Language.find_user_lang(self.data["user"].id)
        if get_core["status"]:
            for i in get_core["languages"]:
                if i.language == text:
                    i.delete()

    def add_exprince_to(self, dateEdit_start_date, dateEdit_end_date, text):
        info = {"user_id":self.data["user"].id,"start_time":dateEdit_start_date.toPyDateTime(),"end_time":dateEdit_end_date.toPyDateTime(),"text":text}
        Experience.add(**info)

    def remove_exprince(self, text):
        get_core = Experience.find_user_experiences(self.data["user"].id)
        if get_core["status"]:
            for i in get_core["experiences"]:
                if i.language == text:
                    i.delete()



ui = Ui_MainWindow()



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
