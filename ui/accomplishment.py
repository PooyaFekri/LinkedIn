import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Accomplishment as AC_Class


class Ui_Accomplishment(object):
    def setupUi(self, Accomplishment, data):
        self.data = data
        Accomplishment.setObjectName("Accomplishment")
        Accomplishment.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(Accomplishment)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_add_accom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_add_accom.setObjectName("lineEdit_add_accom")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_add_accom)
        self.Add_Accomplish = QtWidgets.QPushButton(self.centralwidget)
        self.Add_Accomplish.setObjectName("Add_Accomplish")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Add_Accomplish)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        # self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        # self.commandLinkButton.setObjectName("commandLinkButton")
        # self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.commandLinkButton)
        self.lineEdit_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_delete.setObjectName("lineEdit_delete")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_delete)
        self.lineEdit_prev_acc_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_prev_acc_edit.setObjectName("lineEdit_prev_acc_edit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_prev_acc_edit)
        self.delete_accomplish = QtWidgets.QPushButton(self.centralwidget)
        self.delete_accomplish.setObjectName("delete_accomplish")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.delete_accomplish)
        self.edit_accomplish = QtWidgets.QPushButton(self.centralwidget)
        self.edit_accomplish.setObjectName("edit_accomplish")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.edit_accomplish)
        self.lineEdit_new_acc_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new_acc_edit.setObjectName("lineEdit_new_acc_edit")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_new_acc_edit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_for_error = QtWidgets.QLabel(self.centralwidget)
        self.label_for_error.setObjectName("label_for_error")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.label_for_error)
        self.pushButton_see_profile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_see_profile.setObjectName("pushButton_see_profile")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.pushButton_see_profile)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        Accomplishment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Accomplishment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        Accomplishment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Accomplishment)
        self.statusbar.setObjectName("statusbar")
        Accomplishment.setStatusBar(self.statusbar)
        self.retranslateUi(Accomplishment)

        self.set_accomplishment()
        self.Add_Accomplish.clicked.connect(lambda: self.add_accomplishment(Accomplishment))
        self.delete_accomplish.clicked.connect(lambda: self.delete_accomplishment())
        self.edit_accomplish.clicked.connect(lambda: self.edit_accomplishment())
        from .profile_me import ui as ui_me
        self.pushButton_see_profile.clicked.connect(lambda: ui_me.setupUi(Accomplishment, self.data))
        # from .profile_me import ui as ui_me
        # self.commandLinkButton.clicked.connect(lambda: ui_me.setupUi(Accomplishment, self.data))

        QtCore.QMetaObject.connectSlotsByName(Accomplishment)

    def retranslateUi(self, Accomplishment):
        _translate = QtCore.QCoreApplication.translate
        Accomplishment.setWindowTitle(_translate("Accomplishment", "MainWindow"))
        self.Add_Accomplish.setText(_translate("Accomplishment", "Add"))
        self.label_2.setText(_translate("Accomplishment", "Previous Accomplishments: "))
        # self.commandLinkButton.setText(_translate("Accomplishment", "Back"))
        self.delete_accomplish.setText(_translate("Accomplishment", "Delete"))
        self.edit_accomplish.setText(_translate("Accomplishment", "Edit"))
        self.label_3.setText(_translate("Accomplishment", "Delete Accomplishment"))
        self.label.setText(_translate("Accomplishment", "Add New Accomplishment: "))
        self.label_4.setText(_translate("Accomplishment", "Edit Accomplishment:"))
        self.label_5.setText(_translate("Accomplishment", "Previous Accomplishment Text:"))
        self.label_6.setText(_translate("Accomplishment", "New Accomplishment Text:"))
        self.label_for_error.setText(_translate("Accomplishment", "Text Error:"))
        self.pushButton_see_profile.setText(_translate("Accomplishment", "See Profile"))
        self.label_7.setText(_translate("Accomplishment", "Date:"))

    def set_accomplishment(self):
        accomplishments = AC_Class.get_accomplishments_by_user_id(self.data.get('user').id).get('accomplishments')
        str = ''
        for a in accomplishments:
            str += f'{a.title}  \n\t accomplishment time:{a.accomplishment_time}\n\n'

        self.textBrowser.setText(str)

    def add_accomplishment(self, Accomplishment):
        vars = {
            'user_id': self.data.get('user').id,
            'title': self.lineEdit_add_accom.text(),
            'accomplishment_time': self.dateEdit.dateTime().toPyDateTime(),
            'time': datetime.datetime.now()
        }

        res = AC_Class.create(**vars)
        if res['status']:
            self.set_accomplishment()
        else:
            self.label_for_error.setText(res['error'])

    def delete_accomplishment(self):
        accoms = AC_Class.find({'title': self.lineEdit_delete.text()})
        for acc in accoms:
            acc.delete()
        self.set_accomplishment()

    def edit_accomplishment(self):
        accoms = AC_Class.find({'title': self.lineEdit_prev_acc_edit.text()})
        for acc in accoms:
            acc.update(**{
                'title': self.lineEdit_new_acc_edit.text()
            })
        self.set_accomplishment()


ui = Ui_Accomplishment()
