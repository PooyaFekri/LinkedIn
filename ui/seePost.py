# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeePost.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection, User


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, data,counter = 0):
        data['posts'] = Connection.get_related_posts(data['user'].id)
        self.data = data
        self.counter = counter
        self.set_counter()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.UserName = QtWidgets.QLabel(self.frame)
        self.UserName.setObjectName("UserName")
        self.verticalLayout_2.addWidget(self.UserName)
        self.SeeProfile = QtWidgets.QPushButton(self.frame)
        self.SeeProfile.setObjectName("SeeProfile")
        self.verticalLayout_2.addWidget(self.SeeProfile)
        self.textBrowserOfPost = QtWidgets.QTextBrowser(self.frame)
        self.textBrowserOfPost.setObjectName("textBrowserOfPost")
        self.verticalLayout_2.addWidget(self.textBrowserOfPost)
        self.numberComment = QtWidgets.QLabel(self.frame)
        self.numberComment.setObjectName("numberComment")
        self.verticalLayout_2.addWidget(self.numberComment)
        self.CommentButton = QtWidgets.QPushButton(self.frame)
        self.CommentButton.setObjectName("CommentButton")
        self.verticalLayout_2.addWidget(self.CommentButton)
        self.ShareButton = QtWidgets.QPushButton(self.frame)
        self.ShareButton.setObjectName("ShareButton")
        self.verticalLayout_2.addWidget(self.ShareButton)
        self.LikeButton = QtWidgets.QCheckBox(self.frame)
        self.LikeButton.setObjectName("LikeButton")
        self.verticalLayout_2.addWidget(self.LikeButton)
        self.Number_of_like = QtWidgets.QLabel(self.frame)
        self.Number_of_like.setObjectName("Number_of_like")
        self.verticalLayout_2.addWidget(self.Number_of_like)
        self.ShareFrom_2 = QtWidgets.QLabel(self.frame)
        self.ShareFrom_2.setObjectName("ShareFrom_2")
        self.verticalLayout_2.addWidget(self.ShareFrom_2)
        self.ShareFrom = QtWidgets.QLabel(self.frame)
        self.ShareFrom.setText("")
        self.ShareFrom.setObjectName("ShareFrom")
        self.verticalLayout_2.addWidget(self.ShareFrom)
        self.verticalLayout.addWidget(self.frame)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        from .home import ui as ui_home
        from .SeeOtherPerson import ui as ui_seeOtherPerson
        from .post import ui as ui_post
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda :ui.setupUi(MainWindow,data,self.counter_before))#back
        self.pushButton_2.clicked.connect(lambda : ui.setupUi(MainWindow,data,self.counter_after))#next
        self.pushButton_3.clicked.connect(lambda : ui_home.setupUi(MainWindow,data,self.data['posts']['posts'][self.counter].user_id))#home
        #todo add comment ui to this project
        self.CommentButton.clicked.connect(lambda :print("co"))
        self.ShareButton.clicked.connect(lambda :ui_post.setupUi(MainWindow,self.data,))
        self.SeeProfile.clicked.connect(lambda :ui_seeOtherPerson.setupUi(MainWindow,self.data,User.find_via_pk(self.data['posts']['posts'][self.counter].user_id)))

        self.LikeButton.clicked.connect(lambda :print("like"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "from :"))
        self.UserName.setText(_translate("MainWindow", "User name "))
        self.SeeProfile.setText(_translate("MainWindow", "see profile"))
        self.numberComment.setText(_translate("MainWindow", "number of comment"))
        self.CommentButton.setText(_translate("MainWindow", "Comment"))
        self.ShareButton.setText(_translate("MainWindow", "share"))
        self.LikeButton.setText(_translate("MainWindow", "like"))
        self.Number_of_like.setText(_translate("MainWindow", "number of like"))
        self.ShareFrom_2.setText(_translate("MainWindow", "Share from:"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_3.setText(_translate("MainWindow", "Home"))

    def set_counter(self):
        self.counter_after = self.counter_before = self.counter
        if self.data['posts'] != None and len(self.data['posts']) > self.counter + 1:
            self.counter_after = self.counter + 1
        if self.counter != 0:
            self.counter_before = self.counter - 1

    def set_page(self):
         self.user = User.find_via_pk(self.data['posts']['posts'][self.counter].user_id)
         self.UserName.setText(self.user.username)

         # if

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow,data)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()