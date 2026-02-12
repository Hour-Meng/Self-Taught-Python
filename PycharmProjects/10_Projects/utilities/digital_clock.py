import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase
import os

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,500,200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        #set color
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: hsl(351, 100%, 50%); font-size: 120px;")
        self.setStyleSheet("background-color: black;")
        
        self.update_time()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000) # update every 1000ms or 1s
        folder = os.path.dirname(os.path.abspath(__file__))
        our_file = os.path.join(folder, "custom_alarmclock.ttf")

        custom_font = QFontDatabase.addApplicationFont(our_file)
        font_family = QFontDatabase.applicationFontFamilies(custom_font)[0] # it's a list
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")  # AP to know AM or PM
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    alarm_clock = DigitalClock()
    alarm_clock.show()
    sys.exit(app.exec_())

main()