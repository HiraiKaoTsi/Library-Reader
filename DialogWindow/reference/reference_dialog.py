# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'справка.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Reference(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(711, 275)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0.466, y1:0.159, x2:0.467, y2:0.972, stop:0 rgba(105, 45, 162, 255), stop:0.502488 rgba(32, 25, 121, 255), stop:1 rgba(105, 45, 162, 255));\n"
"    color: white;\n"
"    font-family: Rubick;\n"
"    font-size: 12pt;\n"
"    font-weight: 600;\n"
"    border: none;\n"
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
        self.frame_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_status.setObjectName("frame_status")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_status)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_icnon_status = QtWidgets.QLabel(self.frame_status)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_icnon_status.sizePolicy().hasHeightForWidth())
        self.label_icnon_status.setSizePolicy(sizePolicy)
        self.label_icnon_status.setMinimumSize(QtCore.QSize(40, 30))
        self.label_icnon_status.setStyleSheet("image: url(:/newPrefix/icon2/info.png);")
        self.label_icnon_status.setText("")
        self.label_icnon_status.setObjectName("label_icnon_status")
        self.horizontalLayout.addWidget(self.label_icnon_status, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_name_status = QtWidgets.QLabel(self.frame_status)
        self.label_name_status.setObjectName("label_name_status")
        self.horizontalLayout.addWidget(self.label_name_status, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_close_status = QtWidgets.QPushButton(self.frame_status)
        self.pushButton_close_status.setMaximumSize(QtCore.QSize(40, 50))
        self.pushButton_close_status.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_close_status.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close_status.setIcon(icon1)
        self.pushButton_close_status.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_close_status.setObjectName("pushButton_close_status")
        self.horizontalLayout.addWidget(self.pushButton_close_status, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_status, 0, QtCore.Qt.AlignTop)
        self.label_info = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        spacerItem1 = QtWidgets.QSpacerItem(10, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 30))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Справка"))
        self.label_name_status.setText(_translate("Dialog", "Справка"))
        self.pushButton_close_status.setToolTip(_translate("Dialog", "<html><head/><body><p>Закрыть</p></body></html>"))
        self.label_info.setText(_translate("Dialog", "Название программы: Библиотека Читайка.\n"
"Разработчиками программы являеться курсанты\n"
"ТАТК ГА – филиала МГТУ ГА. 331 группы\n"
"Ефремов М.В.\n"
"Сороника Е.В.\n"
"Программе «Библиотека Читайка» предназначена\n"
"для осуществления ознакомление/заказов книг пользователем\n"
"из представленной библиотеки."))
        self.pushButton.setText(_translate("Dialog", "OK"))
from Resources import icon_cwt