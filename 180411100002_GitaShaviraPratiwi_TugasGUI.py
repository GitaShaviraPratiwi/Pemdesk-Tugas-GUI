import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.label = QLabel(self)
        self.label.setGeometry(10, 5, 201, 21)
        self.label.setText("Kotak Angka")
        
        self.button1 = QPushButton(self)
        self.button1.setGeometry(10, 25, 31, 31)
        self.button1.setStyleSheet("background-color: #B0C4DE; font-size: 28px; font-weight: bold; color: red;")
        self.button1.setText("1")

        self.button2 = QPushButton(self)
        self.button2.setGeometry(46, 25, 31, 31)
        self.button2.setStyleSheet("background-color: #B0C4DE; font-size: 28px; font-weight: bold; color: red;")
        self.button2.setText("2")

        self.button3 = QPushButton(self)
        self.button3.setGeometry(81, 25, 31, 31)
        self.button3.setStyleSheet("background-color: #B0C4DE; font-size: 28px; font-weight: bold; color: red;")
        self.button3.setText("3")

        self.button4 = QPushButton(self)
        self.button4.setGeometry(116, 25, 31, 31)
        self.button4.setStyleSheet("background-color: #B0C4DE; font-size: 28px; font-weight: bold; color: red; ")
        self.button4.setText("4")

        self.button5 = QPushButton(self)
        self.button5.setGeometry(151, 25, 31, 31)
        self.button5.setStyleSheet("background-color: #B0C4DE; font-size: 28px; font-weight: bold; color: red; ")
        self.button5.setText("5")

        self.setGeometry(200, 200, 350, 200)
        self.setWindowTitle("PyQt5 Example")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())


