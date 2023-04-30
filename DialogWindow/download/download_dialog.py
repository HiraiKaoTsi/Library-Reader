# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Download(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 134)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget {\n"
                                 "    \n"
                                 "background-color: qlineargradient(spread:pad, x1:0.466, y1:0.159, x2:0.467, "
                                 "y2:0.972, stop:0 rgba(105, 45, 162, 255), stop:0.502488 rgba(32, 25, 121, 255), "
                                 "stop:1 rgba(105, 45, 162, 255));\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(481, 134))
        self.centralwidget.setMaximumSize(QtCore.QSize(481, 134))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 40))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border: 2px solid black;\n"
                                       "    border-radius: 5px;\n"
                                       "    background-color: rgb(0, 230, 255, 0);\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: rgb(23, 172, 12);\n"
                                       "    border-radius: 5px;\n"
                                       "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Загрузка"))
        self.label_1.setText(_translate("MainWindow", "Производиться загрузка данных"))
        self.label_2.setText(_translate("MainWindow", "Пожалуйста подождите..."))


from Resources import icon_cwt
