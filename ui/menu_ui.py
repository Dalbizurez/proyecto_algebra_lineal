# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(227, 307)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_entre_matrices = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_entre_matrices.setObjectName("btn_entre_matrices")
        self.verticalLayout_2.addWidget(self.btn_entre_matrices)
        self.btn_matriz = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_matriz.setObjectName("btn_matriz")
        self.verticalLayout_2.addWidget(self.btn_matriz)
        self.btn_codificacion = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_codificacion.setObjectName("btn_codificacion")
        self.verticalLayout_2.addWidget(self.btn_codificacion)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 227, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_entre_matrices.setText(_translate("MainWindow", "Operaciones entre matrices"))
        self.btn_matriz.setText(_translate("MainWindow", "Operaciones sobre una matriz"))
        self.btn_codificacion.setText(_translate("MainWindow", "Codificacion"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
