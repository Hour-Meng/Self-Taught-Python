import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button =  QPushButton("Click Me", self)


        self.setWindowTitle("Python GUI")
        self.setGeometry(550, 250, 800, 600)

        #Label
        self.label = QLabel("", self)
        self.label.setGeometry(0, 60, 800, 50)
        self.label.setStyleSheet("font-size: 20px;")

        self.initUI()

    def initUI(self):
        self.button.setGeometry(0, 0, 800, 50)
        self.button.setStyleSheet("font-size: 25px;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.setWindowTitle("Button Clicked")
        self.label.setText("Button was clicked!")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()