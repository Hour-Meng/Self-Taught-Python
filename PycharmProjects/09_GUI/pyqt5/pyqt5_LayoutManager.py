import sys

from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, 
                             QHBoxLayout, QGridLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python GUI")
        self.setGeometry(700, 300, 600, 400)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)  # This is our winsow's central widget

        label1 = QLabel("Label 1", self)
        label2 = QLabel("Label 2", self)
        label3 = QLabel("Label 3", self)
        label4 = QLabel("Label 4", self)

        label1.setStyleSheet("background-color: lightblue;")
        label2.setStyleSheet("background-color: lightgreen;")
        label3.setStyleSheet("background-color: lightcoral;")
        label4.setStyleSheet("background-color: lightgoldenrodyellow;")

        """    vbox = QVBoxLayout() # This is a vertical box layout -

            vbox.addWidget(label1)
            vbox.addWidget(label2)
            vbox.addWidget(label3)
            vbox.addWidget(label4)

            central_widget.setLayout(vbox)"""

        """    hbox = QHBoxLayout() # This is a horizontal box layout |
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)

        central_widget.setLayout(hbox)"""

        grid = QGridLayout()  # This is a grid layout

        grid.addWidget(label1, 0, 0)  # row 0, column 0
        grid.addWidget(label2, 0, 1)  # row 0, column 1
        grid.addWidget(label3, 1, 0)  # row 1, column 0
        grid.addWidget(label4, 1, 1)  # row 1, column 1

        central_widget.setLayout(grid)

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()