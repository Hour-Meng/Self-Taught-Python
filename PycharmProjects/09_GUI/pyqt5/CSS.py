from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QHBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSS Example")
        self.setGeometry(600,300 , 300 , 400)

        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        #give each widget name, so we can target them in the CSS code
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        central_widget.setLayout(hbox)

        # Why use tripple quotes? Because we want to write multiple lines of CSS code
        # tripple quotes allow us to do that without having to worry about escaping characters or adding newline characters.
        self.setStyleSheet(""" 
            QPushButton{
                           font-size: 18px;
                           font-family: Arial;
                           padding: 10px 50px;
                           margin: 20px;
                           border: 2px solid black;
                           border-radius: 15px;}
                           
            QPushButton#button1{background-color: hsl(12, 100%, 62%);}
            QPushButton#button2{ background-color: hsl(198, 100%, 62%);}
            QPushButton#button3{ background-color: hsl(351, 100%, 62%);}
                        
                           
            QPushButton#button1:hover{ background-color: hsl(12, 100%, 82%)}
            QPushButton#button2:hover{ background-color: hsl(198, 100%, 82%);}
            QPushButton#button3:hover{ background-color: hsl(351, 100%, 82%);}

"""  )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
main()
