from ui.menu_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__(None)
        self.setupUi(self)

        self.btn_entre_matrices.clicked.connect(self.operaciones)
        self.btn_matriz.clicked.connect(self.matriz)
        self.btn_codificacion.clicked.connect(self.codificacion)

    def operaciones(self):
        from operaciones import MainWindow
        self.op = MainWindow()
        self.op.show()

    def matriz(self):
        from operaciones_matriz import MainWindow
        self.mat = MainWindow()
        self.mat.show()

    def codificacion(self):
        from coder import MainWindow
        self.cod = MainWindow()
        self.cod.show()