# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nofi.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
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

        self.retranslateUi(MainWindow)
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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
