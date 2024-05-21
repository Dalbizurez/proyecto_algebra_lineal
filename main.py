from PyQt6.QtWidgets import QApplication
from menu import MainWindow as MenuWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MenuWindow()
    window.show()
    app.exec()
    