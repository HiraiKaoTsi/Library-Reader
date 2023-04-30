from PyQt5 import QtCore, QtWidgets

from DialogWindow.notification.notification_dialog import Ui_Notification


class FunctionalNotification(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Notification()
        self.ui.setupUi(self)

        self.old_pos = None

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_close_status.clicked.connect(lambda: self.close())
        self.ui.pushButton_ok.clicked.connect(lambda: self.close())

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
