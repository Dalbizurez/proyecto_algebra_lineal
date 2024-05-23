from ui.operaciones_matriz_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from matrices import inversa_gj, determinante_gauss, cuadrada
from UI_operations import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_inversa.clicked.connect(self.inversa)
        self.btn_determinante.clicked.connect(self.determinante)
        self.btn_rango.clicked.connect(self.rango)
        
        self.txt_matrix1.textChanged.connect(lambda:self.validar(self.txt_matrix1))

        self.actionVer.triggered.connect(str_steps)


    def inversa(self):
        clean_steps()
        matriz = get_matriz(self.txt_matrix1)
        if not matriz[0]:
            return
        resultado = inversa_gj(get_matriz(matriz))
        if resultado == 0:
            self.txt_matrix2.setPlainText("No se puede realizar la operacion, determinante = 0")
        elif resultado == -1:
            self.txt_matrix2.setPlainText("No se puede realizar la operacion, la matriz no es cuadrada")
        else:
            self.txt_matrix2.setPlainText(str_matriz(resultado))

    def determinante(self):
        clean_steps()
        matriz = get_matriz(self.txt_matrix1)
        if cuadrada(matriz):
            resultado = determinante_gauss(matriz)
            self.txt_matrix2.setPlainText(str(resultado))
        else:
            self.txt_matrix2.setPlainText("No se puede realizar la operacion, la matriz no es cuadrada")

    def rango(self):
        pass

    def validar(self, widget:QTextEdit):
        valid = validar_matriz(widget)
        if not valid:
            # Cambiar el color del borde a rojo para indicar un error en la matriz
            widget.setStyleSheet("border: 1px solid red;")
        else:
            # Cambiar el color del borde a gris para indicar que no hay error
            widget.setStyleSheet("border: 1px solid grey;")
        self.btn_inversa.setEnabled(valid)
        self.btn_determinante.setEnabled(valid)
        self.btn_rango.setEnabled(valid)
