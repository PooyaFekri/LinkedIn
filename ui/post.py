from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from tables import Post, notification, Connection
from tables.notification import Notification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data,share_id):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 629)
        self.share_id = share_id
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
        self.sendButton.clicked.connect(lambda: self.post(MainWindow, data))
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
        if self.share_id != -1:
            data = {"user_id": user_id, "time": time, "text": text}
        else:
            data = {"user_id": user_id, "time": time, "text": text,'share':self.share_id}
        Post.send(**data)

        post = Post.find(data)[-1]
        connections = Connection.find_user_connections(user_id).get('connections')
        for connection in connections:
            connect_user_id = user_id if connection.user_caller_id != user_id else connection.user_caller_id
            _data = {"user_id": connect_user_id, "time": time, "type": "Post", 'type_id': post.id}
            res = Notification.notify(**_data)
        ui.setupUi(MainWindow, data)


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

ui = Ui_MainWindow()
