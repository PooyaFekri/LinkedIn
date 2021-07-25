# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeePost.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Connection, User, Comment, Like


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, data,counter = 0):
        data['posts'] = Connection.get_related_posts(data['user'].id)
        self.data = data
        self.counter = counter
        self.set_counter()
        self.post = None
        self.user = None
        self.is_like = False
        self.this_like = None
        self.comments = None
        if self.data['posts'] and self.data['posts']['posts']:
            self.post = self.data['posts']['posts'][self.counter]
            self.comments = Comment.get_comments_by_post_id(self.data['posts']['posts'][self.counter].id).get(
                "comments")
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
        if self.data['posts'] and  self.data['posts']['posts'] and  self.data['posts']['posts'][self.counter].share:
            self.ShareFrom.setText(User.find_via_pk(self.data['posts']['posts'][self.counter].share).get("user").username)
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
        self.set_page()
        from .home import ui as ui_home
        from .seeOtherPerson import ui as ui_seeOtherPerson
        from .post import ui as ui_post
        from .commtopost import ui as ui_comment
        self.retranslateUi(MainWindow)
        # self.pushButton.clicked.connect(lambda :ui.setupUi(MainWindow,data,self.counter_before))#back
        # self.pushButton_2.clicked.connect(lambda : ui.setupUi(MainWindow,data,self.counter_after))#next
        self.pushButton_3.clicked.connect(lambda : ui_home.setupUi(MainWindow,data))#home
        if self.post:
            self.CommentButton.clicked.connect(lambda : ui_comment.setupUi(MainWindow,self.data,self.comments,self.post))
            self.ShareButton.clicked.connect(lambda :ui_post.setupUi(MainWindow,self.data,self.user.id))
            self.SeeProfile.clicked.connect(lambda :ui_seeOtherPerson.setupUi(MainWindow,self.data,User.find_via_pk(self.post.user_id).get("user")))
            self.pushButton.clicked.connect(lambda: ui.setupUi(MainWindow, data, self.counter_before))  # back
            self.pushButton_2.clicked.connect(lambda: ui.setupUi(MainWindow, data, self.counter_after))  # next
            self.LikeButton.clicked.connect(lambda : self.like())

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
        if self.user:
            self.UserName.setText(self.user.username)

    def set_counter(self):
        self.counter_after = self.counter_before = self.counter
        if self.data['posts'] and self.data['posts']['posts'] and len(self.data['posts']['posts']) > self.counter + 1:
            self.counter_after = self.counter + 1
        if self.counter != 0:
            self.counter_before = self.counter - 1


    def set_page(self):

        if self.post:
            self.user = User.find_via_pk(self.post.user_id).get('user')
            self.UserName.setText(self.user.username)
            self.textBrowserOfPost.setText(self.post.text)
        if self.comments:
             self.numberComment.setText(str(len(self.comments)))

        likes = []
        if self.post:
             likes = Like.get_post_likes(self.post.id).get("likes")
             if likes:
                 self.Number_of_like.setText(str(len(likes)))
                 for i in likes:
                     if i.user_id == self.data.get('user').id:
                         self.LikeButton.click()
                         self.is_like = True
                         self.this_like = i

         # if

    def like(self):
        user_id = self.data.get("user").id
        time = datetime.now()
        connections = Connection.find_user_connections(user_id).get('connections')
        if self.is_like == True :
            self.is_like = False
            self.this_like.unlike()
        else :
            # print(self.comments)
            if self.post:
                data = {'post_id':self.post.id,'time':datetime.now(),'user_id':self.data.get('user').id}
                Like.like(**data)
                likes = Like.get_post_likes(self.post.id).get("likes")
                self.this_like = Like.find(data)[-1]
                # for connection in connections:
                #     connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
                #     _data = {"user_id": connect_user_id, "time": time, "event": event, "type": "Post",
                #              'type_id': self.this_like.id}
                #     res = Notification.notify(**_data)
                # for i in likes:
                #     if i.user_id == self.data.get('user').id:
                #         self.LikeButton.click()
                #         self.is_like = True
                #         self.this_like = i
                #

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow,data)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()