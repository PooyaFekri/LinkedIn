# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commtopost.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Comment, Like, Connection
from tables.notification import Notification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, comments, post, counter=0):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.is_like = False
        self.data = data
        self.post = post
        self.comments = comments
        self.counter = counter
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homwButton = QtWidgets.QPushButton(self.centralwidget)
        self.homwButton.setObjectName("homwButton")
        self.verticalLayout.addWidget(self.homwButton)
        self.textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.sendCommentButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendCommentButton.setObjectName("sendCommentButton")
        self.verticalLayout.addWidget(self.sendCommentButton)
        self.textBrowser_show_commend = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_show_commend.setObjectName("textBrowser_show_commend")
        self.verticalLayout.addWidget(self.textBrowser_show_commend)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout.addWidget(self.nextButton)
        self.beforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.beforeButton.setObjectName("beforeButton")
        self.verticalLayout.addWidget(self.beforeButton)
        self.replaycomment_textBrowser = QtWidgets.QTextEdit(self.centralwidget)
        self.replaycomment_textBrowser.setObjectName("replaycomment_textBrowser")
        self.verticalLayout.addWidget(self.replaycomment_textBrowser)
        self.like_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.like_checkBox.setObjectName("like_checkBox")
        self.verticalLayout.addWidget(self.like_checkBox)
        self.replayButton = QtWidgets.QPushButton(self.centralwidget)
        self.replayButton.setObjectName("replayButton")
        self.verticalLayout.addWidget(self.replayButton)
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
        self.homwButton.clicked.connect(lambda: ui_home.setupUi(MainWindow, self.data))
        self.sendCommentButton.clicked.connect(lambda: self.send_comment(MainWindow))
        if self.comments:
            self.nextButton.clicked.connect(lambda: self.next_comment(MainWindow))
            self.beforeButton.clicked.connect(lambda: self.before_comment(MainWindow))
            self.replayButton.clicked.connect(lambda: self.replay(MainWindow))
            self.like_checkBox.clicked.connect(lambda : self.like(MainWindow))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.set_up(MainWindow)
        self.homwButton.setText(_translate("MainWindow", "go home"))
        self.sendCommentButton.setText(_translate("MainWindow", "send comment"))
        self.nextButton.setText(_translate("MainWindow", "Next commend"))
        self.beforeButton.setText(_translate("MainWindow", "Before Commend"))
        self.like_checkBox.setText(_translate("MainWindow", "like"))
        self.replayButton.setText(_translate("MainWindow", "replay"))

    def send_comment(self, MainWindow):
        time = datetime.now()
        user_id = self.data.get("user").id
        connections = Connection.find_user_connections(user_id).get('connections')
        if self.textBrowser.toPlainText():
            data = {"user_id": self.data.get('user').id, 'time': datetime.now(),
                    'text': self.textBrowser.toPlainText(), 'post_id': self.post.id}
            Comment.create(**data)


            comment = Comment.find(data)[-1]
            event = "this post comment by :" + self.data.get("user").username + "in :" + str(time) + "\n" + self.post.text +"\n*******"+"\n"+"comment  : \n"+comment.text
            _data = {"user_id": comment.user_id, "time": time, "event": event, "type": "Comment",
            'type_id': comment.id}
            res = Notification.notify(**_data)
            for connection in connections:

                connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
                if connect_user_id != comment.user_id:
                    _data = {"user_id": connect_user_id, "time": time, "event": event, "type": "Comment",
                             'type_id': comment.id}
                    res = Notification.notify(**_data)
            ui.setupUi(MainWindow, self.data, Comment.get_comments_by_post_id(self.post.id).get("comments"), self.post)

    def next_comment(self, MainWindow):

        if len(self.comments) > self.counter + 1:
            ui.setupUi(MainWindow, self.data, self.comments, self.post, self.counter + 1)

    def before_comment(self, MainWindow):
        if self.counter > 0:
            ui.setupUi(MainWindow, self.data, self.comments, self.post, self.counter - 1)

    def replay(self, MainWindow):

        time = datetime.now()
        user_id = self.data.get("user").id
        connections = Connection.find_user_connections(user_id).get('connections')

        if self.replaycomment_textBrowser.toPlainText():

            data = {"user_id": self.data.get('user').id, 'time': datetime.now(),
                    'text': self.replaycomment_textBrowser.toPlainText()+"\n"+"replay : \n"+self.textBrowser_show_commend.toPlainText(), 'post_id': self.post.id,'comment_reply_id':self.comments[self.counter].id}
            Comment.create(**data)

            comment = Comment.find(data)[-1]
            event = "your comment replay by :" + self.data.get("user").username + "in :" + str(time) + "\n" + self.comments[self.counter].text +"\n*******"+"\n"+"comment  : \n"+comment.text
            event_1 = "this comment replay by :" + self.data.get("user").username + "in :" + str(time) + "\n" + self.comments[self.counter].text +"\n*******"+"\n"+"comment  : \n"+comment.text

            _data = {"user_id": comment.user_id, "time": time, "event": event, "type": "Comment",
            'type_id': comment.id}
            res = Notification.notify(**_data)
            for connection in connections:

                connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
                if connect_user_id != comment.user_id:
                    _data = {"user_id": connect_user_id, "time": time, "event": event_1, "type": "Comment",
                             'type_id': comment.id}
                    res = Notification.notify(**_data)



            ui.setupUi(MainWindow,self.data,Comment.get_comments_by_post_id(self.post.id).get("comments"),self.post)

    def set_up(self, MainWindow):
        if self.comments:
            # print(self.comments)
            # print(self.comments[0].text)
            self.textBrowser_show_commend.setText(self.comments[self.counter].text)

        likes = []
        if self.comments:
            likes = Like.get_comment_likes(self.comments[self.counter].id).get("likes")
            if likes:
                for i in likes:
                    if i.user_id == self.data.get('user').id:
                        self.like_checkBox.click()
                        self.is_like = True
                        self.this_like = i

    def like(self, MainWindow):
        user_id = self.data.get("user").id
        time = datetime.now()
        connections = Connection.find_user_connections(user_id).get('connections')

        if self.is_like == True :
            self.is_like = False
            self.this_like.unlike()

        else :
            # print(self.comments)
            if self.comments:
                comment = self.comments[self.counter]
                data = {'comment_id':self.comments[self.counter].id,'time':datetime.now(),'user_id':self.data.get('user').id}
                Like.like(**data)

                self.this_like = Like.find(data)[-1]
                event = "your comment like by :" + self.data.get("user").username + "in :" + str(time) +"\npost:"+ "\n" + self.post.text + "\n*******\ncomment:"+comment.text
                event_other = "this comment like by :" + self.data.get("user").username + "in :" + str(time) +"\npost:"+ "\n" + self.post.text + "\n*******\ncomment:"+comment.text

                _data = {"user_id": comment.user_id, "time": time, "event": event, "type": "Like",
                         'type_id': self.this_like.id}
                res = Notification.notify(**_data)
                for connection in connections:

                    connect_user_id = connection.user_caller_id if connection.user_caller_id != user_id else connection.user_invited_id
                    if connect_user_id != self.this_like.id:
                        _data = {"user_id": connect_user_id, "time": time, "event": event_other, "type": "Like",
                                 'type_id': self.this_like.id}
                        res = Notification.notify(**_data)
                # likes = Like.get_comment_likes(self.comments[self.counter].id).get("likes")
                #
                # for i in likes:
                #     if i.user_id == self.data.get('user').id:
                #         self.like_checkBox.click()
                #         self.is_like = True
                #         self.this_like = i



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()
