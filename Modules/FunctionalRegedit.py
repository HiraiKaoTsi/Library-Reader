import winreg as wrg
from PyQt5 import QtCore


from Modules.DisplayingMessageBox import OpenNotificationDialog


class FunctionalRegedit(QtCore.QThread):

    info_signal = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.location = wrg.HKEY_CURRENT_USER
        self.name_chapter = "Library-Reader"

    def CreateInfoUsers(self, email: str, password: str):
        key = False
        try:
            key = wrg.CreateKey(self.location, self.name_chapter)
            wrg.SetValueEx(key, "Email", 0, wrg.REG_SZ, f"{email}")
            wrg.SetValueEx(key, "Password", 0, wrg.REG_SZ, f"{password}")
        except wrg.error as error:
            OpenNotificationDialog(f"Ошибка сохранить данные не удалось \n{error}")
        finally:
            self.CloseFolder(key)

    def CheckInfoUser(self):
        soft = False
        try:
            soft = wrg.OpenKeyEx(self.location, self.name_chapter)
            email = wrg.QueryValueEx(soft, "Email")[0]
            password = wrg.QueryValueEx(soft, "Password")[0]
            self.info_signal.emit((email, password))
        except wrg.error:
            pass
        finally:
            self.CloseFolder(soft)

    def DeleteInfoUser(self):
        key = False
        try:
            key = wrg.CreateKey(self.location, self.name_chapter)
            wrg.DeleteValue(key, "Email")
            wrg.DeleteValue(key, "Password")
        except wrg.error:
            pass
        finally:
            self.CloseFolder(key)

    @staticmethod
    def CloseFolder(object_to_close):
        if object_to_close:
            wrg.CloseKey(object_to_close)

