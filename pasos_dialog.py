from ui.dialog_pasos import Ui_Dialog
from PyQt6.QtWidgets import QDialog

class Pasos_Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None) -> None:
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.setModal(True)