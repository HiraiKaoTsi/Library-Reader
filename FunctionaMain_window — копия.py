from sys import argv, exit
from PyQt5 import QtCore, QtGui, QtWidgets

from main import Ui_MainWindow

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
        self.info_window = [1]

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
        self.ui.pushButton_fold__status_mw.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_expand_status_mw.clicked.connect(self.ExpandWindow)
        self.ui.pushButton_close_status_mw.clicked.connect(lambda: self.close())

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
        self.ui.pushButton_all_bookwark_mw.clicked.connect(self.OpenBookMarks)
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
            self.CheckOpenWindow()
            self.ui.frame_all_book.hide()
            self.ui.frame_info_book.hide()
            self.ui.frame_buy_book.hide()
            self.ui.frame_personal_data.show()
            # запуск информации заполнение
        else:
            self.OpenLoginReg()

    def OpenMainMenu(self):
        self.ui.frame_info_book.hide()
        self.ui.frame_buy_book.hide()
        self.ui.frame_personal_data.hide()
        self.ui.frame_all_book.show()

    def OpenBookMarks(self):
        if self.info_log:
            self.CheckOpenWindow()
            self.ui.frame_info_book.hide()
            self.ui.frame_personal_data.hide()
            self.ui.frame_all_book.hide()
            self.ui.frame_buy_book.show()
        else:
            self.OpenLoginReg()

    def EditUserExit(self):
        self.ui.pushButton_profile_user_mw.setText("Пользователь")
        self.ui.pushButton_exit_user_mw.hide()
        self.ui.frame_personal_data.hide()
        self.ui.frame_all_book.show()
        self.regedit.DeleteInfoUser()
        self.info_log = False
        self.users_mail = None

        self.ClearBooks()
        if self.isMaximized() is False:
            self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks())
        else:
            self.CreateBooks_3col(self.BooksSQL.OpeningTableAllBooks())

    def SearchCreateBook(self, frame_book: tuple):
        print(1)
        print(self)
        print(self.isMaximized())
        if self.isMaximized():
            self.CreateBooks_2col(frame_book)
        else:
            self.CreateBooks_3col(frame_book)

    def ChoiceCreateBookWay2(self):
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

    def ChoiceCreateBook(self):
        if self.info_log:
            if self.isMaximized():
                self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks(self.UsersSQL.CheckInfoBookmark(
                    self.users_mail)))
            else:
                self.CreateBooks_3col(self.BooksSQL.OpeningTableAllBooks(self.UsersSQL.CheckInfoBookmark(
                    self.users_mail)))
        else:
            if self.isMaximized():
                self.CreateBooks_2col(self.BooksSQL.OpeningTableAllBooks())
            else:
                self.CreateBooks_3col(self.BooksSQL.OpeningTableAllBooks())

    # Книги заполнение
    def CreateBooks_2col(self, all_books: tuple):
        col = 0
        row = 0
        for frame in all_books:
            self.ui.gridLayout_11.addWidget(frame, row, col, 1, 1)
            col += 1
            if col == 2:
                col = 0
                row += 1

    def CreateBooks_3col(self, all_books: tuple):
        col = 0
        row = 0
        for frame in all_books:
            self.ui.gridLayout_11.addWidget(frame, row, col, 1, 1)
            col += 1
            if col == 3:
                col = 0
                row += 1

    def ClearBooks(self):
        if self.ui.gridLayout_11 is not None:
            for i in range(self.ui.gridLayout_11.count()):
                item = self.ui.gridLayout_11.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.self.ui.gridLayout_11())
        self.ui.pushButton_reset.hide()
        self.ui.label_you_mean.hide()

    # функционал книг
    def OpenSearchMenu(self):
        if self.ui.frame_search.isHidden():
            self.ui.pushButton_sort.setToolTip("Закрыть сортировку")
            self.ui.frame_search.show()
        else:
            self.ui.pushButton_sort.setToolTip("Открыть сортировку")
            self.ui.frame_search.hide()

    def AddBookmarkByUserSQL(self, info_click: list):
        if self.info_log:
            self.UsersSQL.InsertInfoBookmark(self.users_mail, info_click[0])
            info_click[1].emit(True)
        else:
            self.OpenLoginReg()

    def DeleteBookmarkByUserSQl(self, info_click: list):
        self.UsersSQL.DeleteBookmarkUsers(self.users_mail, str(info_click[0]))
        info_click[1].emit(False)

    def ClearSearchAttributes(self):
        self.ui.lineEdit_search_ab.clear()
        self.ui.lineEdit_author.clear()
        self.ui.lineEdit_publisher.clear()
        self.ui.spinBox_from.setValue(0)
        self.ui.spinBox_to.setValue(96799)
        self.ui.dateEdit_first.setDate(QtCore.QDate(1900, 1, 1))
        self.ui.dateEdit_second.setDate(QtCore.QDate(2023, 1, 1))

    def ResetInfo(self):
        self.ClearBooks()
        self.ClearSearchAttributes()
        self.ChoiceCreateBookWay2()

    def OpenInfoBook(self, Id):

        def ClickBookmark():
            self.UsersSQL.DeleteBookmarkUsers(self.users_mail, str(Id))


        info = self.BooksSQL.SearchInfoById(Id)

        self.CheckOpenWindow()

        self.ui.frame_all_book.hide()
        self.ui.frame_info_book.show()

        self.ui.name_book_ib.setText(info[1])
        self.ui.author_ib.setText(info[2])
        self.ui.publisher_ib.setText(info[3])
        self.ui.series_ib.setText(info[4])
        self.ui.year_publication_ib.setText(f"{info[5]}")
        self.ui.ISBN_ib.setText(f"{info[6]}")
        self.ui.interpreter_ib.setText(info[7])
        self.ui.number_pages_ib.setText(f"{info[8]}")
        self.ui.format_ib.setText(info[9])
        self.ui.cove_type_ib.setText(info[10])
        self.ui.weight_g_ib.setText(f"{info[11]}")
        self.ui.age_restrictions_ib.setText(f"{info[12]}")
        self.ui.quantities_ib.setText(f"{info[13]}")
        self.ui.price_ib.setText(f"Цена: {info[14]}")
        self.ui.img_ib.setPixmap(QtGui.QPixmap(info[15]))
        self.ui.evaluation_ib.setText(f"Оценка: {info[16]}")
        self.ui.description_ib.setText(info[17])

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

        if info[13] == 0:
            self.ui.condition_ib.setText("Нет в наличии!")
            self.ui.pushButton_bookmark_ib.setEnabled(False)
            self.ui.pushButton_arrange_ib.setEnabled(False)
        else:
            self.ui.condition_ib.setText(f"В наличии-{info[13]} шт")
            self.ui.pushButton_bookmark_ib.setEnabled(True)
            self.ui.pushButton_arrange_ib.setEnabled(True)

        if self.info_log:
            if Id in self.UsersSQL.CheckInfoBookmark(self.users_mail):
                self.ui.pushButton_bookmark_ib.clicked.connect(ClickBookmark)
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
        else:
            self.ui.pushButton_bookmark_ib.clicked.connect()

        self.ui.pushButton_bookmark_ib.setIcon(icon)

    # Поиск книг
    def ConclusionSearchInfo(self):
        if self.ui.frame_search.isHidden():
            found_books = self.SearchBookName()
        else:
            found_books = self.SearchBookAllInfo()

        if found_books is not None:
            if len(found_books) != 0:
                self.ClearBooks()
                self.SearchCreateBook(found_books)
                self.ui.pushButton_reset.show()
                self.ui.label_you_mean.show()
            else:
                OpenNotificationDialog("Похоже, у нас такого нет\n"
                                       "Но на всякий случай советуем проверить опечатки в запросе.")

    def SearchBookAllInfo(self):
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

    def SearchBookName(self):

        found_books = None
        name_book = self.ui.lineEdit_search_ab.text().strip().lower()
        if name_book != "":
            if self.users_mail is not None:
                found_books = self.BooksSQL.SearchByNameBook(name_book,
                                                             self.UsersSQL.CheckInfoBookmark(self.users_mail))
            else:
                found_books = self.BooksSQL.SearchByNameBook(name_book)
        print(found_books)
        return found_books

    # Пользователя
    def OpenLoginReg(self):
        logg_reg = FunctionalLoginRegistration()
        logg_reg.infoSQL.info_signal.connect(self.EditUserLogin)
        logg_reg.setWindowModality(QtCore.Qt.ApplicationModal)
        logg_reg.show()
        logg_reg.exec()

    def EditUserLogin(self, info):
        print(1)
        print(info)

        name = info[0]
        email = info[1]
        self.ui.pushButton_profile_user_mw.setText(name)
        self.ui.pushButton_exit_user_mw.show()
        self.ui.name_user.setText(name)
        self.info_log = True
        self.users_mail = email

        self.ClearBooks()
        self.ChoiceCreateBookWay2()


    # Модули
    def CheckRememberUsers(self):
        self.regedit.info_signal.connect(self.CheckRememberUsersBase)
        self.regedit.CheckInfoUser()

    def CheckRememberUsersBase(self, remember_info: tuple):
        self.UsersSQL.info_signal.connect(self.EditUserLogin)
        self.UsersSQL.AuthenticationUsers(remember_info[0], remember_info[1])

    # Верхняя панель
    def ExpandWindow(self):
        self.ClearBooks()

        self.ChoiceCreateBook()

        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_expand_status_mw.setToolTip("Развернуть")
        else:
            self.showMaximized()
            self.ui.pushButton_expand_status_mw.setToolTip("Свернуть в окно")

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
                self.ui.frame_personal_data.show()
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

    # функционал №№№

    def Test(self, info):
        print("yra")


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
