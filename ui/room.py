from PyQt5 import QtCore, QtGui, QtWidgets

from .chat import ui as ui_chat


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, un_rooms, arch_rooms, counter=0):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.data = data
        self.un_rooms = un_rooms
        self.counter = counter
        self.arch_rooms = arch_rooms
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ArchiveList = QtWidgets.QPushButton(self.centralwidget)
        self.ArchiveList.setObjectName("ArchiveList")
        self.verticalLayout.addWidget(self.ArchiveList)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(170, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.Delete_this_chat = QtWidgets.QPushButton(self.frame)
        self.Delete_this_chat.setGeometry(QtCore.QRect(440, 80, 75, 23))
        self.Delete_this_chat.setObjectName("Delete_this_chat")
        self.FirstName_lastName = QtWidgets.QLabel(self.frame)
        self.FirstName_lastName.setGeometry(QtCore.QRect(180, 90, 81, 16))
        self.FirstName_lastName.setObjectName("FirstName_lastName")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 30, 81, 16))
        self.label.setObjectName("label")
        self.checkBoxRead = QtWidgets.QCheckBox(self.frame)
        self.checkBoxRead.setGeometry(QtCore.QRect(450, 30, 70, 17))
        self.checkBoxRead.setObjectName("checkBoxRead")
        self.UserName = QtWidgets.QLabel(self.frame)
        self.UserName.setGeometry(QtCore.QRect(180, 50, 47, 13))
        self.UserName.setObjectName("UserName")
        self.SeeChat = QtWidgets.QPushButton(self.frame)
        self.SeeChat.setGeometry(QtCore.QRect(44, 20, 101, 81))
        self.SeeChat.setObjectName("SeeChat")
        self.Archive_this_chat = QtWidgets.QPushButton(self.frame)
        self.Archive_this_chat.setGeometry(QtCore.QRect(440, 50, 75, 23))
        self.Archive_this_chat.setObjectName("Archive_this_chat")
        self.verticalLayout.addWidget(self.frame)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        self.NextButton.setObjectName("NextButton")
        self.verticalLayout.addWidget(self.NextButton)
        self.BeforeButton = QtWidgets.QPushButton(self.centralwidget)
        self.BeforeButton.setObjectName("BeforeButton")
        self.verticalLayout.addWidget(self.BeforeButton)
        self.BackButton = QtWidgets.QCommandLinkButton(self.centralwidget)
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
        self.set_room(MainWindow)
        self.set_counter()
        self.NextButton.clicked.connect(
            lambda: ui.setupUi(MainWindow, self.data, self.un_rooms, self.arch_rooms, self.counter_after))
        self.BeforeButton.clicked.connect(
            lambda: ui.setupUi(MainWindow, self.data, self.un_rooms, self.arch_rooms, self.counter_before))
        self.ArchiveList.clicked.connect(lambda: self.archive_list(MainWindow))
        from .home import ui as ui_home
        self.BackButton.clicked.connect(lambda: ui_home.setupUi(MainWindow, data))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ArchiveList.setText(_translate("MainWindow", "Archive chat"))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.Delete_this_chat.setText(_translate("MainWindow", "Delete"))
        self.FirstName_lastName.setText(_translate("MainWindow", "Name_last_name"))
        self.label.setText(_translate("MainWindow", "User Name:"))
        self.checkBoxRead.setText(_translate("MainWindow", "Read"))
        self.UserName.setText(_translate("MainWindow", "User_"))
        self.SeeChat.setText(_translate("MainWindow", "Chat"))
        self.Archive_this_chat.setText(_translate("MainWindow", "Archive"))
        self.NextButton.setText(_translate("MainWindow", "Next"))
        self.BeforeButton.setText(_translate("MainWindow", "Before"))
        self.BackButton.setText(_translate("MainWindow", "Back"))

    def archive_list(self, MainWindow):
        if len(self.arch_rooms) != 0:
            from .archive_chat import ui as ui_archive_chat
            ui_archive_chat.setupUi(MainWindow, self.data, self.un_rooms, self.arch_rooms)

    def set_counter(self):
        self.counter_after = self.counter_before = self.counter
        if len(self.un_rooms) > self.counter + 1:
            self.counter_after = self.counter + 1
        if self.counter != 0:
            self.counter_before = self.counter - 1

    def set_room(self, MainWindow):
        another_user = self.un_rooms[self.counter][0]
        another_room = self.un_rooms[self.counter][1]
        self.UserName.setText(another_user.username)
        self.FirstName_lastName.setText(f'{another_user.first_name}  {another_user.last_name}')
        self.SeeChat.clicked.connect(lambda: ui_chat.setupUi(MainWindow, self.data, another_room))
        self.Archive_this_chat.clicked.connect(lambda: another_room.archive_room(True))

        self.Delete_this_chat.clicked.connect(lambda: another_room.delete())
        # TODO
        # self.checkBoxRead.clicked.connect(lambda )
        # self.checkBoxRead.isChecked('print checked')


ui = Ui_MainWindow()
