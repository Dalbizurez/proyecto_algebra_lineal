from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QTextEdit
from PyQt6.QtGui import QPixmap
import re
from pasos_dialog import Pasos_Dialog
from grafica_dialog import Graph_Dialog
from matrices import steps, clean_steps

import matplotlib.pyplot as plt
import numpy as np

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

def str_steps():
    dialog = Pasos_Dialog()
    dialog.txt_pasos.setPlainText("\n".join(steps()))
    dialog.show()
    dialog.exec()

def vector_graph(vectors:list, add = False):
    if not add:
        plt.clf()
    if not vectors:
        return
    fig, ax = plt.subplots()
    for x in range(len(vectors)):
        vector = vectors[x]
        if x != 0 and add:
            ax.quiver(vectors[x-1][0], vectors[x-1][1], vector[0], vector[1], angles='xy', scale_units='xy', scale=1)
        else:
            ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    plt.grid()
    plt.savefig("vector.png")

    dialog = Graph_Dialog()
    dialog.lbl_graph.setPixmap(QPixmap("vector.png"))
    dialog.show()
    dialog.exec()