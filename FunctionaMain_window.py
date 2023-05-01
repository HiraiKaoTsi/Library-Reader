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
        # self.BooksSQL = GettingInformationSQLBooks(self.OpenInfoBook, self.AddBookmarkByUserSQL,
        #                                            self.DeleteBookmarkByUserSQl)

        self.ui.pushButton_profile_user_mw.clicked.connect(self.UseButtonUsers)
        # Стартовые запуск методов
        self.CheckRememberUsers()

    def UseButtonUsers(self):
        if self.info_log:
            print(1)
            # self.CheckOpenWindow()
            self.ui.frame_all_book.hide()
            self.ui.frame_info_book.hide()
            self.ui.frame_buy_book.hide()
            self.ui.frame_personal_data.show()
            # запуск информации заполнение
        else:
            self.OpenLoginReg()

    def OpenLoginReg(self):
        logg_reg = FunctionalLoginRegistration()
        logg_reg.infoSQL.info_signal.connect(self.EditUserLogin)
        logg_reg.setWindowModality(QtCore.Qt.ApplicationModal)
        logg_reg.show()
        logg_reg.exec()

    def EditUserLogin(self, info):
        print(info)
        name = info[0]
        email = info[1]
        self.ui.pushButton_profile_user_mw.setText(name)
        self.ui.pushButton_exit_user_mw.show()
        self.info_log = True
        self.users_mail = email


    def CheckRememberUsers(self):
        self.regedit.info_signal.connect(self.CheckRememberUsersBase)
        self.regedit.CheckInfoUser()

    def CheckRememberUsersBase(self, remember_info: tuple):
        self.UsersSQL.info_signal.connect(self.EditUserLogin)
        self.UsersSQL.AuthenticationUsers(remember_info[0], remember_info[1])


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = FunctionalMainWindow()
    myapp.show()
    exit(app.exec_())
