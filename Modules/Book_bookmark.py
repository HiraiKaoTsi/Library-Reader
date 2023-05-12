from PyQt5 import QtCore, QtGui, QtWidgets


class CreateBookBookmark(QtCore.QThread):

    signal_amount = QtCore.pyqtSignal(int)
    signal_plus_amount = QtCore.pyqtSignal(tuple)
    signal_delete = QtCore.pyqtSignal(tuple)

    def __init__(self, Id: int, NameBook: str, Author: str, Publisher: str, Series: str, ISBN: str,
                 Price: int, Quantity: int, img: str, method_amount, method_add, method_delete):
        super().__init__()

        self.Price = Price

        # Сигналы
        self.signal_amount.connect(method_amount)
        self.signal_amount.emit(Price)

        self.signal_plus_amount.connect(method_add)

        self.signal_delete.connect(method_delete)

        # Frame
        self.frame_book = QtWidgets.QFrame()
        self.frame_book.setGeometry(QtCore.QRect(70, 110, 521, 219))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.frame_book.sizePolicy().hasHeightForWidth())
        self.frame_book.setSizePolicy(sizePolicy)
        self.frame_book.setMinimumSize(QtCore.QSize(451, 219))
        self.frame_book.setMaximumSize(QtCore.QSize(10000, 219))
        self.frame_book.setStyleSheet("QFrame {\n"
                                      "    border: 1px solid #54026E;\n"
                                      "    border-radius: 4px;\n"
                                      "}\n"
                                      "QLabel {\n"
                                      "    border: 0px solid;\n"
                                      "    font-family: Rubick;\n"
                                      "}\n"
                                      "QToolTip {\n"
                                      "    font-family: Rubick;\n"
                                      "    font-size: 12pt;\n"
                                      "    color:white; \n"
                                      "    padding:2px;\n"
                                      "    border-width:2px;\n"
                                      "    border-style:solid;\n"
                                      "    border-radius:20px;\n"
                                      "    background-color: rgb(30, 33, 61);\n"
                                      "    border: 1px solid white;\n"
                                      "    border-radius: 7px;\n"
                                      "    overflow:hidden;\n"
                                      "}\n"
                                      "QSpinBox {\n"
                                      "    background-color: rgb(0, 0, 0,0);\n"
                                      " }\n"
                                      "QSpinBox::up-button {\n"
                                      "    subcontrol-origin: border;\n"
                                      "    subcontrol-position: center right; \n"
                                      "    width: 20;\n"
                                      "    height: 20;\n"
                                      "    border-image: url(:/newPrefix/icon2/pluss1.png);\n"
                                      " }\n"
                                      "QSpinBox::down-button {\n"
                                      "    subcontrol-origin: border;\n"
                                      "    subcontrol-position: center left; \n"
                                      "    width: 20;\n"
                                      "    height: 20;\n"
                                      "    border-image: url(:/newPrefix/icon2/pluss1.png);\n"
                                      " }\n"
                                      "\n"
                                      "QSpinBox::up-button:hover {\n"
                                      "    \n"
                                      "    border-image: url(:/newPrefix/icon2/pluss2.png);\n"
                                      "}\n"
                                      "QSpinBox::down-button:hover {\n"
                                      "    border-image: url(:/newPrefix/icon2/pluss2.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::up-button:pressed {\n"
                                      "    border-image: url(:/newPrefix/icon2/pluss3.png);\n"
                                      "}\n"
                                      "\n"
                                      "QSpinBox::down-button:pressed {\n"
                                      "    border-image: url(:/newPrefix/icon2/pluss3.png);\n"
                                      "}\n"
                                      "QPushButton {\n"
                                      "    background-color: transparent;\n"
                                      "    border: none;\n"
                                      "    border-radius: 7px;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(66, 60, 99);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(28, 28, 28);\n"
                                      "}\n")
        self.frame_book.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_book.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_book.setObjectName(f"frame_book - {Id}")


        # Сетка
        self.gridLayout = QtWidgets.QGridLayout(self.frame_book)
        self.gridLayout.setObjectName("gridLayout")

        # id
        self.id = Id

        # Название
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
        self.gridLayout.addWidget(self.label_name, 1, 1, 1, 1)

        # Автор
        self.label_author = QtWidgets.QLabel(self.frame_book)
        self.label_author.setText(f"Автор: {Author}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.label_author.sizePolicy().hasHeightForWidth())
        self.label_author.setSizePolicy(sizePolicy)
        self.label_author.setStyleSheet("font-size: 7pt;")
        self.label_author.setObjectName("label_author")
        self.gridLayout.addWidget(self.label_author, 3, 1, 1, 1)

        # Издательство
        self.label_publisher = QtWidgets.QLabel(self.frame_book)
        self.label_publisher.setText(f"Издательство: {Publisher}")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.label_publisher.sizePolicy().hasHeightForWidth())
        self.label_publisher.setSizePolicy(sizePolicy)
        self.label_publisher.setStyleSheet("font-size: 7pt;")
        self.label_publisher.setObjectName("label_publisher")
        self.gridLayout.addWidget(self.label_publisher, 4, 1, 1, 2)

        # Серия
        self.label_series = QtWidgets.QLabel(self.frame_book)
        self.label_series.setText(f"Серия: {Series}")
        self.label_series.setStyleSheet("font-size: 7pt;")
        self.label_series.setObjectName("label_series")
        self.gridLayout.addWidget(self.label_series, 5, 1, 1, 1)

        # ISBN
        self.label_ISBN = QtWidgets.QLabel(self.frame_book)
        self.label_ISBN.setText(f"ISBN: {ISBN}")
        self.label_ISBN.setStyleSheet("font-size: 7pt;")
        self.label_ISBN.setObjectName("label_ISBN")
        self.gridLayout.addWidget(self.label_ISBN, 6, 1, 1, 1)

        # Цена
        self.label_price = QtWidgets.QLabel(self.frame_book)
        self.label_price.setText(f"Цена: {Price}")
        self.label_price.setStyleSheet("font-size: 8pt;")
        self.label_price.setObjectName("label_price")
        self.gridLayout.addWidget(self.label_price, 7, 1, 1, 2, QtCore.Qt.AlignRight)

        # Картинка
        self.label_icon = QtWidgets.QLabel(self.frame_book)
        self.label_icon.setMinimumSize(QtCore.QSize(108, 152))
        self.label_icon.setSizeIncrement(QtCore.QSize(108, 152))
        new_img = img.replace("\\", "/")
        self.label_icon.setStyleSheet(f'image: url({new_img});')
        self.label_icon.setObjectName("label_icon")
        self.gridLayout.addWidget(self.label_icon, 1, 0, 10, 1)

        # Купить
        self.pushButton = QtWidgets.QPushButton(self.frame_book)
        self.pushButton.setMinimumHeight(30)
        self.pushButton.setText(" Купить ")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 8, 2, 1, 1)

        # Удалить
        self.pushButton_delete = QtWidgets.QPushButton(self.frame_book)
        self.pushButton_delete.clicked.connect(self.DeleteBook)
        self.pushButton_delete.setMinimumHeight(20)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 0, 2, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

        # Количество
        self.spinBox = QtWidgets.QSpinBox(self.frame_book)
        self.spinBox.valueChanged.connect(lambda: self.EmitPriceTheQuantity())
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(Quantity)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; "
                                "font-weight:600;\">Cколько экземпляров заказать</span></p></body></html>")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)

    def EmitPriceTheQuantity(self):
        Price = self.spinBox.value() * self.Price - self.Price
        self.signal_plus_amount.emit((self.id, Price))

    def DeleteBook(self):
        self.signal_delete.emit((self.frame_book.objectName(), self.id, self.Price))

    from Resources import icon_cwt

