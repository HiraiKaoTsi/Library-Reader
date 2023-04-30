from PyQt5 import QtCore, QtWidgets

from DialogWindow.login_registration.loginReg_dialog import Ui_LoginRegistration

from Modules.DisplayingMessageBox import OpenNotificationDialog
from Modules.FunctionalSQLiteUser import FunctionsWorkSQLiteUsers
from Modules.FunctionalRegedit import FunctionalRegedit


class FunctionalLoginRegistration(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_LoginRegistration()
        self.ui.setupUi(self)

        # Модули
        self.infoSQL = FunctionsWorkSQLiteUsers()
        self.regedit = FunctionalRegedit()

        # Для перемещения
        self.old_pos = None

        # Шапка
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_close_status.clicked.connect(lambda: self.close())

        # Дона стройка
        self.ui.frame_registr.hide()

        # Показать / спрятать пароль
        self.ui.pushButton_hide_password_1.pressed.connect(lambda: self.ui.lineEdit_password_log.
                                                           setEchoMode(QtWidgets.QLineEdit.Normal))
        self.ui.pushButton_hide_password_1.clicked.connect(lambda: self.ui.lineEdit_password_log.
                                                           setEchoMode(QtWidgets.QLineEdit.Password))

        self.ui.pushButton_hide_password_2.pressed.connect(lambda: self.ui.lineEdit_password1_reg.
                                                           setEchoMode(QtWidgets.QLineEdit.Normal))
        self.ui.pushButton_hide_password_2.clicked.connect(lambda: self.ui.lineEdit_password1_reg.
                                                           setEchoMode(QtWidgets.QLineEdit.Password))

        # Кнопки функционала
        self.ui.pushButton_register.clicked.connect(self.EditWindowRegister)
        self.ui.pushButton_back.clicked.connect(self.EditWindowLogin)
        self.ui.pushButton_login.clicked.connect(self.Login)
        self.ui.pushButton_register_reg.clicked.connect(self.Registration)

    def Login(self):
        check_info = self.CheckingFullInput(self.ui.lineEdit_email_log, self.ui.lineEdit_password_log)
        if check_info is True:
            info = self.infoSQL.AuthenticationUsers(self.ui.lineEdit_email_log.text(),
                                                    self.ui.lineEdit_password_log.text())
            OpenNotificationDialog(info)
            if info == "Успешная авторизация!":
                if self.ui.radioButton_save_log.isChecked():
                    self.regedit.CreateInfoUsers(self.ui.lineEdit_email_log.text(),
                                                 self.ui.lineEdit_password_log.text())
                self.close()

    def Registration(self):
        check_info = self.CheckingFullInput(self.ui.lineEdit_name, self.ui.lineEdit_email_reg,
                                            self.ui.lineEdit_password1_reg, self.ui.lineEdit_password_reg)
        if check_info is True:
            if self.CheckingInputSymbols(self.ui.lineEdit_name, self.ui.lineEdit_email_reg,
                                         self.ui.lineEdit_password1_reg, self.ui.lineEdit_password_reg):
                if self.ComparingPasswords(self.ui.lineEdit_password1_reg.text(), self.ui.lineEdit_password_reg.text()):
                    OpenNotificationDialog("Пароли не совпадают!")
                else:
                    info = self.infoSQL.RegistrationUsers(self.ui.lineEdit_name.text(),
                                                          self.ui.lineEdit_email_reg.text(),
                                                          self.ui.lineEdit_password1_reg.text())
                    OpenNotificationDialog(info)
                    if info == "Регистрация успешна!":
                        if self.ui.radioButton_save_reg.isChecked():
                            print(1)
                            self.regedit.CreateInfoUsers(self.ui.lineEdit_email_reg.text(),
                                                         self.ui.lineEdit_password1_reg.text())
                        self.close()

    @staticmethod
    def CheckingInputSymbols(*args):
        info = True
        flag = False
        for obj in args:
            for symbol in obj.text():
                if symbol in ("#", "$", "%", "^", "*", "!", "/", "|", "\\", "-", "+", "=", "(", ")", "?", ","):
                    info = False
                    flag = True
                    OpenNotificationDialog(f"Имеются запрещенные символы в {obj.objectName()}!")
                    break
            if flag:
                break
        return info

    @staticmethod
    def ComparingPasswords(first_password, second_password):
        if first_password != second_password:
            return True
        else:
            return False

    def CheckingFullInput(self, *args):
        flag = True
        for obj in args:
            if obj.text().strip() == '':
                self.BlinkingTextField(obj)
                flag = False
                break
        return flag

    @staticmethod
    def BlinkingTextField(filed):
        time = 0
        for quantity in range(3):
            QtCore.QTimer.singleShot(time := time + 400,
                                     lambda: filed.setStyleSheet("border: 2px solid red;"))
            QtCore.QTimer.singleShot(time := time + 400,
                                     lambda: filed.setStyleSheet("border: 1px solid #54026E;"))


    def EditWindowRegister(self):
        self.ClearInfo()
        self.ui.label_name.setText("Регистрация")
        self.setWindowTitle("Регистрация")
        self.ui.frame_login.hide()
        self.ui.frame_button.hide()
        self.ui.frame_registr.show()

    def EditWindowLogin(self):
        self.ClearInfo()
        self.ui.label_name.setText("Вход")
        self.setWindowTitle("Вход")
        self.ui.frame_registr.hide()
        self.ui.frame_login.show()
        self.ui.frame_button.show()

    def ClearInfo(self):
        self.ui.radioButton_save_reg.setChecked(False)
        self.ui.radioButton_save_log.setChecked(False)
        self.ui.lineEdit_email_log.setText("")
        self.ui.lineEdit_password_log.setText("")
        self.ui.lineEdit_name.setText("")
        self.ui.lineEdit_email_reg.setText("")
        self.ui.lineEdit_password1_reg.setText("")
        self.ui.lineEdit_password_reg.setText("")

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
