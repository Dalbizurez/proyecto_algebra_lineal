from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QTextEdit
import re

def validar_matriz(widget:QTextEdit):
    txt = widget.toPlainText()
    valid = txt.replace(" ", "").replace("\n","").replace("-","").isnumeric()
    lengths = []
    for row in txt.split("\n"):
        numbers = len([x for x in re.findall("-?[0-9]+", row)])
        lengths.append(numbers)
    valid &= len(set(lengths)) == 1
    return valid

def get_matriz(txtEdit:QTextEdit):
        filas = txtEdit.toPlainText().split("\n")
        matriz = []
        for fila in filas:
            row = [int(x) for x in re.findall("-?[0-9]+", fila)]
            matriz.append(row)
        return matriz

def str_matriz(matriz:list[list[int]]):
    txt = ""
    for row in matriz:
        txt += " ".join([str(x) for x in row]) + "\n"
    return txt