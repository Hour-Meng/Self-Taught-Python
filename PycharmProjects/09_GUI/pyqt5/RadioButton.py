from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QRadioButton, QButtonGroup

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Python GUI")
        self.setGeometry(550, 250, 800, 600)

        #Label
        self.label = QLabel("", self)
        self.label.setGeometry(0, 60, 800, 50)
        self.label.setStyleSheet("font-size: 20px;")
        #Radio buttons
        self.radio1 = QRadioButton("Car", self)
        self.radio2 = QRadioButton("Moto", self)
        self.radio3 = QRadioButton("Truck", self)
        self.radio4 = QRadioButton("Expensive", self)
        self.radio5 = QRadioButton("Cheap", self)
        #Button Group
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(100, 0, 800, 50)
        self.radio2.setGeometry(100, 50, 800, 50)
        self.radio3.setGeometry(100, 100, 800, 50)
        self.radio4.setGeometry(100, 150, 800, 50)
        self.radio5.setGeometry(100, 200, 800, 50)
        #Grouping the radio buttons
        self.button_group1.addButton((self.radio1))
        self.button_group1.addButton((self.radio2))
        self.button_group1.addButton((self.radio3))
        self.button_group2.addButton((self.radio4))
        self.button_group2.addButton((self.radio5))

        self.setStyleSheet("QRadioButton {font-size: 25px; color: blue; background-color: lightgray;}")

        self.radio1.toggled.connect(self.radio_button_toggled)
        self.radio2.toggled.connect(self.radio_button_toggled)
        self.radio3.toggled.connect(self.radio_button_toggled)
        self.radio4.toggled.connect(self.radio_button_toggled)
        self.radio5.toggled.connect(self.radio_button_toggled)

    def radio_button_toggled(self):
        clicked_button = self.sender()  # This will give us the button that was clicked
        if clicked_button.isChecked():
            print(f"You choose a {clicked_button.text()}")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
main()