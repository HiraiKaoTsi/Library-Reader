from PyQt5 import QtCore, QtWidgets

from DialogWindow.assistance.assistance_dialog import Ui_Dialog_assistance
from DialogWindow.confirmation.FunctionalConfirmation import FunctionalConfirmation


class FunctionalAssistance(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_Dialog_assistance()
        self.ui.setupUi(self)

        self.old_pos = None

        self.img = None

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.pushButton_close_status.clicked.connect(lambda: self.close())

        self.ui.lineEdit_name.returnPressed.connect(self.ChangingNextTextFields)
        self.ui.pushButton_review.clicked.connect(self.ReviewImg)
        self.ui.pushButton_send.clicked.connect(self.DialogConfirmation)

    def ChangingNextTextFields(self):
        self.ui.lineEdit_name.focusNextPrevChild(False)

    def ReviewImg(self):
        self.img, expansion = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.png *.jpeg '
                                                                                             '*.jpg )')
        if len(self.img) > 86:
            self.img = f"{self.img[:86]}\n{self.img[86:]}"
        self.ui.label_way.setText(self.img)


    def DialogConfirmation(self):
        confirmation = FunctionalConfirmation()
        confirmation.info_signal.connect(self.SendInfo)
        confirmation.ui.label.setText("Отправить?")
        confirmation.setWindowModality(QtCore.Qt.ApplicationModal)
        confirmation.show()
        confirmation.exec()

    def SendInfo(self):
        name = self.ui.lineEdit_name
        description = self.ui.textEdit_description
        if name.text().strip() == "":
            self.BlinkingTextField(name)
        elif description.toPlainText().strip() == "":
            self.BlinkingTextField(description)
        else:
            print(name.text())
            print(description.toPlainText())
            print(self.img)
            self.close()

    @staticmethod
    def BlinkingTextField(filed):
        time = 0
        for quantity in range(6):
            QtCore.QTimer.singleShot(time := time+400,
                                     lambda: filed.setStyleSheet("border: 2px solid red;"))
            QtCore.QTimer.singleShot(time := time+400,
                                     lambda: filed.setStyleSheet("border: 1px solid #54026E;"))

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
