from ui.markov_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from matrices import markov, cuadrada
from UI_operations import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.calcular)
        self.txt_matriz_probabilidades.textChanged.connect(lambda:self.validar(self.txt_matriz_probabilidades))
        self.txt_probabilidad_actual.textChanged.connect(lambda:self.validar_vector(self.txt_probabilidad_actual))

    def calcular(self):
        matriz = get_matriz(self.txt_matriz_probabilidades)
        vector = get_matriz(self.txt_probabilidad_actual)
        self.tbl_resultado.clear()
        self.tbl_resultado.setStyleSheet("border: 1px solid grey;")
        if (len(matriz) == 0 or len(vector) == 0) or not cuadrada(matriz):
            self.tbl_resultado.setStyleSheet("border: 1px solid red;")
            self.tbl_resultado.setToolTip("La matriz de probabilidades debe ser cuadrada y el vector de probabilidad actual debe tener el mismo numero de filas que la matriz")
            return
        resultado = markov(matriz, vector, int(self.spn_cambios.text()), False)
        
        self.tbl_resultado.setColumnCount(len(resultado[0]))
        self.tbl_resultado.setRowCount(len(resultado))
        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                self.tbl_resultado.setItem(i, j, QTableWidgetItem(str(resultado[i][j])))

    def validar_vector(self, widget:QTextEdit):
        valid = validar_matriz(widget) and len(get_matriz(widget)[0]) == 1
        if not valid:
            # Cambiar el color del borde a rojo para indicar un error en la matriz
            widget.setStyleSheet("border: 1px solid red;")
        else:
            # Cambiar el color del borde a gris para indicar que no hay error
            widget.setStyleSheet("border: 1px solid grey;")
        self.btn_calcular.setEnabled(valid)

    def validar(self, widget:QTextEdit):
        valid = validar_matriz(widget)
        if not valid:
            # Cambiar el color del borde a rojo para indicar un error en la matriz
            widget.setStyleSheet("border: 1px solid red;")
        else:
            # Cambiar el color del borde a gris para indicar que no hay error
            widget.setStyleSheet("border: 1px solid grey;")
        self.btn_calcular.setEnabled(valid)