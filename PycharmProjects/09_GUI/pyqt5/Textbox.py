from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Enter your name:", self)
        self.label.move(20, 20)
        # Create a QLineEdit for user input
        self.lineEdit = QLineEdit(self) # Why self? Because we want to access this line edit later in the code, so we need to make it an instance variable by using self.
        # Push Button
        self.button = QPushButton("Submit", self)

        self.initUI()

    def initUI(self):
        self.lineEdit.setGeometry(20, 50, 200, 30)
        self.lineEdit.setStyleSheet("font-size: 16px; background-color: lightgray; border: 1px solid black;")
        # set place holder text, you know the half visible text in the line edit
        self.lineEdit.setPlaceholderText("Please enter your name")
        self.button.setGeometry(225, 50, 100, 30)
        #when click submit
        self.button.clicked.connect(self.is_submit)

    def is_submit(self):
        text = self.lineEdit.text()
        print(f"Hello, {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
main()