from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginRegistration(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/registration.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QWidget {\n"
                             "    \n"
                             "background-color: qlineargradient(spread:pad, x1:0.466, y1:0.159, x2:0.467, y2:0.972, "
                             "stop:0 rgba(105, 45, 162, 255), stop:0.502488 rgba(32, 25, 121, 255), stop:1 rgba(105, "
                             "45, 162, 255));\n"
                             "    color: white;\n"
                             "    font-family: Rubick;\n"
                             "    font-size: 12pt;\n"
                             "    font-weight: 600;\n"
                             "    border: none;\n"
                             "}\n"
                             "\n"
                             "QRadioButton{\n"
                             "    background-color: rgba(0, 0, 0, 0);\n"
                             "}\n"
                             "\n"
                             "QFrame{\n"
                             "    background-color: rgba(0,0,0,0);\n"
                             "}\n"
                             "\n"
                             "QLineEdit{\n"
                             "    background-color: rgba(0,0,0,0);\n"
                             "}\n"
                             "\n"
                             "QToolTip {\n"
                             "    font-family: Rubick;\n"
                             "    font-size: 12pt;\n"
                             "    color:white; padding:2px;\n"
                             "    border-width:2px;\n"
                             "    border-style:solid;\n"
                             "    border-radius:20px;\n"
                             "    background-color: rgb(30, 33, 61);\n"
                             "    border: 1px solid white;\n"
                             "    border-radius: 7px;\n"
                             "    overflow:hidden;\n"
                             "}\n"
                             "\n"
                             "QLineEdit {\n"
                             "    background-color: rgb(255, 255, 255);\n"
                             "    border: 1px solid #54026E;\n"
                             "    border-radius: 4px;\n"
                             "    color: rgb(30, 33, 61);\n"
                             "}\n"
                             "\n"
                             "QPushButton {\n"
                             "    background-color: transparent;\n"
                             "    border: none;\n"
                             "    border-radius: 7px;\n"
                             "}\n"
                             "\n"
                             "QPushButton:hover {\n"
                             "    background-color: rgb(66, 60, 99);\n"
                             "}\n"
                             "\n"
                             "QPushButton:pressed {\n"
                             "    background-color: rgb(28, 28, 28);\n"
                             "}\n"
                             "\n"
                             "QScrollBar:horizontal {\n"
                             "    border: 2px solid rrgb(26, 22, 42);\n"
                             "    background: rgb(66, 60, 99);\n"
                             "    height: 15px;\n"
                             "    margin: 0px 20px 0 20px;\n"
                             "}\n"
                             "\n"
                             "QScrollBar::handle:horizontal {\n"
                             "    background-color: rgb(26, 22, 42);\n"
                             "    min-width: 22px;\n"
                             "}\n"
                             "\n"
                             "QScrollBar::add-line:horizontal {\n"
                             "    image: url(:/white_icon/icon2/right_arrow (2).png);\n"
                             "    border: 2px solid rgb(66, 60, 99);\n"
                             "    background: rgb(26, 22, 42);\n"
                             "    width: 20px;\n"
                             "    subcontrol-position: right;\n"
                             "    subcontrol-origin: margin;\n"
                             "}\n"
                             "\n"
                             "QScrollBar::sub-line:horizontal {\n"
                             "    border: 2px solid rgb(66, 60, 99);\n"
                             "    background: rgb(26, 22, 42);\n"
                             "    width: 20px;\n"
                             "    subcontrol-position: left;\n"
                             "    subcontrol-origin: margin;\n"
                             "    image: url(:/white_icon/icon2/left_arrow.png)\n"
                             "}\n"
                             "\n"
                             "QScrollBar:vertical {\n"
                             "    border: 2px solid rrgb(26, 22, 42);\n"
                             "    background: rgb(66, 60, 99);\n"
                             "    width: 15px;\n"
                             "    width: 18px;\n"
                             "    margin: 20px 0 20px 0;\n"
                             "}\n"
                             "\n"
                             "QScrollBar::handle:vertical {\n"
                             "    background-color: rgb(26, 22, 42);;\n"
                             "    min-width: 22px;\n"
                             "}\n"
                             "\n"
                             "QScrollBar::add-line:vertical {\n"
                             "    image: url(:/white_icon/icon2/right_arrow (2).png);\n"
                             "    border: 2px solid rgb(66, 60, 99);\n"
                             "    background: rgb(26, 22, 42);\n"
                             "    height: 20px;\n"
                             "    subcontrol-position: bottom;\n"
                             "    subcontrol-origin: margin;\n"
                             "    image: url(:/white_icon/icon2/bot_arrow.png);\n"
                             "}\n"
                             "\n"
                             "QScrollBar::sub-line:vertical {\n"
                             "    border: 2px solid rgb(66, 60, 99);\n"
                             "    background: rgb(26, 22, 42);\n"
                             "    height: 20px;\n"
                             "    subcontrol-position: top;\n"
                             "    subcontrol-origin: margin;\n"
                             "    image: url(:/white_icon/icon2/up_arrow.png);\n"
                             "}\n"
                             "\n"
                             "QScrollBar::handle:hover {\n"
                             "    background: rgb(66, 60, 99);\n"
                             "}\n"
                             "\n"
                             "QScrollBar::handle:pressed {\n"
                             "    background-color: rgb(28, 28, 28);\n"
                             "}\n"
                             "\n"
                             "QScrollBar::add-page, QScrollBar::sub-page {\n"
                             "    background: rgb(138, 130, 179)\n"
                             "}\n"
                             "\n"
                             "\n"
                             "")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_status = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_status.sizePolicy().hasHeightForWidth())
        self.frame_status.setSizePolicy(sizePolicy)
        self.frame_status.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_status.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_status.setObjectName("frame_status")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_status)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.icon_register = QtWidgets.QLabel(self.frame_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_register.sizePolicy().hasHeightForWidth())
        self.icon_register.setSizePolicy(sizePolicy)
        self.icon_register.setMinimumSize(QtCore.QSize(40, 30))
        self.icon_register.setStyleSheet("image: url(:/newPrefix/icon2/registration.png);")
        self.icon_register.setText("")
        self.icon_register.setObjectName("icon_register")
        self.horizontalLayout_2.addWidget(self.icon_register, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_name = QtWidgets.QLabel(self.frame_status)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_2.addWidget(self.label_name, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_close_status = QtWidgets.QPushButton(self.frame_status)
        self.pushButton_close_status.setMaximumSize(QtCore.QSize(40, 50))
        self.pushButton_close_status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close_status.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close_status.setIcon(icon1)
        self.pushButton_close_status.setIconSize(QtCore.QSize(50, 60))
        self.pushButton_close_status.setObjectName("pushButton_close_status")
        self.horizontalLayout_2.addWidget(self.pushButton_close_status, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_status, 0, QtCore.Qt.AlignTop)
        self.frame_login = QtWidgets.QFrame(Dialog)
        self.frame_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login.setObjectName("frame_login")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_login)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_save_log = QtWidgets.QRadioButton(self.frame_login)
        self.radioButton_save_log.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_save_log.setObjectName("radioButton_save_log")
        self.gridLayout_2.addWidget(self.radioButton_save_log, 4, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_password_log = QtWidgets.QLabel(self.frame_login)
        self.label_password_log.setObjectName("label_password_log")
        self.gridLayout_2.addWidget(self.label_password_log, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.pushButton_hide_password_1 = QtWidgets.QPushButton(self.frame_login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_hide_password_1.sizePolicy().hasHeightForWidth())
        self.pushButton_hide_password_1.setSizePolicy(sizePolicy)
        self.pushButton_hide_password_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_hide_password_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hide_password_1.setIcon(icon2)
        self.pushButton_hide_password_1.setObjectName("pushButton_hide_password_1")
        self.gridLayout_2.addWidget(self.pushButton_hide_password_1, 2, 2, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(262, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        self.label_email_log = QtWidgets.QLabel(self.frame_login)
        self.label_email_log.setObjectName("label_email_log")
        self.gridLayout_2.addWidget(self.label_email_log, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_email_log = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_email_log.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_email_log.setObjectName("lineEdit_email_log")
        self.gridLayout_2.addWidget(self.lineEdit_email_log, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit_password_log = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_password_log.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_password_log.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_log.setObjectName("lineEdit_password_log")
        self.gridLayout_2.addWidget(self.lineEdit_password_log, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_login, 0, QtCore.Qt.AlignTop)
        self.frame_registr = QtWidgets.QFrame(Dialog)
        self.frame_registr.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_registr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_registr.setObjectName("frame_registr")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_registr)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_registr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        self.pushButton_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/left_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon3)
        self.pushButton_back.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_back.setObjectName("pushButton_back")
        self.gridLayout.addWidget(self.pushButton_back, 0, 0, 1, 1)
        self.radioButton_save_reg = QtWidgets.QRadioButton(self.frame_registr)
        self.radioButton_save_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_save_reg.setObjectName("radioButton_save_reg")
        self.gridLayout.addWidget(self.radioButton_save_reg, 11, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lineEdit_email_reg = QtWidgets.QLineEdit(self.frame_registr)
        self.lineEdit_email_reg.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_email_reg.setObjectName("lineEdit_email_reg")
        self.gridLayout.addWidget(self.lineEdit_email_reg, 5, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem3 = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 10, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.name = QtWidgets.QLabel(self.frame_registr)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.label_email_reg = QtWidgets.QLabel(self.frame_registr)
        self.label_email_reg.setObjectName("label_email_reg")
        self.gridLayout.addWidget(self.label_email_reg, 5, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 6, 0, 1, 1)
        self.pushButton_hide_password_2 = QtWidgets.QPushButton(self.frame_registr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_hide_password_2.sizePolicy().hasHeightForWidth())
        self.pushButton_hide_password_2.setSizePolicy(sizePolicy)
        self.pushButton_hide_password_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_hide_password_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hide_password_2.setIcon(icon4)
        self.pushButton_hide_password_2.setObjectName("pushButton_hide_password_2")
        self.gridLayout.addWidget(self.pushButton_hide_password_2, 7, 3, 1, 1, QtCore.Qt.AlignLeft)
        spacerItem8 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem8, 8, 0, 1, 1)
        self.lineEdit_password_reg = QtWidgets.QLineEdit(self.frame_registr)
        self.lineEdit_password_reg.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_password_reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_reg.setObjectName("lineEdit_password_reg")
        self.gridLayout.addWidget(self.lineEdit_password_reg, 9, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        spacerItem9 = QtWidgets.QSpacerItem(10, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 12, 0, 1, 1)
        self.lineEdit_password1_reg = QtWidgets.QLineEdit(self.frame_registr)
        self.lineEdit_password1_reg.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_password1_reg.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password1_reg.setObjectName("lineEdit_password1_reg")
        self.gridLayout.addWidget(self.lineEdit_password1_reg, 7, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lineEdit_name = QtWidgets.QLineEdit(self.frame_registr)
        self.lineEdit_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_password1_reg = QtWidgets.QLabel(self.frame_registr)
        self.label_password1_reg.setObjectName("label_password1_reg")
        self.gridLayout.addWidget(self.label_password1_reg, 7, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_password2_reg = QtWidgets.QLabel(self.frame_registr)
        self.label_password2_reg.setObjectName("label_password2_reg")
        self.gridLayout.addWidget(self.label_password2_reg, 9, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_button_reg = QtWidgets.QFrame(self.frame_registr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_button_reg.sizePolicy().hasHeightForWidth())
        self.frame_button_reg.setSizePolicy(sizePolicy)
        self.frame_button_reg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button_reg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_reg.setObjectName("frame_button_reg")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_button_reg)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_register_reg = QtWidgets.QPushButton(self.frame_button_reg)
        self.pushButton_register_reg.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_register_reg.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_register_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_register_reg.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_register_reg.setObjectName("pushButton_register_reg")
        self.verticalLayout_3.addWidget(self.pushButton_register_reg, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.frame_button_reg, 13, 0, 1, 4)
        self.verticalLayout.addWidget(self.frame_registr)
        self.frame_button = QtWidgets.QFrame(Dialog)
        self.frame_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button.setObjectName("frame_button")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_button)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_login = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_login.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_login.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout_2.addWidget(self.pushButton_login, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_or = QtWidgets.QLabel(self.frame_button)
        font = QtGui.QFont()
        font.setFamily("Rubick")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_or.setFont(font)
        self.label_or.setObjectName("label_or")
        self.verticalLayout_2.addWidget(self.label_or, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_register = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_register.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_register.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_register.setObjectName("pushButton_register")
        self.verticalLayout_2.addWidget(self.pushButton_register, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вход"))
        self.label_name.setText(_translate("Dialog", "Регестрация/вход"))
        self.pushButton_close_status.setToolTip(_translate("Dialog", "<html><head/><body><p>Закрыть</p></body></html>"))
        self.radioButton_save_log.setText(_translate("Dialog", " Запомнить"))
        self.label_password_log.setText(_translate("Dialog", " Пароль:"))
        self.label_email_log.setText(_translate("Dialog", " Email:"))
        self.radioButton_save_reg.setText(_translate("Dialog", " Запомнить"))
        self.name.setText(_translate("Dialog", " Имя пользователя:"))
        self.label_email_reg.setText(_translate("Dialog", " Email:"))
        self.label_password1_reg.setText(_translate("Dialog", " Пароль:"))
        self.label_password2_reg.setText(_translate("Dialog", " Повторите пароль:"))
        self.pushButton_register_reg.setText(_translate("Dialog", " Зарегестрироваться "))
        self.pushButton_login.setText(_translate("Dialog", " Войти "))
        self.label_or.setText(_translate("Dialog", "Или"))
        self.pushButton_register.setText(_translate("Dialog", " Зарегестрироваться "))
    from Resources import icon_cwt
