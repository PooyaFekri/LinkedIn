from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(600, 559)
        self.scrollArea = QtWidgets.QScrollArea(Home)
        self.scrollArea.setGeometry(QtCore.QRect(9, 149, 581, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(10, 10, 561, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowserOfPost = QtWidgets.QTextBrowser(self.frame)
        self.textBrowserOfPost.setGeometry(QtCore.QRect(10, 10, 361, 131))
        self.textBrowserOfPost.setObjectName("textBrowserOfPost")
        self.Number_of_like = QtWidgets.QLabel(self.frame)
        self.Number_of_like.setGeometry(QtCore.QRect(470, 80, 71, 21))
        self.Number_of_like.setObjectName("Number_of_like")
        self.numberComment = QtWidgets.QLabel(self.frame)
        self.numberComment.setGeometry(QtCore.QRect(400, 80, 61, 21))
        self.numberComment.setObjectName("numberComment")
        self.CommentButton = QtWidgets.QPushButton(self.frame)
        self.CommentButton.setGeometry(QtCore.QRect(400, 110, 75, 23))
        self.CommentButton.setObjectName("CommentButton")
        self.ShareButton = QtWidgets.QPushButton(self.frame)
        self.ShareButton.setGeometry(QtCore.QRect(480, 110, 75, 23))
        self.ShareButton.setObjectName("ShareButton")
        self.LikeButton = QtWidgets.QCheckBox(self.frame)
        self.LikeButton.setGeometry(QtCore.QRect(400, 60, 70, 17))
        self.LikeButton.setObjectName("LikeButton")
        self.SeeProfile = QtWidgets.QPushButton(self.frame)
        self.SeeProfile.setGeometry(QtCore.QRect(480, 20, 75, 61))
        self.SeeProfile.setObjectName("SeeProfile")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(390, 10, 47, 16))
        self.label_3.setObjectName("label_3")
        self.UserName = QtWidgets.QLabel(self.frame)
        self.UserName.setGeometry(QtCore.QRect(400, 30, 71, 20))
        self.UserName.setObjectName("UserName")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.profile_button = QtWidgets.QPushButton(Home)
        self.profile_button.setGeometry(QtCore.QRect(30, 10, 111, 91))
        self.profile_button.setObjectName("profile_button")
        self.frame_2 = QtWidgets.QFrame(Home)
        self.frame_2.setGeometry(QtCore.QRect(19, 109, 571, 43))
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
        self.search_edit = QtWidgets.QLineEdit(Home)
        self.search_edit.setGeometry(QtCore.QRect(210, 50, 231, 20))
        self.search_edit.setObjectName("search_edit")
        self.label_5 = QtWidgets.QLabel(Home)
        self.label_5.setGeometry(QtCore.QRect(210, 30, 61, 20))
        self.label_5.setObjectName("label_5")
        self.message_button = QtWidgets.QPushButton(Home)
        self.message_button.setGeometry(QtCore.QRect(210, 80, 75, 23))
        self.message_button.setObjectName("message_button")

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Form"))
        self.Number_of_like.setText(_translate("Home", "number of like"))
        self.numberComment.setText(_translate("Home", "number of comment"))
        self.CommentButton.setText(_translate("Home", "Comment"))
        self.ShareButton.setText(_translate("Home", "share"))
        self.LikeButton.setText(_translate("Home", "like"))
        self.SeeProfile.setText(_translate("Home", "see profile"))
        self.label_3.setText(_translate("Home", "from :"))
        self.UserName.setText(_translate("Home", "User name "))
        self.profile_button.setText(_translate("Home", "Profile"))
        self.homeButton.setText(_translate("Home", "home"))
        self.NetworkButton.setText(_translate("Home", "Network"))
        self.NewPostButton.setText(_translate("Home", "New Post"))
        self.NotificationButton.setText(_translate("Home", "Notification"))
        self.JobsButton.setText(_translate("Home", "Jobs"))
        self.label_5.setText(_translate("Home", "search :"))
        self.message_button.setText(_translate("Home", "message"))

ui = Ui_Home()
