# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nofi.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data,notif,counter = 0):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.data = data
        self.notif = notif
        self.cunter = counter
        self.is_see = False
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setText("")
        self.type_label.setObjectName("type_label")
        self.verticalLayout.addWidget(self.type_label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.mesage_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.mesage_textBrowser.setObjectName("mesage_textBrowser")
        self.verticalLayout.addWidget(self.mesage_textBrowser)
        self.is_see_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.is_see_checkBox.setObjectName("is_see_checkBox")
        self.verticalLayout.addWidget(self.is_see_checkBox)
        self.next_notif_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_notif_button.setObjectName("next_notif_button")
        self.verticalLayout.addWidget(self.next_notif_button)
        self.before_notif_Button = QtWidgets.QPushButton(self.centralwidget)
        self.before_notif_Button.setObjectName("before_notif_Button")
        self.verticalLayout.addWidget(self.before_notif_Button)
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout.addWidget(self.BackButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        from .home import ui as ui_home
        self.retranslateUi(MainWindow)

        self.BackButton.clicked.connect(lambda : ui_home.setupUi(MainWindow,self.data))
        if self.notif:
            self.is_see_checkBox.clicked.connect(lambda : self.click_see(MainWindow))
            self.next_notif_button.clicked.connect(lambda : self.next(MainWindow))
            self.before_notif_Button.clicked.connect(lambda : self.before(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "type :"))
        self.label_3.setText(_translate("MainWindow", "Notification:"))
        self.is_see_checkBox.setText(_translate("MainWindow", "is See"))
        self.next_notif_button.setText(_translate("MainWindow", "next"))
        self.before_notif_Button.setText(_translate("MainWindow", "before"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        if self.notif:
                self.type_label.setText(self.notif[self.cunter].type)
                self.mesage_textBrowser.setText(self.notif[self.cunter].event)
                if self.notif[self.cunter].visited:
                    self.is_see_checkBox.click()
                    self.is_see = True

    def click_see(self, MainWindow):

        if self.is_see:
            self.notif[self.cunter].visit_notification(False)
        else:
            self.notif[self.cunter].visit_notification(True)


    def next(self,MainWindow):
        if self.notif and len(self.notif) > self.notif+1:
          ui.setupUi(MainWindow,self.data,self.notif,self.cunter+1)

    def before(self,MainWindow):
        if self.notif > 0 :
            ui.setupUi(MainWindow,self.data,self.notif,self.cunter-1)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()