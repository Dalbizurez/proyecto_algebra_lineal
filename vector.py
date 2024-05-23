from ui.vector_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QDoubleSpinBox, QSlider
from matrices import suma, producto_punto, magnitud, angulo, componentes

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__(None)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.calcular)
        self.sld_mode.valueChanged.connect(self.cambiar_modo)

    def cambiar_modo(self):
        modo = self.sld_mode.value()

        if modo == 1:
            self.spn_1.setMaximum(1000.0)
            self.spn_1.setMinimum(-1000)
            self.spn_2.setMaximum(1000.0)
            self.spn_2.setMinimum(-1000)
        else:
            self.spn_1.setMinimum(0.0)
            self.spn_2.setMinimum(0)
            self.spn_2.setMaximum(360)

        self.lbl1.setText("Componente X" if modo == 1 else "Magnitud")
        self.lbl2.setText("Componente Y" if modo == 1 else "Angulo (0 - 360)")
    
    def calcular(self):
        modo = self.sld_mode.value()
        if modo == 1:
            x = self.spn_1.value()
            y = self.spn_2.value()
            direction_x = "E" if x >= 0 else "W"
            direction_y = "N" if y >= 0 else "S"
            self.txt_resultado.setText(f"|A|: {magnitud(x, y)}; A°: {angulo(x, y)} {direction_y}{direction_x}")
        else:
            res_magnitud = self.spn_1.value()
            res_angulo = self.spn_2.value()
            direction_x = "E" if res_angulo < 90 or res_angulo>270 else "W"
            direction_y = "N" if res_angulo < 180 else "S"
            x, y = componentes(res_magnitud, res_angulo)
            self.txt_resultado.setText(f"Ax: {x}; Ay: {y} {direction_y}{direction_x}")
        self.resize(self.sizeHint())