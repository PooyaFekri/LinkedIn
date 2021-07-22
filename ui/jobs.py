# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jobs.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Experience


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data,exprince,counter = 0):
        MainWindow.setObjectName("MainWindow")
        self.counter = counter
        MainWindow.resize(600, 600)
        self.data = data
        self.exprince = exprince

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_exprince = QtWidgets.QTextBrowser(self.centralwidget)
        self.show_exprince.setObjectName("show_exprince")
        self.verticalLayout.addWidget(self.show_exprince)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout.addWidget(self.nextButton)
        self.BeforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeButton.setObjectName("BeforeButton")
        self.verticalLayout.addWidget(self.BeforeButton)
        self.Back_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Back_button.setObjectName("Back_button")
        self.verticalLayout.addWidget(self.Back_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        from .home import ui as ui_home
        self.exprince = None
        self.retranslateUi(MainWindow)
        self.Back_button.clicked.connect(lambda : ui_home.setupUi(MainWindow,self.data))
        self.nextButton.clicked.connect(lambda : self.next(MainWindow))
        self.BeforeButton.clicked.connect(lambda : self.before(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "next exprince"))
        self.BeforeButton.setText(_translate("MainWindow", "Before exprince"))
        self.Back_button.setText(_translate("MainWindow", "Back"))
        if self.exprince:
            self.show_exprince.setText(self.exprince[self.counter])

    def next(self,MainWindow):
        if self.exprince and len(self.exprince) > self.counter+1:
          ui.setupUi(MainWindow,self.data,self.exprince,self.counter+1)

    def before(self,MainWindow):
        if self.counter > 0 :
            ui.setupUi(MainWindow,self.data,self.exprince,self.counter-1)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()