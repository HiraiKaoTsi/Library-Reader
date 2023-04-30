from PyQt5 import QtCore

from DialogWindow.notification.FunctionalNotigication import FunctionalNotification
from DialogWindow.confirmation.FunctionalConfirmation import FunctionalConfirmation
from DialogWindow.reference.FunctionalReference import FunctionalReference
from DialogWindow.assistance.FunctionalAssistance import FunctionalAssistance


def OpenNotificationDialog(main_text):
    notification = FunctionalNotification()
    notification.ui.label.setText(f"{main_text}")
    notification.setWindowModality(QtCore.Qt.ApplicationModal)
    notification.show()
    notification.exec()


def DialogConfirmation(method, main_text):
    confirmation = FunctionalConfirmation()
    confirmation.info_signal.connect(method)
    confirmation.ui.label.setText(f"{main_text}")
    confirmation.setWindowModality(QtCore.Qt.ApplicationModal)
    confirmation.show()
    confirmation.exec()


def OpenReference():
    reference = FunctionalReference()
    reference.setWindowModality(QtCore.Qt.ApplicationModal)
    reference.show()
    reference.exec()


def OpenAssistance():
    assistance = FunctionalAssistance()
    assistance.setWindowModality(QtCore.Qt.ApplicationModal)
    assistance.show()
