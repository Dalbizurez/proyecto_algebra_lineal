from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QTextEdit
import re

NUMBER_REGEX = "-?[0-9]+(?:\.?[0-9]+)?"


def validar_matriz(widget:QTextEdit):
    txt = widget.toPlainText()
    valid = len(re.sub(NUMBER_REGEX,"", txt).strip()) == 0
    # valid = txt.replace(" ", "").replace("\n","").replace("-","").replace(".","").isnumeric()
    lengths = []
    for row in txt.split("\n"):
        numbers = len([x for x in re.findall(NUMBER_REGEX, row)])
        lengths.append(numbers)
    valid &= len(set(lengths)) == 1
    return valid

def get_matriz(txtEdit:QTextEdit):
        filas = txtEdit.toPlainText().split("\n")
        matriz = []
        for fila in filas:
            row = []
            vals = re.findall(NUMBER_REGEX, fila)
            for val in vals:
                row.append(float(val)) 
            # row = [float(x) for x in re.findall(NUMBER_REGEX, fila)]
            matriz.append(row)
        return matriz

def str_matriz(matriz:list[list[int]]):
    txt = ""
    for row in matriz:
        txt += " ".join([str(x) for x in row]) + "\n"
    return txt