import sqlite3
from PyQt5 import QtCore
from datetime import date

from Modules.DisplayingMessageBox import OpenNotificationDialog


class FunctionsWorkSQLiteUsers(QtCore.QThread):

    info_signal = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.Base = "Resources\\BaseDataLibrary.db"
        self.Table = "users"

    def AuthenticationUsers(self, email: str, password: str) -> str:
        message = ""
        check = False
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {self.Table} WHERE email ='{email}';")
                request_information = cur.fetchone()
            if request_information is None:
                message = "Такого пользователя не существует!"
            elif request_information[3] != password:
                message = "Неверный пароль!"
            elif request_information[3] == password:
                check = True
                message = "Успешная авторизация!"
        except sqlite3.Error as error:
            message = f"Проблема связанная с базой данных\n{error}"
        finally:
            cur.close()
            con.close()

        if check:
            self.info_signal.emit((request_information[1], request_information[2]))
        return message

    def RegistrationUsers(self, name: str, email: str, password: str) -> str:
        message = ""
        check = False
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {self.Table} WHERE email='{email}';")
                request_information = cur.fetchone()
                if request_information is not None:
                    message = "Такой email уже используется!"
                elif request_information is None:
                    con.execute(f"INSERT INTO users (username, email, password, date_registration) "
                                f"VALUES ('{name}', '{email}', '{password}', '{date.today().strftime('%d.%m')}."
                                f"{date.today().year}')")
                    check = True
                    message = "Регистрация успешна!"
        except sqlite3.Error as error:
            message = f"Проблема связанная с базой данных\n{error}"
        finally:
            cur.close()
            con.close()

        if check:
            self.info_signal.emit((name, email))
        return message

    def CheckInfoBookmark(self, email: str) -> tuple:
        info_bookmark = ()
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT bookmark FROM {self.Table} WHERE email='{email}'")
                received_info = cur.fetchone()
            if received_info[0] is not None:
                received_info = ''.join(received_info).split("|")
                if received_info[0] == "":
                    pass
                elif len(received_info) == 1:
                    info_bookmark = (int(''.join(received_info)),)
                elif len(received_info) > 1:
                    info_bookmark = tuple(map(int, received_info))
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()
        return info_bookmark

    def InsertInfoBookmark(self, email: str, bookmark_id: int):
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT bookmark FROM {self.Table} WHERE email='{email}'")
                info_bookmark = cur.fetchone()[0]
                if (info_bookmark is None) or (info_bookmark == ""):
                    con.execute(f"UPDATE {self.Table} SET bookmark='{bookmark_id}' WHERE email='{email}';")
                else:
                    if (str(bookmark_id) in info_bookmark.split("|")) is False:
                        con.execute(f"UPDATE {self.Table} SET bookmark='{bookmark_id}|{info_bookmark}' "
                                    f"WHERE email='{email}';")
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()

    def DeleteBookmarkUsers(self, email: str, bookmark: str):
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT bookmark FROM {self.Table} WHERE email='{email}'")
                info_bookmark = cur.fetchone()[0]
                if len(info_bookmark) == 1:
                    con.execute(f"UPDATE {self.Table} SET bookmark='' WHERE email='{email}';")
                else:
                    new_bookmark = info_bookmark.split('|')
                    new_bookmark.remove(bookmark)
                    new_bookmark = '|'.join(new_bookmark)
                    con.execute(f"UPDATE {self.Table} SET bookmark='{new_bookmark}' WHERE email='{email}';")
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()
