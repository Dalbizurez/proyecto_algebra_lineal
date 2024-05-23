from ui.coder_ui import Ui_MainWindow
from ui.clave_ui import Ui_Dialog
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from matrices import Cipher
from clave_dialog import Key_Dialog
from UI_operations import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cipher = Cipher()

        self.btn_code.clicked.connect(self.code)
        self.btn_decode.clicked.connect(self.decode)

        self.actionCambiar_clave.triggered.connect(self.change_key)

        self.txt_mensaje.textChanged.connect(lambda:self.validar(self.txt_mensaje))
        self.txt_codigo.textChanged.connect(lambda:self.validar(self.txt_codigo))

        self.actionVer.triggered.connect(str_steps)

    def code(self):
        clean_steps()
        if not self.cipher.key:
            self.txt_codificado.setPlainText("Aun no ha definido una clave")
        else:
            codigo = self.cipher.code(get_matriz(self.txt_mensaje))
            self.txt_codificado.setPlainText(str_matriz(codigo))

    def decode(self):
        clean_steps()
        if not self.cipher.key:
            self.txt_descifrado.setPlainText("Aun no ha definido una clave")
        else:
            descifrado = self.cipher.decipher(get_matriz(self.txt_codigo))
            for row in descifrado:
                for i in range(len(row)):
                    row[i] = round(row[i])
            self.txt_descifrado.setPlainText(str_matriz(descifrado))
        

    def change_key(self):
        dialog = Key_Dialog(self.cipher)
        dialog.btn_guardar_clave.clicked.connect(lambda:self.guardar_clave(dialog.txt_clave_nueva))
        dialog.show()
        dialog.exec()

    def guardar_clave(self, txt:QTextEdit):
        self.cipher.setKey(get_matriz(txt))

    def validar(self, widget:QTextEdit):
        valid = validar_matriz(widget)
        if not valid:
            # Cambiar el color del borde a rojo para indicar un error en la matriz
            widget.setStyleSheet("border: 1px solid red;")
        else:
            # Cambiar el color del borde a gris para indicar que no hay error
            widget.setStyleSheet("border: 1px solid grey;")
        self.btn_code.setEnabled(valid)
        self.btn_decode.setEnabled(valid)
