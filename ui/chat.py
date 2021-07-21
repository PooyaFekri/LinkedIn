import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Message, User
from tables.notification import Notification


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, room):
        self.data = data
        self.room = room
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 5, 581, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.lineEdit_message = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_message.setObjectName("lineEdit_message")
        self.verticalLayout.addWidget(self.lineEdit_message)
        self.Send_button = QtWidgets.QPushButton(self.layoutWidget)
        self.Send_button.setObjectName("Send_button")
        self.verticalLayout.addWidget(self.Send_button)
        self.Back = QtWidgets.QCommandLinkButton(self.layoutWidget)
        self.Back.setObjectName("Back")
        self.verticalLayout.addWidget(self.Back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.set_chat()

        self.retranslateUi(MainWindow)
        self.Send_button.clicked.connect(lambda: self.send_message())
        from .home import ui as ui_home
        self.Back.clicked.connect(lambda: ui_home.setupUi(MainWindow, self.data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Send_button.setText(_translate("MainWindow", "Send"))
        self.Back.setText(_translate("MainWindow", "Back"))

    def set_chat(self):
        messages = Message.get_messages(self.room.id).get('messages')
        str = ''
        for message in messages:
            user_receiver = User.find_via_pk(message.user_receiver_id).get('user')
            user_sender = User.find_via_pk(message.user_sender_id).get('user')
            str += f'{user_sender.username} to {user_receiver.username} : \n\n \t {message.text} \n\n {message.time} \n\n '

        self.textBrowser.setText(str)

    def send_message(self):
        user_id = self.room.user1_id if self.room.user1_id != self.data.get('user').id else self.room.user2_id
        time = datetime.datetime.now()
        variables = {
            'text': self.lineEdit_message.text(),
            'user_sender_id': self.data.get('user').id,
            'user_receiver_id': user_id,
            'room_id': self.room.id,
            'time': time
        }
        result = Message.insert(**variables)
        if result['status']:
            message = Message.find(variables).get('messages')[-1]
            self.lineEdit_message.setText('')
            res = Notification.notify(user_id=user_id,
                                      type_id=message.id,
                                      type="Message",
                                      time=time,
                                      event="Add new message")
            self.set_chat()
        else:
            self.textBrowser.setText(result['error'])
        #  notify
        pass


ui = Ui_MainWindow()
