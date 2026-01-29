# PyQt5 is a GUI for python
# Firstly you need to install PyQt5 package if you haven't already
# Type pip install PyQt5 in your terminal
# Remember when installing every package make sure your virtual environment (venv) is activated
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # This is to set up the title
        self.setWindowTitle("Python")
        # To set the location
        self.setGeometry(700, 300, 600, 400) # (x_pos, y_pos, width, height)

        label = QLabel("Hello guys", self)


def main():
    app = QApplication(sys.argv) # arvg stands for argument variable
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()