from ui.dialog_graph import Ui_Dialog
from PyQt6.QtWidgets import QDialog, QLabel
from PyQt6.QtGui import QPixmap

import matplotlib.pyplot as plt

class Graph_Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None) -> None:
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

    
