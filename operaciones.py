from ui.operaciones_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QTextEdit
from matrices import multiplicacion, suma, resta, producto_punto
from UI_operations import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__(None)
        self.setupUi(self)

        self.btn_suma.clicked.connect(self.suma)
        self.btn_resta.clicked.connect(self.resta)
        self.btn_multiplicacion.clicked.connect(self.multiplicacion)
        self.btn_division.clicked.connect(self.producto_punto)
        self.btn_division.setEnabled(False)
        self.btn_suma.setEnabled(False)
        self.btn_multiplicacion.setEnabled(False)
        self.btn_resta.setEnabled(False)

        self.txt_matriz1.setPlaceholderText("1 2 4\n3 4 5\n6 7 8")
        self.txt_matriz2.setPlaceholderText("1 2 4\n3 4 5\n6 7 8")
        
        self.txt_matriz1.textChanged.connect(lambda:self.validar(self.txt_matriz1))
        self.txt_matriz2.textChanged.connect(lambda:self.validar(self.txt_matriz2))

        self.txt_matriz1.setToolTip("Solo se permite numeros")
        self.txt_matriz2.setToolTip("Solo se permite numeros")

        self.actionVer.triggered.connect(str_steps)

    def suma(self):
        clean_steps()
        m1 = get_matriz(self.txt_matriz1)
        m2 = get_matriz(self.txt_matriz2)
        resultado = suma(m1, m2)
        if resultado:
            self.txt_resultado.setPlainText(str_matriz(resultado))
        else:
            self.txt_resultado.setPlainText("No se puede realizar la operacion, para sumar es necesario que las matrices tengan el mismo orden")

    def resta(self):
        clean_steps()
        m1 = get_matriz(self.txt_matriz1)
        m2 = get_matriz(self.txt_matriz2)
        resultado = resta(m1, m2)
        if resultado:
            self.txt_resultado.setPlainText(str_matriz(resultado))
        else:
            self.txt_resultado.setPlainText("No se puede realizar la operacion, para restar es necesario que las matrices tengan el mismo orden")

    def multiplicacion(self):
        clean_steps()
        m1 = get_matriz(self.txt_matriz1)
        m2 = get_matriz(self.txt_matriz2)
        resultado = multiplicacion(m1, m2)
        if resultado:
            self.txt_resultado.setPlainText(str_matriz(resultado))
        else:
            self.txt_resultado.setPlainText("No se puede realizar la operacion, por favor revise que el numero de columnas de la matriz 1 sea igual al numero de filas de la matriz 2")

    def producto_punto(self):
        return
        m1 = get_matriz(self.txt_matriz1)
        m2 = get_matriz(self.txt_matriz2)
        resultado = producto_punto(m1, m2)
        if resultado:
            self.txt_resultado.setPlainText(str_matriz(resultado))
        else:
            self.txt_resultado.setPlainText("No se puede realizar la operacion")

    def validar(self, widget:QTextEdit):
        valid = validar_matriz(widget)
        if not valid:
            # Cambiar el color del borde a rojo para indicar un error en la matriz
            widget.setStyleSheet("border: 1px solid red;")
        else:
            # Cambiar el color del borde a gris para indicar que no hay error
            widget.setStyleSheet("border: 1px solid grey;")
        self.btn_division.setEnabled(valid)
        self.btn_suma.setEnabled(valid)
        self.btn_multiplicacion.setEnabled(valid)
        self.btn_resta.setEnabled(valid)
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

