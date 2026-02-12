from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QCheckBox
from PyQt5.QtCore import Qt
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
        #Checkbox
        self.checkbox = QCheckBox("Check me", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 25px; color: blue; background-color: lightgray;")
        self.checkbox.setGeometry(100, 0, 800, 50)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changes)

    def checkbox_changes(self, state):
        print(state)  # state will be 0 when unchecked and 2 when checked
        if state == Qt.Checked:
            print("You have checked the checkbox")
        else:
            print("You have unchecked the checkbox")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()