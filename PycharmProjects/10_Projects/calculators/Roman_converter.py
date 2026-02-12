from PyQt5.QtWidgets import QMainWindow, QLineEdit, QWidget, QHBoxLayout, QPushButton, QApplication, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750,350,500,300)
        self.setWindowTitle("Roman Calculator")
        self.setStyleSheet("background-color: grey")
        #label
        self.printer = QLabel("", self)


        self.textbox = QLineEdit(self)
        self.submit = QPushButton("Submit", self)
        self.initUI()
    
    def initUI(self):
        #label
        self.printer.setGeometry(50, 100, 400, 50)
        self.printer.setStyleSheet("font-size: 20px")

        self.textbox.setPlaceholderText("Please enter a number")
        self.submit.setObjectName("submit")
        self.setStyleSheet("""
                           QPushButton#submit{background-color: hsl(0, 8%, 72%);
                            border: 2px solid black
                           ;border-radius: 10px}
                        QPushButton#submit:hover{background-color: hsl(0, 8%, 90%)}
                           
""")
        self.textbox.setGeometry(50,50,150,50)
        self.submit.setGeometry(220, 50, 100, 50)

        self.submit.clicked.connect(self.on_click)

    def on_click(self):
        text = self.textbox.text()
        result = solution(text)
        self.printer.setText(result)

# Roman converter
def solution(n):
    try:
        n = int(n)
    except ValueError:
        return "Please enter a valid number."
    
    if n < 1 or n > 3999:
        return "Please enter a number between 1 and 3999."
    thousand = ["", "M", "MM", "MMM"]
    hundred = ["", "C", "CC", "CCC", "CD", "D" ,"DC", "DCC", "DCCC", "CM"]
    ten_ish = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    one_ish = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    container = [ int(b)*(10**(len(str(n)) - a - 1)) for a ,b in enumerate(str(n))]
    result = list()
    for x in container:
        if len(str(x)) == 4:
            result.append(thousand[ x//1000])
        if len(str(x)) == 3:
            result.append(hundred[x // 100])
        if len(str(x)) == 2:
            result.append(ten_ish[x // 10])
        if len(str(x)) == 1:
            result.append(one_ish[x])
    
    return f" the result of {n} in roman is {"".join(result)}"

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()