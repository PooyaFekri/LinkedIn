from PyQt5 import QtCore, QtGui, QtWidgets

from tables import Accomplishment
from .seeOtherPerson import ui as ui_other_person


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data, user):
        self.data = data
        self.user = user
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser_accom = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_accom.setObjectName("textBrowser_accom")
        self.verticalLayout.addWidget(self.textBrowser_accom)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout.addWidget(self.pushButton_back)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.set_other_accom()
        self.pushButton_back.clicked.connect(lambda: ui_other_person.setupUi(MainWindow, self.data, self.user))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Accomplishments"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))

    def set_other_accom(self):
        accomplishments = Accomplishment.get_accomplishments_by_user_id(self.user.id).get('accomplishments')
        str = ''
        for a in accomplishments:
            str += f'{a.title} \n\t accomplishment time:{a.accomplishment_time}\n\n'

        self.textBrowser_accom.setText(str)


ui = Ui_MainWindow()
