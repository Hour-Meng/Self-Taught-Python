import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap # QPixmap is used to handle images

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Python GUI Image")
        self.setGeometry(700, 300, 600, 400)

        label  = QLabel(self)
        label.setGeometry(0, 0 , 300, 200)

        # Get the directory of this script, then find diddy.png in that directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "diddy.png")
        
        pixmap = QPixmap(image_path) # Load the image

        label.setPixmap(pixmap) # Set the image to the label

        # to correctly scale the image to fit the label
        label.setScaledContents(True)

        label.setGeometry((self.width()-label.width())//2,  
                          (self.height()-label.height())//2, 
                          label.width(), 
                          label.height())   # why use //2? it's to devide by 2 and get an integer result
                                            # Ex: 5/2 = 2.5 but 5//2 = 2


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit((app.exec_()))

main()
