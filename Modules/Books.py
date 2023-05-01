from PyQt5 import QtCore, QtGui, QtWidgets


class CreateBook(QtCore.QThread):
    signal_more_details = QtCore.pyqtSignal(int)
    signal_bookmark = QtCore.pyqtSignal(tuple)

    def __init__(self, Id: int, NameBook: str, Author: str, Publisher: str, Description: str, img: str, Price: int,
                 quantities: int, users_bookmark: tuple,
                 method_more_details, method_bookmark_add, method_bookmark_delete):
        super().__init__()

        self.method_bookmark_delete = method_bookmark_delete
        self.method_bookmark_add = method_bookmark_add

        # Основной фрейм
        self.frame_book = QtWidgets.QFrame()
        self.frame_book.setMinimumSize(QtCore.QSize(401, 219))
        self.frame_book.setMaximumSize(QtCore.QSize(401, 219))
        self.frame_book.setBaseSize(QtCore.QSize(401, 219))
        self.frame_book.setStyleSheet("QFrame {\n"
                                      "    border: 1px solid #54026E;\n"
                                      "    border-radius: 4px;\n"
                                      "}\n"
                                      "QLabel {\n"
                                      "    border: 0px solid;\n"
                                      "    font-family: Rubick;\n"
                                      "}\n"
                                      "QToolTip {\n"
                                      "	    font-family: Rubick;\n"
                                      "     font-size: 12pt;\n"
                                      "     color:white;\n"
                                      "     padding:2px;\n"
                                      "     border-width:2px;\n"
                                      "     border-style:solid;\n"
                                      " 	border-radius:20px;\n"
                                      "     background-color: rgb(30, 33, 61);\n"
                                      " 	border: 1px solid white;\n"
                                      " 	border-radius: 7px;\n"
                                      " 	overflow:hidden;\n"
                                      "}")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_book.sizePolicy().hasHeightForWidth())
        self.frame_book.setSizePolicy(sizePolicy)
        self.frame_book.setObjectName(f"Frame-{Id}")

        # Сетка
        self.gridLayout = QtWidgets.QGridLayout(self.frame_book)
        self.gridLayout.setObjectName("gridLayout")

        # id
        self.id = Id

        # Название книги
        self.label_name = QtWidgets.QLabel(self.frame_book)
        self.label_name.setText(f"Название: {NameBook}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setStyleSheet("font-size: 9pt;")
        self.label_name.setWordWrap(True)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 2, 1, 2)

        # Автор
        self.label_author = QtWidgets.QLabel(self.frame_book)
        self.label_author.setText(f"Автор: {Author}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_author.sizePolicy().hasHeightForWidth())
        self.label_author.setSizePolicy(sizePolicy)
        self.label_author.setStyleSheet("font-size: 7pt;")
        self.label_author.setObjectName("label_author")
        self.gridLayout.addWidget(self.label_author, 1, 2, 1, 1)

        # Издательство
        self.label_publisher = QtWidgets.QLabel(self.frame_book)
        self.label_publisher.setText(f"Издательство: {Publisher}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_publisher.sizePolicy().hasHeightForWidth())
        self.label_publisher.setSizePolicy(sizePolicy)
        self.label_publisher.setStyleSheet("font-size: 7pt;")
        self.label_publisher.setObjectName("label_publisher")
        self.gridLayout.addWidget(self.label_publisher, 2, 2, 1, 2)

        # Описание
        self.label_description = QtWidgets.QLabel(self.frame_book)
        self.label_description.setText(f"{Description}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setStyleSheet("font-size: 7pt;")
        self.label_description.setTextFormat(QtCore.Qt.AutoText)
        self.label_description.setScaledContents(False)
        self.label_description.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_description.setWordWrap(True)
        self.label_description.setIndent(-1)
        self.label_description.setObjectName("label_description")
        self.gridLayout.addWidget(self.label_description, 3, 2, 1, 2)

        # Цена
        self.label_price = QtWidgets.QLabel(self.frame_book)
        self.label_price.setText(f"Цена {Price} руб")
        self.label_price.setStyleSheet("font-size: 8pt;")
        self.label_price.setObjectName("label_price")
        self.gridLayout.addWidget(self.label_price, 4, 2, 1, 2, QtCore.Qt.AlignRight)

        # Картинка
        self.label_icon = QtWidgets.QLabel(self.frame_book)
        self.label_icon.setMinimumSize(QtCore.QSize(108, 152))
        self.label_icon.setSizeIncrement(QtCore.QSize(108, 152))
        new_img = img.replace("\\", "/")
        self.label_icon.setStyleSheet(f'image: url({new_img});')
        self.label_icon.setText("")
        self.label_icon.setObjectName("label_icon")
        self.gridLayout.addWidget(self.label_icon, 0, 0, 7, 1)

        # Добавить/удалить закладку
        self.pushButton_bookmark = QtWidgets.QPushButton(self.frame_book)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_bookmark.sizePolicy().hasHeightForWidth())
        self.pushButton_bookmark.setSizePolicy(sizePolicy)
        self.pushButton_bookmark.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_bookmark.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_bookmark.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        if Id in users_bookmark:

            self.pushButton_bookmark.setStyleSheet("background-color: red")
            self.info_function_bookmark = False
        else:
            self.info_function_bookmark = True

            self.pushButton_bookmark.setStyleSheet("QPushButton {\n"
                                                   "    background-color: rgb(27, 169, 212);\n"
                                                   "    border: none;\n"
                                                   "    border-radius: 7px;\n"
                                                   "}\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: rgb(31, 235, 249);\n"
                                                   "}\n"
                                                   "QPushButton:pressed {\n"
                                                   "    background-color: rgb(20, 131, 161);\n"
                                                   "}\n"
                                                   "QPushButton:disabled {\n"
                                                   "	    background-color: rgba(144,144,144);\n"
                                                   "}")

        self.pushButton_bookmark.clicked.connect(lambda: self.EventBookmark())
        self.pushButton_bookmark.setToolTip("<html><head/><body><p align=\"center\"><span style=\" "
                                            "font-size:12pt; font-weight:600;\">Добавить книгу в "
                                            "закладки</span></p></body></html>")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/bookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_bookmark.setIcon(icon)
        self.pushButton_bookmark.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_bookmark.setObjectName("pushButton_bookmark")
        self.gridLayout.addWidget(self.pushButton_bookmark, 6, 2, 1, 1, QtCore.Qt.AlignRight)

        if quantities == 0:
            self.pushButton_bookmark.setEnabled(False)

        # Больше информации
        self.pushButton_more_details = QtWidgets.QPushButton(self.frame_book)
        self.pushButton_more_details.clicked.connect(lambda: self.EventMoreDetails())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_more_details.sizePolicy().hasHeightForWidth())
        self.pushButton_more_details.setSizePolicy(sizePolicy)
        self.pushButton_more_details.setMinimumSize(QtCore.QSize(35, 35))
        self.pushButton_more_details.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_more_details.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_more_details.setStyleSheet("QPushButton {\n"
                                                   "    background-color: rgb(234, 219, 44);\n"
                                                   "    border: none;\n"
                                                   "    border-radius: 8px;\n"
                                                   "    font-family: Rubick;\n"
                                                   "    font-size: 7pt;\n"
                                                   "    color: rgb(0, 0, 0);\n"
                                                   "}\n"
                                                   "QPushButton:hover {\n"
                                                   "    background-color: rgb(255, 238, 48);\n"
                                                   "}\n"
                                                   "QPushButton:pressed {\n"
                                                   "    background-color: rgb(211, 197, 39);\n"
                                                   "}")
        self.pushButton_more_details.setToolTip("<html><head/><body><p align=\"center\"><span style=\" "
                                                "font-size:12pt; font-weight:600;\">Подробная информация о "
                                                "книге</span></p></body></html>")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_more_details.setIcon(icon1)
        self.pushButton_more_details.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_more_details.setObjectName("pushButton_more_details")
        self.gridLayout.addWidget(self.pushButton_more_details, 6, 3, 1, 1)

        self.signal_more_details.connect(method_more_details)

    def EventMoreDetails(self):
        self.signal_more_details.emit(self.id)

    def EventBookmark(self):
        print(1)
        if self.info_function_bookmark:
            print("add")
            self.signal_bookmark.connect(self.method_bookmark_add)
            self.EventBookmarkAdd()
            self.pushButton_bookmark.setStyleSheet("background-color: red")
            self.info_function_bookmark = False
        else:
            print("delete")
            self.signal_bookmark.connect(self.method_bookmark_delete)
            self.EventBookmarkDelete()
            self.pushButton_bookmark.setStyleSheet("background-color: green")
            self.info_function_bookmark = True

    def EventBookmarkAdd(self):
        self.signal_bookmark.emit((self.id, self.pushButton_bookmark, self.info_function_bookmark))

    def EventBookmarkDelete(self):
        self.signal_bookmark.emit((self.id, self.pushButton_bookmark, self.info_function_bookmark))
    from Resources import icon_cwt
