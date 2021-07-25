from PyQt5 import QtCore, QtGui, QtWidgets


from tables import Message, Room, User, Experience
from tables.notification import Notification
from .room import ui as ui_room_chat
from .archive_chat import ui as ui_room_archive_chat
from .network import ui as ui_network
from .post import ui as ui_post
from .profile_me import ui as ui_me
from .seePost import ui as ui_seePost
from .jobs import ui as ui_jobs
from .nofi import ui as ui_nofi
# from .SeeOtherPerson import ui as ui_ohter_persion


# from .notifi // TODO: notif should be completed
# from .jobs // TODO: jobs should be completed
# from .comment import ui as ui_comment //TODO: edit comment file


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(9, 119, 571, 43))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homeButton = QtWidgets.QPushButton(self.frame_2)
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.homeButton)
        self.NetworkButton = QtWidgets.QPushButton(self.frame_2)
        self.NetworkButton.setObjectName("NetworkButton")
        self.horizontalLayout.addWidget(self.NetworkButton)
        self.NewPostButton = QtWidgets.QPushButton(self.frame_2)
        self.NewPostButton.setObjectName("NewPostButton")
        self.horizontalLayout.addWidget(self.NewPostButton)
        self.NotificationButton = QtWidgets.QPushButton(self.frame_2)
        self.NotificationButton.setObjectName("NotificationButton")
        self.horizontalLayout.addWidget(self.NotificationButton)
        self.JobsButton = QtWidgets.QPushButton(self.frame_2)
        self.JobsButton.setObjectName("JobsButton")
        self.horizontalLayout.addWidget(self.JobsButton)
        self.profile_button = QtWidgets.QPushButton(self.centralwidget)
        self.profile_button.setGeometry(QtCore.QRect(20, 20, 111, 91))
        self.profile_button.setObjectName("profile_button")
        self.search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_edit.setGeometry(QtCore.QRect(200, 60, 231, 20))
        self.search_edit.setObjectName("search_edit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 40, 61, 20))
        self.label_5.setObjectName("label_5")
        # self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea.setGeometry(QtCore.QRect(-1, 159, 581, 381))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 379))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.frame.setGeometry(QtCore.QRect(10, 10, 561, 191))
        # self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame.setObjectName("frame")
        # self.textBrowserOfPost = QtWidgets.QTextBrowser(self.frame)
        # self.textBrowserOfPost.setGeometry(QtCore.QRect(10, 10, 361, 131))
        # self.textBrowserOfPost.setObjectName("textBrowserOfPost")
        # self.Number_of_like = QtWidgets.QLabel(self.frame)
        # self.Number_of_like.setGeometry(QtCore.QRect(470, 80, 71, 21))
        # self.Number_of_like.setObjectName("Number_of_like")
        # self.numberComment = QtWidgets.QLabel(self.frame)
        # self.numberComment.setGeometry(QtCore.QRect(400, 80, 61, 21))
        # self.numberComment.setObjectName("numberComment")
        # self.CommentButton = QtWidgets.QPushButton(self.frame)
        # self.CommentButton.setGeometry(QtCore.QRect(400, 110, 75, 23))
        # self.CommentButton.setObjectName("CommentButton")
        # self.ShareButton = QtWidgets.QPushButton(self.frame)
        # self.ShareButton.setGeometry(QtCore.QRect(480, 110, 75, 23))
        # self.ShareButton.setObjectName("ShareButton")
        # self.LikeButton = QtWidgets.QCheckBox(self.frame)
        # self.LikeButton.setGeometry(QtCore.QRect(400, 60, 70, 17))
        # self.LikeButton.setObjectName("LikeButton")
        # self.SeeProfile = QtWidgets.QPushButton(self.frame)
        # self.SeeProfile.setGeometry(QtCore.QRect(480, 20, 75, 61))
        # self.SeeProfile.setObjectName("SeeProfile")
        # self.label_3 = QtWidgets.QLabel(self.frame)
        # self.label_3.setGeometry(QtCore.QRect(390, 10, 47, 16))
        # self.label_3.setObjectName("label_3")
        # self.UserName = QtWidgets.QLabel(self.frame)
        # self.UserName.setGeometry(QtCore.QRect(400, 30, 71, 20))
        # self.UserName.setObjectName("UserName")
        # self.label = QtWidgets.QLabel(self.frame)
        # self.label.setGeometry(QtCore.QRect(16, 160, 81, 20))
        # self.label.setObjectName("label")
        # self.ShareFrom = QtWidgets.QLabel(self.frame)
        # self.ShareFrom.setGeometry(QtCore.QRect(106, 160, 301, 20))
        # self.ShareFrom.setText("")
        # self.ShareFrom.setObjectName("ShareFrom")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.message_button = QtWidgets.QPushButton(self.centralwidget)
        self.message_button.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.message_button.setObjectName("message_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.data = data
        self.retranslateUi(MainWindow)
        self.message_button.clicked.connect(lambda: self.search_rooms(MainWindow))
        self.homeButton.clicked.connect(lambda: ui_seePost.setupUi(MainWindow, self.data))
        self.NetworkButton.clicked.connect(lambda: ui_network.setupUi(MainWindow, data))
        self.NewPostButton.clicked.connect(lambda: ui_post.setupUi(MainWindow, self.data, -1))
        self.profile_button.clicked.connect(lambda: ui_me.setupUi(MainWindow, self.data))
        self.JobsButton.clicked.connect(lambda : ui_jobs.setupUi(MainWindow,self.data, Experience.find_user_experiences(self.data.get("user").id).get("experiences")))
        self.NotificationButton.clicked.connect(lambda : ui_nofi.setupUi(MainWindow,self.data,Notification.user_notification(self.data.get("user").id).get('notifications')))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "SeePost"))
        self.NetworkButton.setText(_translate("MainWindow", "Network"))
        self.NewPostButton.setText(_translate("MainWindow", "New Post"))
        self.NotificationButton.setText(_translate("MainWindow", "Notification"))
        self.JobsButton.setText(_translate("MainWindow", "Jobs"))
        self.profile_button.setText(_translate("MainWindow", "Profile"))
        self.label_5.setText(_translate("MainWindow", "search :"))
        # self.Number_of_like.setText(_translate("MainWindow", "number of like"))
        # self.numberComment.setText(_translate("MainWindow", "number of comment"))
        # self.CommentButton.setText(_translate("MainWindow", "Comment"))
        # self.ShareButton.setText(_translate("MainWindow", "share"))
        # self.LikeButton.setText(_translate("MainWindow", "like"))
        # self.SeeProfile.setText(_translate("MainWindow", "see profile"))
        # self.label_3.setText(_translate("MainWindow", "from :"))
        # self.UserName.setText(_translate("MainWindow", "User name "))
        # self.label.setText(_translate("MainWindow", "Share from:"))
        self.message_button.setText(_translate("MainWindow", "message"))

    def search_rooms(self, MainWindow):
        # TODO: Fix error that happened if rooms was None
        rooms = Message.get_rooms_info(self.data.get('user').id).get('rooms_info')
        all_rooms_users_unarchive = []
        all_rooms_users_archived = []

        if len(rooms) != 0:
            for room in rooms:
                user_id = room[1] if room[1] != self.data.get('user').id else room[2]
                user = User.find_via_pk(user_id).get('user')
                room_obj = Room.find_via_pk(room[0]).get('room')
                if not room_obj.archive:
                    all_rooms_users_unarchive.append((user, room_obj))
                else:
                    all_rooms_users_archived.append((user, room_obj))
            if len(all_rooms_users_unarchive) != 0:
                ui_room_chat.setupUi(MainWindow, self.data, all_rooms_users_unarchive, all_rooms_users_archived)
            elif len(all_rooms_users_archived) != 0:
                ui_room_archive_chat.setupUi(MainWindow, self.data, all_rooms_users_unarchive, all_rooms_users_archived)


ui = Ui_MainWindow()
