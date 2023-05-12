from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

from main_interface import Ui_MainWindow

from DialogWindow.login_registration.FunctionalLoginRegistration import FunctionalLoginRegistration

from Modules.DisplayingMessageBox import *
from Modules.FunctionalBookSQL import GettingInformationSQLBooks
from Modules.FunctionalRegedit import FunctionalRegedit
from Modules.FunctionalSQLiteUser import FunctionsWorkSQLiteUsers


class FunctionalMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # До настройки (скрытие лишних объектов)
        self.ui.frame_info_book.hide()
        self.ui.frame_buy_book.hide()
        self.ui.frame_search.hide()
        self.ui.label_you_mean.hide()
        self.ui.pushButton_exit_user_mw.hide()
        self.ui.pushButton_reset.hide()
        self.ui.frame_personal_data.hide()

        # Переменные
        self.old_pos = None
        self.info_log = False
        self.users_mail = None
        self.users_name = ""
        self.info_window = [1]
        self.info_search_book = False
        self.bookmark_more_details = None
        self.book_event_info = "A"
        self.sum = 0
        self.price_bookmark = {}

        # Модули
        self.regedit = FunctionalRegedit()
        self.UsersSQL = FunctionsWorkSQLiteUsers()
        self.BooksSQL = GettingInformationSQLBooks(self.OpenInfoBook, self.AddBookmarkByUserSQL,
                                                   self.DeleteBookmarkByUserSQl)

        # Стартовые запуск методов
        self.CheckRememberUsers()

        if self.users_mail is not None:
            self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks(self.UsersSQL.CheckInfoBookmark(self.users_mail)))
        else:
            self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks())

        # Шапка
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_fold__status_mw.clicked.connect(self.showMinimized)
        self.ui.pushButton_expand_status_mw.clicked.connect(self.ExpandWindow)
        self.ui.pushButton_close_status_mw.clicked.connect(self.close)

        # Кнопка меню пользователя
        self.ui.pushButton_fold_user_mw.clicked.connect(self.ShowHideMenu)
        self.ui.pushButton_menu_ab.clicked.connect(self.ShowHideMenu)
        self.ui.pushButton_menu_ib.clicked.connect(self.ShowHideMenu)
        self.ui.pushButton_menu_bb.clicked.connect(self.ShowHideMenu)
        self.ui.pushButton_menu_pd.clicked.connect(self.ShowHideMenu)

        # Функционал кнопок меню пользователя
        self.ui.pushButton_profile_user_mw.clicked.connect(self.UseButtonUsers)
        self.ui.pushButton_main_menu_mw.clicked.connect(self.OpenMainMenu)
        # setting
        self.ui.pushButton_reference_user_mw.clicked.connect(OpenReference)
        self.ui.pushButton_help_user_mw.clicked.connect(OpenAssistance)
        self.ui.pushButton_all_bookwark_mw.clicked.connect(self.ClickBookmark)
        self.ui.pushButton_exit_user_mw.clicked.connect(lambda: DialogConfirmation(self.EditUserExit, "Выйти из "
                                                                                                      "аккаунта"))

        # Кнопка назад
        self.ui.pushButton_back_bb.clicked.connect(self.BackButton)
        self.ui.pushButton_back_ib.clicked.connect(self.BackButton)
        self.ui.pushButton_back_pd.clicked.connect(self.BackButton)

        # Основное окно с книгами бинды
        self.ui.pushButton_sort.clicked.connect(self.OpenSearchMenu)
        self.ui.pushButton_close_status_mw_2.clicked.connect(self.OpenSearchMenu)
        self.ui.pushButton_search.clicked.connect(self.ConclusionSearchInfo)
        self.ui.pushButton_search_sort.clicked.connect(self.ConclusionSearchInfo)
        self.ui.lineEdit_search_ab.returnPressed.connect(self.ConclusionSearchInfo)
        self.ui.pushButton_clear.clicked.connect(self.ClearSearchAttributes)
        self.ui.pushButton_reset.clicked.connect(self.ResetInfo)

        # More-details бинд
        self.ui.pushButton_arrange_ib.clicked.connect(self.MoreDetailsPlaceOrder)
        self.ui.pushButton_bookmark_ib.clicked.connect(self.MoreDetailsBookmark)

    # menu users
    def ShowHideMenu(self):
        if self.ui.frame_menu_mw.isHidden():
            self.ui.frame_menu_mw.show()
            self.ui.pushButton_menu_ab.setToolTip("Скрыть меню пользователя")
            self.ui.pushButton_menu_ib.setToolTip("Скрыть меню пользователя")
            self.ui.pushButton_menu_bb.setToolTip("Скрыть меню пользователя")
        else:
            self.ui.frame_menu_mw.hide()
            self.ui.pushButton_menu_ab.setToolTip("Раскрыть меню пользователя")
            self.ui.pushButton_menu_ib.setToolTip("Раскрыть меню пользователя")
            self.ui.pushButton_menu_bb.setToolTip("Раскрыть меню пользователя")

    def UseButtonUsers(self):
        if self.info_log:
            self.OpenProfileUsers()
        else:
            self.OpenLoginReg()

    def OpenProfileUsers(self):
        self.CheckOpenWindow()
        self.ui.frame_all_book.hide()
        self.ui.frame_info_book.hide()
        self.ui.frame_buy_book.hide()
        self.ui.frame_personal_data.show()

        self.ui.name_user.setText(self.users_name)
        self.ui.lineEdit_name.setText(self.users_name)
        self.ui.lineEdit_mail.setText(self.users_mail)

    def OpenMainMenu(self):
        self.ui.frame_info_book.hide()
        self.ui.frame_buy_book.hide()
        self.ui.frame_personal_data.hide()
        self.ui.frame_all_book.show()

    def ClickBookmark(self):
        if self.info_log:
            self.OpenBookmark()
        else:
            self.OpenLoginReg()
            if self.info_log:
                self.OpenBookmark()

    def OpenBookmark(self):
        self.CheckOpenWindow()
        self.ClearBooksBookmark()
        self.CreateBooksBookmark()
        self.ui.frame_info_book.hide()
        self.ui.frame_personal_data.hide()
        self.ui.frame_all_book.hide()
        self.ui.frame_buy_book.show()

    def EditUserExit(self):
        self.ui.pushButton_profile_user_mw.setText("Пользователь")

        self.ui.pushButton_exit_user_mw.hide()
        self.ui.frame_personal_data.hide()
        self.ui.frame_buy_book.hide()

        if self.ui.frame_all_book.isHidden() is False:
            self.info_window = [1]
        elif self.ui.frame_info_book.isHidden() is False:
            self.info_window = [1, 2]
        else:
            self.ui.frame_all_book.show()
            self.info_window = [1]

        self.info_log = False
        self.users_mail = None

        self.regedit.DeleteInfoUser()
        self.MoreDetailsEditAtLoginOrExitUsers()
        self.ClearBooks()
        self.ChoiceCreateBook()

    # Выбор заполнения
    def SearchCreateBook(self, frame_book: tuple[QtWidgets.QFrame, ...]):
        if self.isMaximized() is False:
            self.CreateBooks_2col(frame_book)
        else:
            self.CreateBooks_3col(frame_book)

    def ChoiceCreateBook(self):
        self.ClearBooks()
        try:
            if self.info_search_book:
                self.SearchCreateBook(self.SearchBookAllInfo())
            else:
                if self.info_log:
                    if self.isMaximized() is False:
                        self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks(self.UsersSQL.CheckInfoBookmark(
                            self.users_mail)))
                    else:
                        self.CreateBooks_3col(self.BooksSQL.OpeningTableAllBooks(self.UsersSQL.CheckInfoBookmark(
                            self.users_mail)))
                else:
                    if self.isMaximized() is False:
                        self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks())
                    else:
                        self.CreateBooks_3col(self.BooksSQL.OpeningTableAllBooks())
        except:
            self.ResetInfo()

    # Книги создание(выставление)
    def CreateBooks_2col(self, frame_book: tuple[QtWidgets.QFrame, ...]):
        col = 0
        row = 0
        for frame in frame_book:
            self.ui.gridLayout_11.addWidget(frame, row, col, 1, 1)
            col += 1
            if col == 2:
                col = 0
                row += 1

    def CreateBooks_3col(self, frame_book: tuple[QtWidgets.QFrame, ...]):
        col = 0
        row = 0
        for frame in frame_book:
            self.ui.gridLayout_11.addWidget(frame, row, col, 1, 1)
            col += 1
            if col == 3:
                col = 0
                row += 1

    def CreateBooksBookmark(self):
        self.sum = 0
        self.ui.frame_bb_info.show()
        bookmark = self.UsersSQL.CheckInfoBookmark(self.users_mail)
        if len(bookmark) >= 1:
            self.ui.label_info_bb.hide()
            frame = self.BooksSQL.SearchBooksByIdBookmark(bookmark, self.DefaultSumBookmark, self.PlusSumBookmark,
                                                          self.DeleteBookmarkFrameAndInfo)
            for i in range(len(frame)):
                self.ui.verticalLayout_4.addWidget(frame[i], i, QtCore.Qt.AlignTop)
        else:
            self.ui.frame_bb_info.hide()
            self.ui.label_info_bb.show()

    def ClearBooksBookmark(self):
        if self.ui.verticalLayout_4 is not None:
            for i in range(self.ui.verticalLayout_4.count()):
                item = self.ui.verticalLayout_4.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.self.ui.verticalLayout_4())

    def ClearBooks(self):
        if self.ui.gridLayout_11 is not None:
            for i in range(self.ui.gridLayout_11.count()):
                item = self.ui.gridLayout_11.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.self.ui.gridLayout_11())

    # Цена для Bookmark
    def DefaultSumBookmark(self, plus_price: int):
        self.sum += plus_price
        self.ui.label_price_bb.setText(f"{self.sum}")

    def PlusSumBookmark(self, info: tuple[int, int]):
        self.price_bookmark[info[0]] = info[1]
        add_price = 0
        for value in self.price_bookmark.values():
            add_price += value
        self.ui.label_price_bb.setText(f"{self.sum + add_price}")

    # функционал поиска
    def OpenSearchMenu(self):
        if self.ui.frame_search.isHidden():
            self.ui.pushButton_sort.setToolTip("Закрыть сортировку")
            self.ui.frame_search.show()
        else:
            self.ui.pushButton_sort.setToolTip("Открыть сортировку")
            self.ui.frame_search.hide()

    def ConclusionSearchInfo(self):
        if self.ui.frame_search.isHidden():
            found_books = self.SearchBookName()
        else:
            found_books = self.SearchBookAllInfo()

        self.info_search_book = found_books

        if found_books is not None:
            if len(found_books) != 0:
                self.ClearBooks()
                self.SearchCreateBook(found_books)
                self.info_search_book = True
                self.ui.pushButton_reset.show()
                self.ui.label_you_mean.show()
            else:
                OpenNotificationDialog("Похоже, у нас такого нет\n"
                                       "Но на всякий случай советуем проверить опечатки в запросе.")

    def SearchBookAllInfo(self) -> tuple[QtWidgets.QFrame, ...]:

        found_books = None
        name_book = self.ui.lineEdit_search_ab.text().strip().lower()
        author = self.ui.lineEdit_author.text().strip().lower()
        publisher = self.ui.lineEdit_publisher.text().strip().lower()
        price_from = self.ui.spinBox_from.value()
        price_to = self.ui.spinBox_to.value()
        date_from = self.ui.dateEdit_first.date().year()
        date_to = self.ui.dateEdit_second.date().year()

        if (name_book != "") or (author != "") or (publisher != "") or \
                (price_from != 0 or price_to != 96799) or (date_from != 1900 or date_to != 2023):

            if self.info_log:
                found_books = self.BooksSQL.SearchByAllCategoriesBooks(name_book, author, price_from, price_to,
                                                                       publisher, date_from, date_to,
                                                                       self.UsersSQL.CheckInfoBookmark(self.users_mail))
            else:
                found_books = self.BooksSQL.SearchByAllCategoriesBooks(name_book, author, price_from, price_to,
                                                                       publisher, date_from, date_to)
        return found_books

    def SearchBookName(self) -> tuple[QtWidgets.QFrame, ...]:
        found_books = None
        name_book = self.ui.lineEdit_search_ab.text().strip().lower()
        if name_book != "":
            if self.users_mail is not None:
                found_books = self.BooksSQL.SearchByNameBook(name_book,
                                                             self.UsersSQL.CheckInfoBookmark(self.users_mail))
            else:
                found_books = self.BooksSQL.SearchByNameBook(name_book)

        return found_books

    def ClearSearchAttributes(self):
        self.ui.lineEdit_search_ab.clear()
        self.ui.lineEdit_author.clear()
        self.ui.lineEdit_publisher.clear()
        self.ui.spinBox_from.setValue(0)
        self.ui.spinBox_to.setValue(96799)
        self.ui.dateEdit_first.setDate(QtCore.QDate(1900, 1, 1))
        self.ui.dateEdit_second.setDate(QtCore.QDate(2023, 1, 1))

    def ResetInfo(self):
        self.info_search_book = False
        self.ClearSearchAttributes()
        self.ChoiceCreateBook()
        self.ui.pushButton_reset.hide()
        self.ui.label_you_mean.hide()

    # Закладки база данных
    def AddBookmarkByUserSQL(self, info_click: list):
        if self.info_log:
            self.UsersSQL.InsertInfoBookmark(self.users_mail, info_click[0])
            info_click[1].emit(True)
        else:
            self.OpenLoginReg()

    def DeleteBookmarkByUserSQl(self, info_click: list):
        self.UsersSQL.DeleteBookmarkUsers(self.users_mail, str(info_click[0]))
        info_click[1].emit(False)

    def DeleteBookmarkFrameAndInfo(self, info: tuple[str, int, int]):
        if self.ui.verticalLayout_4 is not None:
            for i in range(self.ui.verticalLayout_4.count()):
                item = self.ui.verticalLayout_4.itemAt(i)
                widget = item.widget()
                frame_name = widget.objectName()
                if info[0] == frame_name:
                    if widget is not None:
                        widget.deleteLater()
                        break

        self.UsersSQL.DeleteBookmarkUsers(self.users_mail, f"{info[1]}")
        self.ChoiceCreateBook()
        if info[1] == self.bookmark_more_details:
            self.AzureButtonBookmark()

        self.sum = self.sum - info[2]
        self.PlusSumBookmark((info[1], 0))

        if self.sum == 0:
            self.ui.label_info_bb.show()
            self.ui.frame_bb_info.hide()

    # Информация о книге
    def MoreDetailsPlaceOrder(self):
        print(self.bookmark_more_details)

    def MoreDetailsBookmark(self):
        if self.info_log:
            if self.book_event_info == "A":
                self.UsersSQL.InsertInfoBookmark(self.users_mail, self.bookmark_more_details)
                self.RedButtonBookmark()
                self.ChoiceCreateBook()
            elif self.book_event_info == "R":

                self.UsersSQL.DeleteBookmarkUsers(self.users_mail, f"{self.bookmark_more_details}")
                self.AzureButtonBookmark()
                self.ChoiceCreateBook()
        else:
            self.OpenLoginReg()
            if self.info_log:
                self.UsersSQL.InsertInfoBookmark(self.users_mail, self.bookmark_more_details)
                self.RedButtonBookmark()
                self.ChoiceCreateBook()

    def OpenInfoBook(self, Id: int):
        self.bookmark_more_details = Id

        book_info = self.BooksSQL.SearchInfoById(Id)

        self.MoreDetailsEditAtLoginOrExitUsers()
        self.CheckOpenWindow()

        self.ui.frame_all_book.hide()
        self.ui.frame_info_book.show()

        self.ui.name_book_ib.setText(book_info[1])
        self.ui.author_ib.setText(book_info[2])
        self.ui.publisher_ib.setText(book_info[3])
        self.ui.series_ib.setText(book_info[4])
        self.ui.year_publication_ib.setText(f"{book_info[5]}")
        self.ui.ISBN_ib.setText(f"{book_info[6]}")
        self.ui.interpreter_ib.setText(book_info[7])
        self.ui.number_pages_ib.setText(f"{book_info[8]}")
        self.ui.format_ib.setText(book_info[9])
        self.ui.cove_type_ib.setText(book_info[10])
        self.ui.weight_g_ib.setText(f"{book_info[11]}")
        self.ui.age_restrictions_ib.setText(f"{book_info[12]}")
        self.ui.quantities_ib.setText(f"{book_info[13]}")
        self.ui.price_ib.setText(f"Цена: {book_info[14]}")
        self.ui.img_ib.setPixmap(QtGui.QPixmap(book_info[15]))
        self.ui.evaluation_ib.setText(f"Оценка: {book_info[16]}")
        self.ui.description_ib.setText(book_info[17])

        if book_info[13] == 0:
            self.ui.condition_ib.setText("Нет в наличии!")
            self.ui.pushButton_bookmark_ib.setEnabled(False)
            self.ui.pushButton_arrange_ib.setEnabled(False)
        else:
            self.ui.condition_ib.setText(f"В наличии-{book_info[13]} шт")
            self.ui.pushButton_bookmark_ib.setEnabled(True)
            self.ui.pushButton_arrange_ib.setEnabled(True)

    def MoreDetailsEditAtLoginOrExitUsers(self):
        if self.info_log:
            if self.bookmark_more_details is not None:
                if self.bookmark_more_details in self.UsersSQL.CheckInfoBookmark(self.users_mail):
                    self.RedButtonBookmark()
                else:
                    self.AzureButtonBookmark()
            else:
                self.AzureButtonBookmark()
        else:
            self.AzureButtonBookmark()

    def AzureButtonBookmark(self):
        self.book_event_info = "A"
        self.ui.pushButton_bookmark_ib.setStyleSheet("QPushButton {\n"
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

        self.ui.pushButton_bookmark_ib.setToolTip("<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:12pt; font-weight:600;\">Добавить книгу в "
                                                  "закладки</span></p></body></html>")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/bookmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.pushButton_bookmark_ib.setIcon(icon)

    def RedButtonBookmark(self):
        self.book_event_info = "R"
        self.ui.pushButton_bookmark_ib.setStyleSheet("QPushButton {\n"
                                                     "    background-color: rgb(203, 25, 25);\n"
                                                     "    border: none;\n"
                                                     "    border-radius: 7px;\n"
                                                     "}\n"
                                                     "QPushButton:hover {\n"
                                                     "    background-color: rgb(226, 41, 41);\n"
                                                     "}\n"
                                                     "QPushButton:pressed {\n"
                                                     "    background-color: rgb(175, 33, 33);\n"
                                                     "}\n"
                                                     "QPushButton:disabled {\n"
                                                     "	    background-color: rgba(144,144,144);\n"
                                                     "}")
        self.ui.pushButton_bookmark_ib.setToolTip("<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:12pt; font-weight:600;\">Удалить книгу из "
                                                  "закладок</span></p></body></html>")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icon2/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.pushButton_bookmark_ib.setIcon(icon)

    # Пользователя
    def OpenLoginReg(self):
        logg_reg = FunctionalLoginRegistration()
        logg_reg.infoSQL.info_signal.connect(self.EditUserLogin)
        logg_reg.setWindowModality(QtCore.Qt.ApplicationModal)
        logg_reg.show()
        logg_reg.exec()

    def EditUserLogin(self, info: tuple[str, str]):
        name = info[0]
        email = info[1]
        self.ui.pushButton_profile_user_mw.setText(name)
        self.ui.pushButton_exit_user_mw.show()
        self.ui.name_user.setText(name)
        self.info_log = True
        self.bookmark_more_details = None
        self.users_mail = email
        self.users_name = name

        self.MoreDetailsEditAtLoginOrExitUsers()
        self.ChoiceCreateBook()

    # Модули при заходе в программу
    def CheckRememberUsers(self):
        self.regedit.info_signal.connect(self.CheckRememberUsersBase)
        self.regedit.CheckInfoUser()

    def CheckRememberUsersBase(self, remember_info: tuple[str, str]):
        self.UsersSQL.info_signal.connect(self.EditUserLogin)
        self.UsersSQL.AuthenticationUsers(remember_info[0], remember_info[1])

    # Верхняя панель
    def ExpandWindow(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_expand_status_mw.setToolTip("Развернуть")
        else:
            self.showMaximized()
            self.ui.pushButton_expand_status_mw.setToolTip("Свернуть в окно")

        self.ChoiceCreateBook()

    # Функционал окон
    def CheckOpenWindow(self):
        if self.ui.all_book.isHidden() is False:
            self.info_window = [1]
        if self.ui.frame_info_book.isHidden() is False:
            self.info_window.append(2)
        elif self.ui.frame_buy_book.isHidden() is False:
            self.info_window.append(3)
        elif self.ui.frame_personal_data.isHidden() is False:
            self.info_window.append(4)

    def BackButton(self):
        self.ui.frame_all_book.hide()
        self.ui.frame_info_book.hide()
        self.ui.frame_buy_book.hide()
        self.ui.frame_personal_data.hide()

        if len(self.info_window) > 1:
            if self.info_window[-1] == 1:
                self.ui.frame_all_book.show()
                self.info_window.pop(-1)

            elif self.info_window[-1] == 2:
                self.ui.frame_info_book.show()
                self.info_window.pop(-1)

            elif self.info_window[-1] == 3:
                self.ui.frame_buy_book.show()
                self.info_window.pop(-1)

            elif self.info_window[-1] == 4:
                self.OpenProfileUsers()
                self.info_window.pop(-1)
        else:
            self.ui.frame_all_book.show()

    # Перемещение окна
    def mousePressEvent(self, event):
        if self.isMaximized() is False:
            if event.button() == QtCore.Qt.LeftButton:
                self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if self.isMaximized() is False:
            if event.button() == QtCore.Qt.LeftButton:
                self.old_pos = None

    def mouseMoveEvent(self, event):
        if self.isMaximized() is False:
            if not self.old_pos:
                return
            delta = event.pos() - self.old_pos
            self.move(self.pos() + delta)


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
