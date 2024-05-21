from ui.clave_ui import Ui_Dialog
from PyQt6.QtWidgets import QDialog, QTextEdit
from matrices import Cipher
from UI_operations import validar_matriz, get_matriz, str_matriz

class Key_Dialog(QDialog, Ui_Dialog):
    def __init__(self, cipher:Cipher, parent = None) -> None:
        super(QDialog, self).__init__(parent)
        self.setModal(True)
        self.setupUi(self)
        self.cipher = cipher
        if cipher.key:
            self.txt_clave_previa.setText(str_matriz(cipher.key))
            self.txt_clave_nueva.setText(str_matriz(cipher.key))
        
        self.btn_guardar_clave.clicked.connect(self.close)

        self.txt_clave_nueva.textChanged.connect(lambda:self.validar(self.txt_clave_nueva))



    def validar(self, widget:QTextEdit):
        valid = validar_matriz(widget)
        if not valid:
            # Cambiar el color del borde a rojo para indicar un error en la matriz
            widget.setStyleSheet("border: 1px solid red;")
        else:
            # Cambiar el color del borde a gris para indicar que no hay error
            widget.setStyleSheet("border: 1px solid grey;")
        self.btn_guardar_clave.setEnabled(valid)
        