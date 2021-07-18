from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from tables import Post, notification, Connection


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 581, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        self.Back_button = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.Back_button.setObjectName("Back_button")
        self.verticalLayout.addWidget(self.Back_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        from .home import ui as ui_home
        self.sendButton.clicked.connect(self.post(MainWindow, data))
        self.Back_button.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.Back_button.setText(_translate("MainWindow", "Back"))

    def post(self, MainWindow, data):
        text = self.plainTextEdit.toPlainText()
        time = datetime.datetime.now()
        user_id = data.get("user").id
        data = {"user_id": user_id, "time": time, "text": text}
        Post.insert(**data)
        connections = Connection.find_user_connections(user_id)
        for connection in connections:
            connect_user_id = user_id if connection.user_caller_id != user_id else connection.user_caller_id
            data = {"user_id":connect_user_id,"time":time,type:"Post"}
        notification.Notification.insert(**data)
        ui.setupUi(MainWindow,data)
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
