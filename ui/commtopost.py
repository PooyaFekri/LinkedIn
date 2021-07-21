# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commtopost.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data,comments,counter=0):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.data = data
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
        self.homwButton.clicked.connect(lambda : ui_home.setupUi(MainWindow,self.data))
        self.sendCommentButton.clicked.connect(lambda : self.send_comment())
        self.nextButton.clicked.connect(lambda : self.next_comment())
        self.beforeButton.clicked.connect(lambda : self.before_comment())
        self.replayButton.clicked.connect(lambda : self.replay())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homwButton.setText(_translate("MainWindow", "go home"))
        self.sendCommentButton.setText(_translate("MainWindow", "send comment"))
        self.nextButton.setText(_translate("MainWindow", "Next commend"))
        self.beforeButton.setText(_translate("MainWindow", "Before Commend"))
        self.like_checkBox.setText(_translate("MainWindow", "like"))
        self.replayButton.setText(_translate("MainWindow", "replay"))

    def send_comment(self):
        # if self.textBrowser_show_commend
        pass
    def next_comment(self):
        pass

    def before_comment(self):
        pass

    def replay(self):
        pass

    def set_up(self):
        pass

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()