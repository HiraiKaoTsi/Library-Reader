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
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {self.Table} WHERE email ='{email}';")
                request_information = cur.fetchone()
            if request_information is None:
                return "Такого пользователя не существует!"
            elif request_information[3] != password:
                return "Неверный пароль!"
            elif request_information[3] == password:
                self.info_signal.emit((request_information[1], request_information[2]))
                return "Успешная авторизация!"
        except sqlite3.Error as error:
            return f"Проблема связанная с базой данных\n{error}"
        finally:
            cur.close()
            con.close()

    def RegistrationUsers(self, name: str, email: str, password: str) -> str:
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT * FROM {self.Table} WHERE email='{email}';")
                request_information = cur.fetchone()
                if request_information is not None:
                    return "Такой email уже используется!"
                elif request_information is None:
                    con.execute(f"INSERT INTO users (username, email, password, date_registration) "
                                f"VALUES ('{name}', '{email}', '{password}', '{date.today().strftime('%d.%m')}."
                                f"{date.today().year}')")
                    self.info_signal.emit((name, email))
                    return "Регистрация успешна!"
        except sqlite3.Error as error:
            return f"Проблема связанная с базой данных\n{error}"
        finally:
            cur.close()
            con.close()

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
            return f"Проблема связанная с базой данных\n{error}"
        finally:
            cur.close()
            con.close()


    def CheckInfoBookmark(self, email: str) -> tuple:
        info_bookmark = ()
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT bookmark FROM {self.Table} WHERE email='{email}'")
                received_info = cur.fetchone()
            if received_info[0] is not None:
                received_info = ''.join(received_info).split("|")
                info_bookmark = map(int, received_info)
        except sqlite3.Error as error:
            OpenNotificationDialog(f"Проблема связанная с базой данных\n{error}")
        finally:
            cur.close()
            con.close()

        return tuple(info_bookmark)

    def DeleteBookmarkUsers(self, email: str, bookmark: str):
        try:
            with sqlite3.connect(self.Base) as con:
                cur = con.cursor()
                cur.execute(f"SELECT bookmark FROM {self.Table} WHERE email='{email}'")
                info_bookmark = cur.fetchone()[0]
                edit_bookmark = info_bookmark.split('|').remove(bookmark)
                con.execute(f"UPDATE {self.Table} SET bookmark='{edit_bookmark}' WHERE email='{email}';")
        except sqlite3.Error as error:
            return f"Проблема связанная с базой данных\n{error}"
        finally:
            cur.close()
            con.close()
