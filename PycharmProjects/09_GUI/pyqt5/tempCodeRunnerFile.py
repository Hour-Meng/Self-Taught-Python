# PyQt5 is a GUI for python
# Firstly you need to install PyQt5 package if you haven't already
# Type pip install PyQt5 in your terminal
# Remember when installing every package make sure your virtual environment (venv) is activated
import os


import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt # What does Qt do? --> It helps with alignment


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # This is to set up the title
        self.setWindowTitle("Python GUI")
        # To set the location
        self.setGeometry(700, 300, 600, 400) # (x_pos, y_pos, width, height)

        label = QLabel("Hello guys", self)
        #This one is to increase the font size
        label.setFont(QFont("Celedea", 24))
        # Without setting the position and size, your label will be cut off
        label.setGeometry(0,0, 600, 50)
        # To set the font color
        label.setStyleSheet("color: black;"
                            "background-color: #8ececb;"
                            "font-weight: bold;") # you can also use hex color codes or a RGN too
        
        # label.setAlignment(Qt.AlignTop) # This is to align the text to the top of the label
        # label.setAlignment(Qt.AlignCenter) # This is to align the text to the center of the label
        # label.setAlignment(Qt.AlignVCenter) # This is to align the text vertically to the center of the label (original position)
        # label.setAlignment(Qt.AlignRight) # This is to align the text to the right of the label
        label.setAlignment(Qt.AlignHCenter) # This is to align the text horizontally to the center of the label

        

def main():
    app = QApplication(sys.argv) # arvg stands for argument variable
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()