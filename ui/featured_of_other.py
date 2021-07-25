from PyQt5 import QtCore, QtGui, QtWidgets
from .home import ui as ui_home

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,data,other_post,counter):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.data = data
        self.other_post = other_post
        self.counter = counter
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.post_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.post_textBrowser.setObjectName("post_textBrowser")
        self.verticalLayout.addWidget(self.post_textBrowser)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout.addWidget(self.NextButton)
        self.BeforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeButton.setObjectName("BeforeButton")
        self.verticalLayout.addWidget(self.BeforeButton)
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
        if self.counter:
            self.NextButton.clicked.connect(lambda : self.next_page(MainWindow))
            self.BeforeButton.clicked.connect(lambda : self.befor_page(MainWindow))
        self.homeButton.clicked.connect(lambda : ui_home.setupUi(MainWindow,self.data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.BeforeButton.setText(_translate("MainWindow", "Before"))
        self.homeButton.setText(_translate("MainWindow", "home"))
        if self.other_post:
            self.post_textBrowser.setText(self.other_post[self.counter].text)

    def befor_page(self, MainWindow):
        if self.counter + 1 < len(self.other_post):
            ui.setupUi(MainWindow, self.data, self.other_post, self.counter + 1)

    def next_page(self, MainWindow):
        if self.counter > 0 :
            ui.setupUi(MainWindow,self.data,self.other_post,self.counter-1)



#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
ui = Ui_MainWindow()