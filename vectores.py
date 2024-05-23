from ui.operaciones_vectores_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QDoubleSpinBox, QLineEdit

from matrices import suma, producto_punto, magnitud, angulo, componentes
from UI_operations import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__(None)
        self.setupUi(self)

        self.btn_suma.clicked.connect(self.sumar)
        self.btn_producto_punto.clicked.connect(self.producto_punto)

        self.sld_v1.valueChanged.connect(lambda:self.cambiar_modo(self.sld_v1, 1))
        self.sld_v2.valueChanged.connect(lambda:self.cambiar_modo(self.sld_v2, 2))
    

    def cambiar_modo(self, sld, vector):
        modo = sld.value()
        if vector == 1:
            self.lbl1_v1.setText("Componente X" if modo == 2 else "Magnitud")
            self.lbl2_v1.setText("Componente Y" if modo == 2 else "Angulo (0 - 360)")
            if modo == 2:
                self.spn1_v1.setMaximum(1000.0)
                self.spn1_v1.setMinimum(-1000)
                self.spn2_v1.setMaximum(1000.0)
                self.spn2_v1.setMinimum(-1000)
            else:
                self.spn1_v1.setMinimum(0.0)
                self.spn2_v1.setMinimum(0)
                self.spn2_v1.setMaximum(360)
        else:
            self.lbl1_v2.setText("Componente X" if modo == 2 else "Magnitud")
            self.lbl2_v2.setText("Componente Y" if modo == 2 else "Angulo (0 - 360)")
            if modo == 2:
                self.spn1_v2.setMaximum(1000.0)
                self.spn1_v2.setMinimum(-1000)
                self.spn2_v2.setMaximum(1000.0)
                self.spn2_v2.setMinimum(-1000)
            else:
                self.spn1_v2.setMinimum(0.0)
                self.spn2_v2.setMinimum(0)
                self.spn2_v2.setMaximum(360)

    def obtener_vector(self, vector):
        sld = self.sld_v1 if vector == 1 else self.sld_v2
        modo = sld.value()
        if vector == 1:
            a = self.spn1_v1.value()
            b = self.spn2_v1.value()
        else:
            a = self.spn1_v2.value()
            b = self.spn2_v2.value()
        match modo:
            case 1:
                return [componentes(a, b)]
            case 2:
                return [[a, b]]
        

    def sumar(self):
        v1 = self.obtener_vector(1)
        v2 = self.obtener_vector(2)
        resultado = suma(v1, v2)
        x = resultado[0][0]
        y = resultado[0][1]
        res_magnitud = magnitud(x, y)
        res_angulo = angulo(x, y)
        res_angulo += 90 if x < 0 and y > 0 else 0
        res_angulo += 270 if x > 0 and y < 0 else 0
        res_angulo += 180 if y < 0 else 0 
        direction_x = "E" if res_angulo < 90 or res_angulo>270 else "W"
        direction_y = "N" if res_angulo < 180 else "S"
        self.txt_resultado.setText(f"Ax: {resultado[0][0]}; Ay: {resultado[0][1]}\n|A|: {res_magnitud}; A°: {res_angulo} {direction_y}{direction_x}")
    
        self.resize(self.sizeHint())

    def producto_punto(self):
        v1 = self.obtener_vector(1)
        v2 = self.obtener_vector(2)
        resultado = producto_punto(v1, v2)
        if resultado:
            self.txt_resultado.setText(f"Producto punto: {resultado}")
        else:
            self.txt_resultado.setText("No se puede realizar la operacion")
        self.resize(self.sizeHint())

