from PyQt5 import QtCore, QtWidgets

from DialogWindow.confirmation.confirmation_dialog import Ui_Confirmation


class FunctionalConfirmation(QtWidgets.QDialog):

    info_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Confirmation()
        self.ui.setupUi(self)

        self.old_pos = None

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_close_status.clicked.connect(lambda: self.close())
        self.ui.pushButton_ok.clicked.connect(self.Confirmation)
        self.ui.pushButton_close.clicked.connect(lambda: self.close())

    def Confirmation(self):
        self.info_signal.emit()
        self.close()

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
