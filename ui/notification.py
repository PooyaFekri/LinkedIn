# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notification.ui'
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.type = QtWidgets.QLabel(self.centralwidget)
        self.type.setText("")
        self.type.setObjectName("type")
        self.verticalLayout.addWidget(self.type)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.see_notif = QtWidgets.QTextBrowser(self.centralwidget)
        self.see_notif.setObjectName("see_notif")
        self.verticalLayout.addWidget(self.see_notif)
        self.SeeItButton = QtWidgets.QPushButton(self.centralwidget)
        self.SeeItButton.setObjectName("SeeItButton")
        self.verticalLayout.addWidget(self.SeeItButton)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout.addWidget(self.nextButton)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setObjectName("BackButton")
        self.verticalLayout.addWidget(self.BackButton)
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout.addWidget(self.homeButton)
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
        self.label_2.setText(_translate("MainWindow", "Type :"))
        self.label.setText(_translate("MainWindow", "Notification:"))
        self.SeeItButton.setText(_translate("MainWindow", "I See it"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.BackButton.setText(_translate("MainWindow", "Back"))
        self.homeButton.setText(_translate("MainWindow", "Home"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
