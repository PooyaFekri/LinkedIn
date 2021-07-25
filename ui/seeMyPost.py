# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seePost.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Post


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data,mypost,counter=0):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.data = data
        self.counter = counter
        self.is_featured = False
        self.myPost = mypost
        # Post.get_post_by_user_id(self.data.get("user").id).get("posts")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser_see_post = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_see_post.setObjectName("textBrowser_see_post")
        self.verticalLayout.addWidget(self.textBrowser_see_post)
        self.checkBox_Featured = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Featured.setObjectName("checkBox_Featured")
        self.verticalLayout.addWidget(self.checkBox_Featured)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout.addWidget(self.NextButton)
        self.BeforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeButton.setObjectName("BeforeButton")
        self.verticalLayout.addWidget(self.BeforeButton)
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setObjectName("home")
        self.verticalLayout.addWidget(self.home)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        from .home import ui as ui_home
        self.home.clicked.connect(lambda: ui_home.setupUi(MainWindow, self.data))
        if self.myPost:
            self.NextButton.clicked.connect(lambda : self.nextPage(MainWindow))
            self.BeforeButton.clicked.connect(lambda : self.beforeBage(MainWindow))
            self.checkBox_Featured.clicked.connect(lambda : self.featured())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_Featured.setText(_translate("MainWindow", "‫‪Featured‬‬ ‫‪"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.BeforeButton.setText(_translate("MainWindow", "Before"))
        self.home.setText(_translate("MainWindow", "Home"))
        if self.myPost:
            self.textBrowser_see_post.setText(self.myPost[self.counter].text)
            self.is_featured = self.myPost[self.counter].is_featured
            if self.is_featured:
                self.checkBox_Featured.click()


    def nextPage(self,MainWindow):

        if self.counter+1  < len(self.myPost):
            ui.setupUi(MainWindow,self.data,self.myPost,self.counter+1)

    def beforeBage(self,MainWindow):

        if self.counter > 0 :
            ui.setupUi(MainWindow,self.data,self.myPost,self.counter-1)

    def featured(self):

        self.is_featured = not self.featured()

        self.myPost[self.counter].change_featured(self.is_featured)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()
