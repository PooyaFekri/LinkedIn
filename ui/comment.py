# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment.ui'
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comment_textEdit = QtWidgets.QTextEdit(self.frame)
        self.comment_textEdit.setGeometry(QtCore.QRect(23, 20, 231, 201))
        self.comment_textEdit.setObjectName("comment_textEdit")
        self.likeButton = QtWidgets.QPushButton(self.frame)
        self.likeButton.setGeometry(QtCore.QRect(290, 50, 89, 25))
        self.likeButton.setObjectName("likeButton")
        self.unlikeButton = QtWidgets.QPushButton(self.frame)
        self.unlikeButton.setGeometry(QtCore.QRect(400, 50, 89, 25))
        self.unlikeButton.setObjectName("unlikeButton")
        self.like_message = QtWidgets.QLabel(self.frame)
        self.like_message.setGeometry(QtCore.QRect(300, 90, 141, 17))
        self.like_message.setObjectName("like_message")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 140, 67, 17))
        self.label.setObjectName("label")
        self.replay_to_commetn_of = QtWidgets.QLabel(self.frame)
        self.replay_to_commetn_of.setGeometry(QtCore.QRect(370, 140, 181, 17))
        self.replay_to_commetn_of.setObjectName("replay_to_commetn_of")
        self.replayButton = QtWidgets.QPushButton(self.frame)
        self.replayButton.setGeometry(QtCore.QRect(20, 370, 89, 25))
        self.replayButton.setObjectName("replayButton")
        self.replay_textEdit = QtWidgets.QTextEdit(self.frame)
        self.replay_textEdit.setGeometry(QtCore.QRect(20, 280, 361, 71))
        self.replay_textEdit.setObjectName("replay_textEdit")
        self.verticalLayout.addWidget(self.frame)
        self.setCommentButton = QtWidgets.QPushButton(self.centralwidget)
        self.setCommentButton.setObjectName("setCommentButton")
        self.verticalLayout.addWidget(self.setCommentButton)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setObjectName("nextButton")
        self.verticalLayout.addWidget(self.nextButton)
        self.befforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.befforeButton.setObjectName("befforeButton")
        self.verticalLayout.addWidget(self.befforeButton)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
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
        self.likeButton.setText(_translate("MainWindow", "like"))
        self.unlikeButton.setText(_translate("MainWindow", "unlike"))
        self.like_message.setText(_translate("MainWindow", "you like or not"))
        self.label.setText(_translate("MainWindow", "replay :"))
        self.replay_to_commetn_of.setText(_translate("MainWindow", "replay to comment of"))
        self.replayButton.setText(_translate("MainWindow", "replay"))
        self.setCommentButton.setText(_translate("MainWindow", "set comment"))
        self.nextButton.setText(_translate("MainWindow", "next comment"))
        self.befforeButton.setText(_translate("MainWindow", "before comment"))
        self.BackButton.setText(_translate("MainWindow", "Back post"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
